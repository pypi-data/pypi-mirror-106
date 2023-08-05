from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 156 total commands, 7 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("source", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_state'):
			from .Source_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def iqSettings(self):
		"""iqSettings commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_iqSettings'):
			from .Source_.IqSettings import IqSettings
			self._iqSettings = IqSettings(self._core, self._base)
		return self._iqSettings

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Source_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def arb(self):
		"""arb commands group. 6 Sub-classes, 10 commands."""
		if not hasattr(self, '_arb'):
			from .Source_.Arb import Arb
			self._arb = Arb(self._core, self._base)
		return self._arb

	@property
	def dtone(self):
		"""dtone commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtone'):
			from .Source_.Dtone import Dtone
			self._dtone = Dtone(self._core, self._base)
		return self._dtone

	@property
	def listPy(self):
		"""listPy commands group. 13 Sub-classes, 8 commands."""
		if not hasattr(self, '_listPy'):
			from .Source_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def sequencer(self):
		"""sequencer commands group. 5 Sub-classes, 4 commands."""
		if not hasattr(self, '_sequencer'):
			from .Source_.Sequencer import Sequencer
			self._sequencer = Sequencer(self._core, self._base)
		return self._sequencer

	# noinspection PyTypeChecker
	def get_bb_mode(self) -> enums.BasebandMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:BBMode \n
		Snippet: value: enums.BasebandMode = driver.source.get_bb_mode() \n
		Selects the baseband mode for the generator signal. \n
			:return: baseband_mode: CW | DTONe | ARB CW: Unmodulated CW signal DTONe: Dual-tone signal (see commands SOURce:GPRF:GENi:DTONe...) ARB: ARB generator (waveform file; see method RsCmwGprfGen.Source.Arb.File.set)
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:BBMode?')
		return Conversions.str_to_scalar_enum(response, enums.BasebandMode)

	def set_bb_mode(self, baseband_mode: enums.BasebandMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:BBMode \n
		Snippet: driver.source.set_bb_mode(baseband_mode = enums.BasebandMode.ARB) \n
		Selects the baseband mode for the generator signal. \n
			:param baseband_mode: CW | DTONe | ARB CW: Unmodulated CW signal DTONe: Dual-tone signal (see commands SOURce:GPRF:GENi:DTONe...) ARB: ARB generator (waveform file; see method RsCmwGprfGen.Source.Arb.File.set)
		"""
		param = Conversions.enum_scalar_to_str(baseband_mode, enums.BasebandMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:BBMode {param}')

	def clone(self) -> 'Source':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Source(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
