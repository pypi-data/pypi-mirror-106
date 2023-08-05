from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edpdch:
	"""Edpdch commands group definition. 8 total commands, 4 Sub-groups, 0 group commands
	Repeated Capability: EdpdChannel, default value after init: EdpdChannel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("edpdch", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_edpdChannel_get', 'repcap_edpdChannel_set', repcap.EdpdChannel.Nr1)

	def repcap_edpdChannel_set(self, enum_value: repcap.EdpdChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to EdpdChannel.Default
		Default value after init: EdpdChannel.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_edpdChannel_get(self) -> repcap.EdpdChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Edpdch_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Edpdch_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Edpdch_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .Edpdch_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	def clone(self) -> 'Edpdch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Edpdch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
