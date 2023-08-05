from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plmn:
	"""Plmn commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("plmn", core, parent)

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Plmn_.Info import Info
			self._info = Info(self._core, self._base)
		return self._info

	@property
	def mnc(self):
		"""mnc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mnc'):
			from .Plmn_.Mnc import Mnc
			self._mnc = Mnc(self._core, self._base)
		return self._mnc

	@property
	def mcc(self):
		"""mcc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcc'):
			from .Plmn_.Mcc import Mcc
			self._mcc = Mcc(self._core, self._base)
		return self._mcc

	def clone(self) -> 'Plmn':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Plmn(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
