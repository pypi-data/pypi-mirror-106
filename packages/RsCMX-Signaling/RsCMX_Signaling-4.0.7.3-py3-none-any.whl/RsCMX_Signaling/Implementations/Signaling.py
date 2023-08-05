from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signaling:
	"""Signaling commands group definition. 21 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("signaling", core, parent)

	@property
	def measurement(self):
		"""measurement commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Signaling_.Measurement import Measurement
			self._measurement = Measurement(self._core, self._base)
		return self._measurement

	@property
	def topology(self):
		"""topology commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_topology'):
			from .Signaling_.Topology import Topology
			self._topology = Topology(self._core, self._base)
		return self._topology

	@property
	def ue(self):
		"""ue commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Signaling_.Ue import Ue
			self._ue = Ue(self._core, self._base)
		return self._ue

	@property
	def lte(self):
		"""lte commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Signaling_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	@property
	def nradio(self):
		"""nradio commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nradio'):
			from .Signaling_.Nradio import Nradio
			self._nradio = Nradio(self._core, self._base)
		return self._nradio

	def clone(self) -> 'Signaling':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Signaling(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
