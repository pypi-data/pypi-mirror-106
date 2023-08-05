from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	def get(self, index: int) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:TTIMe:ALL \n
		Snippet: value: List[float] = driver.source.sequencer.listPy.ttime.all.get(index = 1) \n
		Queries the transition times for all sequencer list entries. \n
			:param index: Comma-separated list of values, one value per list entry Range: 0 s to 500E-6 s, Unit: s
			:return: trans_time: Comma-separated list of values, one value per list entry Range: 0 s to 500E-6 s, Unit: s"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_bin_or_ascii_float_list(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:TTIMe:ALL? {param}')
		return response
