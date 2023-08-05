from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Register:
	"""Register commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("register", core, parent)

	@property
	def existing(self):
		"""existing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_existing'):
			from .Register_.Existing import Existing
			self._existing = Existing(self._core, self._base)
		return self._existing

	def clone(self) -> 'Register':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Register(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
