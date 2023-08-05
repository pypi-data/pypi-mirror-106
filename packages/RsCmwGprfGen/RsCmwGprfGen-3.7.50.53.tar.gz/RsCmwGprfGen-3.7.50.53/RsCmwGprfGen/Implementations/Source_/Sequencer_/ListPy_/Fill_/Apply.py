from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apply:
	"""Apply commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("apply", core, parent)

	def set(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:APPLy \n
		Snippet: driver.source.sequencer.listPy.fill.apply.set() \n
		Fills the sequencer list with a sequence of entries, as configured by the other SOURce:GPRF:GEN<i>:SEQuencer:LIST:FILL:...
		commands. \n
		"""
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:APPLy')

	def set_with_opc(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:APPLy \n
		Snippet: driver.source.sequencer.listPy.fill.apply.set_with_opc() \n
		Fills the sequencer list with a sequence of entries, as configured by the other SOURce:GPRF:GEN<i>:SEQuencer:LIST:FILL:...
		commands. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwGprfGen.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:APPLy')
