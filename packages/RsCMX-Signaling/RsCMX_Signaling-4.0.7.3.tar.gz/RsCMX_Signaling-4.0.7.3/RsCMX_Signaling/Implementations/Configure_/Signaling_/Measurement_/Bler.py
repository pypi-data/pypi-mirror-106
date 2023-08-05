from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bler:
	"""Bler commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bler", core, parent)

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.signaling.measurement.bler.get_repetition() \n
		Specifies whether the measurement is stopped after a single shot or repeated continuously. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:BLER:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:REPetition \n
		Snippet: driver.configure.signaling.measurement.bler.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies whether the measurement is stopped after a single shot or repeated continuously. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:BLER:REPetition {param}')

	# noinspection PyTypeChecker
	class SconditionStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Stop_Condition: enums.StopConditionB: SAMPles: number of samples reached for at least one cell TIME: measurement duration reached
			- Value: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Stop_Condition', enums.StopConditionB),
			ArgStruct.scalar_float('Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Stop_Condition: enums.StopConditionB = None
			self.Value: float = None

	# noinspection PyTypeChecker
	def get_scondition(self) -> SconditionStruct:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:SCONdition \n
		Snippet: value: SconditionStruct = driver.configure.signaling.measurement.bler.get_scondition() \n
		Defines a stop condition for single-shot BLER measurements. A single-shot measurement stops when the <Value> is reached.
		<StopCondition> defines whether <Value> is a number of samples or a measurement duration. \n
			:return: structure: for return value, see the help for SconditionStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:SIGNaling:MEASurement:BLER:SCONdition?', self.__class__.SconditionStruct())

	def set_scondition(self, value: SconditionStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:SCONdition \n
		Snippet: driver.configure.signaling.measurement.bler.set_scondition(value = SconditionStruct()) \n
		Defines a stop condition for single-shot BLER measurements. A single-shot measurement stops when the <Value> is reached.
		<StopCondition> defines whether <Value> is a number of samples or a measurement duration. \n
			:param value: see the help for SconditionStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:SIGNaling:MEASurement:BLER:SCONdition', value)
