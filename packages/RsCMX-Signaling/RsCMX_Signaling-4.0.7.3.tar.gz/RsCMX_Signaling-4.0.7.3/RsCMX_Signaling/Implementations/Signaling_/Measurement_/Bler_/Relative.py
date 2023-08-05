from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("relative", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Cell_Name: str: Name of the cell providing the measured connection
			- Ack: float: Number of received acknowledgments as percentage
			- Nack: float: Number of received negative acknowledgments as percentage
			- Dtx: float: Number of missing answers (no ACK, no NACK) as percentage
			- Bler: float: Block error ratio as percentage
			- Throughput_Avg: float: Average throughput as percentage of scheduled throughput"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_float('Ack'),
			ArgStruct.scalar_float('Nack'),
			ArgStruct.scalar_float('Dtx'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_float('Throughput_Avg')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: str = None
			self.Ack: float = None
			self.Nack: float = None
			self.Dtx: float = None
			self.Bler: float = None
			self.Throughput_Avg: float = None

	def fetch(self, algorithm: enums.Algorithm = None) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:RELative \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.relative.fetch(algorithm = enums.Algorithm.ERC1) \n
		Returns the relative results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <ACK>, <NACK>, <DTX>, <BLER>, <ThroughputAvg>}, {...}, {...}, ... \n
			:param algorithm: Selects the formula for calculation of the BLER from the number of ACK, NACK and DTX. ERC1 (Default) : BLER = (NACK + DTX) / (ACK + NACK + DTX) ERC2: BLER = DTX / (ACK + NACK + DTX) ERC3: BLER = NACK / (ACK + NACK + DTX) ERC4: BLER = NACK / (ACK + NACK)
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('algorithm', algorithm, DataType.Enum, True))
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:RELative? {param}'.rstrip(), self.__class__.FetchStruct())
