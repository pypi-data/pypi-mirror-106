from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UePower:
	"""UePower commands group definition. 11 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uePower", core, parent)

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_maximum'):
			from .UePower_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_minimum'):
			from .UePower_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .UePower_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def statistics(self):
		"""statistics commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_statistics'):
			from .UePower_.Statistics import Statistics
			self._statistics = Statistics(self._core, self._base)
		return self._statistics

	def clone(self) -> 'UePower':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UePower(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
