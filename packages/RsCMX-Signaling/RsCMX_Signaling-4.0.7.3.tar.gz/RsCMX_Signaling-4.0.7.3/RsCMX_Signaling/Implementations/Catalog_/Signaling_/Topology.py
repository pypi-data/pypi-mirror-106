from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Topology:
	"""Topology commands group definition. 5 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("topology", core, parent)

	@property
	def eps(self):
		"""eps commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eps'):
			from .Topology_.Eps import Eps
			self._eps = Eps(self._core, self._base)
		return self._eps

	@property
	def fgs(self):
		"""fgs commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fgs'):
			from .Topology_.Fgs import Fgs
			self._fgs = Fgs(self._core, self._base)
		return self._fgs

	def get_plmn(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:TOPology:PLMN \n
		Snippet: value: List[str] = driver.catalog.signaling.topology.get_plmn() \n
		Queries a list of all created PLMNs. \n
			:return: name_plmn: Comma-separated list of PLMN names, one string per PLMN.
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:TOPology:PLMN?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Topology':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Topology(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
