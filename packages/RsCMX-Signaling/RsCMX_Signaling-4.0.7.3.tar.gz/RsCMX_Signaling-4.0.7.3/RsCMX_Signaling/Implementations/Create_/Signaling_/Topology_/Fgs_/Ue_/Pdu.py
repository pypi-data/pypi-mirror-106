from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdu:
	"""Pdu commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdu", core, parent)

	# noinspection PyTypeChecker
	class QosFlowStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Ue_Id: str: No parameter help available
			- Pdu_Session_Id: int: No parameter help available
			- Qi: enums.Qi: No parameter help available
			- Max_Dl_Bitrate: float: No parameter help available
			- Dl_Bit_Rate_Unit: enums.ItRateUnit: No parameter help available
			- Max_Ul_Bitrate: float: No parameter help available
			- Ul_Bit_Rate_Unit: enums.ItRateUnit: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Ue_Id'),
			ArgStruct.scalar_int('Pdu_Session_Id'),
			ArgStruct.scalar_enum('Qi', enums.Qi),
			ArgStruct.scalar_float('Max_Dl_Bitrate'),
			ArgStruct.scalar_enum('Dl_Bit_Rate_Unit', enums.ItRateUnit),
			ArgStruct.scalar_float('Max_Ul_Bitrate'),
			ArgStruct.scalar_enum('Ul_Bit_Rate_Unit', enums.ItRateUnit)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ue_Id: str = None
			self.Pdu_Session_Id: int = None
			self.Qi: enums.Qi = None
			self.Max_Dl_Bitrate: float = None
			self.Dl_Bit_Rate_Unit: enums.ItRateUnit = None
			self.Max_Ul_Bitrate: float = None
			self.Ul_Bit_Rate_Unit: enums.ItRateUnit = None

	def set_qos_flow(self, value: QosFlowStruct) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow \n
		Snippet: driver.create.signaling.topology.fgs.ue.pdu.set_qos_flow(value = QosFlowStruct()) \n
		No command help available \n
			:param value: see the help for QosFlowStruct structure arguments.
		"""
		self._core.io.write_struct('CREate:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow', value)
