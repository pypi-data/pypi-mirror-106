from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdMarker:
	"""UdMarker commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("udMarker", core, parent)

	@property
	def clist(self):
		"""clist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clist'):
			from .UdMarker_.Clist import Clist
			self._clist = Clist(self._core, self._base)
		return self._clist

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Period: int: Period of the user-defined marker sequence Range: 1 to 1E+9
			- Start_State: enums.SignalSlope: REDGe | FEDGe Polarity of marker pulses (first transition)
			- Positions: List[int or bool]: Positions of marker signals. Eight values must be specified; the first value must be 0. Range: 0 (pos. 0) or 1 (other positions) to max. (must not exceed the Period) . OFF disables a position."""
		__meta_args_list = [
			ArgStruct.scalar_int('Period'),
			ArgStruct.scalar_enum('Start_State', enums.SignalSlope),
			ArgStruct('Positions', DataType.IntegerExtList, None, False, False, 8)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Period: int = None
			self.Start_State: enums.SignalSlope = None
			self.Positions: List[int or bool] = None

	def get_value(self) -> ValueStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:UDMarker \n
		Snippet: value: ValueStruct = driver.source.arb.udMarker.get_value() \n
		Defines the marker period plus up to 8 marker events relative to the processed waveform file. The user-defined marker is
		available as an ARB output trigger source. Example: The command SOURce:GPRF:GEN<i>:ARB:UDMarker 30, FEDG, 0, 2, 4, 6, 8,
		10, OFF, OFF sets the user-defined marker as follows: \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:ARB:UDMarker?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:UDMarker \n
		Snippet: driver.source.arb.udMarker.set_value(value = ValueStruct()) \n
		Defines the marker period plus up to 8 marker events relative to the processed waveform file. The user-defined marker is
		available as an ARB output trigger source. Example: The command SOURce:GPRF:GEN<i>:ARB:UDMarker 30, FEDG, 0, 2, 4, 6, 8,
		10, OFF, OFF sets the user-defined marker as follows: \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:ARB:UDMarker', value)

	def clone(self) -> 'UdMarker':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UdMarker(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
