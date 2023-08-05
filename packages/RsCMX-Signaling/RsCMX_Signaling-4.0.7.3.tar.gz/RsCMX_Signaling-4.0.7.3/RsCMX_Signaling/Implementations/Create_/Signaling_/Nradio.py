from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nradio:
	"""Nradio commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nradio", core, parent)

	def set_cgroup(self, cell_group_name: str) -> None:
		"""SCPI: CREate:SIGNaling:NRADio:CGRoup \n
		Snippet: driver.create.signaling.nradio.set_cgroup(cell_group_name = '1') \n
		Creates an LTE or NR cell group. \n
			:param cell_group_name: Assigns a name to the cell group. The string is used in other commands to select this cell group.
		"""
		param = Conversions.value_to_quoted_str(cell_group_name)
		self._core.io.write(f'CREate:SIGNaling:NRADio:CGRoup {param}')

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Cell_Name: str: Assigns a name to the cell. The string is used in other commands to select this cell.
			- Physical_Cell_Id: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_float_optional('Physical_Cell_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Physical_Cell_Id: float = None

	def set_cell(self, value: CellStruct) -> None:
		"""SCPI: CREate:SIGNaling:NRADio:CELL \n
		Snippet: driver.create.signaling.nradio.set_cell(value = CellStruct()) \n
		Creates an NR cell. \n
			:param value: see the help for CellStruct structure arguments.
		"""
		self._core.io.write_struct('CREate:SIGNaling:NRADio:CELL', value)
