from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sms:
	"""Sms commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sms", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Address: str: Address of the originator of the message
			- Message: str: Message text
			- Type_Py: enums.Type: Optional setting parameter. Coding group GDC: general data coding DCMC: data coding / message class
			- Coding: enums.Coding: Optional setting parameter. Data coding, selecting the used character set GSM: GSM 7-bit default alphabet coding (ASCII) EIGHt: 8-bit binary data UCS2: UCS-2 16-bit coding (only for GDC, not for DCMC)
			- Class: enums.Class: Optional setting parameter. Message class 0 to 3, selecting to which component of the UE the message is delivered.
			- Core_Network: enums.CoreNetwork: Optional setting parameter. Type of network delivering the message, EPS or 5G"""
		__meta_args_list = [
			]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Address: str = None
			self.Message: str = None
			self.Type_Py: enums.Type = None
			self.Coding: enums.Coding = None
			self.Class: enums.Class = None
			self.Core_Network: enums.CoreNetwork = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: PROCedure:SIGNaling:SMS \n
		Snippet: driver.procedure.signaling.sms.set(value = [PROPERTY_STRUCT_NAME]()) \n
		Sends a short message to the UE. For background information, see 3GPP TS 23.038. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'PROCedure:SIGNaling:SMS', structure)
