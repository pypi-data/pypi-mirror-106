from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Soffset:
	"""Soffset commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("soffset", core, parent)

	def get(self, cell_name: str, slot: float) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:SOFFset \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.tdomain.soffset.get(cell_name = '1', slot = 1.0) \n
		Queries the slot offset k0 for the PDSCH, for the slot with the index <Slot>, for user-defined scheduling. \n
			:param cell_name: No help available
			:param slot: No help available
			:return: offset: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Float))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:SOFFset? {param}'.rstrip())
		return Conversions.str_to_int(response)
