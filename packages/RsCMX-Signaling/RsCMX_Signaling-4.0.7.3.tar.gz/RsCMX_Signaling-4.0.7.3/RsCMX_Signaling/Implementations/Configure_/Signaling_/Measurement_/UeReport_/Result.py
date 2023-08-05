from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("result", core, parent)

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rsrp: bool: No parameter help available
			- Rsrq: bool: No parameter help available
			- Rssi_Nr: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Rsrp'),
			ArgStruct.scalar_bool('Rsrq'),
			ArgStruct.scalar_bool('Rssi_Nr')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rsrp: bool = None
			self.Rsrq: bool = None
			self.Rssi_Nr: bool = None

	def get_enable(self) -> EnableStruct:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:RESult:ENABle \n
		Snippet: value: EnableStruct = driver.configure.signaling.measurement.ueReport.result.get_enable() \n
		Selects the quantities to be reported by the UE. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:SIGNaling:MEASurement:UEReport:RESult:ENABle?', self.__class__.EnableStruct())

	def set_enable(self, value: EnableStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:RESult:ENABle \n
		Snippet: driver.configure.signaling.measurement.ueReport.result.set_enable(value = EnableStruct()) \n
		Selects the quantities to be reported by the UE. \n
			:param value: see the help for EnableStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:SIGNaling:MEASurement:UEReport:RESult:ENABle', value)
