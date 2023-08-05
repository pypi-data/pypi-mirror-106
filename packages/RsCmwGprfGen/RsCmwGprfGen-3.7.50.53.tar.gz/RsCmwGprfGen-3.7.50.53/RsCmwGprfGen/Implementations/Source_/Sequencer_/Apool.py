from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apool:
	"""Apool commands group definition. 30 total commands, 12 Sub-groups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("apool", core, parent)

	@property
	def download(self):
		"""download commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_download'):
			from .Apool_.Download import Download
			self._download = Download(self._core, self._base)
		return self._download

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_path'):
			from .Apool_.Path import Path
			self._path = Path(self._core, self._base)
		return self._path

	@property
	def crcProtect(self):
		"""crcProtect commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_crcProtect'):
			from .Apool_.CrcProtect import CrcProtect
			self._crcProtect = CrcProtect(self._core, self._base)
		return self._crcProtect

	@property
	def paratio(self):
		"""paratio commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_paratio'):
			from .Apool_.Paratio import Paratio
			self._paratio = Paratio(self._core, self._base)
		return self._paratio

	@property
	def poffset(self):
		"""poffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_poffset'):
			from .Apool_.Poffset import Poffset
			self._poffset = Poffset(self._core, self._base)
		return self._poffset

	@property
	def roption(self):
		"""roption commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_roption'):
			from .Apool_.Roption import Roption
			self._roption = Roption(self._core, self._base)
		return self._roption

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_duration'):
			from .Apool_.Duration import Duration
			self._duration = Duration(self._core, self._base)
		return self._duration

	@property
	def samples(self):
		"""samples commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_samples'):
			from .Apool_.Samples import Samples
			self._samples = Samples(self._core, self._base)
		return self._samples

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_symbolRate'):
			from .Apool_.SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._base)
		return self._symbolRate

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_waveform'):
			from .Apool_.Waveform import Waveform
			self._waveform = Waveform(self._core, self._base)
		return self._waveform

	@property
	def rmessage(self):
		"""rmessage commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rmessage'):
			from .Apool_.Rmessage import Rmessage
			self._rmessage = Rmessage(self._core, self._base)
		return self._rmessage

	@property
	def reliability(self):
		"""reliability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reliability'):
			from .Apool_.Reliability import Reliability
			self._reliability = Reliability(self._core, self._base)
		return self._reliability

	# noinspection PyTypeChecker
	def get_valid(self) -> enums.YesNoStatus:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:VALid \n
		Snippet: value: enums.YesNoStatus = driver.source.sequencer.apool.get_valid() \n
		Queries whether the ARB file pool is valid. \n
			:return: valid: NO | YES
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:VALid?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	# noinspection PyTypeChecker
	def get_loaded(self) -> enums.YesNoStatus:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:LOADed \n
		Snippet: value: enums.YesNoStatus = driver.source.sequencer.apool.get_loaded() \n
		Queries whether the ARB file pool is downloaded to the ARB RAM. \n
			:return: loaded: NO | YES
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:LOADed?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	def get_rrequired(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RREQuired \n
		Snippet: value: float = driver.source.sequencer.apool.get_rrequired() \n
		Queries the amount of RAM required by the ARB files in the pool. \n
			:return: ram_required: Unit: Mbyte
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RREQuired?')
		return Conversions.str_to_float(response)

	def get_rtotal(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RTOTal \n
		Snippet: value: float = driver.source.sequencer.apool.get_rtotal() \n
		Queries the amount of RAM available for ARB files. \n
			:return: ram_total: Unit: Mbyte
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:RTOTal?')
		return Conversions.str_to_float(response)

	def set_file(self, arb_file: str) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:FILE \n
		Snippet: driver.source.sequencer.apool.set_file(arb_file = '1') \n
		Adds an ARB file to the ARB file pool. \n
			:param arb_file: Path and filename as string Example: '@waveform/myARBfile.wv'
		"""
		param = Conversions.value_to_quoted_str(arb_file)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:FILE {param}')

	def set_remove(self, indices: List[int]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:REMove \n
		Snippet: driver.source.sequencer.apool.set_remove(indices = [1, 2, 3]) \n
		Removes selected files from the ARB file pool. \n
			:param indices: Indices of the files to be removed. You can specify a single index or a comma-separated list of indices.
		"""
		param = Conversions.list_to_csv_str(indices)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:REMove {param}')

	def clear(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CLEar \n
		Snippet: driver.source.sequencer.apool.clear() \n
		Removes all files from the ARB file pool. \n
		"""
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CLEar')

	def clear_with_opc(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CLEar \n
		Snippet: driver.source.sequencer.apool.clear_with_opc() \n
		Removes all files from the ARB file pool. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsCmwGprfGen.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CLEar')

	def get_mindex(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:MINDex \n
		Snippet: value: int = driver.source.sequencer.apool.get_mindex() \n
		Queries the highest index of the ARB file pool. The pool contains files with the indices 0 to <MaximumIndex>. \n
			:return: maximum_index: Highest index. If the file pool is empty, NAV is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:MINDex?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Apool':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Apool(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
