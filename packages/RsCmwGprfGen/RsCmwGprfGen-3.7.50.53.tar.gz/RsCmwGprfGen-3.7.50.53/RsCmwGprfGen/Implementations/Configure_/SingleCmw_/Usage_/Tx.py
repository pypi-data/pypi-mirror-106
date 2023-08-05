from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tx", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .Tx_.All import All
			self._all = All(self._core, self._base)
		return self._all

	def set(self, tx_connector: enums.TxConnectorCmws, usage: bool) -> None:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:CMWS:USAGe:TX \n
		Snippet: driver.configure.singleCmw.usage.tx.set(tx_connector = enums.TxConnectorCmws.R11, usage = False) \n
		Activates or deactivates a single RF connector of a connector bench. The generated signal is available at all active
		connectors of the currently selected connector bench. For possible connector values, see 'Values for Signal Path
		Selection'. \n
			:param tx_connector: Selects a single connector of the bench
			:param usage: OFF | ON ON: Activates the selected connector OFF: Deactivates the selected connector
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tx_connector', tx_connector, DataType.Enum), ArgSingle('usage', usage, DataType.Boolean))
		self._core.io.write(f'CONFigure:GPRF:GENerator<Instance>:CMWS:USAGe:TX {param}'.rstrip())

	def get(self, tx_connector: enums.TxConnectorCmws) -> bool:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:CMWS:USAGe:TX \n
		Snippet: value: bool = driver.configure.singleCmw.usage.tx.get(tx_connector = enums.TxConnectorCmws.R11) \n
		Activates or deactivates a single RF connector of a connector bench. The generated signal is available at all active
		connectors of the currently selected connector bench. For possible connector values, see 'Values for Signal Path
		Selection'. \n
			:param tx_connector: Selects a single connector of the bench
			:return: usage: OFF | ON ON: Activates the selected connector OFF: Deactivates the selected connector"""
		param = Conversions.enum_scalar_to_str(tx_connector, enums.TxConnectorCmws)
		response = self._core.io.query_str(f'CONFigure:GPRF:GENerator<Instance>:CMWS:USAGe:TX? {param}')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Tx':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tx(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
