from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reliability:
	"""Reliability commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("reliability", core, parent)

	def get(self, index: int) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RELiability \n
		Snippet: value: int = driver.source.sequencer.apool.reliability.get(index = 1) \n
		Queries the reliability indicator for the ARB file with the specified <Index>. For possible values, see 'Reliability
		Indicator'. \n
			:param index: Reliability indicator as decimal value
			:return: reliability: Reliability indicator as decimal value"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RELiability? {param}')
		return Conversions.str_to_int(response)
