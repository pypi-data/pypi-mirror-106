from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 8 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def rcMode(self):
		"""rcMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcMode'):
			from .Uplink_.RcMode import RcMode
			self._rcMode = RcMode(self._core, self._base)
		return self._rcMode

	@property
	def meRms(self):
		"""meRms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_meRms'):
			from .Uplink_.MeRms import MeRms
			self._meRms = MeRms(self._core, self._base)
		return self._meRms

	@property
	def meepre(self):
		"""meepre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_meepre'):
			from .Uplink_.Meepre import Meepre
			self._meepre = Meepre(self._core, self._base)
		return self._meepre

	@property
	def auto(self):
		"""auto commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_auto'):
			from .Uplink_.Auto import Auto
			self._auto = Auto(self._core, self._base)
		return self._auto

	@property
	def prStep(self):
		"""prStep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prStep'):
			from .Uplink_.PrStep import PrStep
			self._prStep = PrStep(self._core, self._base)
		return self._prStep

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cindex'):
			from .Uplink_.Cindex import Cindex
			self._cindex = Cindex(self._core, self._base)
		return self._cindex

	@property
	def prtPower(self):
		"""prtPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prtPower'):
			from .Uplink_.PrtPower import PrtPower
			self._prtPower = PrtPower(self._core, self._base)
		return self._prtPower

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
