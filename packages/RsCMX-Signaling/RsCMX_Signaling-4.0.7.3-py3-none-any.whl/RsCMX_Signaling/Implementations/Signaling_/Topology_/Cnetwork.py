from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cnetwork:
	"""Cnetwork commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cnetwork", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Cnetwork_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def delete(self) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:CNETwork \n
		Snippet: driver.signaling.topology.cnetwork.delete() \n
		Deletes the core network. \n
		"""
		self._core.io.write(f'DELete:SIGNaling:TOPology:CNETwork')

	def delete_with_opc(self) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:CNETwork \n
		Snippet: driver.signaling.topology.cnetwork.delete_with_opc() \n
		Deletes the core network. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'DELete:SIGNaling:TOPology:CNETwork')

	def clone(self) -> 'Cnetwork':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cnetwork(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
