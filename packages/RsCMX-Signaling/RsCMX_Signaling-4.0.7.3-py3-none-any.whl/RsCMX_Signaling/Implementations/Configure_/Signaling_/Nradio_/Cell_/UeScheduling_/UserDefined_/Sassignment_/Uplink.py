from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 8 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Uplink_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def rb(self):
		"""rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb'):
			from .Uplink_.Rb import Rb
			self._rb = Rb(self._core, self._base)
		return self._rb

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Uplink_.Mcs import Mcs
			self._mcs = Mcs(self._core, self._base)
		return self._mcs

	@property
	def dciFormat(self):
		"""dciFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dciFormat'):
			from .Uplink_.DciFormat import DciFormat
			self._dciFormat = DciFormat(self._core, self._base)
		return self._dciFormat

	@property
	def mimo(self):
		"""mimo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mimo'):
			from .Uplink_.Mimo import Mimo
			self._mimo = Mimo(self._core, self._base)
		return self._mimo

	@property
	def tdomain(self):
		"""tdomain commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdomain'):
			from .Uplink_.Tdomain import Tdomain
			self._tdomain = Tdomain(self._core, self._base)
		return self._tdomain

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
