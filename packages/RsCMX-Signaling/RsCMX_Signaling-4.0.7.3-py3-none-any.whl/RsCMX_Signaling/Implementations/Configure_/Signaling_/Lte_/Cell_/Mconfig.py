from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mconfig:
	"""Mconfig commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mconfig", core, parent)

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Mconfig_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def crSports(self):
		"""crSports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crSports'):
			from .Mconfig_.CrSports import CrSports
			self._crSports = CrSports(self._core, self._base)
		return self._crSports

	@property
	def csirsPorts(self):
		"""csirsPorts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csirsPorts'):
			from .Mconfig_.CsirsPorts import CsirsPorts
			self._csirsPorts = CsirsPorts(self._core, self._base)
		return self._csirsPorts

	def clone(self) -> 'Mconfig':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mconfig(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
