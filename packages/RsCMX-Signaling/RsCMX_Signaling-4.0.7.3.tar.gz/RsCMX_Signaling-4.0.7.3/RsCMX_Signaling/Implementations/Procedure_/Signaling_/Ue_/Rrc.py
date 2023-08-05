from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rrc:
	"""Rrc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rrc", core, parent)

	def set(self, ue_id: str, action: enums.Action) -> None:
		"""SCPI: PROCedure:SIGNaling:UE:RRC \n
		Snippet: driver.procedure.signaling.ue.rrc.set(ue_id = '1', action = enums.Action.DISConnect) \n
		No command help available \n
			:param ue_id: No help available
			:param action: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String), ArgSingle('action', action, DataType.Enum))
		self._core.io.write(f'PROCedure:SIGNaling:UE:RRC {param}'.rstrip())
