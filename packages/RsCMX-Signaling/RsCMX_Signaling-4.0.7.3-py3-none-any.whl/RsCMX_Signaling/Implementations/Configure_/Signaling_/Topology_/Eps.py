from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eps:
	"""Eps commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eps", core, parent)

	@property
	def timer(self):
		"""timer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_timer'):
			from .Eps_.Timer import Timer
			self._timer = Timer(self._core, self._base)
		return self._timer

	@property
	def taCode(self):
		"""taCode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taCode'):
			from .Eps_.TaCode import TaCode
			self._taCode = TaCode(self._core, self._base)
		return self._taCode

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Eps_.Info import Info
			self._info = Info(self._core, self._base)
		return self._info

	def clone(self) -> 'Eps':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eps(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
