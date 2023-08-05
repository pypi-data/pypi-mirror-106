from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signaling:
	"""Signaling commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("signaling", core, parent)

	def reset(self) -> None:
		"""SCPI: SYSTem:SIGNaling:RESet \n
		Snippet: driver.system.signaling.reset() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:SIGNaling:RESet')

	def reset_with_opc(self) -> None:
		"""SCPI: SYSTem:SIGNaling:RESet \n
		Snippet: driver.system.signaling.reset_with_opc() \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:SIGNaling:RESet')
