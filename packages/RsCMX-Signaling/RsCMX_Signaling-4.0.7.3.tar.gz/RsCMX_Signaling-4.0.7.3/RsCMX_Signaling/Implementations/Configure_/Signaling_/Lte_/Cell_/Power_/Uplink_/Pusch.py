from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pusch", core, parent)

	@property
	def nominal(self):
		"""nominal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nominal'):
			from .Pusch_.Nominal import Nominal
			self._nominal = Nominal(self._core, self._base)
		return self._nominal

	@property
	def ue(self):
		"""ue commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ue'):
			from .Pusch_.Ue import Ue
			self._ue = Ue(self._core, self._base)
		return self._ue

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
