from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Afrequency:
	"""Afrequency commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("afrequency", core, parent)

	@property
	def arfcn(self):
		"""arfcn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_arfcn'):
			from .Afrequency_.Arfcn import Arfcn
			self._arfcn = Arfcn(self._core, self._base)
		return self._arfcn

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Afrequency_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	def clone(self) -> 'Afrequency':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Afrequency(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
