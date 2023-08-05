from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.Types import DataType
from ...........Internal.StructBase import StructBase
from ...........Internal.ArgStruct import ArgStruct
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcs:
	"""Mcs commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mcs", core, parent)

	# noinspection PyTypeChecker
	class McsStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Subframe: int: No parameter help available
			- Mcs: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int('Subframe'),
			ArgStruct.scalar_int('Mcs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Subframe: int = None
			self.Mcs: int = None

	def set(self, structure: McsStruct, cword=repcap.Cword.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:CWORd<no>:MCS \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.cword.mcs.set(value = [PROPERTY_STRUCT_NAME](), cword = repcap.Cword.Default) \n
		Specifies the MCS index for the DL subframe with the index <Subframe>, code word <no>, for user-defined scheduling. \n
			:param structure: for set value, see the help for McsStruct structure arguments.
			:param cword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cword')"""
		cword_cmd_val = self._base.get_repcap_cmd_value(cword, repcap.Cword)
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:CWORd{cword_cmd_val}:MCS', structure)

	def get(self, cell_name: str, subframe: int, cword=repcap.Cword.Default) -> McsStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:CWORd<no>:MCS \n
		Snippet: value: McsStruct = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.cword.mcs.get(cell_name = '1', subframe = 1, cword = repcap.Cword.Default) \n
		Specifies the MCS index for the DL subframe with the index <Subframe>, code word <no>, for user-defined scheduling. \n
			:param cell_name: No help available
			:param subframe: No help available
			:param cword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cword')
			:return: structure: for return value, see the help for McsStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer))
		cword_cmd_val = self._base.get_repcap_cmd_value(cword, repcap.Cword)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:CWORd{cword_cmd_val}:MCS? {param}'.rstrip(), self.__class__.McsStruct())
