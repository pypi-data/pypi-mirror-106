from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 5 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sense", core, parent)

	@property
	def elog(self):
		"""elog commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_elog'):
			from .Sense_.Elog import Elog
			self._elog = Elog(self._core, self._base)
		return self._elog

	@property
	def signaling(self):
		"""signaling commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_signaling'):
			from .Sense_.Signaling import Signaling
			self._signaling = Signaling(self._core, self._base)
		return self._signaling

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
