from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signaling:
	"""Signaling commands group definition. 15 total commands, 7 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("signaling", core, parent)

	@property
	def logging(self):
		"""logging commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_logging'):
			from .Signaling_.Logging import Logging
			self._logging = Logging(self._core, self._base)
		return self._logging

	@property
	def topology(self):
		"""topology commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_topology'):
			from .Signaling_.Topology import Topology
			self._topology = Topology(self._core, self._base)
		return self._topology

	@property
	def register(self):
		"""register commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_register'):
			from .Signaling_.Register import Register
			self._register = Register(self._core, self._base)
		return self._register

	@property
	def registration(self):
		"""registration commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_registration'):
			from .Signaling_.Registration import Registration
			self._registration = Registration(self._core, self._base)
		return self._registration

	@property
	def dapi(self):
		"""dapi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dapi'):
			from .Signaling_.Dapi import Dapi
			self._dapi = Dapi(self._core, self._base)
		return self._dapi

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Signaling_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	@property
	def nradio(self):
		"""nradio commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nradio'):
			from .Signaling_.Nradio import Nradio
			self._nradio = Nradio(self._core, self._base)
		return self._nradio

	# noinspection PyTypeChecker
	def get_routing(self) -> enums.Routing:
		"""SCPI: DIAGnostic:SIGNaling:ROUTing \n
		Snippet: value: enums.Routing = driver.diagnostic.signaling.get_routing() \n
		No command help available \n
			:return: routing: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:SIGNaling:ROUTing?')
		return Conversions.str_to_scalar_enum(response, enums.Routing)

	def set_routing(self, routing: enums.Routing) -> None:
		"""SCPI: DIAGnostic:SIGNaling:ROUTing \n
		Snippet: driver.diagnostic.signaling.set_routing(routing = enums.Routing.DUT) \n
		No command help available \n
			:param routing: No help available
		"""
		param = Conversions.enum_scalar_to_str(routing, enums.Routing)
		self._core.io.write(f'DIAGnostic:SIGNaling:ROUTing {param}')

	def clone(self) -> 'Signaling':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Signaling(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
