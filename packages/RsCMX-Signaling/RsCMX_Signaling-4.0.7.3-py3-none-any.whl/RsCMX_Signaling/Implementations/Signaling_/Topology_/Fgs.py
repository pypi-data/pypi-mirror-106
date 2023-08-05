from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fgs:
	"""Fgs commands group definition. 4 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fgs", core, parent)

	@property
	def ue(self):
		"""ue commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Fgs_.Ue import Ue
			self._ue = Ue(self._core, self._base)
		return self._ue

	def delete(self, name_ta_5_g: str) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:FGS \n
		Snippet: driver.signaling.topology.fgs.delete(name_ta_5_g = '1') \n
		Deletes a 5G tracking area. \n
			:param name_ta_5_g: No help available
		"""
		param = Conversions.value_to_quoted_str(name_ta_5_g)
		self._core.io.write(f'DELete:SIGNaling:TOPology:FGS {param}')

	def clone(self) -> 'Fgs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fgs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
