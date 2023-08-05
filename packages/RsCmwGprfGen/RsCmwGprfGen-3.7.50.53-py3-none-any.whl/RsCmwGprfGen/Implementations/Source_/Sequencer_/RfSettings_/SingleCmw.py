from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCmw:
	"""SingleCmw commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("singleCmw", core, parent)

	# noinspection PyTypeChecker
	def get_cset(self) -> enums.ParameterSetMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:RFSettings:CMWS:CSET \n
		Snippet: value: enums.ParameterSetMode = driver.source.sequencer.rfSettings.singleCmw.get_cset() \n
		Specifies how the active RF connectors of a connector bench are selected. \n
			:return: cmws_connector_set: GLOBal | LIST GLOBal The same connectors are active for all sequencer list entries. To configure the active connectors, see method RsCmwGprfGen.Configure.SingleCmw.Usage.Tx.set and method RsCmwGprfGen.Configure.SingleCmw.Usage.Tx.All.set. LIST The connectors are activated individually per list entry. See method RsCmwGprfGen.Source.Sequencer.ListPy.SingleCmw.Usage.Tx.set.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:RFSettings:CMWS:CSET?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_cset(self, cmws_connector_set: enums.ParameterSetMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:RFSettings:CMWS:CSET \n
		Snippet: driver.source.sequencer.rfSettings.singleCmw.set_cset(cmws_connector_set = enums.ParameterSetMode.GLOBal) \n
		Specifies how the active RF connectors of a connector bench are selected. \n
			:param cmws_connector_set: GLOBal | LIST GLOBal The same connectors are active for all sequencer list entries. To configure the active connectors, see method RsCmwGprfGen.Configure.SingleCmw.Usage.Tx.set and method RsCmwGprfGen.Configure.SingleCmw.Usage.Tx.All.set. LIST The connectors are activated individually per list entry. See method RsCmwGprfGen.Source.Sequencer.ListPy.SingleCmw.Usage.Tx.set.
		"""
		param = Conversions.enum_scalar_to_str(cmws_connector_set, enums.ParameterSetMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:RFSettings:CMWS:CSET {param}')
