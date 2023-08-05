from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("absolute", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Cell_Name: str: Name of the cell providing the measured connection
			- Ack: int: Number of received acknowledgments
			- Nack: int: Number of received negative acknowledgments
			- Dtx: int: Number of missing answers (no ACK, no NACK)
			- Throughput_Avg: int: Average throughput in bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int('Ack'),
			ArgStruct.scalar_int('Nack'),
			ArgStruct.scalar_int('Dtx'),
			ArgStruct.scalar_int('Throughput_Avg')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: str = None
			self.Ack: int = None
			self.Nack: int = None
			self.Dtx: int = None
			self.Throughput_Avg: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:ABSolute \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.absolute.fetch() \n
		Returns the absolute results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <ACK>, <NACK>, <DTX>, <ThroughputAvg>}, {...}, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:ABSolute?', self.__class__.FetchStruct())
