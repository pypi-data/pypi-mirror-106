from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Pdu_Session_Id: List[int]: No parameter help available
			- Pdu_State: List[enums.PduState]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Pdu_Session_Id', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Pdu_State', DataType.EnumList, enums.PduState, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pdu_Session_Id: List[int] = None
			self.Pdu_State: List[enums.PduState] = None

	def fetch(self, ue_id: str = None, pdu_session_id: int = None) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:TOPology:FGS:UE:PDU:STATe \n
		Snippet: value: FetchStruct = driver.signaling.topology.fgs.ue.pdu.state.fetch(ue_id = '1', pdu_session_id = 1) \n
		No command help available \n
			:param ue_id: No help available
			:param pdu_session_id: No help available
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, True), ArgSingle('pdu_session_id', pdu_session_id, DataType.Integer, True))
		return self._core.io.query_struct(f'FETCh:SIGNaling:TOPology:FGS:UE:PDU:STATe? {param}'.rstrip(), self.__class__.FetchStruct())
