from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefined:
	"""UserDefined commands group definition. 22 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("userDefined", core, parent)

	@property
	def sassignment(self):
		"""sassignment commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sassignment'):
			from .UserDefined_.Sassignment import Sassignment
			self._sassignment = Sassignment(self._core, self._base)
		return self._sassignment

	@property
	def pdcch(self):
		"""pdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcch'):
			from .UserDefined_.Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._base)
		return self._pdcch

	@property
	def downlink(self):
		"""downlink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .UserDefined_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	def clone(self) -> 'UserDefined':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefined(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
