from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Control:
	"""Control commands group definition. 7 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("control", core, parent)

	@property
	def tpControl(self):
		"""tpControl commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpControl'):
			from .Control_.TpControl import TpControl
			self._tpControl = TpControl(self._core, self._base)
		return self._tpControl

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Control_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	def clone(self) -> 'Control':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Control(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
