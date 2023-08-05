from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsa:
	"""Nsa commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nsa", core, parent)

	# noinspection PyTypeChecker
	class ActivateStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Ue_Id: str: Optional setting parameter. For future use. Enter any value if you want to use optional parameters.
			- Linked_Bearer_Id: int: Optional setting parameter. ID of the default bearer to that the dedicated bearer is linked. To get a list of all default bearer IDs, see [CMDLINK: CATalog:SIGNaling:LTE:UE:DBEarer? CMDLINK].
			- Data_Flow: enums.DataFlow: Optional setting parameter. Configures the user data flow for the dedicated bearer. MCGSplit: MCG split bearer, with traffic split in the eNB SCG: no traffic split SCGSplit: SCG split bearer, with traffic split in the gNB
			- Traffic_Dist: float: Optional setting parameter. Traffic distribution for split bearer is configured automatically.
			- Qci: enums.Qi: Optional setting parameter. Value of the quality-of-service class identifier. Values defined in 3GPP TS 23.203, table 6.1.7. The GUI shows also the designation of each value.
			- Max_Dl_Bitrate: float: Optional setting parameter. Maximum DL bit rate allowed in the network.
			- Max_Ul_Bitrate: float: Optional setting parameter. Maximum UL bit rate allowed in the network.
			- Gtd_Dl_Bitrate: float: Optional setting parameter. DL bit rate guaranteed by the network for the bearer.
			- Gtd_Ul_Bitrate: float: Optional setting parameter. UL bit rate guaranteed by the network for the bearer."""
		__meta_args_list = [
			]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ue_Id: str = None
			self.Linked_Bearer_Id: int = None
			self.Data_Flow: enums.DataFlow = None
			self.Traffic_Dist: float = None
			self.Qci: enums.Qi = None
			self.Max_Dl_Bitrate: float = None
			self.Max_Ul_Bitrate: float = None
			self.Gtd_Dl_Bitrate: float = None
			self.Gtd_Ul_Bitrate: float = None

	def activate(self, structure: ActivateStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:UE:NSA:ACTivate \n
		Snippet: driver.configure.signaling.lte.ue.nsa.activate(value = [PROPERTY_STRUCT_NAME]()) \n
		Activates the EN-DC mode and establishes a dedicated bearer. \n
			:param structure: for set value, see the help for ActivateStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:UE:NSA:ACTivate', structure)

	def deactivate(self, ue_id: str = None, bearer_id: int = None, esm_cause: enums.EsmCause = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:UE:NSA:DEACtivate \n
		Snippet: driver.configure.signaling.lte.ue.nsa.deactivate(ue_id = '1', bearer_id = 1, esm_cause = enums.EsmCause.C100) \n
		Deactivates the EN-DC mode and releases a dedicated bearer. \n
			:param ue_id: For future use. Enter any value if you want to use optional parameters.
			:param bearer_id: ID of the dedicated bearer to be released. To get a list of all dedicated bearer IDs, see method RsCMX_Signaling.Catalog.Signaling.Lte.Ue.Bearer.get_.
			:param esm_cause: Release cause to be sent. Values defined in 3GPP TS 24.301, chapter 9.9.4.4.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, True), ArgSingle('bearer_id', bearer_id, DataType.Integer, True), ArgSingle('esm_cause', esm_cause, DataType.Enum, True))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:UE:NSA:DEACtivate {param}'.rstrip())
