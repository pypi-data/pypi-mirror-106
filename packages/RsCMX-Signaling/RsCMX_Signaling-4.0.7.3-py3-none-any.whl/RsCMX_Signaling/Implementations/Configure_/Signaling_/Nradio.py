from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nradio:
	"""Nradio commands group definition. 113 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nradio", core, parent)

	@property
	def cell(self):
		"""cell commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Nradio_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	@property
	def asynchron(self):
		"""asynchron commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_asynchron'):
			from .Nradio_.Asynchron import Asynchron
			self._asynchron = Asynchron(self._core, self._base)
		return self._asynchron

	@property
	def ca(self):
		"""ca commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ca'):
			from .Nradio_.Ca import Ca
			self._ca = Ca(self._core, self._base)
		return self._ca

	def clone(self) -> 'Nradio':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nradio(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
