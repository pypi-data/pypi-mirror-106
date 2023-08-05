from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class T:
	"""T commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Tnum, default value after init: Tnum.Nr300"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("t", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_tnum_get', 'repcap_tnum_set', repcap.Tnum.Nr300)

	def repcap_tnum_set(self, enum_value: repcap.Tnum) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Tnum.Default
		Default value after init: Tnum.Nr300"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_tnum_get(self) -> repcap.Tnum:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, cell_name: str, timer: int, tnum=repcap.Tnum.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TOUT:T<no> \n
		Snippet: driver.configure.signaling.lte.cell.timeout.t.set(cell_name = '1', timer = 1, tnum = repcap.Tnum.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param timer: No help available
			:param tnum: optional repeated capability selector. Default value: Nr300 (settable in the interface 'T')"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('timer', timer, DataType.Integer))
		tnum_cmd_val = self._base.get_repcap_cmd_value(tnum, repcap.Tnum)
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:TOUT:T{tnum_cmd_val} {param}'.rstrip())

	def get(self, cell_name: str, tnum=repcap.Tnum.Default) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TOUT:T<no> \n
		Snippet: value: int = driver.configure.signaling.lte.cell.timeout.t.get(cell_name = '1', tnum = repcap.Tnum.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param tnum: optional repeated capability selector. Default value: Nr300 (settable in the interface 'T')
			:return: timer: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		tnum_cmd_val = self._base.get_repcap_cmd_value(tnum, repcap.Tnum)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:TOUT:T{tnum_cmd_val}? {param}')
		return Conversions.str_to_int(response)

	def clone(self) -> 'T':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = T(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
