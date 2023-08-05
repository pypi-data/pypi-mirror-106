from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lte:
	"""Lte commands group definition. 89 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("lte", core, parent)

	@property
	def ca(self):
		"""ca commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ca'):
			from .Lte_.Ca import Ca
			self._ca = Ca(self._core, self._base)
		return self._ca

	@property
	def cell(self):
		"""cell commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Lte_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	@property
	def ue(self):
		"""ue commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Lte_.Ue import Ue
			self._ue = Ue(self._core, self._base)
		return self._ue

	def clone(self) -> 'Lte':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lte(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
