from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 32 total commands, 13 Sub-groups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .ListPy_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	@property
	def slist(self):
		"""slist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slist'):
			from .ListPy_.Slist import Slist
			self._slist = Slist(self._core, self._base)
		return self._slist

	@property
	def esingle(self):
		"""esingle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_esingle'):
			from .ListPy_.Esingle import Esingle
			self._esingle = Esingle(self._core, self._base)
		return self._esingle

	@property
	def rlist(self):
		"""rlist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlist'):
			from .ListPy_.Rlist import Rlist
			self._rlist = Rlist(self._core, self._base)
		return self._rlist

	@property
	def increment(self):
		"""increment commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_increment'):
			from .ListPy_.Increment import Increment
			self._increment = Increment(self._core, self._base)
		return self._increment

	@property
	def sstop(self):
		"""sstop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sstop'):
			from .ListPy_.Sstop import Sstop
			self._sstop = Sstop(self._core, self._base)
		return self._sstop

	@property
	def rfLevel(self):
		"""rfLevel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rfLevel'):
			from .ListPy_.RfLevel import RfLevel
			self._rfLevel = RfLevel(self._core, self._base)
		return self._rfLevel

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .ListPy_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def irepetition(self):
		"""irepetition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_irepetition'):
			from .ListPy_.Irepetition import Irepetition
			self._irepetition = Irepetition(self._core, self._base)
		return self._irepetition

	@property
	def dgain(self):
		"""dgain commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dgain'):
			from .ListPy_.Dgain import Dgain
			self._dgain = Dgain(self._core, self._base)
		return self._dgain

	@property
	def dtime(self):
		"""dtime commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dtime'):
			from .ListPy_.Dtime import Dtime
			self._dtime = Dtime(self._core, self._base)
		return self._dtime

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_modulation'):
			from .ListPy_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def reenabling(self):
		"""reenabling commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_reenabling'):
			from .ListPy_.Reenabling import Reenabling
			self._reenabling = Reenabling(self._core, self._base)
		return self._reenabling

	def get_aindex(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:AINDex \n
		Snippet: value: int = driver.source.listPy.get_aindex() \n
		Returns the currently active list index. \n
			:return: active_index: Range: 0 to 19
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:AINDex?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	class FillStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Start_Index: float: The start index of the list segment to be 'filled'. Range: 0 to 1999
			- Range_Py: float: The range (length) of the list segment to be 'filled'. Range: 1 to 2000
			- Index_Repetition: int: The constant 'Index Repetition' within this list segment. Range: 1 to 10000
			- Start_Frequency: float: The frequency of list item StartIndex. Range: 70 MHz to 6 GHz , Unit: Hz
			- Freq_Increment: float: The frequency increment within this list segment. Range: -282.45 MHz to 1.20005 GHz , Unit: Hz
			- Start_Power: float: The RMS level of list item StartIndex. Range: Depends on the instrument model, the connector and other settings; please notice the ranges quoted in the data sheet , Unit: dBm
			- Power_Increment: float: The power increment within this list segment. Range: -29.5 dBm to 3 dBm , Unit: dBm
			- Start_Dwell_Time: float: Optional setting parameter. The constant dwell time within this list segment. Range: 2.0E-4 s to 20 s , Unit: s
			- Reenable: bool: Optional setting parameter. OFF | ON The constant 'Reenable' property within this list segment.
			- Modulation: bool: Optional setting parameter. OFF | ON The constant 'Modulation ON|OFF' property within this list segment.
			- Start_Gain: float: Optional setting parameter. The digital gain of list item StartIndex. Range: -30 dB to 0 dB , Unit: dB
			- Gain_Increment: float: Optional setting parameter. The digital gain increment within this list segment. Range: -7.5 dB to 0 dB , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Start_Index'),
			ArgStruct.scalar_float('Range_Py'),
			ArgStruct.scalar_int('Index_Repetition'),
			ArgStruct.scalar_float('Start_Frequency'),
			ArgStruct.scalar_float('Freq_Increment'),
			ArgStruct.scalar_float('Start_Power'),
			ArgStruct.scalar_float('Power_Increment'),
			ArgStruct.scalar_float_optional('Start_Dwell_Time'),
			ArgStruct.scalar_bool_optional('Reenable'),
			ArgStruct.scalar_bool_optional('Modulation'),
			ArgStruct.scalar_float_optional('Start_Gain'),
			ArgStruct.scalar_float_optional('Gain_Increment')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: float = None
			self.Range_Py: float = None
			self.Index_Repetition: int = None
			self.Start_Frequency: float = None
			self.Freq_Increment: float = None
			self.Start_Power: float = None
			self.Power_Increment: float = None
			self.Start_Dwell_Time: float = None
			self.Reenable: bool = None
			self.Modulation: bool = None
			self.Start_Gain: float = None
			self.Gain_Increment: float = None

	def set_fill(self, value: FillStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:FILL \n
		Snippet: driver.source.listPy.set_fill(value = FillStruct()) \n
		Convenience command to simplify the configuration of the frequency/level list. Within a list segment determined by its
		start index and range (length) , the frequency, power and (optionally) the digital gain are incremented by configurable
		step sizes. The other list item settings are fixed. \n
			:param value: see the help for FillStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:LIST:FILL', value)

	def get_goto(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:GOTO \n
		Snippet: value: int = driver.source.listPy.get_goto() \n
		Defines the start index for the second and all following generator cycles in continuous mode (method RsCmwGprfGen.Source.
		ListPy.repetition) . The index must be in the selected list section (method RsCmwGprfGen.Source.ListPy.Sstop.set) . \n
			:return: goto_index: Range: 1 to 2000
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:GOTO?')
		return Conversions.str_to_int(response)

	def set_goto(self, goto_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:GOTO \n
		Snippet: driver.source.listPy.set_goto(goto_index = 1) \n
		Defines the start index for the second and all following generator cycles in continuous mode (method RsCmwGprfGen.Source.
		ListPy.repetition) . The index must be in the selected list section (method RsCmwGprfGen.Source.ListPy.Sstop.set) . \n
			:param goto_index: Range: 1 to 2000
		"""
		param = Conversions.decimal_value_to_str(goto_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:GOTO {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepeatMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:REPetition \n
		Snippet: value: enums.RepeatMode = driver.source.listPy.get_repetition() \n
		Defines how often the RF generator runs through the list. \n
			:return: repetition: CONTinuous | SINGle CONTinuous: The generator cycles through the list. SINGle: The generator runs through the list for a single time. The sequence is triggered via method RsCmwGprfGen.Source.ListPy.Esingle.set.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepeatMode)

	def set_repetition(self, repetition: enums.RepeatMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:REPetition \n
		Snippet: driver.source.listPy.set_repetition(repetition = enums.RepeatMode.CONTinuous) \n
		Defines how often the RF generator runs through the list. \n
			:param repetition: CONTinuous | SINGle CONTinuous: The generator cycles through the list. SINGle: The generator runs through the list for a single time. The sequence is triggered via method RsCmwGprfGen.Source.ListPy.Esingle.set.
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepeatMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:REPetition {param}')

	def get_start(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:STARt \n
		Snippet: value: int = driver.source.listPy.get_start() \n
		Defines the number of the first measured frequency/level step in the list. The start index must not be larger than the
		stop index (see method RsCmwGprfGen.Source.ListPy.stop) . \n
			:return: start_index: Range: 0 to 1999
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:STARt \n
		Snippet: driver.source.listPy.set_start(start_index = 1) \n
		Defines the number of the first measured frequency/level step in the list. The start index must not be larger than the
		stop index (see method RsCmwGprfGen.Source.ListPy.stop) . \n
			:param start_index: Range: 0 to 1999
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:STOP \n
		Snippet: value: int = driver.source.listPy.get_stop() \n
		Defines the number of the last measured frequency/level step in the list. The stop index must not be smaller than the
		start index (see method RsCmwGprfGen.Source.ListPy.start) . \n
			:return: stop_index: Range: 0 to 1999
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:STOP \n
		Snippet: driver.source.listPy.set_stop(stop_index = 1) \n
		Defines the number of the last measured frequency/level step in the list. The stop index must not be smaller than the
		start index (see method RsCmwGprfGen.Source.ListPy.start) . \n
			:param stop_index: Range: 0 to 1999
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:STOP {param}')

	def get_count(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:COUNt \n
		Snippet: value: int = driver.source.listPy.get_count() \n
		Queries the number of frequency/level steps of the RF generator in list mode. \n
			:return: list_count: Number of frequency/level steps in list mode Range: 1 to 2000
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def get_value(self) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST \n
		Snippet: value: bool = driver.source.listPy.get_value() \n
		Enables or disables the list mode of the RF generator. \n
			:return: enable_list_mode: ON | OFF ON: List mode enabled OFF: List mode disabled (constant-frequency generator)
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable_list_mode: bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST \n
		Snippet: driver.source.listPy.set_value(enable_list_mode = False) \n
		Enables or disables the list mode of the RF generator. \n
			:param enable_list_mode: ON | OFF ON: List mode enabled OFF: List mode disabled (constant-frequency generator)
		"""
		param = Conversions.bool_to_str(enable_list_mode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
