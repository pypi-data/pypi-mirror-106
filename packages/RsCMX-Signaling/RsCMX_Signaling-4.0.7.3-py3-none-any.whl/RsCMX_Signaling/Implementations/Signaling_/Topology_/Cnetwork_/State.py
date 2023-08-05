from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, timeout: float = None, target_state: List[enums.TargetState] = None) -> enums.StateB:
		"""SCPI: FETCh:SIGNaling:TOPology:CNETwork:STATe \n
		Snippet: value: enums.StateB = driver.signaling.topology.cnetwork.state.fetch(timeout = 1.0, target_state = [TargetState.OFF, TargetState.RDYPending]) \n
		Queries the state of the core network, including the states 'edit mode' and 'live mode'. \n
			:param timeout: No help available
			:param target_state: No help available
			:return: state: NAV: no core network available CREating: creating the core network IDLE: core network available, edit mode TESTing: checking whether enough resources are available EXHausted: not enough resources to switch to live mode STARting: switching from edit mode to live mode RUNNing: live mode STOPping: switching from live mode to edit mode DELeting: deleting the core network"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('timeout', timeout, DataType.Float, True), ArgSingle('target_state', target_state, DataType.EnumList, True, True, 1))
		response = self._core.io.query_str(f'FETCh:SIGNaling:TOPology:CNETwork:STATe? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.StateB)
