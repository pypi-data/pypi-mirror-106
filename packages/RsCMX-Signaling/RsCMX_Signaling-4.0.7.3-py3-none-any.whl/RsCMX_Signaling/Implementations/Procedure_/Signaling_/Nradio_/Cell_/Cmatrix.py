from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmatrix:
	"""Cmatrix commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cmatrix", core, parent)

	def set_hadamard(self, cell_name: str) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:CMATrix:HADamard \n
		Snippet: driver.procedure.signaling.nradio.cell.cmatrix.set_hadamard(cell_name = '1') \n
		Applies a Hadamard matrix as channel matrix. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:CMATrix:HADamard {param}')
