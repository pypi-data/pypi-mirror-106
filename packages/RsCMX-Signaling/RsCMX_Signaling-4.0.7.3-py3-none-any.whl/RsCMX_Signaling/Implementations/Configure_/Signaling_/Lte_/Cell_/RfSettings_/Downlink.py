from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 4 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Downlink_.Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._base)
		return self._bandwidth

	@property
	def earfcn(self):
		"""earfcn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_earfcn'):
			from .Downlink_.Earfcn import Earfcn
			self._earfcn = Earfcn(self._core, self._base)
		return self._earfcn

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Downlink_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def rblocks(self):
		"""rblocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rblocks'):
			from .Downlink_.Rblocks import Rblocks
			self._rblocks = Rblocks(self._core, self._base)
		return self._rblocks

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
