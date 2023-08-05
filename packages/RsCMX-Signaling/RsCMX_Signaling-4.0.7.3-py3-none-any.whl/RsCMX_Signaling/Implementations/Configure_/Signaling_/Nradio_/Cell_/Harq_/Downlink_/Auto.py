from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("auto", core, parent)

	@property
	def mret(self):
		"""mret commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mret'):
			from .Auto_.Mret import Mret
			self._mret = Mret(self._core, self._base)
		return self._mret

	def clone(self) -> 'Auto':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Auto(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
