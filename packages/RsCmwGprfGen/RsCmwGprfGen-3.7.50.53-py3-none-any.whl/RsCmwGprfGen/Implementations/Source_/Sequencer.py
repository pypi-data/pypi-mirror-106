from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequencer:
	"""Sequencer commands group definition. 80 total commands, 5 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sequencer", core, parent)

	@property
	def apool(self):
		"""apool commands group. 12 Sub-classes, 8 commands."""
		if not hasattr(self, '_apool'):
			from .Sequencer_.Apool import Apool
			self._apool = Apool(self._core, self._base)
		return self._apool

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_state'):
			from .Sequencer_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def rfSettings(self):
		"""rfSettings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Sequencer_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def listPy(self):
		"""listPy commands group. 13 Sub-classes, 3 commands."""
		if not hasattr(self, '_listPy'):
			from .Sequencer_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def marker(self):
		"""marker commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_marker'):
			from .Sequencer_.Marker import Marker
			self._marker = Marker(self._core, self._base)
		return self._marker

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepeatMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition \n
		Snippet: value: enums.RepeatMode = driver.source.sequencer.get_repetition() \n
		Defines how often the sequencer list is processed. \n
			:return: repetition: CONTinuous | SINGle CONTinuous: Unlimited, cyclic processing SINGle: Single execution
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepeatMode)

	def set_repetition(self, repetition: enums.RepeatMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition \n
		Snippet: driver.source.sequencer.set_repetition(repetition = enums.RepeatMode.CONTinuous) \n
		Defines how often the sequencer list is processed. \n
			:param repetition: CONTinuous | SINGle CONTinuous: Unlimited, cyclic processing SINGle: Single execution
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepeatMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition {param}')

	def get_signal(self) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:SIGNal \n
		Snippet: value: bool = driver.source.sequencer.get_signal() \n
		Queries whether a signal is generated or not. \n
			:return: signal: OFF | ON
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:SIGNal?')
		return Conversions.str_to_bool(response)

	def get_centry(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:CENTry \n
		Snippet: value: int = driver.source.sequencer.get_centry() \n
		Queries the index of the processed entry. \n
			:return: current_entry: Index - if the sequencer is not running, NAV is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:CENTry?')
		return Conversions.str_to_int(response)

	def get_uoptions(self) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:UOPTions \n
		Snippet: value: str = driver.source.sequencer.get_uoptions() \n
		Queries a list of the used software options. \n
			:return: used_options: Single string containing a comma-separated list of options. If the sequencer is OFF, NAV is returned. If the sequencer is not OFF but no options are used by the sequencer list, 'None' is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:UOPTions?')
		return trim_str_response(response)

	def clone(self) -> 'Sequencer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sequencer(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
