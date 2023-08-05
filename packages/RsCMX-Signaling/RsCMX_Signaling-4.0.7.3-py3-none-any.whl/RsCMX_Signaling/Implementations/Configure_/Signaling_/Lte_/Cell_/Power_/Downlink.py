from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 13 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def rsepre(self):
		"""rsepre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsepre'):
			from .Downlink_.Rsepre import Rsepre
			self._rsepre = Rsepre(self._core, self._base)
		return self._rsepre

	@property
	def reference(self):
		"""reference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reference'):
			from .Downlink_.Reference import Reference
			self._reference = Reference(self._core, self._base)
		return self._reference

	@property
	def ocng(self):
		"""ocng commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ocng'):
			from .Downlink_.Ocng import Ocng
			self._ocng = Ocng(self._core, self._base)
		return self._ocng

	@property
	def offset(self):
		"""offset commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_offset'):
			from .Downlink_.Offset import Offset
			self._offset = Offset(self._core, self._base)
		return self._offset

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Downlink_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
