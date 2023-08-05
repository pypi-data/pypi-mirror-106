from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 6 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def sepre(self):
		"""sepre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sepre'):
			from .Downlink_.Sepre import Sepre
			self._sepre = Sepre(self._core, self._base)
		return self._sepre

	@property
	def tcell(self):
		"""tcell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcell'):
			from .Downlink_.Tcell import Tcell
			self._tcell = Tcell(self._core, self._base)
		return self._tcell

	@property
	def ocng(self):
		"""ocng commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ocng'):
			from .Downlink_.Ocng import Ocng
			self._ocng = Ocng(self._core, self._base)
		return self._ocng

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
