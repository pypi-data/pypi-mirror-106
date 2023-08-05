''' Handles DSO details including lookup and catalogue entry
'''

import math
from functools import partial

from loguru import logger

from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, DictProperty
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView

from jocular.component import Component
from jocular.widgets import JPopup
from jocular.RA_and_Dec import RA, Dec

from kivymd.uix.list import TwoLineListItem

Builder.load_string('''

<DSO_chooser>:
    dsos: _dsos
    pos_hint: {'top': .75, 'x': -100} 
    MDList:
        id: _dsos

<MyTextField@MDTextField>:
    current_hint_text_color: app.hint_color
    size_hint: (None, None)
    height: '28dp'
    width: '100dp'
    helper_text_mode: 'on_focus'        
    color_mode: 'accent'
    font_size: app.form_font_size # '20sp'

<DSOBoxLayout@BoxLayout>:
    size_hint: (1, None)
    height: '36dp'

<DSO_panel>:
    name_field: _name
    padding: '10dp'
    adaptive_height: True
    #adaptive_width: True
    pos_hint: {'top': .99, 'x': 0} if root.dso.show_DSO else {'top': .99, 'right': -1000} 
    size_hint: None, None
    orientation: 'vertical'

    BoxLayout:
        size_hint: (1, None)
        height: '48dp'

        MyTextField:
            id: _name
            width: '300dp'
            height: '32dp'
            helper_text: 'DSO'
            hint_text: 'dso'
            on_text: root.dso.Name_changed(self.text)
            font_size: '{:}sp'.format(int(app.form_font_size[:-2]) + 8) # 28sp

    DSOBoxLayout:
        MyTextField:
            hint_text: 'type'
            helper_text: 'e.g. PN, GX'
            on_focus: root.dso.OT_changed(self) if not self.focus else None
            text: root.dso.OT
        MyTextField:
            hint_text: 'con'
            helper_text: 'e.g. PER'
            on_focus: root.dso.Con_changed(self) if not self.focus else None
            text: root.dso.Con

    DSOBoxLayout:
        MyTextField:
            hint_text: 'RA'
            helper_text: "e.g. 21h30'42"
            on_focus: root.dso.RA_changed(self) if not self.focus else None
            text: root.dso.RA
        MyTextField:
            hint_text: 'dec'
            helper_text: "-3 21' 4"
            on_focus: root.dso.Dec_changed(self) if not self.focus else None
            text: root.dso.Dec

    DSOBoxLayout:
        MyTextField:
            hint_text: 'diam'
            helper_text: "e.g. 21'"
            on_focus: root.dso.Diam_changed(self) if not self.focus else None
            text: root.dso.Diam

        MyTextField:
            hint_text: 'mag'
            helper_text: "e.g. 14.1"
            on_focus: root.dso.Mag_changed(self) if not self.focus else None
            text: root.dso.Mag

    DSOBoxLayout:
        MyTextField:
            width: '200dp'
            hint_text: 'other'
            helper_text: ""
            on_focus: root.dso.Other_changed(self) if not self.focus else None
            text: root.dso.Other
''')


class DSO_chooser(ScrollView):

    ''' simple class representing popup of object type
        options in the case of ambiguous object name
    '''

    def __init__(self, dso, **kwargs):
        self.dso = dso
        super().__init__(**kwargs)


class DSO_panel(MDBoxLayout):

    ''' visual representation of editable DSO properties
    '''

    def __init__(self, dso, **kwargs):
        self.dso = dso
        super().__init__(**kwargs)


