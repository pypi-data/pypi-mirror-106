from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.Types import DataType
from ...........Internal.StructBase import StructBase
from ...........Internal.ArgStruct import ArgStruct
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbol:
	"""Symbol commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("symbol", core, parent)

	def set(self, cell_name: str, slot: float, number_symbol: int, start_symbol: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:SYMBol \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.uplink.tdomain.symbol.set(cell_name = '1', slot = 1.0, number_symbol = 1, start_symbol = 1) \n
		No command help available \n
			:param cell_name: No help available
			:param slot: No help available
			:param number_symbol: No help available
			:param start_symbol: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Float), ArgSingle('number_symbol', number_symbol, DataType.Integer), ArgSingle('start_symbol', start_symbol, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:SYMBol {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Symbol: int: No parameter help available
			- Start_Symbol: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Symbol'),
			ArgStruct.scalar_int('Start_Symbol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Symbol: int = None
			self.Start_Symbol: int = None

	def get(self, cell_name: str, slot: float) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:SYMBol \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.uplink.tdomain.symbol.get(cell_name = '1', slot = 1.0) \n
		No command help available \n
			:param cell_name: No help available
			:param slot: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Float))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:SYMBol? {param}'.rstrip(), self.__class__.GetStruct())
