from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Chmapping:
	"""Chmapping commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("chmapping", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell_name: str, slot: float) -> enums.Mapping:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:CHMapping \n
		Snippet: value: enums.Mapping = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.tdomain.chmapping.get(cell_name = '1', slot = 1.0) \n
		Queries the type of PDSCH mapping, for the slot with the index <Slot>, for user-defined scheduling. \n
			:param cell_name: No help available
			:param slot: No help available
			:return: mapping: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Float))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:CHMapping? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.Mapping)
