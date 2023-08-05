from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dhib:
	"""Dhib commands group definition. 11 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dhib", core, parent)

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_maximum'):
			from .Dhib_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_minimum'):
			from .Dhib_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Dhib_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def statistics(self):
		"""statistics commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_statistics'):
			from .Dhib_.Statistics import Statistics
			self._statistics = Statistics(self._core, self._base)
		return self._statistics

	@property
	def minimumc(self):
		"""minimumc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimumc'):
			from .Dhib_.Minimumc import Minimumc
			self._minimumc = Minimumc(self._core, self._base)
		return self._minimumc

	def clone(self) -> 'Dhib':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dhib(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
