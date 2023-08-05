''' Handles new and previous object logic, and associated confirmation
    dialogues.
'''

import os
from datetime import date
from loguru import logger

from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from jocular.component import Component
from jocular.settingsmanager import Settings
from jocular.utils import add_if_not_exists, generate_observation_name, unique_member, move_to_dir
from jocular.widgets import JPopup
from jocular.image import save_image, Image

Builder.load_string('''

<MyLabel@Label>:
    size_hint: 1, None
    height: dp(24)
    text_size: self.size
    markup: True
    halign: 'left'
 
<Confirmation>:
    orientation: 'vertical'
    size_hint: None, None
    width: dp(280)
    spacing: dp(0), dp(15)
    height:  _temp_box.height + _confirm_box.height + dp(20)

    BoxLayout:
        id: _temp_box
        size_hint: 1, None
        height: dp(60) if root.show_temperature else dp(0)
        opacity: 1 if root.show_temperature else 0
        disabled: not root.show_temperature
        orientation: 'vertical'

        MyLabel:
            text: 'Temperature {:}\N{DEGREE SIGN}C'.format(_temperature.value) if _temperature.value > -26 else 'Temperature not set'
        Slider:
            size_hint: 1, None
            height: dp(30)
            id: _temperature
            value: root.session.temperature if root.session.temperature is not None else -26
            on_value: root.session.temperature = self.value if self.value > -26 else None
            min: -26
            max: 40
            step: 1
            
    BoxLayout:
        id: _confirm_box
        size_hint: 1, None
        height: dp(40)
        opacity: 1

        Button:
            text: 'Save master' if root.calibration else 'Save'
            size_hint: .5, .8
            on_press: root.objectio.save_master() if root.calibration else root.objectio.save()
        Button:
            text: "Don't save master" if root.calibration else 'Cancel'
            size_hint: .5, .8
            on_press: root.objectio.save() if root.calibration else root.objectio.cancel_save()
''')


class Confirmation(BoxLayout):
    
    def __init__(self, objectio=None, **kwargs):
        self.objectio = objectio
        self.show_temperature = objectio.sub_type == 'dark'
        self.calibration = objectio.sub_type in {'dark', 'flat', 'bias'}
        self.session = Component.get('Session')
        super().__init__(**kwargs)


