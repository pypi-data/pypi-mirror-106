from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sstop:
	"""Sstop commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sstop", core, parent)

	def set(self, start_index: int, stop_index: int, goto_index: int = None) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:SSTop \n
		Snippet: driver.source.listPy.sstop.set(start_index = 1, stop_index = 1, goto_index = 1) \n
		Defines the first and last generated frequency/level steps in list mode. \n
			:param start_index: Range: 0 to min{StopIndex,1999}
			:param stop_index: Range: StartIndex to 1999
			:param goto_index: The start index for all but the first generator cycle in continuous mode. See also method RsCmwGprfGen.Source.ListPy.goto. Range: StartIndex to StopIndex
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start_index', start_index, DataType.Integer), ArgSingle('stop_index', stop_index, DataType.Integer), ArgSingle('goto_index', goto_index, DataType.Integer, True))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:SSTop {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Start_Index: int: Range: 0 to min{StopIndex,1999}
			- Stop_Index: int: Range: StartIndex to 1999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Stop_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Stop_Index: int = None

	def get(self) -> GetStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:SSTop \n
		Snippet: value: GetStruct = driver.source.listPy.sstop.get() \n
		Defines the first and last generated frequency/level steps in list mode. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:GPRF:GENerator<Instance>:LIST:SSTop?', self.__class__.GetStruct())
