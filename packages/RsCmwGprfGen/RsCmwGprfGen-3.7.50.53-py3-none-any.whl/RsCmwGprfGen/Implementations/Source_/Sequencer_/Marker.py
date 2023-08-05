from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Marker:
	"""Marker commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("marker", core, parent)

	# noinspection PyTypeChecker
	class DelaysStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Restart_Marker: float: Range: 0 s to 0.1 s, Unit: s
			- Marker_2: float: Range: 0 s to 0.1 s, Unit: s
			- Marker_3: float: Range: 0 s to 0.1 s, Unit: s
			- Marker_4: float: Range: 0 s to 0.1 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Restart_Marker'),
			ArgStruct.scalar_float('Marker_2'),
			ArgStruct.scalar_float('Marker_3'),
			ArgStruct.scalar_float('Marker_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Restart_Marker: float = None
			self.Marker_2: float = None
			self.Marker_3: float = None
			self.Marker_4: float = None

	def get_delays(self) -> DelaysStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays \n
		Snippet: value: DelaysStruct = driver.source.sequencer.marker.get_delays() \n
		Defines delay times for the ARB output trigger events relative to the marker events. \n
			:return: structure: for return value, see the help for DelaysStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays?', self.__class__.DelaysStruct())

	def set_delays(self, value: DelaysStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays \n
		Snippet: driver.source.sequencer.marker.set_delays(value = DelaysStruct()) \n
		Defines delay times for the ARB output trigger events relative to the marker events. \n
			:param value: see the help for DelaysStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays', value)
