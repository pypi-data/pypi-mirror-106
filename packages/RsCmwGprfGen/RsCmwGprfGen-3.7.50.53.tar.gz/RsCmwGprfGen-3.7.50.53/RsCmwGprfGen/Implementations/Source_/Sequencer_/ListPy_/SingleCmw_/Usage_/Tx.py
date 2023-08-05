from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tx", core, parent)

	def set(self, index: int, usage: List[bool]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:CMWS:USAGe:TX \n
		Snippet: driver.source.sequencer.listPy.singleCmw.usage.tx.set(index = 1, usage = [True, False, True]) \n
		Activates or deactivates the individual output connectors of a connector bench, for the sequencer list entry with the
		selected <Index>. \n
			:param index: No help available
			:param usage: OFF | ON Comma-separated list of eight values, one value per connector of the bench
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle.as_open_list('usage', usage, DataType.BooleanList))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:CMWS:USAGe:TX {param}'.rstrip())

	def get(self, index: int) -> List[bool]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:CMWS:USAGe:TX \n
		Snippet: value: List[bool] = driver.source.sequencer.listPy.singleCmw.usage.tx.get(index = 1) \n
		Activates or deactivates the individual output connectors of a connector bench, for the sequencer list entry with the
		selected <Index>. \n
			:param index: No help available
			:return: usage: OFF | ON Comma-separated list of eight values, one value per connector of the bench"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:CMWS:USAGe:TX? {param}')
		return Conversions.str_to_bool_list(response)
