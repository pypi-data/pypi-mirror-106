from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enable", core, parent)

	def set(self, cell_name: str, slot: float, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:ENABle \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.uplink.enable.set(cell_name = '1', slot = 1.0, enable = False) \n
		Enables or disables scheduling of the UL slot with the index <Slot>, for user-defined scheduling. \n
			:param cell_name: No help available
			:param slot: No help available
			:param enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Float), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:ENABle {param}'.rstrip())

	def get(self, cell_name: str, slot: float) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:ENABle \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.uplink.enable.get(cell_name = '1', slot = 1.0) \n
		Enables or disables scheduling of the UL slot with the index <Slot>, for user-defined scheduling. \n
			:param cell_name: No help available
			:param slot: No help available
			:return: enable: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Float))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:ENABle? {param}'.rstrip())
		return Conversions.str_to_bool(response)
