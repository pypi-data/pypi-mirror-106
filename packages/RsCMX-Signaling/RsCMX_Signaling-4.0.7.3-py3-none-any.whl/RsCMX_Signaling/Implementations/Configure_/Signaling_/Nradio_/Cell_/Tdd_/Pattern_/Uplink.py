from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def nslots(self):
		"""nslots commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nslots'):
			from .Uplink_.Nslots import Nslots
			self._nslots = Nslots(self._core, self._base)
		return self._nslots

	@property
	def fsSymbol(self):
		"""fsSymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fsSymbol'):
			from .Uplink_.FsSymbol import FsSymbol
			self._fsSymbol = FsSymbol(self._core, self._base)
		return self._fsSymbol

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
