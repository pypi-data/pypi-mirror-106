from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DcMode:
	"""DcMode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dcMode", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.DcMode:
		"""SCPI: FETCh:SIGNaling:UE:DCMode \n
		Snippet: value: enums.DcMode = driver.signaling.ue.dcMode.fetch() \n
		Queries the dual connectivity mode. Checking this mode is especially useful when setting up NSA connections, to see
		whether the connection setup is complete (mode EN-DC reached, connected to LTE and NR) . \n
			:return: dc_mode: No help available"""
		response = self._core.io.query_str(f'FETCh:SIGNaling:UE:DCMode?')
		return Conversions.str_to_scalar_enum(response, enums.DcMode)
