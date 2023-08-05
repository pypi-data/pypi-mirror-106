from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqSettings:
	"""IqSettings commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqSettings", core, parent)

	def get_symbol_rate(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:SRATe \n
		Snippet: value: float = driver.source.iqSettings.get_symbol_rate() \n
		Sets/gets the sample rate of the digital IQ out signal. \n
			:return: sample_rate: Range: 100E+6 | 30.72E+6 | 15.36E+6 | 7.68E+6 | 3.84E+6 | 1.92E+6 , Unit: Samples per second
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:SRATe?')
		return Conversions.str_to_float(response)

	def set_symbol_rate(self, sample_rate: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:SRATe \n
		Snippet: driver.source.iqSettings.set_symbol_rate(sample_rate = 1.0) \n
		Sets/gets the sample rate of the digital IQ out signal. \n
			:param sample_rate: Range: 100E+6 | 30.72E+6 | 15.36E+6 | 7.68E+6 | 3.84E+6 | 1.92E+6 , Unit: Samples per second
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:IQSettings:SRATe {param}')

	# noinspection PyTypeChecker
	def get_tmode(self) -> enums.TransferMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:TMODe \n
		Snippet: value: enums.TransferMode = driver.source.iqSettings.get_tmode() \n
		Sets/gets the transfer mode for the digital output. \n
			:return: transfer_mode: ENABlemode | REQuestmode 'enable mode' or 'request mode'
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:TMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TransferMode)

	def set_tmode(self, transfer_mode: enums.TransferMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:TMODe \n
		Snippet: driver.source.iqSettings.set_tmode(transfer_mode = enums.TransferMode.ENABlemode) \n
		Sets/gets the transfer mode for the digital output. \n
			:param transfer_mode: ENABlemode | REQuestmode 'enable mode' or 'request mode'
		"""
		param = Conversions.enum_scalar_to_str(transfer_mode, enums.TransferMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:IQSettings:TMODe {param}')

	def get_level(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:LEVel \n
		Snippet: value: float = driver.source.iqSettings.get_level() \n
		Returns the RMS level of the outgoing IQ signal relative to the maximum power level. \n
			:return: level: Unit: dBFS
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:LEVel?')
		return Conversions.str_to_float(response)

	def get_pep(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:PEP \n
		Snippet: value: float = driver.source.iqSettings.get_pep() \n
		Returns the peak envelope power of the outgoing IQ signal relative to the maximum power level. \n
			:return: pep: Unit: dBFS
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:PEP?')
		return Conversions.str_to_float(response)

	def get_crest(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:CRESt \n
		Snippet: value: float = driver.source.iqSettings.get_crest() \n
		Returns the crest factor (peak-to-average power ratio) of the outgoing IQ signal. \n
			:return: crest: Unit: dB
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:CRESt?')
		return Conversions.str_to_float(response)
