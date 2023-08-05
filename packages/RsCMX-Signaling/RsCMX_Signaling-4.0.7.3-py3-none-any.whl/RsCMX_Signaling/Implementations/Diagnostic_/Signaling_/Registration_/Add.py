from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("add", core, parent)

	def set(self, target: enums.Target, name: str, resource: str) -> None:
		"""SCPI: DIAGnostic:SIGNaling:REGistration:ADD \n
		Snippet: driver.diagnostic.signaling.registration.add.set(target = enums.Target.ALL, name = '1', resource = '1') \n
		No command help available \n
			:param target: No help available
			:param name: No help available
			:param resource: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('target', target, DataType.Enum), ArgSingle('name', name, DataType.String), ArgSingle('resource', resource, DataType.String))
		self._core.io.write(f'DIAGnostic:SIGNaling:REGistration:ADD {param}'.rstrip())
