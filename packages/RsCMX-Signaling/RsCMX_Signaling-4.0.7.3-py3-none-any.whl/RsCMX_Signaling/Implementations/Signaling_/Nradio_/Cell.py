from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	def delete(self, cell_name: str) -> None:
		"""SCPI: DELete:SIGNaling:NRADio:CELL \n
		Snippet: driver.signaling.nradio.cell.delete(cell_name = '1') \n
		Deletes an LTE or NR cell. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'DELete:SIGNaling:NRADio:CELL {param}')
