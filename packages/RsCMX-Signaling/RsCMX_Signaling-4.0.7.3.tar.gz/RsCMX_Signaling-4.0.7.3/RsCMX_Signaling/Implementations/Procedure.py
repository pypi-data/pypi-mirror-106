from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Procedure:
	"""Procedure commands group definition. 5 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("procedure", core, parent)

	@property
	def signaling(self):
		"""signaling commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_signaling'):
			from .Procedure_.Signaling import Signaling
			self._signaling = Signaling(self._core, self._base)
		return self._signaling

	def clone(self) -> 'Procedure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Procedure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
