from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	def get_svalue(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:SVALue \n
		Snippet: value: float = driver.source.sequencer.listPy.fill.frequency.get_svalue() \n
		Configures the start value for filling the sequencer list with frequency values. \n
			:return: start_value: Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:SVALue?')
		return Conversions.str_to_float(response)

	def set_svalue(self, start_value: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:SVALue \n
		Snippet: driver.source.sequencer.listPy.fill.frequency.set_svalue(start_value = 1.0) \n
		Configures the start value for filling the sequencer list with frequency values. \n
			:param start_value: Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(start_value)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:SVALue {param}')

	def get_increment(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:INCRement \n
		Snippet: value: float = driver.source.sequencer.listPy.fill.frequency.get_increment() \n
		Configures the increment for filling the sequencer list with frequency values. \n
			:return: increment: Range: Depends on the number of entries and on the start value , Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:INCRement?')
		return Conversions.str_to_float(response)

	def set_increment(self, increment: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:INCRement \n
		Snippet: driver.source.sequencer.listPy.fill.frequency.set_increment(increment = 1.0) \n
		Configures the increment for filling the sequencer list with frequency values. \n
			:param increment: Range: Depends on the number of entries and on the start value , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(increment)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:INCRement {param}')

	def get_keep(self) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:KEEP \n
		Snippet: value: bool = driver.source.sequencer.listPy.fill.frequency.get_keep() \n
		Selects whether the frequency of existing entries is kept or overwritten when the sequencer list is filled. \n
			:return: keep_flag: OFF | ON OFF: overwrite values ON: keep values
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:KEEP?')
		return Conversions.str_to_bool(response)

	def set_keep(self, keep_flag: bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:KEEP \n
		Snippet: driver.source.sequencer.listPy.fill.frequency.set_keep(keep_flag = False) \n
		Selects whether the frequency of existing entries is kept or overwritten when the sequencer list is filled. \n
			:param keep_flag: OFF | ON OFF: overwrite values ON: keep values
		"""
		param = Conversions.bool_to_str(keep_flag)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:FREQuency:KEEP {param}')
