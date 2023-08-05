from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Arb:
	"""Arb commands group definition. 28 total commands, 6 Sub-groups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("arb", core, parent)

	@property
	def samples(self):
		"""samples commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_samples'):
			from .Arb_.Samples import Samples
			self._samples = Samples(self._core, self._base)
		return self._samples

	@property
	def udMarker(self):
		"""udMarker commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_udMarker'):
			from .Arb_.UdMarker import UdMarker
			self._udMarker = UdMarker(self._core, self._base)
		return self._udMarker

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_file'):
			from .Arb_.File import File
			self._file = File(self._core, self._base)
		return self._file

	@property
	def msegment(self):
		"""msegment commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_msegment'):
			from .Arb_.Msegment import Msegment
			self._msegment = Msegment(self._core, self._base)
		return self._msegment

	@property
	def marker(self):
		"""marker commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_marker'):
			from .Arb_.Marker import Marker
			self._marker = Marker(self._core, self._base)
		return self._marker

	@property
	def segments(self):
		"""segments commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_segments'):
			from .Arb_.Segments import Segments
			self._segments = Segments(self._core, self._base)
		return self._segments

	def get_foffset(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:FOFFset \n
		Snippet: value: float = driver.source.arb.get_foffset() \n
		Sets/gets the frequency offset to be imposed at the baseband during ARB generation. In the standalone scenario, the
		offset results in an equivalent frequency offset at the RF. \n
			:return: frequency_offset: Range: -40E+6 to +40E+6, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, frequency_offset: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:FOFFset \n
		Snippet: driver.source.arb.set_foffset(frequency_offset = 1.0) \n
		Sets/gets the frequency offset to be imposed at the baseband during ARB generation. In the standalone scenario, the
		offset results in an equivalent frequency offset at the RF. \n
			:param frequency_offset: Range: -40E+6 to +40E+6, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency_offset)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:FOFFset {param}')

	# noinspection PyTypeChecker
	class ScountStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sample_Count_Time: float: No parameter help available
			- Sample_Count: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Sample_Count_Time'),
			ArgStruct('Sample_Count', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sample_Count_Time: float = None
			self.Sample_Count: List[int] = None

	def get_scount(self) -> ScountStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SCOunt \n
		Snippet: value: ScountStruct = driver.source.arb.get_scount() \n
		Queries the progress of ARB file processing.
			INTRO_CMD_HELP: During ARB file processing, the command behavior depends on the instrument model as follows: \n
			- R&S CMW100/CMW with MUA As long as the ARB file is processed, the command returns 0,0,0. In continuous mode, the command always returns 0,0,0. You can use the command to check in single-shot mode whether ARB file processing is complete.
			- R&S CMW500/2xx with BB Meas As long as the ARB file is processed, the command evaluates the position of the currently processed sample within the ARB file and returns corresponding results. The remote query takes between 2 ms and 3 ms, which introduces an uncertainty to the results. You can use the command to check the progress in single-shot mode and in continuous mode.
		If ARB file processing is complete, the command returns results for the previous ARB file processing. \n
			:return: structure: for return value, see the help for ScountStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:ARB:SCOunt?', self.__class__.ScountStruct())

	def get_asamples(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:ASAMples \n
		Snippet: value: int = driver.source.arb.get_asamples() \n
		Extends the processing time of a waveform file by the specified number of samples. The additional samples are valid in
		single-shot repetition mode only (see method RsCmwGprfGen.Source.Arb.repetition) . \n
			:return: add_samples: Range: 0 to max. (depending on waveform file)
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:ASAMples?')
		return Conversions.str_to_int(response)

	def set_asamples(self, add_samples: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:ASAMples \n
		Snippet: driver.source.arb.set_asamples(add_samples = 1) \n
		Extends the processing time of a waveform file by the specified number of samples. The additional samples are valid in
		single-shot repetition mode only (see method RsCmwGprfGen.Source.Arb.repetition) . \n
			:param add_samples: Range: 0 to max. (depending on waveform file)
		"""
		param = Conversions.decimal_value_to_str(add_samples)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:ASAMples {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepeatMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:REPetition \n
		Snippet: value: enums.RepeatMode = driver.source.arb.get_repetition() \n
		Defines how often the ARB file is processed. \n
			:return: repetition: CONTinuous | SINGle CONTinuous: Unlimited, cyclic processing SINGle: File is processed n times, where n is the number of cycles (see method RsCmwGprfGen.Source.Arb.cycles)
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepeatMode)

	def set_repetition(self, repetition: enums.RepeatMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:REPetition \n
		Snippet: driver.source.arb.set_repetition(repetition = enums.RepeatMode.CONTinuous) \n
		Defines how often the ARB file is processed. \n
			:param repetition: CONTinuous | SINGle CONTinuous: Unlimited, cyclic processing SINGle: File is processed n times, where n is the number of cycles (see method RsCmwGprfGen.Source.Arb.cycles)
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepeatMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:REPetition {param}')

	def get_cycles(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:CYCLes \n
		Snippet: value: int = driver.source.arb.get_cycles() \n
		Defines how often the ARB file is processed in single mode (see method RsCmwGprfGen.Source.Arb.repetition) . \n
			:return: cycles: Range: 1 to 10E+3
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:CYCLes?')
		return Conversions.str_to_int(response)

	def set_cycles(self, cycles: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:CYCLes \n
		Snippet: driver.source.arb.set_cycles(cycles = 1) \n
		Defines how often the ARB file is processed in single mode (see method RsCmwGprfGen.Source.Arb.repetition) . \n
			:param cycles: Range: 1 to 10E+3
		"""
		param = Conversions.decimal_value_to_str(cycles)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:CYCLes {param}')

	def get_poffset(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:POFFset \n
		Snippet: value: float = driver.source.arb.get_poffset() \n
		Queries the peak offset of the loaded waveform file. Note: If a multi-segment waveform file is loaded, this command
		returns the peak offset in the last segment. Use method RsCmwGprfGen.Source.Arb.Msegment.poffset to query the peak offset
		values of the individual segments. \n
			:return: peak_offset: Offset value as specified in WinIQSIM2 Unit: dB
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:POFFset?')
		return Conversions.str_to_float(response)

	def get_crate(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:CRATe \n
		Snippet: value: float = driver.source.arb.get_crate() \n
		Queries the clock rate of the loaded waveform file. The clock rates of waveform file created with R&S WinIQSIM2 are
		compatible with the R&S CMW; see 'Generating and Transferring Waveform Files'. Note: If a multi-segment waveform file is
		loaded, this command returns the clock rate in the last segment. Use method RsCmwGprfGen.Source.Arb.Msegment.crate to
		query the clock rates of the individual segments. \n
			:return: clock_rate: Range: as defined in the waveform file , Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:CRATe?')
		return Conversions.str_to_float(response)

	def get_loffset(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:LOFFset \n
		Snippet: value: float = driver.source.arb.get_loffset() \n
		Queries the level offset (peak to average ratio, PAR) of the loaded waveform file. The PAR is equal to the absolute value
		of the difference between the 'RMS Offset' and the 'Peak Offset' defined in WinIQSIM2 (crest factor) .
		Note: If a multi-segment waveform file is loaded, this command returns the PAR in the last segment.
		Use method RsCmwGprfGen.Source.Arb.Msegment.par to query the PAR values of the individual segments. \n
			:return: level_offset: PAR value; see above Unit: dB
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:LOFFset?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_crc_protect(self) -> enums.YesNoStatus:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:CRCProtect \n
		Snippet: value: enums.YesNoStatus = driver.source.arb.get_crc_protect() \n
		Indicates whether the loaded ARB file contains a CRC checksum. To get a valid result, the related ARB file must be loaded
		into the memory, i.e. the baseband mode must be ARB and the generator state must be ON. Otherwise NAV is returned. \n
			:return: crc_protection: NO | YES
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:CRCProtect?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	def get_status(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:STATus \n
		Snippet: value: int = driver.source.arb.get_status() \n
		Queries the number of the currently processed segment. Even for the repetition 'Continuous Seamless', the currently
		processed segment is returned, independent of whether a trigger event for the next segment has already been received or
		not. This command is only supported by R&S CMW100/CMW with MUA, not by R&S CMW500/2xx with BB Meas. \n
			:return: arb_segment_no: Integer number. NAV is returned if no file is loaded. Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:STATus?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Arb':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Arb(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
