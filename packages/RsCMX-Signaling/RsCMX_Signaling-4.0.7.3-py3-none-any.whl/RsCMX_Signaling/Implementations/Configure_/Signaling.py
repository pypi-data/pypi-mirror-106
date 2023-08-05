from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signaling:
	"""Signaling commands group definition. 223 total commands, 7 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("signaling", core, parent)

	@property
	def measurement(self):
		"""measurement commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Signaling_.Measurement import Measurement
			self._measurement = Measurement(self._core, self._base)
		return self._measurement

	@property
	def topology(self):
		"""topology commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_topology'):
			from .Signaling_.Topology import Topology
			self._topology = Topology(self._core, self._base)
		return self._topology

	@property
	def tmode(self):
		"""tmode commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_tmode'):
			from .Signaling_.Tmode import Tmode
			self._tmode = Tmode(self._core, self._base)
		return self._tmode

	@property
	def sms(self):
		"""sms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sms'):
			from .Signaling_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def dbearer(self):
		"""dbearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbearer'):
			from .Signaling_.Dbearer import Dbearer
			self._dbearer = Dbearer(self._core, self._base)
		return self._dbearer

	@property
	def lte(self):
		"""lte commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Signaling_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	@property
	def nradio(self):
		"""nradio commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_nradio'):
			from .Signaling_.Nradio import Nradio
			self._nradio = Nradio(self._core, self._base)
		return self._nradio

	def get_mc_group(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:MCGRoup \n
		Snippet: value: str = driver.configure.signaling.get_mc_group() \n
		Defines which cell group is used as master cell group (MCG) . There is exactly one master cell group. Modifying this
		setting means removing the role from a cell group and assigning it to another one. \n
			:return: cell_group_name: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MCGRoup?')
		return trim_str_response(response)

	def set_mc_group(self, cell_group_name: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MCGRoup \n
		Snippet: driver.configure.signaling.set_mc_group(cell_group_name = '1') \n
		Defines which cell group is used as master cell group (MCG) . There is exactly one master cell group. Modifying this
		setting means removing the role from a cell group and assigning it to another one. \n
			:param cell_group_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_group_name)
		self._core.io.write(f'CONFigure:SIGNaling:MCGRoup {param}')

	def get_sc_group(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:SCGRoup \n
		Snippet: value: str = driver.configure.signaling.get_sc_group() \n
		Defines which cell group is used as secondary cell group (SCG) . There is exactly one secondary cell group. Modifying
		this setting means removing the role from a cell group and assigning it to another one. \n
			:return: cell_group_name: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:SCGRoup?')
		return trim_str_response(response)

	def set_sc_group(self, cell_group_name: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:SCGRoup \n
		Snippet: driver.configure.signaling.set_sc_group(cell_group_name = '1') \n
		Defines which cell group is used as secondary cell group (SCG) . There is exactly one secondary cell group. Modifying
		this setting means removing the role from a cell group and assigning it to another one. \n
			:param cell_group_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_group_name)
		self._core.io.write(f'CONFigure:SIGNaling:SCGRoup {param}')

	def clone(self) -> 'Signaling':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Signaling(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
