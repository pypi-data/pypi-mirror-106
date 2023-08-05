from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dbearer:
	"""Dbearer commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dbearer", core, parent)

	def get_apn(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:DBEarer:APN \n
		Snippet: value: str = driver.configure.signaling.dbearer.get_apn() \n
		Configures the default APN for default bearers. \n
			:return: apn: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:DBEarer:APN?')
		return trim_str_response(response)

	def set_apn(self, apn: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:DBEarer:APN \n
		Snippet: driver.configure.signaling.dbearer.set_apn(apn = '1') \n
		Configures the default APN for default bearers. \n
			:param apn: No help available
		"""
		param = Conversions.value_to_quoted_str(apn)
		self._core.io.write(f'CONFigure:SIGNaling:DBEarer:APN {param}')
