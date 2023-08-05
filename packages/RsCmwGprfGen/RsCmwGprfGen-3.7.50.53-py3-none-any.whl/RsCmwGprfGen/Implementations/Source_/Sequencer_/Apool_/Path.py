from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("path", core, parent)

	def get_all(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:PATH:ALL \n
		Snippet: value: List[str] = driver.source.sequencer.apool.path.get_all() \n
		Queries the path and file name of the ARB files in the file pool. \n
			:return: path: Comma-separated list of strings, one string per file String example: 'C:/ProgramData/Rohde-Schwarz/CMW/Data/waveform/myARBfile.wv'
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:PATH:ALL?')
		return Conversions.str_to_str_list(response)

	def get(self, index: int) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:PATH \n
		Snippet: value: str = driver.source.sequencer.apool.path.get(index = 1) \n
		Queries the path and file name of the ARB file with the specified <Index>. \n
			:param index: String, for example: 'C:/ProgramData/Rohde-Schwarz/CMW/Data/waveform/myARBfile.wv'
			:return: path: String, for example: 'C:/ProgramData/Rohde-Schwarz/CMW/Data/waveform/myARBfile.wv'"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:PATH? {param}')
		return trim_str_response(response)
