from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ue:
	"""Ue commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ue", core, parent)

	@property
	def dcMode(self):
		"""dcMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcMode'):
			from .Ue_.DcMode import DcMode
			self._dcMode = DcMode(self._core, self._base)
		return self._dcMode

	@property
	def rrcState(self):
		"""rrcState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrcState'):
			from .Ue_.RrcState import RrcState
			self._rrcState = RrcState(self._core, self._base)
		return self._rrcState

	@property
	def imei(self):
		"""imei commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imei'):
			from .Ue_.Imei import Imei
			self._imei = Imei(self._core, self._base)
		return self._imei

	def clone(self) -> 'Ue':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ue(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
