from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nradio:
	"""Nradio commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nradio", core, parent)

	@property
	def ca(self):
		"""ca commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ca'):
			from .Nradio_.Ca import Ca
			self._ca = Ca(self._core, self._base)
		return self._ca

	def get_cgroup(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:NRADio:CGRoup \n
		Snippet: value: List[str] = driver.catalog.signaling.nradio.get_cgroup() \n
		Queries a list of all LTE or NR cell groups. \n
			:return: cell_group_name: Comma-separated list of cell group names, one string per cell group.
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:NRADio:CGRoup?')
		return Conversions.str_to_str_list(response)

	def get_cell(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:NRADio:CELL \n
		Snippet: value: List[str] = driver.catalog.signaling.nradio.get_cell() \n
		Queries a list of all LTE or NR cells. \n
			:return: cell_name: Comma-separated list of cell names, one string per cell.
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:NRADio:CELL?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Nradio':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nradio(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
