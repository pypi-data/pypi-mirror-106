from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Registration:
	"""Registration commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("registration", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .Registration_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Registration_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	def reset(self, target: enums.Target) -> None:
		"""SCPI: DIAGnostic:SIGNaling:REGistration:RESet \n
		Snippet: driver.diagnostic.signaling.registration.reset(target = enums.Target.ALL) \n
		No command help available \n
			:param target: No help available
		"""
		param = Conversions.enum_scalar_to_str(target, enums.Target)
		self._core.io.write(f'DIAGnostic:SIGNaling:REGistration:RESet {param}')

	def clone(self) -> 'Registration':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Registration(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
