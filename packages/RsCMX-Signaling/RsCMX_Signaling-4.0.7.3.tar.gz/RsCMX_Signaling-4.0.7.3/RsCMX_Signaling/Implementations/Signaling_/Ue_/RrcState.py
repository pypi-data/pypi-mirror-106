from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrcState:
	"""RrcState commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rrcState", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Rrc_State: enums.RrcState: RRC connection state
			- Uec_State: enums.UecState: UE connection status information
				- OK: The UE is idle or connected, see RRC state.
				- PAGing: The UE is idle. Paging is in progress.
				- CESTablish: Connection establishment in progress (transition from idle to connected) .
				- CREestablish: Radio link failure or configuration error. The UE tries to reconnect.
				- SCGFailure: The link between the UE and the secondary node is broken. The UE tries to reconnect.
				- HANDover: A handover to another cell is in progress.
				- CRELease: Connection release in progress (transition from connected to idle) ."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rrc_State', enums.RrcState),
			ArgStruct.scalar_enum('Uec_State', enums.UecState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rrc_State: enums.RrcState = None
			self.Uec_State: enums.UecState = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:UE:RRCState \n
		Snippet: value: FetchStruct = driver.signaling.ue.rrcState.fetch() \n
		Queries the RRC connection state and the more detailed UE connection status information. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:UE:RRCState?', self.__class__.FetchStruct())
