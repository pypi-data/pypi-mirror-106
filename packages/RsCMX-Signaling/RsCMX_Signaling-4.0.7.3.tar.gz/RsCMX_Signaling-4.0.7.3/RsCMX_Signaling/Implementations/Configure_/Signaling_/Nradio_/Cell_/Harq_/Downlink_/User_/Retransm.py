from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Retransm:
	"""Retransm commands group definition. 7 total commands, 5 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("retransm", core, parent)

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Retransm_.Count import Count
			self._count = Count(self._core, self._base)
		return self._count

	@property
	def rversion(self):
		"""rversion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rversion'):
			from .Retransm_.Rversion import Rversion
			self._rversion = Rversion(self._core, self._base)
		return self._rversion

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Retransm_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def ariv(self):
		"""ariv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ariv'):
			from .Retransm_.Ariv import Ariv
			self._ariv = Ariv(self._core, self._base)
		return self._ariv

	@property
	def rb(self):
		"""rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb'):
			from .Retransm_.Rb import Rb
			self._rb = Rb(self._core, self._base)
		return self._rb

	def set_add(self, cell_name: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm:ADD \n
		Snippet: driver.configure.signaling.nradio.cell.harq.downlink.user.retransm.set_add(cell_name = '1') \n
		Adds a retransmission to the retransmission configuration for user-defined DL HARQ. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm:ADD {param}')

	def delete(self, cell_name: str, index: int, count: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm:DELete \n
		Snippet: driver.configure.signaling.nradio.cell.harq.downlink.user.retransm.delete(cell_name = '1', index = 1, count = 1) \n
		Removes retransmissions from the retransmission configuration for user-defined DL HARQ. \n
			:param cell_name: No help available
			:param index: Index of the first retransmission to be deleted. Item 1 in the GUI corresponds to Index = 0.
			:param count: Number of retransmissions to be deleted.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('count', count, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm:DELete {param}'.rstrip())

	def clone(self) -> 'Retransm':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Retransm(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
