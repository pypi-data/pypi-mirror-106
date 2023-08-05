from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cword:
	"""Cword commands group definition. 4 total commands, 4 Sub-groups, 0 group commands
	Repeated Capability: Cword, default value after init: Cword.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cword", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_cword_get', 'repcap_cword_set', repcap.Cword.Nr1)

	def repcap_cword_set(self, enum_value: repcap.Cword) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Cword.Default
		Default value after init: Cword.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_cword_get(self) -> repcap.Cword:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def tbsIndex(self):
		"""tbsIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbsIndex'):
			from .Cword_.TbsIndex import TbsIndex
			self._tbsIndex = TbsIndex(self._core, self._base)
		return self._tbsIndex

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Cword_.Mcs import Mcs
			self._mcs = Mcs(self._core, self._base)
		return self._mcs

	@property
	def tbsBits(self):
		"""tbsBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbsBits'):
			from .Cword_.TbsBits import TbsBits
			self._tbsBits = TbsBits(self._core, self._base)
		return self._tbsBits

	@property
	def crtype(self):
		"""crtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crtype'):
			from .Cword_.Crtype import Crtype
			self._crtype = Crtype(self._core, self._base)
		return self._crtype

	def clone(self) -> 'Cword':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cword(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
