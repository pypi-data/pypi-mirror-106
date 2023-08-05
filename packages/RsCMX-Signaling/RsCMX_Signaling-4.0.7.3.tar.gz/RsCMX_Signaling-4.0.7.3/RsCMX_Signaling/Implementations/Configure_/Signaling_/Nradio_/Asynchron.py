from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Asynchron:
	"""Asynchron commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("asynchron", core, parent)

	@property
	def test(self):
		"""test commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_test'):
			from .Asynchron_.Test import Test
			self._test = Test(self._core, self._base)
		return self._test

	def clone(self) -> 'Asynchron':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Asynchron(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
