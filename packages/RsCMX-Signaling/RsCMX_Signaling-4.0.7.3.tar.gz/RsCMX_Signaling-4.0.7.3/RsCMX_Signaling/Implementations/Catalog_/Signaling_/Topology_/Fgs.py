from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fgs:
	"""Fgs commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fgs", core, parent)

	@property
	def ue(self):
		"""ue commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Fgs_.Ue import Ue
			self._ue = Ue(self._core, self._base)
		return self._ue

	def get(self, name_plmn: str = None) -> List[str]:
		"""SCPI: CATalog:SIGNaling:TOPology:FGS \n
		Snippet: value: List[str] = driver.catalog.signaling.topology.fgs.get(name_plmn = '1') \n
		Queries a list of all 5G tracking areas. You can restrict the query to a selected PLMN. \n
			:param name_plmn: No help available
			:return: name_ta_5_g: Comma-separated list of tracking area names, one string per tracking area."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_plmn', name_plmn, DataType.String, True))
		response = self._core.io.query_str(f'CATalog:SIGNaling:TOPology:FGS? {param}'.rstrip())
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Fgs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fgs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
