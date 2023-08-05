from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cloop:
	"""Cloop commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cloop", core, parent)

	@property
	def tolerance(self):
		"""tolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tolerance'):
			from .Cloop_.Tolerance import Tolerance
			self._tolerance = Tolerance(self._core, self._base)
		return self._tolerance

	@property
	def tpower(self):
		"""tpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpower'):
			from .Cloop_.Tpower import Tpower
			self._tpower = Tpower(self._core, self._base)
		return self._tpower

	def clone(self) -> 'Cloop':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cloop(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
