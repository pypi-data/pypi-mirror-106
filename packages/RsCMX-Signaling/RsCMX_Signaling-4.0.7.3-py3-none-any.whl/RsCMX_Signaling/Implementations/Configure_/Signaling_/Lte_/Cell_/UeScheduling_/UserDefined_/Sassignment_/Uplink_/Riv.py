from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Riv:
	"""Riv commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("riv", core, parent)

	def set(self, cell_name: str, subframe: float, riv: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:RIV \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.uplink.riv.set(cell_name = '1', subframe = 1.0, riv = 1) \n
		Defines the resource indication value (RIV) for the UL subframe with the index <Subframe>, for user-defined scheduling. \n
			:param cell_name: No help available
			:param subframe: No help available
			:param riv: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Float), ArgSingle('riv', riv, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:RIV {param}'.rstrip())

	def get(self, cell_name: str, subframe: float) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:RIV \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.uplink.riv.get(cell_name = '1', subframe = 1.0) \n
		Defines the resource indication value (RIV) for the UL subframe with the index <Subframe>, for user-defined scheduling. \n
			:param cell_name: No help available
			:param subframe: No help available
			:return: riv: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Float))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:RIV? {param}'.rstrip())
		return Conversions.str_to_int(response)
