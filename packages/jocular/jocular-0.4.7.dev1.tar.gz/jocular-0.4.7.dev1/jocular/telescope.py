''' telescope is really the mount of course...
'''


from kivy.properties import StringProperty
from jocular.component import Component
from jocular.devicemanager import DeviceFamily, Device

class Telescope(Component, DeviceFamily):

	modes = {
		'Manual': 'ManualTelescope', 
		'Simulator': 'SimulatorTelescope',
		'ASCOM': 'ASCOMTelescope'
	}
	default_mode = 'Manual'
	family = 'Telescope'

class GenericTelescope(Device):
	family = StringProperty('Telescope')

class ManualTelescope(GenericTelescope):
	pass

class SimulatorTelescope(GenericTelescope):
	pass

class ASCOMTelescope(GenericTelescope):
	pass

