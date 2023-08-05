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
			- Marker_2: int: Range: -10 to 4000
			- Marker_3: int: Range: -10 to 4000
			- Marker_4: int: Range: -10 to 4000
			- Restart_Marker: int: Range: 0 to max. (depending on waveform file)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Marker_2'),
			ArgStruct.scalar_int('Marker_3'),
			ArgStruct.scalar_int('Marker_4'),
			ArgStruct.scalar_int('Restart_Marker')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Marker_2: int = None
			self.Marker_3: int = None
			self.Marker_4: int = None
			self.Restart_Marker: int = None

	def get_delays(self) -> DelaysStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays \n
		Snippet: value: DelaysStruct = driver.source.arb.marker.get_delays() \n
		Defines delay times for the ARB output trigger events relative to the marker events. \n
			:return: structure: for return value, see the help for DelaysStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays?', self.__class__.DelaysStruct())

	def set_delays(self, value: DelaysStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays \n
		Snippet: driver.source.arb.marker.set_delays(value = DelaysStruct()) \n
		Defines delay times for the ARB output trigger events relative to the marker events. \n
			:param value: see the help for DelaysStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays', value)
