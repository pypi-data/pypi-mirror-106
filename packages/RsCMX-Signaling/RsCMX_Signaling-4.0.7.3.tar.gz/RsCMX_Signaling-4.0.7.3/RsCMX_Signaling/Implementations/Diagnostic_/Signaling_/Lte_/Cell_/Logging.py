from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Logging:
	"""Logging commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("logging", core, parent)

	# noinspection PyTypeChecker
	class MacStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Log_Type: enums.LogType: No parameter help available
			- Payload: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Log_Type', enums.LogType),
			ArgStruct.scalar_int('Payload')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Log_Type: enums.LogType = None
			self.Payload: int = None

	def get_mac(self) -> MacStruct:
		"""SCPI: DIAGnostic:SIGNaling:LTE:CELL:LOGGing:MAC \n
		Snippet: value: MacStruct = driver.diagnostic.signaling.lte.cell.logging.get_mac() \n
		No command help available \n
			:return: structure: for return value, see the help for MacStruct structure arguments.
		"""
		return self._core.io.query_struct('DIAGnostic:SIGNaling:LTE:CELL:LOGGing:MAC?', self.__class__.MacStruct())

	def set_mac(self, value: MacStruct) -> None:
		"""SCPI: DIAGnostic:SIGNaling:LTE:CELL:LOGGing:MAC \n
		Snippet: driver.diagnostic.signaling.lte.cell.logging.set_mac(value = MacStruct()) \n
		No command help available \n
			:param value: see the help for MacStruct structure arguments.
		"""
		self._core.io.write_struct('DIAGnostic:SIGNaling:LTE:CELL:LOGGing:MAC', value)

	# noinspection PyTypeChecker
	class RlcStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Log_Type: enums.LogType: No parameter help available
			- Payload: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Log_Type', enums.LogType),
			ArgStruct.scalar_int('Payload')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Log_Type: enums.LogType = None
			self.Payload: int = None

	def get_rlc(self) -> RlcStruct:
		"""SCPI: DIAGnostic:SIGNaling:LTE:CELL:LOGGing:RLC \n
		Snippet: value: RlcStruct = driver.diagnostic.signaling.lte.cell.logging.get_rlc() \n
		No command help available \n
			:return: structure: for return value, see the help for RlcStruct structure arguments.
		"""
		return self._core.io.query_struct('DIAGnostic:SIGNaling:LTE:CELL:LOGGing:RLC?', self.__class__.RlcStruct())

	def set_rlc(self, value: RlcStruct) -> None:
		"""SCPI: DIAGnostic:SIGNaling:LTE:CELL:LOGGing:RLC \n
		Snippet: driver.diagnostic.signaling.lte.cell.logging.set_rlc(value = RlcStruct()) \n
		No command help available \n
			:param value: see the help for RlcStruct structure arguments.
		"""
		self._core.io.write_struct('DIAGnostic:SIGNaling:LTE:CELL:LOGGing:RLC', value)

	# noinspection PyTypeChecker
	class PdcpStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Log_Type: enums.LogType: No parameter help available
			- Payload: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Log_Type', enums.LogType),
			ArgStruct.scalar_int('Payload')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Log_Type: enums.LogType = None
			self.Payload: int = None

	def get_pdcp(self) -> PdcpStruct:
		"""SCPI: DIAGnostic:SIGNaling:LTE:CELL:LOGGing:PDCP \n
		Snippet: value: PdcpStruct = driver.diagnostic.signaling.lte.cell.logging.get_pdcp() \n
		No command help available \n
			:return: structure: for return value, see the help for PdcpStruct structure arguments.
		"""
		return self._core.io.query_struct('DIAGnostic:SIGNaling:LTE:CELL:LOGGing:PDCP?', self.__class__.PdcpStruct())

	def set_pdcp(self, value: PdcpStruct) -> None:
		"""SCPI: DIAGnostic:SIGNaling:LTE:CELL:LOGGing:PDCP \n
		Snippet: driver.diagnostic.signaling.lte.cell.logging.set_pdcp(value = PdcpStruct()) \n
		No command help available \n
			:param value: see the help for PdcpStruct structure arguments.
		"""
		self._core.io.write_struct('DIAGnostic:SIGNaling:LTE:CELL:LOGGing:PDCP', value)
