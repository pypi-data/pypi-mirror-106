from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Default:
	"""Default commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("default", core, parent)

	# noinspection PyTypeChecker
	def get_voice(self) -> enums.VoiceHandling:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:DEFault:VOICe \n
		Snippet: value: enums.VoiceHandling = driver.configure.signaling.topology.fgs.default.get_voice() \n
		No command help available \n
			:return: voice_handling: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TOPology:FGS:DEFault:VOICe?')
		return Conversions.str_to_scalar_enum(response, enums.VoiceHandling)

	def set_voice(self, voice_handling: enums.VoiceHandling) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:DEFault:VOICe \n
		Snippet: driver.configure.signaling.topology.fgs.default.set_voice(voice_handling = enums.VoiceHandling.EFRedirect) \n
		No command help available \n
			:param voice_handling: No help available
		"""
		param = Conversions.enum_scalar_to_str(voice_handling, enums.VoiceHandling)
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:FGS:DEFault:VOICe {param}')
