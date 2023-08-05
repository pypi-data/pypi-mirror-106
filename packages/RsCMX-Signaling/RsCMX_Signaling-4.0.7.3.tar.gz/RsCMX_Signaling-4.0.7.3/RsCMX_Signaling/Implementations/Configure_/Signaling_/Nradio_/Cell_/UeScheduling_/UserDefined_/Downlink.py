from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 6 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def padding(self):
		"""padding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_padding'):
			from .Downlink_.Padding import Padding
			self._padding = Padding(self._core, self._base)
		return self._padding

	@property
	def bpid(self):
		"""bpid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bpid'):
			from .Downlink_.Bpid import Bpid
			self._bpid = Bpid(self._core, self._base)
		return self._bpid

	@property
	def alevel(self):
		"""alevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alevel'):
			from .Downlink_.Alevel import Alevel
			self._alevel = Alevel(self._core, self._base)
		return self._alevel

	@property
	def ssid(self):
		"""ssid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssid'):
			from .Downlink_.Ssid import Ssid
			self._ssid = Ssid(self._core, self._base)
		return self._ssid

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .Downlink_.McsTable import McsTable
			self._mcsTable = McsTable(self._core, self._base)
		return self._mcsTable

	@property
	def vpMapping(self):
		"""vpMapping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vpMapping'):
			from .Downlink_.VpMapping import VpMapping
			self._vpMapping = VpMapping(self._core, self._base)
		return self._vpMapping

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
