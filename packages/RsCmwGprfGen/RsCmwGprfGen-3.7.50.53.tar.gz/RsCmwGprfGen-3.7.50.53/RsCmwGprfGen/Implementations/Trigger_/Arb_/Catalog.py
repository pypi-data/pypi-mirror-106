from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("catalog", core, parent)

	def get_source(self) -> List[str]:
		"""SCPI: TRIGger:GPRF:GENerator<Instance>:ARB:CATalog:SOURce \n
		Snippet: value: List[str] = driver.trigger.arb.catalog.get_source() \n
		Lists all available trigger sources, to be set via method RsCmwGprfGen.Trigger.Arb.source. The list depends on the
		installed options. \n
			:return: trigger_sources: Comma-separated list of all sources. Each value is a string (e.g. 'Manual' for manual trigger) .
		"""
		response = self._core.io.query_str('TRIGger:GPRF:GENerator<Instance>:ARB:CATalog:SOURce?')
		return Conversions.str_to_str_list(response)
