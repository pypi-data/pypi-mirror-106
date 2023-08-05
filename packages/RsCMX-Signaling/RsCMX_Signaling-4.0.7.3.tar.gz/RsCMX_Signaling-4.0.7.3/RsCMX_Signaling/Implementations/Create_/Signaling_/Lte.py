from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lte:
	"""Lte commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("lte", core, parent)

	def set_cgroup(self, cell_group_name: str) -> None:
		"""SCPI: CREate:SIGNaling:LTE:CGRoup \n
		Snippet: driver.create.signaling.lte.set_cgroup(cell_group_name = '1') \n
		Creates an LTE or NR cell group. \n
			:param cell_group_name: Assigns a name to the cell group. The string is used in other commands to select this cell group.
		"""
		param = Conversions.value_to_quoted_str(cell_group_name)
		self._core.io.write(f'CREate:SIGNaling:LTE:CGRoup {param}')

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Cell_Name: str: Assigns a name to the cell. The string is used in other commands to select this cell.
			- Preferred_Netw: enums.PreferredNetw: No parameter help available
			- Physical_Cell_Id: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum_optional('Preferred_Netw', enums.PreferredNetw),
			ArgStruct.scalar_float_optional('Physical_Cell_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Preferred_Netw: enums.PreferredNetw = None
			self.Physical_Cell_Id: float = None

	def set_cell(self, value: CellStruct) -> None:
		"""SCPI: CREate:SIGNaling:LTE:CELL \n
		Snippet: driver.create.signaling.lte.set_cell(value = CellStruct()) \n
		Creates an LTE cell. \n
			:param value: see the help for CellStruct structure arguments.
		"""
		self._core.io.write_struct('CREate:SIGNaling:LTE:CELL', value)
