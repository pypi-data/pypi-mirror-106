from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tx_Connector: enums.TxConnector: RF connector for the output path
			- Rf_Converter: enums.TxConverter: TX module for the output path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tx_Connector: enums.TxConnector = None
			self.Rf_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_salone(self) -> SaloneStruct:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.scenario.get_salone() \n
		Activates the standalone scenario and selects the output path for the generated RF signal. For possible connector and
		converter values, see 'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:GENerator<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())

	def set_salone(self, value: SaloneStruct) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:SALone \n
		Snippet: driver.route.scenario.set_salone(value = SaloneStruct()) \n
		Activates the standalone scenario and selects the output path for the generated RF signal. For possible connector and
		converter values, see 'Values for Signal Path Selection'. \n
			:param value: see the help for SaloneStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:GPRF:GENerator<Instance>:SCENario:SALone', value)

	# noinspection PyTypeChecker
	class IqOutStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tx_Connector: enums.TxConnector: DIG I/Q output connector
			- Tx_Converter: enums.TxConverter: I/Q TX module"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_iq_out(self) -> IqOutStruct:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:IQOut \n
		Snippet: value: IqOutStruct = driver.route.scenario.get_iq_out() \n
		Activates the 'IQ Out' scenario and selects the output path for the generated digital baseband (I/Q) signal. For possible
		connector and converter values, see 'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for IqOutStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:GENerator<Instance>:SCENario:IQOut?', self.__class__.IqOutStruct())

	def set_iq_out(self, value: IqOutStruct) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:IQOut \n
		Snippet: driver.route.scenario.set_iq_out(value = IqOutStruct()) \n
		Activates the 'IQ Out' scenario and selects the output path for the generated digital baseband (I/Q) signal. For possible
		connector and converter values, see 'Values for Signal Path Selection'. \n
			:param value: see the help for IqOutStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:GPRF:GENerator<Instance>:SCENario:IQOut', value)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Scenario:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario \n
		Snippet: value: enums.Scenario = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: scenario: SALone | IQOut SALone: An RF signal is generated (standalone scenario) IQOut: The generated baseband signal is sent to an IQ out connector (digital baseband interface)
		"""
		response = self._core.io.query_str('ROUTe:GPRF:GENerator<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.Scenario)
