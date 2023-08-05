from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 12 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def cmode(self):
		"""cmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmode'):
			from .Downlink_.Cmode import Cmode
			self._cmode = Cmode(self._core, self._base)
		return self._cmode

	@property
	def user(self):
		"""user commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .Downlink_.User import User
			self._user = User(self._core, self._base)
		return self._user

	@property
	def auto(self):
		"""auto commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_auto'):
			from .Downlink_.Auto import Auto
			self._auto = Auto(self._core, self._base)
		return self._auto

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
