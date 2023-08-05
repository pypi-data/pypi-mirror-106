from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 5 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Uplink_.Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._base)
		return self._bandwidth

	@property
	def earfcn(self):
		"""earfcn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_earfcn'):
			from .Uplink_.Earfcn import Earfcn
			self._earfcn = Earfcn(self._core, self._base)
		return self._earfcn

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Uplink_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def rblocks(self):
		"""rblocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rblocks'):
			from .Uplink_.Rblocks import Rblocks
			self._rblocks = Rblocks(self._core, self._base)
		return self._rblocks

	@property
	def asEmission(self):
		"""asEmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asEmission'):
			from .Uplink_.AsEmission import AsEmission
			self._asEmission = AsEmission(self._core, self._base)
		return self._asEmission

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
