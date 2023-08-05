from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeScheduling:
	"""UeScheduling commands group definition. 22 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueScheduling", core, parent)

	@property
	def userDefined(self):
		"""userDefined commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_userDefined'):
			from .UeScheduling_.UserDefined import UserDefined
			self._userDefined = UserDefined(self._core, self._base)
		return self._userDefined

	def clone(self) -> 'UeScheduling':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeScheduling(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
