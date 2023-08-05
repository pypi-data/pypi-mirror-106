from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sassignment:
	"""Sassignment commands group definition. 20 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sassignment", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Sassignment_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Sassignment_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	def clone(self) -> 'Sassignment':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sassignment(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
