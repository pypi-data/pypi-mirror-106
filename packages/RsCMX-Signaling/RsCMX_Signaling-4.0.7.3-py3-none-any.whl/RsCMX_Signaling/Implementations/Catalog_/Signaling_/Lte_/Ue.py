from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ue:
	"""Ue commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ue", core, parent)

	@property
	def dbearer(self):
		"""dbearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbearer'):
			from .Ue_.Dbearer import Dbearer
			self._dbearer = Dbearer(self._core, self._base)
		return self._dbearer

	@property
	def bearer(self):
		"""bearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bearer'):
			from .Ue_.Bearer import Bearer
			self._bearer = Bearer(self._core, self._base)
		return self._bearer

	def clone(self) -> 'Ue':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ue(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
