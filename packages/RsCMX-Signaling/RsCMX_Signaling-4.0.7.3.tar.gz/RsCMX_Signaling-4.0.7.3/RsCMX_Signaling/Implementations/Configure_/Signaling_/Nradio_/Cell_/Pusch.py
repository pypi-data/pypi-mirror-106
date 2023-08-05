from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 3 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pusch", core, parent)

	@property
	def tprecoding(self):
		"""tprecoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tprecoding'):
			from .Pusch_.Tprecoding import Tprecoding
			self._tprecoding = Tprecoding(self._core, self._base)
		return self._tprecoding

	@property
	def dtfs(self):
		"""dtfs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dtfs'):
			from .Pusch_.Dtfs import Dtfs
			self._dtfs = Dtfs(self._core, self._base)
		return self._dtfs

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
