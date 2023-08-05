from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 6 total commands, 4 Sub-groups, 0 group commands
	Repeated Capability: Pattern, default value after init: Pattern.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pattern", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_pattern_get', 'repcap_pattern_set', repcap.Pattern.Nr1)

	def repcap_pattern_set(self, enum_value: repcap.Pattern) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Pattern.Default
		Default value after init: Pattern.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_pattern_get(self) -> repcap.Pattern:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def periodicity(self):
		"""periodicity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_periodicity'):
			from .Pattern_.Periodicity import Periodicity
			self._periodicity = Periodicity(self._core, self._base)
		return self._periodicity

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Pattern_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Pattern_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Pattern_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	def clone(self) -> 'Pattern':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pattern(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
