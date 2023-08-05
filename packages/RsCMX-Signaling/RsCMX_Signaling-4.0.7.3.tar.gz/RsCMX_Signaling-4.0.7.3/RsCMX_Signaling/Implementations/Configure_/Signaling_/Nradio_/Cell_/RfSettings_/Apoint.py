from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apoint:
	"""Apoint commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("apoint", core, parent)

	@property
	def location(self):
		"""location commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_location'):
			from .Apoint_.Location import Location
			self._location = Location(self._core, self._base)
		return self._location

	@property
	def arfcn(self):
		"""arfcn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_arfcn'):
			from .Apoint_.Arfcn import Arfcn
			self._arfcn = Arfcn(self._core, self._base)
		return self._arfcn

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Apoint_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	def clone(self) -> 'Apoint':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Apoint(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
