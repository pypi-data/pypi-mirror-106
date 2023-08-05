from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clist:
	"""Clist commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("clist", core, parent)

	def set(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:UDMarker:CLISt \n
		Snippet: driver.source.arb.udMarker.clist.set() \n
		Clears the user-defined marker list, i.e. resets the method RsCmwGprfGen.Source.Arb.UdMarker.value command and sets the
		'Period' equal to the number of samples in the loaded waveform file. If no waveform file is loaded, the 'Period' is reset
		to 1. \n
		"""
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:UDMarker:CLISt')

	def set_with_opc(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:UDMarker:CLISt \n
		Snippet: driver.source.arb.udMarker.clist.set_with_opc() \n
		Clears the user-defined marker list, i.e. resets the method RsCmwGprfGen.Source.Arb.UdMarker.value command and sets the
		'Period' equal to the number of samples in the loaded waveform file. If no waveform file is loaded, the 'Period' is reset
		to 1. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwGprfGen.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:ARB:UDMarker:CLISt')
