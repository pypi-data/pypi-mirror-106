from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	def set(self) -> None:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:THRoughput \n
		Snippet: driver.fetch.signaling.measurement.bler.throughput.set() \n
		Returns the throughput results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <RelAvg>, <AbsAck>, <AbsScheduled>}, {...}, ... \n
		"""
		self._core.io.write(f'FETCh:SIGNaling:MEASurement:BLER:THRoughput')

	def set_with_opc(self) -> None:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:THRoughput \n
		Snippet: driver.fetch.signaling.measurement.bler.throughput.set_with_opc() \n
		Returns the throughput results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <RelAvg>, <AbsAck>, <AbsScheduled>}, {...}, ... \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'FETCh:SIGNaling:MEASurement:BLER:THRoughput')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Cell_Name: str: Name of the cell providing the measured connection
			- Rel_Avg: float: Average throughput as percentage of scheduled throughput
			- Abs_Ack: int: Average throughput in bit/s
			- Abs_Scheduled: int: Scheduled throughput in bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_float('Rel_Avg'),
			ArgStruct.scalar_int('Abs_Ack'),
			ArgStruct.scalar_int('Abs_Scheduled')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: str = None
			self.Rel_Avg: float = None
			self.Abs_Ack: int = None
			self.Abs_Scheduled: int = None

	def get(self) -> GetStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:THRoughput \n
		Snippet: value: GetStruct = driver.fetch.signaling.measurement.bler.throughput.get() \n
		Returns the throughput results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <RelAvg>, <AbsAck>, <AbsScheduled>}, {...}, ... \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:THRoughput?', self.__class__.GetStruct())
