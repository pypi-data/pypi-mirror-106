from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Elog:
	"""Elog commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("elog", core, parent)

	@property
	def last(self):
		"""last commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_last'):
			from .Elog_.Last import Last
			self._last = Last(self._core, self._base)
		return self._last

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Elog_.Time import Time
			self._time = Time(self._core, self._base)
		return self._time

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Severity: List[enums.Severity]: No parameter help available
			- Timestamp: List[str]: No parameter help available
			- Message: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Severity', DataType.EnumList, enums.Severity, False, True, 1),
			ArgStruct('Timestamp', DataType.StringList, None, False, True, 1),
			ArgStruct('Message', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Severity: List[enums.Severity] = None
			self.Timestamp: List[str] = None
			self.Message: List[str] = None

	# noinspection PyTypeChecker
	def get_all(self) -> AllStruct:
		"""SCPI: SENSe:ELOG:ALL \n
		Snippet: value: AllStruct = driver.sense.elog.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:ELOG:ALL?', self.__class__.AllStruct())

	def clone(self) -> 'Elog':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Elog(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
