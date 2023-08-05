from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fgs:
	"""Fgs commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

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

	def set(self, name_ta_5_g: str, name_plmn: str, ta_code: float = None) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:FGS \n
		Snippet: driver.create.signaling.topology.fgs.set(name_ta_5_g = '1', name_plmn = '1', ta_code = 1.0) \n
		Creates a 5G tracking area in a selected PLMN and optionally defines the TAC. \n
			:param name_ta_5_g: Assigns a name to the tracking area. The string is used in other commands to select this tracking area.
			:param name_plmn: PLMN containing the tracking area.
			:param ta_code: Tracking area code (TAC) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta_5_g', name_ta_5_g, DataType.String), ArgSingle('name_plmn', name_plmn, DataType.String), ArgSingle('ta_code', ta_code, DataType.Float, True))
		self._core.io.write(f'CREate:SIGNaling:TOPology:FGS {param}'.rstrip())

	def clone(self) -> 'Fgs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fgs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
