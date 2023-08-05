from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 11 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def tmode(self):
		"""tmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmode'):
			from .Downlink_.Tmode import Tmode
			self._tmode = Tmode(self._core, self._base)
		return self._tmode

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Downlink_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def pdcchFormat(self):
		"""pdcchFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcchFormat'):
			from .Downlink_.PdcchFormat import PdcchFormat
			self._pdcchFormat = PdcchFormat(self._core, self._base)
		return self._pdcchFormat

	@property
	def dciFormat(self):
		"""dciFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dciFormat'):
			from .Downlink_.DciFormat import DciFormat
			self._dciFormat = DciFormat(self._core, self._base)
		return self._dciFormat

	@property
	def riv(self):
		"""riv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_riv'):
			from .Downlink_.Riv import Riv
			self._riv = Riv(self._core, self._base)
		return self._riv

	@property
	def rb(self):
		"""rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb'):
			from .Downlink_.Rb import Rb
			self._rb = Rb(self._core, self._base)
		return self._rb

	@property
	def cword(self):
		"""cword commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cword'):
			from .Downlink_.Cword import Cword
			self._cword = Cword(self._core, self._base)
		return self._cword

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .Downlink_.McsTable import McsTable
			self._mcsTable = McsTable(self._core, self._base)
		return self._mcsTable

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
