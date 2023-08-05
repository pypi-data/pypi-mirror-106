from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 86 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def timing(self):
		"""timing commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Cell_.Timing import Timing
			self._timing = Timing(self._core, self._base)
		return self._timing

	@property
	def mconfig(self):
		"""mconfig commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mconfig'):
			from .Cell_.Mconfig import Mconfig
			self._mconfig = Mconfig(self._core, self._base)
		return self._mconfig

	@property
	def pcid(self):
		"""pcid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcid'):
			from .Cell_.Pcid import Pcid
			self._pcid = Pcid(self._core, self._base)
		return self._pcid

	@property
	def rfSettings(self):
		"""rfSettings commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Cell_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def tdd(self):
		"""tdd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdd'):
			from .Cell_.Tdd import Tdd
			self._tdd = Tdd(self._core, self._base)
		return self._tdd

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Cell_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def antenna(self):
		"""antenna commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_antenna'):
			from .Cell_.Antenna import Antenna
			self._antenna = Antenna(self._core, self._base)
		return self._antenna

	@property
	def ueScheduling(self):
		"""ueScheduling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueScheduling'):
			from .Cell_.UeScheduling import UeScheduling
			self._ueScheduling = UeScheduling(self._core, self._base)
		return self._ueScheduling

	@property
	def timeout(self):
		"""timeout commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_timeout'):
			from .Cell_.Timeout import Timeout
			self._timeout = Timeout(self._core, self._base)
		return self._timeout

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
