from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nradio:
	"""Nradio commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nradio", core, parent)

	@property
	def cgroup(self):
		"""cgroup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cgroup'):
			from .Nradio_.Cgroup import Cgroup
			self._cgroup = Cgroup(self._core, self._base)
		return self._cgroup

	@property
	def cell(self):
		"""cell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cell'):
			from .Nradio_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	def clone(self) -> 'Nradio':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nradio(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
