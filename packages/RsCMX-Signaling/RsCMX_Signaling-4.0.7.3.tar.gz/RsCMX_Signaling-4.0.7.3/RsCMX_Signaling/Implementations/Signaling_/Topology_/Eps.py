from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eps:
	"""Eps commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eps", core, parent)

	@property
	def ue(self):
		"""ue commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Eps_.Ue import Ue
			self._ue = Ue(self._core, self._base)
		return self._ue

	def delete(self, name_ta_eps: str) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:EPS \n
		Snippet: driver.signaling.topology.eps.delete(name_ta_eps = '1') \n
		Deletes an EPS tracking area. \n
			:param name_ta_eps: No help available
		"""
		param = Conversions.value_to_quoted_str(name_ta_eps)
		self._core.io.write(f'DELete:SIGNaling:TOPology:EPS {param}')

	def clone(self) -> 'Eps':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eps(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
