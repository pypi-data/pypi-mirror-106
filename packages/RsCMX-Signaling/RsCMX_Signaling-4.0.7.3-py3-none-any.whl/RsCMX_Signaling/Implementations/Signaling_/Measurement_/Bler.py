from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bler:
	"""Bler commands group definition. 5 total commands, 3 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bler", core, parent)

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Bler_.Absolute import Absolute
			self._absolute = Absolute(self._core, self._base)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Bler_.Relative import Relative
			self._relative = Relative(self._core, self._base)
		return self._relative

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Bler_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def abort(self) -> None:
		"""SCPI: ABORt:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.abort() \n
		Stops the measurement. The measurement enters the 'RDY' state. \n
		"""
		self._core.io.write(f'ABORt:SIGNaling:MEASurement:BLER')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.abort_with_opc() \n
		Stops the measurement. The measurement enters the 'RDY' state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:SIGNaling:MEASurement:BLER')

	def initiate(self) -> None:
		"""SCPI: INITiate:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.initiate() \n
		Starts the measurement. The measurement enters the 'RUN' state. \n
		"""
		self._core.io.write(f'INITiate:SIGNaling:MEASurement:BLER')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.initiate_with_opc() \n
		Starts the measurement. The measurement enters the 'RUN' state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:SIGNaling:MEASurement:BLER')

	def clone(self) -> 'Bler':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bler(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
