from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scell:
	"""Scell commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scell", core, parent)

	def set(self, cell_group_name: str, cell_name: str, activation: bool = None) -> None:
		"""SCPI: ADD:SIGNaling:NRADio:CA:SCELl \n
		Snippet: driver.add.signaling.nradio.ca.scell.set(cell_group_name = '1', cell_name = '1', activation = False) \n
		Adds an existing LTE or NR cell to an existing cell group, as SCell. \n
			:param cell_group_name: No help available
			:param cell_name: No help available
			:param activation: ON: automatic MAC activation (default) OFF: manual MAC activation via separate command
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_group_name', cell_group_name, DataType.String), ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('activation', activation, DataType.Boolean, True))
		self._core.io.write(f'ADD:SIGNaling:NRADio:CA:SCELl {param}'.rstrip())
