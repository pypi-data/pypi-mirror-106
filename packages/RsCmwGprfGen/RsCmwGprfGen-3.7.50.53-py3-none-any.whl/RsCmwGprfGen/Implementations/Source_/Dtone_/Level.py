from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: LevelSource, default value after init: LevelSource.Src1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_levelSource_get', 'repcap_levelSource_set', repcap.LevelSource.Src1)

	def repcap_levelSource_set(self, enum_value: repcap.LevelSource) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to LevelSource.Default
		Default value after init: LevelSource.Src1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_levelSource_get(self) -> repcap.LevelSource:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def get(self, levelSource=repcap.LevelSource.Default) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:DTONe:LEVel<source> \n
		Snippet: value: float = driver.source.dtone.level.get(levelSource = repcap.LevelSource.Default) \n
		Queries the output level of the source signal <source>. The output level is a function of the generator output level (see
		method RsCmwGprfGen.Source.RfSettings.level) and the ratio (see method RsCmwGprfGen.Source.Dtone.ratio) . \n
			:param levelSource: optional repeated capability selector. Default value: Src1 (settable in the interface 'Level')
			:return: level: Range: Depends on the instrument model, the connector and other settings; please notice the ranges quoted in the data sheet , Unit: dBm"""
		levelSource_cmd_val = self._base.get_repcap_cmd_value(levelSource, repcap.LevelSource)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:DTONe:LEVel{levelSource_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
