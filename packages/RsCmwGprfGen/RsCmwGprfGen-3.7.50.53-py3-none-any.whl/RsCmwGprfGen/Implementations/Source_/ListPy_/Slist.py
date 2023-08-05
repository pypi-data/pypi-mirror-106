from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slist:
	"""Slist commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("slist", core, parent)

	def set(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:SLISt \n
		Snippet: driver.source.listPy.slist.set() \n
		This command initiates the list cycling in CONTinuous repetition mode (see method RsCmwGprfGen.Source.ListPy.repetition) ,
		for lists incremented by dwell time or ARB file marker (see method RsCmwGprfGen.Source.ListPy.Increment.value) and with
		'Manual' list increment enabling (see method RsCmwGprfGen.Source.ListPy.Increment.Enabling.value) . The active list index
		can be queried using method RsCmwGprfGen.Source.ListPy.aindex. \n
		"""
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:LIST:SLISt')

	def set_with_opc(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:LIST:SLISt \n
		Snippet: driver.source.listPy.slist.set_with_opc() \n
		This command initiates the list cycling in CONTinuous repetition mode (see method RsCmwGprfGen.Source.ListPy.repetition) ,
		for lists incremented by dwell time or ARB file marker (see method RsCmwGprfGen.Source.ListPy.Increment.value) and with
		'Manual' list increment enabling (see method RsCmwGprfGen.Source.ListPy.Increment.Enabling.value) . The active list index
		can be queried using method RsCmwGprfGen.Source.ListPy.aindex. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwGprfGen.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:LIST:SLISt')
