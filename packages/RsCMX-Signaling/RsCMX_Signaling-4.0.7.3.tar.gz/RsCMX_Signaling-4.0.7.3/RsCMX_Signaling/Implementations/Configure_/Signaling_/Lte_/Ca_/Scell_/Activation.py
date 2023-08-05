from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Activation:
	"""Activation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("activation", core, parent)

	def set(self, cell_name: str, activation: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CA:SCELl:ACTivation \n
		Snippet: driver.configure.signaling.lte.ca.scell.activation.set(cell_name = '1', activation = False) \n
		Triggers the manual MAC activation or MAC deactivation for an SCell. A query returns the current MAC activation state. \n
			:param cell_name: No help available
			:param activation: ON: activate MAC (setting) / MAC is active (query) OFF: deactivate MAC (setting) / MAC is inactive (query)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('activation', activation, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CA:SCELl:ACTivation {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CA:SCELl:ACTivation \n
		Snippet: value: bool = driver.configure.signaling.lte.ca.scell.activation.get(cell_name = '1') \n
		Triggers the manual MAC activation or MAC deactivation for an SCell. A query returns the current MAC activation state. \n
			:param cell_name: No help available
			:return: activation: ON: activate MAC (setting) / MAC is active (query) OFF: deactivate MAC (setting) / MAC is inactive (query)"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CA:SCELl:ACTivation? {param}')
		return Conversions.str_to_bool(response)
