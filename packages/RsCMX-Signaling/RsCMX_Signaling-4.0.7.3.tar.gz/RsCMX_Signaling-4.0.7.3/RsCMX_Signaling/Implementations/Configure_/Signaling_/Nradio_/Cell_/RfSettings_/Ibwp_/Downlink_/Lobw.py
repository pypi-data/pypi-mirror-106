from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lobw:
	"""Lobw commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("lobw", core, parent)

	def set(self, cell_name: str, lobw: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:IBWP:DL:LOBW \n
		Snippet: driver.configure.signaling.nradio.cell.rfSettings.ibwp.downlink.lobw.set(cell_name = '1', lobw = 1) \n
		No command help available \n
			:param cell_name: No help available
			:param lobw: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('lobw', lobw, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:IBWP:DL:LOBW {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:IBWP:DL:LOBW \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.rfSettings.ibwp.downlink.lobw.get(cell_name = '1') \n
		No command help available \n
			:param cell_name: No help available
			:return: lobw: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:IBWP:DL:LOBW? {param}')
		return Conversions.str_to_int(response)
