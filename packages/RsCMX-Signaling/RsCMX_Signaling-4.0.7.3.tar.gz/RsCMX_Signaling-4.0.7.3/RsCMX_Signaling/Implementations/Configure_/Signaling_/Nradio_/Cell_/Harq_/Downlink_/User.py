from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 10 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("user", core, parent)

	@property
	def ack(self):
		"""ack commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ack'):
			from .User_.Ack import Ack
			self._ack = Ack(self._core, self._base)
		return self._ack

	@property
	def dtx(self):
		"""dtx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtx'):
			from .User_.Dtx import Dtx
			self._dtx = Dtx(self._core, self._base)
		return self._dtx

	@property
	def minOffset(self):
		"""minOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minOffset'):
			from .User_.MinOffset import MinOffset
			self._minOffset = MinOffset(self._core, self._base)
		return self._minOffset

	@property
	def retransm(self):
		"""retransm commands group. 5 Sub-classes, 2 commands."""
		if not hasattr(self, '_retransm'):
			from .User_.Retransm import Retransm
			self._retransm = Retransm(self._core, self._base)
		return self._retransm

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
