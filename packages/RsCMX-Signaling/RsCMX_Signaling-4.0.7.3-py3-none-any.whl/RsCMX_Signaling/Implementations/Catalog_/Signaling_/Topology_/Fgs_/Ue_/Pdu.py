from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdu:
	"""Pdu commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdu", core, parent)

	@property
	def qosFlow(self):
		"""qosFlow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qosFlow'):
			from .Pdu_.QosFlow import QosFlow
			self._qosFlow = QosFlow(self._core, self._base)
		return self._qosFlow

	def get(self, ue_id: str = None) -> List[int]:
		"""SCPI: CATalog:SIGNaling:TOPology:FGS:UE:PDU \n
		Snippet: value: List[int] = driver.catalog.signaling.topology.fgs.ue.pdu.get(ue_id = '1') \n
		No command help available \n
			:param ue_id: No help available
			:return: pdu_session_id: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, True))
		response = self._core.io.query_bin_or_ascii_int_list(f'CATalog:SIGNaling:TOPology:FGS:UE:PDU? {param}'.rstrip())
		return response

	def clone(self) -> 'Pdu':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdu(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
