''' Mainly handles the tabbed panel with capture mode, exposure
    etc.
'''

import json
from functools import partial
from loguru import logger

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import OptionProperty

from jocular.component import Component
from jocular.widgets import Panel
from jocular.exposurechooser import exp_to_str

faf_scripts = ['align', 'focus', 'frame']
light_scripts = ['light', 'seq']
calibration_scripts = ['dark', 'bias', 'autoflat', 'flat']
all_scripts = faf_scripts + light_scripts + calibration_scripts

class CaptureScript(Panel, Component):

    current_script = OptionProperty('align', options=all_scripts)
    capture_controls = {'devices', 'script_button', 'exposure_button', 'filter_button'}

    def __init__(self, **args):
        super().__init__(**args)
        self.app = App.get_running_app()
        try:
            with open(self.app.get_path('capture_scripts.json'), 'r') as f:
                self.scripts = json.load(f)
        except:
            # any problem loading => set up afresh
            self.scripts = {}
            for s in all_scripts:
                self.scripts[s] = {
                    'exposure': .1 if s in faf_scripts else 1, 
                    'filter': ['dark' if s in {'bias', 'dark'} else 'L']
                    }
            self.scripts['bias']['exposure'] = .001
            self.scripts['seq']['nsubs'] = 4
            self.scripts['seq']['filter'] = ['B', 'G', 'R', 'L']
            self.save()
        self.build()
        # initialise via current script once dependencies have been built
        Clock.schedule_once(self.on_current_script, 0)

    # def post_init(self, dt=None):
    #     self.on_current_script()

    def save(self, *args):
        with open(self.app.get_path('capture_scripts.json'), 'w') as f:
            json.dump(self.scripts, f, indent=1)  

    def on_new_object(self, *args):
        self.app.gui.enable(self.capture_controls)
        self.current_script = 'frame'
        self.on_current_script()

    def on_previous_object(self, *args):
        self.app.gui.disable(self.capture_controls)

    def on_current_script(self, *args):
        logger.debug('Changed script to {:}'.format(self.current_script))
        self.app.gui.set('script_button', self.current_script)
        self.update()
        self.app.gui.set('show_reticle', self.current_script == 'align', update_property=True)
        self.app.gui.set('80' if self.current_script == 'flat' else 'mean' , 
            True, update_property=True)

    def build(self, dt=None):
        logger.debug('building script panel')
        self.buts = {'name': {}, 'expo': {}, 'filt': {}}
        for s in all_scripts:
            if s in calibration_scripts:
                col = .9, .8, .8, 1
            elif s in light_scripts:
                col = .8, 1, .8, 1
            else:
                col = 1, 1, .8, 1 
            b1 = self.buts['name'][s] = ToggleButton(
                text=s, size_hint=(.4, 1), group='script', color=col,
                on_press=partial(self.script_selected, s))            
            b2 = self.buts['expo'][s] = Button(
                text=exp_to_str(self.scripts[s]['exposure']),
                size_hint=(.3, 1), background_color=(.5, .5, .5, 0),
                on_press=partial(self.exposure_selected, s))            
            b3 = self.buts['filt'][s] = Button(
                text=''.join(self.scripts[s]['filter']),
                size_hint=(.3, 1), background_color=(.5, .5, .5, 0),
                on_press=partial(self.filter_selected, s))
            bh = BoxLayout(orientation='horizontal', size_hint=(1, 1))
            bh.add_widget(b3)
            bh.add_widget(b2)
            bh.add_widget(b1)
            self.add_widget(bh)
        self.app.gui.add_widget(self)
        # self.on_current_script()

    def filterwheel_changed(self):
        ''' when filterwheel changes we need to change the available
            filters in the capture scripts and therefore update the scripts
        '''
        state = Component.get('FilterWheel').get_state()
        filts = list(state['filtermap'].keys())
        logger.debug('filters available in new filterwheel {:}'.format(filts))
        default = ['L'] if 'L' in filts else [f for f in filts if f != '-']
        logger.debug('Default filter is {:}'.format(default))
        if len(default) == 0:
            default = 'L'
        for k, v in self.scripts.items():
            v['filter'] = [f for f in v['filter'] if f in filts]
            if len(v['filter']) == 0:
                v['filter'] = default if k not in {'dark', 'bias'} else ['dark']
        logger.debug('scripts changed to accommodate new filterwheel')
        self.update()

    def update(self):
        # update panel, gui elements and save if ncessary
        logger.debug('updating script panel and capture interface')
        current = self.current_script
        for but in self.buts['name'].values():
            but.state = 'down' if but.text == current else 'normal'

        for s, props in self.scripts.items():
            self.buts['expo'][s].text = exp_to_str(props['exposure'])
            self.buts['filt'][s].text = ''.join(props['filter'])

        script = self.scripts[current]
        self.app.gui.set('exposure_button', exp_to_str(script['exposure']))
        self.app.gui.set('filter_button', ''.join(script['filter']))
        self.save()
        self.reset_generator()

    def script_selected(self, script, *args):
        self.current_script = script
        self.hide()

    def exposure_selected(self, script, *args):
        self.current_script = script
        self.hide()
        Component.get('ExposureChooser').show()

    def filter_selected(self, script, *args):
        self.current_script = script
        self.hide()
        Component.get('FilterChooser').show()


    def get_script(self):
        return self.scripts[self.current_script]

    def exposure_changed(self, exposure):
        # called by ExposureChooser
        self.scripts[self.current_script]['exposure'] = exposure
        self.update()

    def filter_changed(self, filt, nsubs=None):
        # called by FilterChooser
        self.scripts[self.current_script]['filter'] = filt
        if nsubs is not None:
            self.scripts['seq']['nsubs'] = nsubs
        self.update()

    def set_external_details(self, exposure=None, sub_type=None, filt=None):
        ''' This is a little different. Here we need to set the details on
            the interface regardless of what the scripts say. Need to 
            think this through. What happens if a user used an exposure that
            didn't exist. Easiest is just to not allow any editing for
            previous exposures.
        '''
        if type(filt) == list:
            filt = ''.join(filt)
        self.app.gui.set('exposure_button', '?' if exposure is None else exp_to_str(exposure))
        self.app.gui.set('filter_button', '?' if filt is None else filt)
        self.app.gui.set('script_button', '?' if sub_type is None else sub_type)


    # ---- the script definitions in terms of generators

    def light_generator(self):
        script = self.scripts['light']
        yield 'set filter', script['filter'][0]
        yield 'set exposure', script['exposure']
        while True:
            yield 'expose long'

    def seq_generator(self):
        script = self.scripts['seq']
        yield 'set exposure', script['exposure']
        while True:
            for f in Component.get('FilterChooser').order_by_transmission(script['filter']):
                yield 'set filter', f
                for i in range(script['nsubs']):
                    yield 'expose long'

    def frame_generator(self):
        script = self.scripts['frame']
        yield 'set filter', script['filter'][0]
        yield 'set exposure', script['exposure']
        while True:
            yield 'expose short'

    def focus_generator(self):
        script = self.scripts['focus']
        yield 'set filter', script['filter'][0]
        yield 'set exposure', script['exposure']
        while True:
            yield 'expose short'

    def align_generator(self):
        script = self.scripts['align']
        yield 'set filter', script['filter'][0]
        yield 'set exposure', script['exposure']
        while True:
            yield 'expose short'

    def dark_generator(self):
        yield 'set filter', 'dark'
        yield 'set exposure', self.scripts['dark']['exposure']
        while True:
            yield 'expose long'

    def bias_generator(self):
        yield 'set filter', 'dark'
        yield 'set exposure', self.scripts['bias']['exposure']
        while True:
            yield 'expose bias'

    def autoflat_generator(self):
        yield 'set filter', self.scripts['autoflat']['filter'][0]
        yield 'autoflat'
        while True:
            yield 'expose long'

    def flat_generator(self):
        script = self.scripts['flat']
        yield 'set filter', script['filter'][0]
        yield 'set exposure', script['exposure']
        while True:
            yield 'expose long'

    def reset_generator(self):
        logger.debug('reset {:} generator'.format(self.current_script))
        self.generator = getattr(self, '{:}_generator'.format(self.current_script))()

