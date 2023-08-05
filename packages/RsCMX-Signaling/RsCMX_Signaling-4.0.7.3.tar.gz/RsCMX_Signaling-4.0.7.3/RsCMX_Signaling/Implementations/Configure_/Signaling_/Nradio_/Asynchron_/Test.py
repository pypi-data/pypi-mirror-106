from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("test", core, parent)

	def set(self, cell_name: str, func_nr: int, timeout_ms: int, working_time_ms: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:ASYNchron:TEST \n
		Snippet: driver.configure.signaling.nradio.asynchron.test.set(cell_name = '1', func_nr = 1, timeout_ms = 1, working_time_ms = 1) \n
		No command help available \n
			:param cell_name: No help available
			:param func_nr: No help available
			:param timeout_ms: No help available
			:param working_time_ms: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('func_nr', func_nr, DataType.Integer), ArgSingle('timeout_ms', timeout_ms, DataType.Integer), ArgSingle('working_time_ms', working_time_ms, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:ASYNchron:TEST {param}'.rstrip())
