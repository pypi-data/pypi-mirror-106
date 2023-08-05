from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Increment:
	"""Increment commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("increment", core, parent)

	@property
	def enabling(self):
		"""enabling commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_enabling'):
			from .Increment_.Enabling import Enabling
			self._enabling = Enabling(self._core, self._base)
		return self._enabling

	def get_catalog(self) -> List[str]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:INCRement:CATalog \n
		Snippet: value: List[str] = driver.source.listPy.increment.get_catalog() \n
		Lists all list increment modes that can be set using method RsCmwGprfGen.Source.ListPy.Increment.value. \n
			:return: list_incr_srcs: Comma-separated list of strings. Each string represents a supported increment mode.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:INCRement:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:INCRement \n
		Snippet: value: str = driver.source.listPy.increment.get_value() \n
		Defines how the RF generator steps through the list. \n
			:return: list_incr_src: String parameter, specifies the source for the list increment. Examples: 'Dwell Time' The generator transmits at each frequency/level step for the selected dwell time (method RsCmwGprfGen.Source.ListPy.Dtime.set) 'GPRF Geni: some marker' List incremented by a marker in the played-back ARB file (only for baseband mode ARB, see method RsCmwGprfGen.Source.bbMode) 'Some measurement' (e.g. 'GPRF Measi: Power') List incremented in line with a running measurement Use method RsCmwGprfGen.Source.ListPy.Increment.catalog to query the list of possible sources for the current HW/SW configuration.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:INCRement?')
		return trim_str_response(response)

	def set_value(self, list_incr_src: str) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:INCRement \n
		Snippet: driver.source.listPy.increment.set_value(list_incr_src = '1') \n
		Defines how the RF generator steps through the list. \n
			:param list_incr_src: String parameter, specifies the source for the list increment. Examples: 'Dwell Time' The generator transmits at each frequency/level step for the selected dwell time (method RsCmwGprfGen.Source.ListPy.Dtime.set) 'GPRF Geni: some marker' List incremented by a marker in the played-back ARB file (only for baseband mode ARB, see method RsCmwGprfGen.Source.bbMode) 'Some measurement' (e.g. 'GPRF Measi: Power') List incremented in line with a running measurement Use method RsCmwGprfGen.Source.ListPy.Increment.catalog to query the list of possible sources for the current HW/SW configuration.
		"""
		param = Conversions.value_to_quoted_str(list_incr_src)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:INCRement {param}')

	def clone(self) -> 'Increment':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Increment(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
