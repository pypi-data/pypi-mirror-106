from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signaling:
	"""Signaling commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("signaling", core, parent)

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Signaling_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	# noinspection PyTypeChecker
	class SmsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Core_Network: List[enums.CoreNetwork]: Type of network delivering the message, EPS or 5G
			- Address: List[str]: Address of the originator of the message
			- State: List[enums.StateC]: Indicates whether an error occurred.
			- Message: List[str]: For successful transmission, the short message contents. For erroneous transmission, information about the error."""
		__meta_args_list = [
			ArgStruct('Core_Network', DataType.EnumList, enums.CoreNetwork, False, True, 1),
			ArgStruct('Address', DataType.StringList, None, False, True, 1),
			ArgStruct('State', DataType.EnumList, enums.StateC, False, True, 1),
			ArgStruct('Message', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Core_Network: List[enums.CoreNetwork] = None
			self.Address: List[str] = None
			self.State: List[enums.StateC] = None
			self.Message: List[str] = None

	# noinspection PyTypeChecker
	def get_sms(self) -> SmsStruct:
		"""SCPI: SENSe:SIGNaling:SMS \n
		Snippet: value: SmsStruct = driver.sense.signaling.get_sms() \n
		Queries information about the last received mobile-originating short message. \n
			:return: structure: for return value, see the help for SmsStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:SIGNaling:SMS?', self.__class__.SmsStruct())

	def clone(self) -> 'Signaling':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Signaling(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
