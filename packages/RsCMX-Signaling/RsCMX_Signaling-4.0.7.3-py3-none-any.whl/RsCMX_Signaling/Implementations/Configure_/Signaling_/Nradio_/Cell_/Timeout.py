from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timeout:
	"""Timeout commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("timeout", core, parent)

	@property
	def t(self):
		"""t commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_t'):
			from .Timeout_.T import T
			self._t = T(self._core, self._base)
		return self._t

	@property
	def n(self):
		"""n commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n'):
			from .Timeout_.N import N
			self._n = N(self._core, self._base)
		return self._n

	def clone(self) -> 'Timeout':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Timeout(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
