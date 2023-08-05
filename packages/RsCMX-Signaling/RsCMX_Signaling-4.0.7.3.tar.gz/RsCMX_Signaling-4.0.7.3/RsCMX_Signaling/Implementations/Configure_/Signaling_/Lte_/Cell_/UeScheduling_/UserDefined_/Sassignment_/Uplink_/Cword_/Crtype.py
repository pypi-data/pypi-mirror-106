from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.Types import DataType
from ...........Internal.StructBase import StructBase
from ...........Internal.ArgStruct import ArgStruct
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crtype:
	"""Crtype commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("crtype", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Cell_Name: str: No parameter help available
			- Subframe: int: No parameter help available
			- Coderate_Type: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int('Subframe'),
			ArgStruct.scalar_float('Coderate_Type')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Subframe: int = None
			self.Coderate_Type: float = None

	def get(self, cell_name: str, subframe: int, cword=repcap.Cword.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:CWORd<no>:CRTYpe \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.uplink.cword.crtype.get(cell_name = '1', subframe = 1, cword = repcap.Cword.Default) \n
		Queries the code rate for the UL subframe with the index <Subframe>, code word <no>, for user-defined scheduling. \n
			:param cell_name: No help available
			:param subframe: No help available
			:param cword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cword')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer))
		cword_cmd_val = self._base.get_repcap_cmd_value(cword, repcap.Cword)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:CWORd{cword_cmd_val}:CRTYpe? {param}'.rstrip(), self.__class__.GetStruct())
