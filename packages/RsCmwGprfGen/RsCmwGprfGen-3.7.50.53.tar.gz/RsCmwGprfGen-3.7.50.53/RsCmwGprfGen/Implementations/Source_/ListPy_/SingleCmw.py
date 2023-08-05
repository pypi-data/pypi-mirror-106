from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCmw:
	"""SingleCmw commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("singleCmw", core, parent)

	@property
	def usage(self):
		"""usage commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_usage'):
			from .SingleCmw_.Usage import Usage
			self._usage = Usage(self._core, self._base)
		return self._usage

	# noinspection PyTypeChecker
	def get_cset(self) -> enums.ParameterSetMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:CMWS:CSET \n
		Snippet: value: enums.ParameterSetMode = driver.source.listPy.singleCmw.get_cset() \n
		Specifies how the active RF connectors of a connector bench are selected for the GPRF generator list mode. \n
			:return: cmws_connector_set: GLOBal | LIST GLOBal: The same connectors are active for all list entries. They are activated in the same way as without list mode. See method RsCmwGprfGen.Configure.SingleCmw.Usage.Tx.set and method RsCmwGprfGen.Configure.SingleCmw.Usage.Tx.All.set. LIST: The connectors are activated individually per list entry. See method RsCmwGprfGen.Source.ListPy.SingleCmw.Usage.Tx.set.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:LIST:CMWS:CSET?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_cset(self, cmws_connector_set: enums.ParameterSetMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:CMWS:CSET \n
		Snippet: driver.source.listPy.singleCmw.set_cset(cmws_connector_set = enums.ParameterSetMode.GLOBal) \n
		Specifies how the active RF connectors of a connector bench are selected for the GPRF generator list mode. \n
			:param cmws_connector_set: GLOBal | LIST GLOBal: The same connectors are active for all list entries. They are activated in the same way as without list mode. See method RsCmwGprfGen.Configure.SingleCmw.Usage.Tx.set and method RsCmwGprfGen.Configure.SingleCmw.Usage.Tx.All.set. LIST: The connectors are activated individually per list entry. See method RsCmwGprfGen.Source.ListPy.SingleCmw.Usage.Tx.set.
		"""
		param = Conversions.enum_scalar_to_str(cmws_connector_set, enums.ParameterSetMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:CMWS:CSET {param}')

	def clone(self) -> 'SingleCmw':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SingleCmw(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
