from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 2 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: CARRierExt, default value after init: CARRierExt.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_cARRierExt_get', 'repcap_cARRierExt_set', repcap.CARRierExt.Nr1)

	def repcap_cARRierExt_set(self, enum_value: repcap.CARRierExt) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CARRierExt.Default
		Default value after init: CARRierExt.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_cARRierExt_get(self) -> repcap.CARRierExt:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def uepPower(self):
		"""uepPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uepPower'):
			from .Carrier_.UepPower import UepPower
			self._uepPower = UepPower(self._core, self._base)
		return self._uepPower

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
