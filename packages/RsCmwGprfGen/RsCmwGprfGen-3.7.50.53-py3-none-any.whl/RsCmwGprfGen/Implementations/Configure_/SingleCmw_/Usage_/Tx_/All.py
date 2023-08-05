from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	def set(self, tx_connector_bench: enums.TxConnectorBench, usage: List[bool]) -> None:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:CMWS:USAGe:TX:ALL \n
		Snippet: driver.configure.singleCmw.usage.tx.all.set(tx_connector_bench = enums.TxConnectorBench.R118, usage = [True, False, True]) \n
		Activates or deactivates the individual RF connectors of a connector bench. For possible bench values, see 'Values for
		Signal Path Selection'. \n
			:param tx_connector_bench: Selects a bench with 4 or 8 connectors
			:param usage: OFF | ON Comma-separated list of 4 or 8 values, one for each connector of the bench ON: activate the connector OFF: deactivate the connector
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tx_connector_bench', tx_connector_bench, DataType.Enum), ArgSingle.as_open_list('usage', usage, DataType.BooleanList))
		self._core.io.write(f'CONFigure:GPRF:GENerator<Instance>:CMWS:USAGe:TX:ALL {param}'.rstrip())

	def get(self, tx_connector_bench: enums.TxConnectorBench) -> List[bool]:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:CMWS:USAGe:TX:ALL \n
		Snippet: value: List[bool] = driver.configure.singleCmw.usage.tx.all.get(tx_connector_bench = enums.TxConnectorBench.R118) \n
		Activates or deactivates the individual RF connectors of a connector bench. For possible bench values, see 'Values for
		Signal Path Selection'. \n
			:param tx_connector_bench: Selects a bench with 4 or 8 connectors
			:return: usage: OFF | ON Comma-separated list of 4 or 8 values, one for each connector of the bench ON: activate the connector OFF: deactivate the connector"""
		param = Conversions.enum_scalar_to_str(tx_connector_bench, enums.TxConnectorBench)
		response = self._core.io.query_str(f'CONFigure:GPRF:GENerator<Instance>:CMWS:USAGe:TX:ALL? {param}')
		return Conversions.str_to_bool_list(response)
