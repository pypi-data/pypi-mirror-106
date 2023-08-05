
from functools import partial
from plyer import filechooser
from loguru import logger

from kivy.metrics import dp
from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
#from kivy.uix.slider import Slider
from kivymd.uix.slider import MDSlider
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from jocular.widgets import LabelL, LabelR


from kivy.lang import Builder

@logger.catch()
def configurable_to_widget(text=None, name=None, spec=None, initval=None, helptext=None,
	changed=None):
	''' creates a widget and its handler, which calls function 'changed' on any change
	'''

	font_size = '16sp'
	help_font_size = '15sp'
	textwidth = dp(280)
	widgetwidth = dp(130)
	# color = App.get_running_app().highlight_color
	color = App.get_running_app().theme_cls.accent_color

	bv = BoxLayout(padding=(dp(5), dp(5)), size_hint=(1, None), height=dp(60), 
		orientation='vertical')
	bh = BoxLayout(size_hint=(1, .55))
	bh.add_widget(Label(size_hint=(1, 1)))
	bh.add_widget(LabelR(text=text, size_hint=(None, 1), width=textwidth, font_size=font_size))

	# bh = BoxLayout(size_hint=(prop_width, 1))

	if 'options' in spec:
		opts = spec['options']
		widget = Spinner(text=initval, values=spec['options'], 
			size_hint=(None, 1), width=widgetwidth, font_size=font_size)
		widget.bind(text=partial(__option_changed, name, spec, changed))
		bh.add_widget(widget)
		bh.add_widget(Label(size_hint=(None, 1), width=widgetwidth))

	elif 'boolean' in spec:
		opts = spec['boolean'].keys()
		# lookup names e.g. yes/no for true or false
		val = {v: k for k, v in spec['boolean'].items()}[initval]
		widget = Spinner(text=val, values=opts, size_hint=(None, 1), width=widgetwidth, 
			font_size=font_size)
		widget.bind(text=partial(__boolean_changed, name, spec, changed))
		bh.add_widget(widget)
		bh.add_widget(Label(size_hint=(None, 1), width=widgetwidth))

	elif 'switch' in spec:
		widget = MDSwitch(size_hint=(None, 1), width=widgetwidth, active=initval,
			pos_hint={'center_x': .5, 'center_y': .5})
		widget.bind(active=partial(__switch_changed, name, spec, changed))
		bh.add_widget(widget)
		bh.add_widget(Label(size_hint=(None, 1), width=widgetwidth - dp(36)))
		bh.add_widget(Label(size_hint=(None, 1), width=widgetwidth))

	elif 'float' in spec:
		fmt = spec.get('fmt', '{:.2f}')
		slabel = LabelL(text=fmt.format(initval), size_hint=(None, 1), width=widgetwidth, 
			font_size=font_size, color=color)
		bh.add_widget(slabel)
		smin, smax, step = spec['float']
		# widget = Slider(size_hint=(None, 1), width=widgetwidth, 
		# 	step=step, min=smin, max=smax, value=float(initval))
		widget = MDSlider(size_hint=(None, 1), width=widgetwidth, 
			step=step, min=smin, max=smax, value=float(initval))
		widget.hint_bg_color=(.6,.6,.6,1)
		widget._set_colors()
		widget.bind(value=partial(__sfloat_changed, name, spec, slabel, fmt, changed))
		bh.add_widget(widget)

	elif 'action' in spec:
		widget = Button(text=spec['button'], size_hint=(None, 1), width=widgetwidth, 
			font_size=font_size)
		widget.bind(on_press=partial(__action_pressed, name, spec, changed))
		bh.add_widget(widget)
		bh.add_widget(Label(size_hint=(None, 1), width=widgetwidth))

	elif 'filechooser' in spec:
		widget = Button(text='choose...', size_hint=(None, 1), width=widgetwidth,
		 font_size=font_size)
		widget.bind(on_press=partial(__filechooser_pressed, name, spec, changed))
		bh.add_widget(widget)
		bh.add_widget(Label(size_hint=(None, 1), width=widgetwidth))

	bh.add_widget(Label(size_hint=(1, 1)))

	# lower row contains only help text
	blow = BoxLayout(size_hint=(1, .45))
	blow.add_widget(Label(text=helptext, size_hint=(1, 1),
		font_size=help_font_size, color=(.5, .5, .5, 1)))
	bv.add_widget(bh)
	bv.add_widget(blow)

	return bv


def __sfloat_changed(name, spec, slabel, fmt, changed, slider, *args):
	slabel.text = fmt.format(slider.value)
	changed(name, slider.value, spec)

def __option_changed(name, spec, changed, widget, value, *args):
	changed(name, value, spec)

def __boolean_changed(name, spec, changed, widget, value, *args):
	changed(name, spec['boolean'][value], spec)

@logger.catch()
def __switch_changed(name, spec, changed, widget, *args):
	changed(name, widget.active, spec)

def __action_pressed(name, spec, changed, widget, *args):
	changed(name, spec['action'], spec)

def __filechooser_pressed(name, spec, changed, *args):
	filechooser.choose_dir(
		on_selection=partial(__handle_selection, name, changed, spec),
		multiple=False)

def __handle_selection(name, changed, spec, selection):
	changed(name, selection[0], spec)

# 	try:
# 		widget.text = 'processing...'
# 		self.current_action_widget = widget
# 		getattr(self.current_settings, pspec['action'])(
# 			success_callback=partial(__action_succeeded, widget),
# 			failure_callback=partial(__action_failed, widget))
# 	except Exception as e:
# 		logger.exception(e)

# def action_succeeded(self, message, *args):
# 	self.current_action_widget.text = message

# def action_failed(self, message, *args):
# 	self.current_action_widget.text = message

