from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchFormat:
	"""PdcchFormat commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdcchFormat", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell_name: str, subframe: float) -> enums.PdcchFormat:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:PDCChformat \n
		Snippet: value: enums.PdcchFormat = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.pdcchFormat.get(cell_name = '1', subframe = 1.0) \n
		Queries the number of CCEs used for transmission of the PDCCH, for the DL subframe with the index <Subframe>, for
		user-defined scheduling. \n
			:param cell_name: No help available
			:param subframe: No help available
			:return: pdcch_format: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Float))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:PDCChformat? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.PdcchFormat)
