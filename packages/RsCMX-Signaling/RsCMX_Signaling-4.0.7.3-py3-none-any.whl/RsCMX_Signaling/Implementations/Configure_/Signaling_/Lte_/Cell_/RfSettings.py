from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 13 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	@property
	def dmode(self):
		"""dmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmode'):
			from .RfSettings_.Dmode import Dmode
			self._dmode = Dmode(self._core, self._base)
		return self._dmode

	@property
	def fbIndicator(self):
		"""fbIndicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fbIndicator'):
			from .RfSettings_.FbIndicator import FbIndicator
			self._fbIndicator = FbIndicator(self._core, self._base)
		return self._fbIndicator

	@property
	def bchannel(self):
		"""bchannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bchannel'):
			from .RfSettings_.Bchannel import Bchannel
			self._bchannel = Bchannel(self._core, self._base)
		return self._bchannel

	@property
	def downlink(self):
		"""downlink commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .RfSettings_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .RfSettings_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	@property
	def asEmission(self):
		"""asEmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asEmission'):
			from .RfSettings_.AsEmission import AsEmission
			self._asEmission = AsEmission(self._core, self._base)
		return self._asEmission

	def clone(self) -> 'RfSettings':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettings(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