class ObjectIO(Component, Settings):

    existing_object = BooleanProperty(False)
    confirm_on_new = BooleanProperty(True)

    tab_name = 'Saving'
    configurables = [
        ('confirm_on_new', {
            'name': 'confirmation before saving?', 
            'switch': '',
            'help': 'You will be asked to confirm when you hit the save button'})
        ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.current_object_dir = None
        self.closing = False
        dformat = '%y_%m_%d'
        self.session_dir = os.path.join(self.app.get_path('captures'), date.today().strftime(dformat))
        add_if_not_exists(self.session_dir)

    def on_close(self):
        self.closing = True
        # self.confirm_new_object(closedown=True)

    @logger.catch()
    def confirm_new_object(self, *args):
        # before saving, check for confirmations where required

        subs = Component.get('Stacker').subs

        # don't save if nothing changes, no current object, or no subs
        if not self.app.gui.something_has_changed() or not self.current_object_dir:
            logger.debug('no need to save anything')
            self.new_object()
            return

        # new in v0.4.5; if name has been changed, set as calibration type
        name = Component.get('DSO').Name
        if name.lower()[:4] in {'dark', 'flat', 'bias'}:
            self.sub_type = name.lower()[:4]
        else:
            self.sub_type = unique_member([s.sub_type for s in subs])

        # if calibration, ask user if they want to save master
        if self.sub_type in {'bias', 'flat', 'dark'}:
            self.popup = JPopup(title='Create new master{:}?'.format(self.sub_type), 
                content=Confirmation(objectio=self))
            self.popup.open()

        # user asked for confirmation?
        elif self.confirm_on_new:
            self.popup = JPopup(title='Confirm save (metadata changed)' if self.existing_object else 'Confirm save', 
                content=Confirmation(objectio=self))
            self.popup.open()

        # save silently
        else:
            self.save()


    def save(self, *args):
        # save info.json, handle rejects, and update observations table

        subs = Component.get('Stacker').subs
        Component.get('Metadata').set('exposure', unique_member([s.exposure for s in subs]))
        Component.get('Metadata').set('sub_type', self.sub_type)

        oldpath = self.current_object_dir
        Component.save_object()

        # check if name has been changed
        name = Component.get('Metadata').get('Name', default='')
        if name:
            session_dir, object_dir = os.path.split(self.current_object_dir)
            if name != object_dir:
                # user has changed name, so generate a (unique) new folder name
                new_name = generate_observation_name(session_dir, prefix=name)
                # change directory name; any problem, don't bother
                try:
                    os.rename(self.current_object_dir, 
                        os.path.join(session_dir, new_name)) 
                    self.current_object_dir = os.path.join(session_dir, new_name)
                    self.info('saved {:}'.format(new_name))
                except Exception as e:
                    logger.exception('cannot change name ({:})'.format(e))
                    self.warn('cannot change name')

        # save metadata, and if successful update observations
        newpath = self.current_object_dir
        try:
            Component.get('Metadata').save(newpath)            
            Component.get('Observations').update(oldpath, newpath)
            Component.get('ObservingList').new_observation()
        except Exception as e:
            logger.exception('OSError saving info3.json to {:} ({:})'.format(newpath, e))
            self.warn('saving metadata')

        self.new_object()
        if hasattr(self, 'popup'):
            self.popup.dismiss()

    def save_master(self):
        subs = Component.get('Stacker').subs
        Component.get('Calibrator').save_master(
            exposure=unique_member([s.exposure for s in subs]), 
            temperature=Component.get('Session').temperature,
            filt=unique_member([s.filter for s in subs]),
            sub_type=self.sub_type)
        self.save()

    def cancel_save(self, *args):
        self.popup.dismiss()

    def new_object(self, *args):
        if self.closing:
            return
        self.current_object_dir = None
        self.existing_object = False
        self.sub_type = None
        # Component.get('Metadata').reset()
        Component.initialise_new_object()
        # App.get_running_app().gui.enable()
        # this should be done by the camera mode; so don't do it for watched or controlled watched
        self.app.gui.set('frame_script', True, update_property=True)
        # print('calling gui reset changes')
        # self.app.gui.reset_changes()

    def load_previous(self, path):
        # previous will have been saved by this point
        self.existing_object = True
        # self.changed = False # we start off assuming nothing has changed
        # Component.get('Metadata').load(path)
        gui = self.app.gui
        gui.enable()
        gui.set('show_reticle', False, update_property=True)
        self.current_object_dir = path
        Component.initialise_previous_object()
        # self.app.gui.reset_changes()

        # stacker = Component.get('Stacker')
        # # stacker.recompute()
        # # Component.get('Capture').disable_capture_controls()

        # # # disable change to exposure if we are sure it is not an estimate
        # subs = stacker.subs
        # if len(subs) == 0:
        #     return

        # sub_type=unique_member([s.sub_type for s in subs])
        # if subs[0].exposure_is_an_estimate:
        #     self.app.gui.enable(['exposure_button', '{:}_script'.format(sub_type)])

        # # add info on exposure and filter(s)
        # expo = unique_member([s.exposure for s in subs])
        # if expo is None:
        #     expo = Component.get('Metadata').get('exposure')
        # if expo is None:
        #     expo = 0

        # Component.get('CaptureScript').set_external_details(exposure=expo, 
        #     sub_type=sub_type, 
        #     filt=''.join({s.filter for s in subs}))


    def new_sub(self, data=None, name=None, exposure=None, filt=None, temperature=None, sub_type=None):

        if data is None or name is None:
            return

        logger.debug('New sub | type {:} name {:} expo {:} filt {:} temp {:}'.format(
            sub_type, name, exposure, filt, temperature))

        stacker = Component.get('Stacker')
 
        if self.current_object_dir is None:
            # new object, so check if calibration or light
            if sub_type in {'dark', 'flat', 'bias'}:
                self.current_object_dir = os.path.join(self.session_dir, 
                    generate_observation_name(self.session_dir, prefix=sub_type))
                stacker.sub_type = sub_type  # is this needed any more?
                Component.get('DSO').Name = sub_type
            else:
                self.current_object_dir = os.path.join(self.session_dir, 
                    generate_observation_name(self.session_dir, prefix=Component.get('DSO').Name))
                self.app.gui.disable(['load_previous'])
            add_if_not_exists(self.current_object_dir)

        path = os.path.join(self.current_object_dir, name)

        try:
            save_image(data=data, path=path, exposure=exposure, filt=filt, 
                temperature=temperature, sub_type=sub_type)
            stacker.add_sub(Image(path))
        except Exception as e:
            logger.exception('cannot add sub to stack ({:})'.format(e))
           



    # def new_sub_from_watcher(self, sub):
    #     ''' Receiving a new sub from watcher might be the first we hear of 
    #     a new object, so method checks if we have a current object directory
    #     '''

    #     stacker = Component.get('Stacker')
    #     sub_type = sub.sub_type
 
    #     if self.current_object_dir is None:
    #         # new object, so check if calibration or light
    #         if sub_type in {'dark', 'flat', 'bias'}:
    #             self.current_object_dir = os.path.join(self.session_dir, 
    #                 generate_observation_name(self.session_dir, prefix=sub_type))
    #             stacker.sub_type = sub.sub_type  # is this needed any more?
    #             Component.get('DSO').Name = sub_type
    #         else:
    #             self.current_object_dir = os.path.join(self.session_dir, 
    #                 generate_observation_name(self.session_dir, prefix=Component.get('DSO').Name))
    #             self.app.gui.disable(['load_previous'])
    #         add_if_not_exists(self.current_object_dir)

    #     newpath = os.path.join(self.current_object_dir, sub.name)

    #     try:
    #         os.rename(sub.path, newpath)
    #         sub.path = newpath
    #         stacker.add_sub(sub)
    #     except Exception as e:
    #         Logger.error('ObjectIO: cannot add sub to stack ({:})'.format(e))

        # if we have an estimated exposure for this sub and if so, allow user to change it via GUI
        # disable change to exposure if we are sure it is not an estimate

        # if sub.exposure_is_an_estimate:
        #     self.app.gui.disable(['filter_button'])
        #     self.app.gui.enable(['exposure_button', '{:}_script'.format(sub_type)])
        #     Component.get('CaptureScript').set_external_details(sub_type=sub_type)


    def save_original(self, path):
        ''' Move non-Jocular sub from path (in Watched) to current object subdirectory
        '''
        if self.current_object_dir is None:
            self.current_object_dir = os.path.join(self.session_dir, 
                generate_observation_name(self.session_dir, prefix=Component.get('DSO').Name))
            add_if_not_exists(self.current_object_dir)
        move_to_dir(path, os.path.join(self.current_object_dir, 'originals'))

