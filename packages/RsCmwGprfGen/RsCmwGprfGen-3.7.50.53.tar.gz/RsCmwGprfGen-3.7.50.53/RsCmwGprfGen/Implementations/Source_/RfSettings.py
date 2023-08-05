from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	def get_dgain(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:DGAin \n
		Snippet: value: float = driver.source.rfSettings.get_dgain() \n
		Defines the digital gain of the constant-frequency RF generator. \n
			:return: digital_gain: Range: -30 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:DGAin?')
		return Conversions.str_to_float(response)

	def set_dgain(self, digital_gain: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:DGAin \n
		Snippet: driver.source.rfSettings.set_dgain(digital_gain = 1.0) \n
		Defines the digital gain of the constant-frequency RF generator. \n
			:param digital_gain: Range: -30 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(digital_gain)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:RFSettings:DGAin {param}')

	def get_pe_power(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:PEPower \n
		Snippet: value: float = driver.source.rfSettings.get_pe_power() \n
		Queries the peak envelope power for single-tone and dual-tone signals. \n
			:return: peak_envelope_pow: Range: Depends on the instrument model, the connector and other settings; please notice the ranges quoted in the data sheet , Unit: dBm
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:PEPower?')
		return Conversions.str_to_float(response)

	def get_eattenuation(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.source.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF output connector. \n
			:return: ext_rf_out_att: Range: -50 dB to 90 dB, Unit: dB
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, ext_rf_out_att: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.source.rfSettings.set_eattenuation(ext_rf_out_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF output connector. \n
			:param ext_rf_out_att: Range: -50 dB to 90 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(ext_rf_out_att)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:RFSettings:EATTenuation {param}')

	def get_frequency(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.source.rfSettings.get_frequency() \n
		Selects the frequency of the RF generator (generator frequency) . Some of the baseband modes (modulation types) modify
		the generator frequency. \n
			:return: frequency: Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:FREQuency \n
		Snippet: driver.source.rfSettings.set_frequency(frequency = 1.0) \n
		Selects the frequency of the RF generator (generator frequency) . Some of the baseband modes (modulation types) modify
		the generator frequency. \n
			:param frequency: Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:RFSettings:FREQuency {param}')

	def get_level(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:LEVel \n
		Snippet: value: float = driver.source.rfSettings.get_level() \n
		Sets the base RMS level of the constant-frequency RF generator. \n
			:return: level: Range: Depends on the instrument model, the connector and other settings; please notice the ranges quoted in the data sheet , Unit: dBm
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:LEVel \n
		Snippet: driver.source.rfSettings.set_level(level = 1.0) \n
		Sets the base RMS level of the constant-frequency RF generator. \n
			:param level: Range: Depends on the instrument model, the connector and other settings; please notice the ranges quoted in the data sheet , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:RFSettings:LEVel {param}')
