from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ocng:
	"""Ocng commands group definition. 4 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ocng", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Ocng_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def pdsch(self):
		"""pdsch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Ocng_.Pdsch import Pdsch
			self._pdsch = Pdsch(self._core, self._base)
		return self._pdsch

	@property
	def pdcch(self):
		"""pdcch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Ocng_.Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._base)
		return self._pdcch

	def clone(self) -> 'Ocng':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ocng(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
