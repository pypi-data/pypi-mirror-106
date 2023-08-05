from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 111 total commands, 14 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Cell_.Pusch import Pusch
			self._pusch = Pusch(self._core, self._base)
		return self._pusch

	@property
	def pcid(self):
		"""pcid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcid'):
			from .Cell_.Pcid import Pcid
			self._pcid = Pcid(self._core, self._base)
		return self._pcid

	@property
	def rfSettings(self):
		"""rfSettings commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Cell_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Cell_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def tdd(self):
		"""tdd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdd'):
			from .Cell_.Tdd import Tdd
			self._tdd = Tdd(self._core, self._base)
		return self._tdd

	@property
	def ueScheduling(self):
		"""ueScheduling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueScheduling'):
			from .Cell_.UeScheduling import UeScheduling
			self._ueScheduling = UeScheduling(self._core, self._base)
		return self._ueScheduling

	@property
	def cssZero(self):
		"""cssZero commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cssZero'):
			from .Cell_.CssZero import CssZero
			self._cssZero = CssZero(self._core, self._base)
		return self._cssZero

	@property
	def ssb(self):
		"""ssb commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssb'):
			from .Cell_.Ssb import Ssb
			self._ssb = Ssb(self._core, self._base)
		return self._ssb

	@property
	def harq(self):
		"""harq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Cell_.Harq import Harq
			self._harq = Harq(self._core, self._base)
		return self._harq

	@property
	def bler(self):
		"""bler commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bler'):
			from .Cell_.Bler import Bler
			self._bler = Bler(self._core, self._base)
		return self._bler

	@property
	def mconfig(self):
		"""mconfig commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mconfig'):
			from .Cell_.Mconfig import Mconfig
			self._mconfig = Mconfig(self._core, self._base)
		return self._mconfig

	@property
	def timeout(self):
		"""timeout commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_timeout'):
			from .Cell_.Timeout import Timeout
			self._timeout = Timeout(self._core, self._base)
		return self._timeout

	@property
	def timing(self):
		"""timing commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Cell_.Timing import Timing
			self._timing = Timing(self._core, self._base)
		return self._timing

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Cell_.Info import Info
			self._info = Info(self._core, self._base)
		return self._info

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
