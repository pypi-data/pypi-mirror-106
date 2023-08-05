from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cnetwork:
	"""Cnetwork commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cnetwork", core, parent)

	def set(self) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:CNETwork \n
		Snippet: driver.create.signaling.topology.cnetwork.set() \n
		Creates the core network. This action can take some minutes. \n
		"""
		self._core.io.write(f'CREate:SIGNaling:TOPology:CNETwork')

	def set_with_opc(self) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:CNETwork \n
		Snippet: driver.create.signaling.topology.cnetwork.set_with_opc() \n
		Creates the core network. This action can take some minutes. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CREate:SIGNaling:TOPology:CNETwork')
