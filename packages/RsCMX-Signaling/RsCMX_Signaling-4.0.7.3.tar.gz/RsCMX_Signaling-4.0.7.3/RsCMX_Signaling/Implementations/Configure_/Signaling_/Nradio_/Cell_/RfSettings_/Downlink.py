from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 6 total commands, 4 Sub-groups, 0 group commands"""

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
	def apoint(self):
		"""apoint commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_apoint'):
			from .Downlink_.Apoint import Apoint
			self._apoint = Apoint(self._core, self._base)
		return self._apoint

	@property
	def ibwp(self):
		"""ibwp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ibwp'):
			from .Downlink_.Ibwp import Ibwp
			self._ibwp = Ibwp(self._core, self._base)
		return self._ibwp

	@property
	def ocarrier(self):
		"""ocarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ocarrier'):
			from .Downlink_.Ocarrier import Ocarrier
			self._ocarrier = Ocarrier(self._core, self._base)
		return self._ocarrier

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
