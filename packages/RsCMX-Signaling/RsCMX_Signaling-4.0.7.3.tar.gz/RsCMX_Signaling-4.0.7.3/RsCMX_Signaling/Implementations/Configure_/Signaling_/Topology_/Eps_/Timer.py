from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timer:
	"""Timer commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("timer", core, parent)

	def set(self, name_ta_eps: str, timer: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TIMer \n
		Snippet: driver.configure.signaling.topology.eps.timer.set(name_ta_eps = '1', timer = 1) \n
		Configures the EPS tracking area timer. \n
			:param name_ta_eps: No help available
			:param timer: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta_eps', name_ta_eps, DataType.String), ArgSingle('timer', timer, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:EPS:TIMer {param}'.rstrip())

	def get(self, name_ta_eps: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TIMer \n
		Snippet: value: int = driver.configure.signaling.topology.eps.timer.get(name_ta_eps = '1') \n
		Configures the EPS tracking area timer. \n
			:param name_ta_eps: No help available
			:return: timer: No help available"""
		param = Conversions.value_to_quoted_str(name_ta_eps)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:TOPology:EPS:TIMer? {param}')
		return Conversions.str_to_int(response)
