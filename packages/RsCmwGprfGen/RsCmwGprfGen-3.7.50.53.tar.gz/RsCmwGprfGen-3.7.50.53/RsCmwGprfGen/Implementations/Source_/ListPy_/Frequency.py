from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	def set(self, index: int, frequency: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:FREQuency \n
		Snippet: driver.source.listPy.frequency.set(index = 1, frequency = 1.0) \n
		Defines or queries the frequency of a selected frequency/level step. \n
			:param index: Number of the frequency/level step in the table Range: 0 to 1999
			:param frequency: Frequency of the frequency/level step Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('frequency', frequency, DataType.Float))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:FREQuency {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:FREQuency \n
		Snippet: value: float = driver.source.listPy.frequency.get(index = 1) \n
		Defines or queries the frequency of a selected frequency/level step. \n
			:param index: Number of the frequency/level step in the table Range: 0 to 1999
			:return: frequency: Frequency of the frequency/level step Range: 70 MHz to 6 GHz, Unit: Hz"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:LIST:FREQuency? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:FREQuency:ALL \n
		Snippet: value: List[float] = driver.source.listPy.frequency.get_all() \n
		Defines the frequencies of all frequency/level steps. \n
			:return: all_frequencies: Comma-separated list of n values, one per frequency/level step, where n 2001. The query returns 2000 results. Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:GPRF:GENerator<Instance>:LIST:FREQuency:ALL?')
		return response

	def set_all(self, all_frequencies: List[float]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:FREQuency:ALL \n
		Snippet: driver.source.listPy.frequency.set_all(all_frequencies = [1.1, 2.2, 3.3]) \n
		Defines the frequencies of all frequency/level steps. \n
			:param all_frequencies: Comma-separated list of n values, one per frequency/level step, where n 2001. The query returns 2000 results. Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.list_to_csv_str(all_frequencies)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:FREQuency:ALL {param}')
