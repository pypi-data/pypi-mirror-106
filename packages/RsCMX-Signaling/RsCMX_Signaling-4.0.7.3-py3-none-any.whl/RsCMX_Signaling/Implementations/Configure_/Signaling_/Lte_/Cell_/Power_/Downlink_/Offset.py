from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 6 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("offset", core, parent)

	@property
	def pss(self):
		"""pss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pss'):
			from .Offset_.Pss import Pss
			self._pss = Pss(self._core, self._base)
		return self._pss

	@property
	def sss(self):
		"""sss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sss'):
			from .Offset_.Sss import Sss
			self._sss = Sss(self._core, self._base)
		return self._sss

	@property
	def rs(self):
		"""rs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rs'):
			from .Offset_.Rs import Rs
			self._rs = Rs(self._core, self._base)
		return self._rs

	@property
	def pbch(self):
		"""pbch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbch'):
			from .Offset_.Pbch import Pbch
			self._pbch = Pbch(self._core, self._base)
		return self._pbch

	@property
	def pcfich(self):
		"""pcfich commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcfich'):
			from .Offset_.Pcfich import Pcfich
			self._pcfich = Pcfich(self._core, self._base)
		return self._pcfich

	@property
	def pdcch(self):
		"""pdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcch'):
			from .Offset_.Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._base)
		return self._pdcch

	def clone(self) -> 'Offset':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Offset(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
