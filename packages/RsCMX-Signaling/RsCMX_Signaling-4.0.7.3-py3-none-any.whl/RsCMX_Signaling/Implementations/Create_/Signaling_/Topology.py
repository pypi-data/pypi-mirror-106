from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Topology:
	"""Topology commands group definition. 5 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("topology", core, parent)

	@property
	def cnetwork(self):
		"""cnetwork commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cnetwork'):
			from .Topology_.Cnetwork import Cnetwork
			self._cnetwork = Cnetwork(self._core, self._base)
		return self._cnetwork

	@property
	def eps(self):
		"""eps commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eps'):
			from .Topology_.Eps import Eps
			self._eps = Eps(self._core, self._base)
		return self._eps

	@property
	def fgs(self):
		"""fgs commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fgs'):
			from .Topology_.Fgs import Fgs
			self._fgs = Fgs(self._core, self._base)
		return self._fgs

	# noinspection PyTypeChecker
	class PlmnStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Name_Plmn: str: Assigns a name to the PLMN. The string is used in other commands to select this PLMN.
			- Mcc: str: No parameter help available
			- Mnc: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Name_Plmn'),
			ArgStruct.scalar_str_optional('Mcc'),
			ArgStruct.scalar_str_optional('Mnc')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name_Plmn: str = None
			self.Mcc: str = None
			self.Mnc: str = None

	def set_plmn(self, value: PlmnStruct) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:PLMN \n
		Snippet: driver.create.signaling.topology.set_plmn(value = PlmnStruct()) \n
		Creates a PLMN and optionally defines MCC and MNC of the PLMN. \n
			:param value: see the help for PlmnStruct structure arguments.
		"""
		self._core.io.write_struct('CREate:SIGNaling:TOPology:PLMN', value)

	def clone(self) -> 'Topology':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Topology(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
