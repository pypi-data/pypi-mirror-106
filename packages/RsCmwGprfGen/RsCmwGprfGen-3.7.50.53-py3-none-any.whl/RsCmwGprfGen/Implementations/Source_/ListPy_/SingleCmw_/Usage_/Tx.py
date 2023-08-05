from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tx", core, parent)

	def set(self, index: int, usage: List[bool]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:CMWS:USAGe:TX \n
		Snippet: driver.source.listPy.singleCmw.usage.tx.set(index = 1, usage = [True, False, True]) \n
		Activates or deactivates the individual output connectors of connector benches for a selected entry of the GPRF generator
		list mode configuration. The settings apply to all available benches. For benches with 4 connectors, only the first 4
		values are relevant. \n
			:param index: Selects the entry of the list mode configuration Range: 0 to 1999
			:param usage: OFF | ON Comma-separated list of n values, for the first n connectors of all benches, range for n = 1 to 8 A query returns 4 or 8 values, depending on the currently used bench.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle.as_open_list('usage', usage, DataType.BooleanList))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:CMWS:USAGe:TX {param}'.rstrip())

	def get(self, index: int) -> List[bool]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:CMWS:USAGe:TX \n
		Snippet: value: List[bool] = driver.source.listPy.singleCmw.usage.tx.get(index = 1) \n
		Activates or deactivates the individual output connectors of connector benches for a selected entry of the GPRF generator
		list mode configuration. The settings apply to all available benches. For benches with 4 connectors, only the first 4
		values are relevant. \n
			:param index: Selects the entry of the list mode configuration Range: 0 to 1999
			:return: usage: OFF | ON Comma-separated list of n values, for the first n connectors of all benches, range for n = 1 to 8 A query returns 4 or 8 values, depending on the currently used bench."""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:LIST:CMWS:USAGe:TX? {param}')
		return Conversions.str_to_bool_list(response)
