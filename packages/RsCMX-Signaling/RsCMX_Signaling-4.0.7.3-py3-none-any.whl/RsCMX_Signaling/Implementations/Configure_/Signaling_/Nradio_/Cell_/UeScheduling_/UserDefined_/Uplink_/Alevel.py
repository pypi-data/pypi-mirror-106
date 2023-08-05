from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alevel:
	"""Alevel commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("alevel", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Level:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:ALEVel \n
		Snippet: value: enums.Level = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.uplink.alevel.get(cell_name = '1') \n
		Queries the aggregation level, for user-defined scheduling. \n
			:param cell_name: No help available
			:return: level: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:ALEVel? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Level)
