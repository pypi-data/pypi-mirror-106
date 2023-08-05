from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrStep:
	"""PrStep commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prStep", core, parent)

	def set(self, cell_name: str, pwr_ramping_step: enums.PwrRampingStepB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:PRSTep \n
		Snippet: driver.configure.signaling.nradio.cell.power.uplink.prStep.set(cell_name = '1', pwr_ramping_step = enums.PwrRampingStepB.S0) \n
		No command help available \n
			:param cell_name: No help available
			:param pwr_ramping_step: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('pwr_ramping_step', pwr_ramping_step, DataType.Enum))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:PRSTep {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PwrRampingStepB:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:PRSTep \n
		Snippet: value: enums.PwrRampingStepB = driver.configure.signaling.nradio.cell.power.uplink.prStep.get(cell_name = '1') \n
		No command help available \n
			:param cell_name: No help available
			:return: pwr_ramping_step: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:PRSTep? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PwrRampingStepB)
