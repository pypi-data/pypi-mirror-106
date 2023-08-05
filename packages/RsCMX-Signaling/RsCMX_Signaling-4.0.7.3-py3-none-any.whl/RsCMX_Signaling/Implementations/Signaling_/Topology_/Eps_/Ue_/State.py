from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Emm_Reg_State_Sum: enums.RegStateB: Overall state registered or deregistered.
			- Emm_Reg_State: enums.RegStateB: Detailed state DREG: deregistered LRIP: EPS-only registration in progress CRIP: combined registration in progress ERIP: emergency registration in progress LREG: EPS-only registered (LTE registered) CREG: combined registered (EPS-IMSI) EREG: emergency registered DRIP: deregistration in progress"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Emm_Reg_State_Sum', enums.RegStateB),
			ArgStruct.scalar_enum('Emm_Reg_State', enums.RegStateB)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Emm_Reg_State_Sum: enums.RegStateB = None
			self.Emm_Reg_State: enums.RegStateB = None

	def fetch(self, ui_id: str = None) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:TOPology:EPS:UE:STATe \n
		Snippet: value: FetchStruct = driver.signaling.topology.eps.ue.state.fetch(ui_id = '1') \n
		Queries the UE registration state for EPS tracking areas. \n
			:param ui_id: No help available
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ui_id', ui_id, DataType.String, True))
		return self._core.io.query_struct(f'FETCh:SIGNaling:TOPology:EPS:UE:STATe? {param}'.rstrip(), self.__class__.FetchStruct())
