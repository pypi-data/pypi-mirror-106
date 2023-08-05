from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ttime:
	"""Ttime commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ttime", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .Ttime_.All import All
			self._all = All(self._core, self._base)
		return self._all

	def get(self, index: int) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:TTIMe \n
		Snippet: value: float = driver.source.sequencer.listPy.ttime.get(index = 1) \n
		Queries the transition time for the sequencer list entry with the selected <Index>. \n
			:param index: Range: 0 s to 500E-6 s, Unit: s
			:return: trans_time: Range: 0 s to 500E-6 s, Unit: s"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:TTIMe? {param}')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Ttime':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ttime(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
