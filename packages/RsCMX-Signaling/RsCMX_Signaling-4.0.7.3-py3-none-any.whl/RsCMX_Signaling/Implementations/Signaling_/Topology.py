from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Topology:
	"""Topology commands group definition. 9 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("topology", core, parent)

	@property
	def cnetwork(self):
		"""cnetwork commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cnetwork'):
			from .Topology_.Cnetwork import Cnetwork
			self._cnetwork = Cnetwork(self._core, self._base)
		return self._cnetwork

	@property
	def plmn(self):
		"""plmn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plmn'):
			from .Topology_.Plmn import Plmn
			self._plmn = Plmn(self._core, self._base)
		return self._plmn

	@property
	def eps(self):
		"""eps commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_eps'):
			from .Topology_.Eps import Eps
			self._eps = Eps(self._core, self._base)
		return self._eps

	@property
	def fgs(self):
		"""fgs commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fgs'):
			from .Topology_.Fgs import Fgs
			self._fgs = Fgs(self._core, self._base)
		return self._fgs

	def clone(self) -> 'Topology':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Topology(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