class DSO(Component):

    save_settings = ['show_DSO']

    Name = StringProperty('')
    Con = StringProperty('')
    RA = StringProperty('')
    Dec = StringProperty('')
    OT = StringProperty('')
    Mag = StringProperty('')
    Diam = StringProperty('')
    Other = StringProperty('')
    otypes = DictProperty({})

    props = ['Name', 'Con', 'OT', 'RA', 'Dec', 'Mag', 'Diam', 'Other']

    show_DSO = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        otypes = Component.get('Catalogues').get_object_types()
        self.otypes = {k: v['name'] for k, v in otypes.items()}
        self.dso_panel = DSO_panel(self)
        self.app.gui.add_widget(self.dso_panel)
        self.dso_chooser = DSO_chooser(self)
        self.app.gui.add_widget(self.dso_chooser)
        logger.debug('initialised')

    def on_new_object(self, settings=None):
        ''' Called whenever user selects new object *or previous object*. 
            Also called when user selects a row from the DSO table (in 
            which case setttings is not None).
        '''

        if settings is None:
            self.settings = Component.get('Metadata').get({'Name', 'OT'})
            self._new_object()
        else:
            ''' Ask user for confirmation that they wish to rename the object
            '''
            self.settings = settings
            if self.Name:
                self.popup = JPopup(
                    title='Change name to {:}?'.format(settings['Name']),
                    actions={
                        'Cancel': self.cancel_name_change,
                        'Yes': self.confirmed_name_change,
                    },
                )
                self.popup.open()
            else:
                self.confirmed_name_change()

    def confirmed_name_change(self, *args):
        # self.changed = not Component.get('Stacker').is_empty()
        self._new_object()

    def cancel_name_change(self, *args):
        pass

    def _new_object(self, *args):
        ''' Helper method called after normal new object selection or confirmation
            of change of name
        '''
        settings = self.settings

        if 'Name' in settings and 'OT' in settings:
            #  translate a few cases to new OTs
            nm = settings['Name']
            ot = settings['OT'].upper()
            # deal with some legacies from v1
            if ot == 'G+':
                if nm.startswith('Arp') or nm.startswith('VV') or nm.startswith('AM '):
                    ot = 'PG'
                elif (
                    nm.startswith('Hick')
                    or nm.startswith('PCG')
                    or nm.startswith('SHK')
                ):
                    ot = 'CG'
            lookup_settings = Component.get('ObservingList').lookup_name(
                '{:}/{:}'.format(nm, ot)
            )
            if lookup_settings is not None:
                settings = lookup_settings

        # handle nans
        for k in {'RA', 'Dec', 'Mag', 'Diam'}:
            if k in settings and math.isnan(float(settings[k])):
                settings[k] = ''

        # extract settings (which also updates display)
        for p in self.props:
            setattr(self, p, str(settings.get(p, '')))

        # store initial values so we can check for changes 
        self.initial_values = {p: getattr(self, p) for p in self.props}

        self.new_values = {}

        # update display of Name separately
        self.dso_panel.name_field.text = self.Name


    ''' Name is changed as soon as the text is altered to allow lookup
        while other properties are changed on defocus
    '''

    @logger.catch()
    def Name_changed(self, val, *args):
        #self.dso_chooser.dsos.clear_widgets()
        #self.dso_chooser.x = -1000
        # lookup
        OTs = Component.get('ObservingList').lookup_OTs(val)

        # if unique match, fill in
        if len(OTs) ==  1:
            self.exact_match(val + '/' + OTs[0])
            return

        # clear all but name field to signal ambiguity
        for p in set(self.props) - {'Name'}:
            setattr(self, p, '')

        if len(OTs) > 1:
            self.dso_chooser.pos_hint = {'top': .75, 'x': 0} 
            self.dso_chooser.dsos.clear_widgets()
            for ot in OTs:
                self.dso_chooser.dsos.add_widget(
                    TwoLineListItem(
                        text=val, secondary_text=ot,
                        on_press=partial(self.choose_match, val + '/' + ot)))

    def choose_match(self, val, *args):
        self.exact_match(val)
        self.dso_chooser.dsos.clear_widgets()        
        self.dso_chooser.pos_hint = {'top': .75, 'x': -100} 

    def exact_match(self, m):
        settings = Component.get('ObservingList').lookup_name(m)
        for p in self.props:
            setattr(self, p, str(settings.get(p, '')))
        self.check_for_change()

    def OT_changed(self, widget):
        ''' For the moment we allow any object type but in the future
            could check if one of known types and allow user to
            introduce a new type via a dialog
        '''
        widget.current_hint_text_color = self.app.hint_color
        ot = widget.text.upper()
        if len(ot) > 3:
            widget.current_hint_text_color = [1, 0, 0, 1]
        else:
            self.OT = ot
            self.new_values['OT'] = ot
            self.check_for_change() 

    def Con_changed(self, widget):
        ''' Likewise, we should check constellations in future
        '''
        widget.current_hint_text_color = self.app.hint_color
        con = widget.text.upper()
        if len(con) > 3:
            widget.current_hint_text_color = [1, 0, 0, 1]
        else:
            self.Con = con
            self.new_values['Con'] = con
            self.check_for_change() 

    @logger.catch()
    def RA_changed(self, widget):
        '''
        '''
        widget.current_hint_text_color = self.app.hint_color
        RA_str = widget.text.strip()
        if not RA_str:
            return
        ra_deg = RA.parse(RA_str)
        if ra_deg is None:
            widget.current_hint_text_color = [1, 0, 0, 1]
        else:
            self.RA = '-'  # need to force an update
            self.RA = str(RA(ra_deg))
            self.new_values['RA'] = self.RA
            self.check_for_change() 

    def Dec_changed(self, widget):
        widget.current_hint_text_color = self.app.hint_color
        Dec_str = widget.text.strip()
        if not Dec_str:
            return
        dec_deg = Dec.parse(Dec_str)
        if dec_deg is None:
            widget.current_hint_text_color = [1, 0, 0, 1]
        else:
            self.Dec = '-'  # need to force an update
            self.Dec = str(Dec(dec_deg))
            self.new_values['Dec'] = self.Dec
            self.check_for_change() 

    def Mag_changed(self, widget):
        ''' should be a int or float
        '''
        widget.current_hint_text_color = self.app.hint_color
        mag_str = widget.text.strip()
        if not mag_str:
            return
        try:
            mag = str(float(mag_str))
            self.Mag = '-'
            self.Mag = mag
            self.new_values['Mag'] = mag_str
            self.check_for_change() 
        except:
            widget.current_hint_text_color = [1, 0, 0, 1]

    def Diam_changed(self, widget):
        ''' Suffix can be d or degree symbol, ' or "
            assume arcmin if no suffix
        '''
        widget.current_hint_text_color = self.app.hint_color
        diam = widget.text.strip()
        if not diam:
            return
        try:
            if diam.endswith('d') or diam.endswith('\u00b0'):
                diam = float(diam[:-1]) * 60
            elif diam.endswith('"'):
                diam = float(diam[:-1]) / 60
            elif diam.endswith("'"):
                diam = float(diam[:-1])
            else:
                diam = float(diam)
            self.Diam = self.diam_str(diam)
            self.new_values['Diam'] = str(diam)
            self.check_for_change() 
        except Exception as e:
            logger.exception(e)
            widget.current_hint_text_color = [1, 0, 0, 1]

    def diam_str(self, diam):
        if diam > 60:
            return "{:.2f}\u00b0".format(diam / 60)
        if diam < 1:
            return '{:.2f}"'.format(diam * 60)
        return "{:.2f}'".format(diam)

    def Other_changed(self, widget):
        self.Other = widget.text.strip()
        self.new_values['Other'] = self.Other
        self.check_for_change() 
 
    @logger.catch()
    def check_for_change(self):
        ''' Check if any property has changed and stack is not empty
        '''
        changes = []
        for k, v in self.initial_values.items():
            if k in self.new_values and self.new_values[k] != v:
                changes += [True]

        # tell gui about any changes
        self.app.gui.has_changed('DSO', any(changes))

    @logger.catch()
    def on_save_object(self):

        ''' On saving we ensure that Name, OT and Con is saved as these 
            appear in the previous object table; other props don't need to
            be saved as they are looked up from the DSO database on each
            load.
        '''
        Component.get('Metadata').set(
            {'Name': self.Name.strip(), 'OT': self.OT, 'Con': self.Con}
        )

        ''' If there have been any changes update user objects catalogue
        '''

        props = {p: getattr(self, p) for p in self.props}

        # convert RA/Dec etc
        if 'RA' in props:
            props['RA'] = RA.parse(props['RA'])
        if 'Dec' in props:
            props['Dec'] = Dec.parse(props['Dec'])
        if 'Diam' in self.props:
            try:
                diam = float(props['Diam'])
            except:
                diam = float(props['Diam'][:-1])  # remove units
            props['Diam'] = diam

        Component.get('Catalogues').update_user_catalogue(props)


    def current_object_coordinates(self):
        if self.RA and self.Dec:
            return (float(RA(self.RA)), float(Dec(self.Dec)))
        return None, None

    # def paste_RA(self, *args):
    #     Clipboard.copy(self.RA)

