from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UePower:
	"""UePower commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uePower", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .UePower_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def chip(self):
		"""chip commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_chip'):
			from .UePower_.Chip import Chip
			self._chip = Chip(self._core, self._base)
		return self._chip

	def clone(self) -> 'UePower':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UePower(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
