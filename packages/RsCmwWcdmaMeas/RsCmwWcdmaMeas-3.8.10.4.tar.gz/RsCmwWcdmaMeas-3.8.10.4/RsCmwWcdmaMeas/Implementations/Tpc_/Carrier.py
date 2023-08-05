from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 28 total commands, 3 Sub-groups, 0 group commands
	Repeated Capability: Carrier, default value after init: Carrier.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_carrier_get', 'repcap_carrier_set', repcap.Carrier.Nr1)

	def repcap_carrier_set(self, enum_value: repcap.Carrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Carrier.Default
		Default value after init: Carrier.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_carrier_get(self) -> repcap.Carrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def psteps(self):
		"""psteps commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_psteps'):
			from .Carrier_.Psteps import Psteps
			self._psteps = Psteps(self._core, self._base)
		return self._psteps

	@property
	def uePower(self):
		"""uePower commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_uePower'):
			from .Carrier_.UePower import UePower
			self._uePower = UePower(self._core, self._base)
		return self._uePower

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Carrier_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
