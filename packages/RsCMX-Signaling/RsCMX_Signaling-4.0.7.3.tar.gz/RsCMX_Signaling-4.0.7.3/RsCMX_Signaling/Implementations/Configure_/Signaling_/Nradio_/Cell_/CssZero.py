from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CssZero:
	"""CssZero commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cssZero", core, parent)

	@property
	def crZero(self):
		"""crZero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crZero'):
			from .CssZero_.CrZero import CrZero
			self._crZero = CrZero(self._core, self._base)
		return self._crZero

	@property
	def ssZero(self):
		"""ssZero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssZero'):
			from .CssZero_.SsZero import SsZero
			self._ssZero = SsZero(self._core, self._base)
		return self._ssZero

	def clone(self) -> 'CssZero':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CssZero(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
