from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 261 total commands, 5 Sub-groups, 0 group commands
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
	def trace(self):
		"""trace commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Carrier_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def modulation(self):
		"""modulation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Carrier_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def rcdError(self):
		"""rcdError commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_rcdError'):
			from .Carrier_.RcdError import RcdError
			self._rcdError = RcdError(self._core, self._base)
		return self._rcdError

	@property
	def cdPower(self):
		"""cdPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdPower'):
			from .Carrier_.CdPower import CdPower
			self._cdPower = CdPower(self._core, self._base)
		return self._cdPower

	@property
	def cdError(self):
		"""cdError commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdError'):
			from .Carrier_.CdError import CdError
			self._cdError = CdError(self._core, self._base)
		return self._cdError

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
