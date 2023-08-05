from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dtfs:
	"""Dtfs commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dtfs", core, parent)

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .Dtfs_.McsTable import McsTable
			self._mcsTable = McsTable(self._core, self._base)
		return self._mcsTable

	@property
	def pibPsk(self):
		"""pibPsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pibPsk'):
			from .Dtfs_.PibPsk import PibPsk
			self._pibPsk = PibPsk(self._core, self._base)
		return self._pibPsk

	def clone(self) -> 'Dtfs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dtfs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
