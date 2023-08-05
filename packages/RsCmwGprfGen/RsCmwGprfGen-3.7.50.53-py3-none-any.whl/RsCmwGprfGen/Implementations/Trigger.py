from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 15 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trigger", core, parent)

	@property
	def arb(self):
		"""arb commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_arb'):
			from .Trigger_.Arb import Arb
			self._arb = Arb(self._core, self._base)
		return self._arb

	@property
	def sequencer(self):
		"""sequencer commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequencer'):
			from .Trigger_.Sequencer import Sequencer
			self._sequencer = Sequencer(self._core, self._base)
		return self._sequencer

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
