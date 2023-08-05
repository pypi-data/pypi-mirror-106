from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 15 total commands, 12 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def cmode(self):
		"""cmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmode'):
			from .Uplink_.Cmode import Cmode
			self._cmode = Cmode(self._core, self._base)
		return self._cmode

	@property
	def auto(self):
		"""auto commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_auto'):
			from .Uplink_.Auto import Auto
			self._auto = Auto(self._core, self._base)
		return self._auto

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Uplink_.Pucch import Pucch
			self._pucch = Pucch(self._core, self._base)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Uplink_.Pusch import Pusch
			self._pusch = Pusch(self._core, self._base)
		return self._pusch

	@property
	def epre(self):
		"""epre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_epre'):
			from .Uplink_.Epre import Epre
			self._epre = Epre(self._core, self._base)
		return self._epre

	@property
	def rms(self):
		"""rms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rms'):
			from .Uplink_.Rms import Rms
			self._rms = Rms(self._core, self._base)
		return self._rms

	@property
	def pmax(self):
		"""pmax commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmax'):
			from .Uplink_.Pmax import Pmax
			self._pmax = Pmax(self._core, self._base)
		return self._pmax

	@property
	def alpha(self):
		"""alpha commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alpha'):
			from .Uplink_.Alpha import Alpha
			self._alpha = Alpha(self._core, self._base)
		return self._alpha

	@property
	def prStep(self):
		"""prStep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prStep'):
			from .Uplink_.PrStep import PrStep
			self._prStep = PrStep(self._core, self._base)
		return self._prStep

	@property
	def iptPower(self):
		"""iptPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iptPower'):
			from .Uplink_.IptPower import IptPower
			self._iptPower = IptPower(self._core, self._base)
		return self._iptPower

	@property
	def fcoefficient(self):
		"""fcoefficient commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fcoefficient'):
			from .Uplink_.Fcoefficient import Fcoefficient
			self._fcoefficient = Fcoefficient(self._core, self._base)
		return self._fcoefficient

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cindex'):
			from .Uplink_.Cindex import Cindex
			self._cindex = Cindex(self._core, self._base)
		return self._cindex

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
