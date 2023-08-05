from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Cell_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def cmatrix(self):
		"""cmatrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmatrix'):
			from .Cell_.Cmatrix import Cmatrix
			self._cmatrix = Cmatrix(self._core, self._base)
		return self._cmatrix

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
