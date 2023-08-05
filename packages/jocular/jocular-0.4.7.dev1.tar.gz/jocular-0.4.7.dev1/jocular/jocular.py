''' Main app, called after some checks by startjocular function (at base)
'''

import os
import json
import sys

#from kivy.app import App
from kivymd.app import MDApp

from kivy.metrics import dp
from kivy.config import Config
from loguru import logger

from kivy.properties import ListProperty, NumericProperty, OptionProperty, StringProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.text import LabelBase

from jocular import __version__
from jocular.component import Component
from jocular.gui import GUI
from jocular.utils import get_datadir

# delete from here
from jocular.appearance import sat_to_hue

class Jocular(MDApp):

    showing = OptionProperty(
        'main', options=['main', 'observing list', 'calibration', 'observations']
    )

    # highlight_color = ListProperty([1, 1, 1, 1])
    lowlight_color = ListProperty([0.5, 0.5, 0.5, 1])
    hint_color = ListProperty([0.25, 0.25, 0.25, 1])
    lever_color = ListProperty([0.32, 0.32, 0.32, 1])
    background_color = ListProperty([0.06, 0.06, 0.06, 0])  # was 1 transp
    line_color = ListProperty([0.3, 0.3, 0.3, 1])  # used in Obj and Table only

    ring_font_size = StringProperty('14sp')
    info_font_size = StringProperty('14sp')
    form_font_size = StringProperty('15sp')

    data_dir = StringProperty(None)

    subdirs = {'captures', 'calibration', 'snapshots', 'watched', 'deleted', 'exports', 'catalogues', 'settings'}

    brightness = NumericProperty(1)
    transparency = NumericProperty(0)

    def get_dir_in_datadir(self, name):
        path = os.path.join(self.data_dir, name)
        try:
            if not os.path.exists(path):
                logger.debug('Jocular: creating path {:} -> {:}'.format(name, path))
                os.mkdir(path)
            return os.path.join(self.data_dir, name)
        except Exception as e:
            logger.exception('Cannot create path {:} ({:})'.format(path, e))
            sys.exit('Cannot create subdirectory of Jocular data directory')

    def get_path(self, name):
        # centralised way to handle accessing resources Jocular needs

        #  if path, return path to data dir, else return path to resource
        if name in self.subdirs:
            return self.get_dir_in_datadir(name)

        # jocular's own resources

        elif name == 'dsos':
            return os.path.join(self.directory, 'dsos')

        elif name in {'configurables.json', 'gui.json', 'object_types.json'}:
            return os.path.join(self.directory, 'resources', name)

        # user-accessible settings
        elif name in {'observing_list.json', 'observing_notes.json', 'previous_observations.json'}:
            return os.path.join(self.data_dir, name)

        # jocular settings
        elif name.endswith('.json'):
            return os.path.join(self.get_dir_in_datadir('settings'), name)

        # specific files
        elif name == 'libusb':
            return os.path.join(self.directory, 'resources', 'libusb-1.0.dll')
        elif name == 'star_db':
            return os.path.join(self.data_dir, 'platesolving', 'star_tiles.npz')
        elif name == 'dso_db':
            return os.path.join(self.data_dir, 'platesolving', 'dso_tiles')

        # everything else is in jocular's own resources
        else:
            return os.path.join(self.directory, 'resources', name)

    def on_brightness(self, *args):
        for c in ['hint_color', 'lowlight_color', 'line_color', 'lever_color']:
            getattr(self, c)[-1] = self.brightness

    @logger.catch()
    def build(self):

        self.data_dir = get_datadir()

        self.title = 'Jocular v{:}'.format(__version__)
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = '50'
        self.theme_cls.theme_style = "Dark"     

        LabelBase.register(name='Jocular', fn_regular=self.get_path('jocular4.ttf'))

        try:
            with open(self.get_path('Appearance.json'), 'r') as f:
                settings = json.load(f)
            for p, v in settings.items():
                if p == 'highlight_color':
                    self.theme_cls.accent_palette = v
                    self.theme_cls.primary_palette = v
                elif p.endswith('_color'):
                    lg = v / 100
                    setattr(self, p, [lg, lg, lg, 1])
                elif p.endswith('font_size'):
                    setattr(self, p, '{:}sp'.format(v))
                elif p == 'transparency':
                    self.transparency = int(v) / 100
                elif p == 'colour_saturation':
                    self.theme_cls.accent_hue = sat_to_hue(v)
        except:
            pass

        self.gui = GUI()

        # draw GUI
        Clock.schedule_once(self.gui.draw, -1)

        return self.gui


    @logger.catch()
    def on_stop(self):

        # save geometry
        Config.set('graphics', 'position', 'custom')
        Config.set('graphics', 'left', str(int(Window.left)))
        Config.set('graphics', 'top', str(int(Window.top)))
        Config.set('graphics', 'width', str(int(Window.width/ dp(1))))
        Config.set('graphics', 'height', str(int(Window.height/dp(1))))
        Config.write()
 
        Component.close()
        self.gui.on_close()

    # reset showing to main when any table is hidden
    def table_hiding(self, *args):
        self.showing = 'main'


def startjocular():

    # from loguru import logger

    os.environ["KIVY_NO_ARGS"] = "1"
    # logger.add('logfile')

    # remove logging to terminal and set up a single log file for easy debugging
    output_to_stderr = True
    logger.remove()
    logger.level("DEBUG", color='<black><dim>')
    logger.level("WARNING", color='<red>')
    logger.level("ERROR", color='<red><bold>')
    if output_to_stderr:
        time_fmt = '<fg 20,20,20>{time:HH:mm:ss.SSS}</fg 20,20,20>'
        level_fmt = '<level>{level: <8}</level>'
        name_fmt = '<light-blue>{name}</light-blue>:<cyan>{function}</cyan>:<fg 20,20,20>{line}</fg 20,20,20>'
        message_fmt = '{message}'
        logger.add(sys.stdout, 
            format='{:} {:} {:} | {:}'.format(time_fmt, level_fmt, name_fmt, message_fmt),
            colorize=True)
        logger.debug('fred')
    else:
        # fix logpath here
        logger.add(os.path.join(logpath, 'jocular.log'), mode='w', 
            format='{time: HH:mm:ss.SSS} {level} {name} {message}')

    # write critical kivy preferences
    from kivy.config import Config
    Config.set('kivy', 'log_level', 'error')
    Config.set('kivy', 'keyboard_mode', 'system')
    #Config.set('kivy', 'log_enable', 0)
    Config.set('kivy', 'exit_on_escape', '0')
    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'fullscreen', 0)
    Config.set('graphics', 'borderless', 0)
    Config.set('postproc', 'double_tap_time', 250)
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    Config.write()

    # finally we can start app
    # from jocular.jocular import Jocular
    try:
        Jocular().run()
    except Exception as e:
        sys.exit('Jocular failed with error {:}'.format(e))

