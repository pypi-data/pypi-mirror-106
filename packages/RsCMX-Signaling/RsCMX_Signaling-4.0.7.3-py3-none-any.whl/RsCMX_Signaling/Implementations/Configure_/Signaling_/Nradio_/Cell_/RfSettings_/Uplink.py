from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 7 total commands, 5 Sub-groups, 0 group commands"""

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
	def apoint(self):
		"""apoint commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_apoint'):
			from .Uplink_.Apoint import Apoint
			self._apoint = Apoint(self._core, self._base)
		return self._apoint

	@property
	def ibwp(self):
		"""ibwp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ibwp'):
			from .Uplink_.Ibwp import Ibwp
			self._ibwp = Ibwp(self._core, self._base)
		return self._ibwp

	@property
	def ocarrier(self):
		"""ocarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ocarrier'):
			from .Uplink_.Ocarrier import Ocarrier
			self._ocarrier = Ocarrier(self._core, self._base)
		return self._ocarrier

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
