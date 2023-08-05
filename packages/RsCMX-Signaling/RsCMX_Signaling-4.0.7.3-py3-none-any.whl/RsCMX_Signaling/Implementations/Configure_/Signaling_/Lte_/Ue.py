from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ue:
	"""Ue commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ue", core, parent)

	@property
	def nsa(self):
		"""nsa commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_nsa'):
			from .Ue_.Nsa import Nsa
			self._nsa = Nsa(self._core, self._base)
		return self._nsa

	def clone(self) -> 'Ue':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ue(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
