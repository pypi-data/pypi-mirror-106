from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqError:
	"""FreqError commands group definition. 8 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("freqError", core, parent)

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .FreqError_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .FreqError_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .FreqError_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .FreqError_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	def clone(self) -> 'FreqError':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FreqError(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
