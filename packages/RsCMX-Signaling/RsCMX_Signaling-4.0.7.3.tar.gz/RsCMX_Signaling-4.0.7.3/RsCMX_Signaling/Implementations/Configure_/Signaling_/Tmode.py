from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmode:
	"""Tmode commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tmode", core, parent)

	# noinspection PyTypeChecker
	def get_tloop(self) -> enums.TestLoopState:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:TLOop \n
		Snippet: value: enums.TestLoopState = driver.configure.signaling.tmode.get_tloop() \n
		No command help available \n
			:return: test_loop_state: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TMODe:TLOop?')
		return Conversions.str_to_scalar_enum(response, enums.TestLoopState)

	def set_tloop(self, test_loop_state: enums.TestLoopState) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:TLOop \n
		Snippet: driver.configure.signaling.tmode.set_tloop(test_loop_state = enums.TestLoopState.CLOSe) \n
		No command help available \n
			:param test_loop_state: No help available
		"""
		param = Conversions.enum_scalar_to_str(test_loop_state, enums.TestLoopState)
		self._core.io.write(f'CONFigure:SIGNaling:TMODe:TLOop {param}')

	def get_block(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:BLOCk \n
		Snippet: value: bool = driver.configure.signaling.tmode.get_block() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TMODe:BLOCk?')
		return Conversions.str_to_bool(response)

	def set_block(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:BLOCk \n
		Snippet: driver.configure.signaling.tmode.set_block(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:TMODe:BLOCk {param}')

	def get_value(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:TMODe \n
		Snippet: value: bool = driver.configure.signaling.tmode.get_value() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TMODe?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TMODe \n
		Snippet: driver.configure.signaling.tmode.set_value(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:TMODe {param}')
