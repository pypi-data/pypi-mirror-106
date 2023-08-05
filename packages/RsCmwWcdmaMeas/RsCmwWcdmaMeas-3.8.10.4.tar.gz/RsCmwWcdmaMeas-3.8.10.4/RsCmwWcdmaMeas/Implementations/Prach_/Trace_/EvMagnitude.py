from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvMagnitude:
	"""EvMagnitude commands group definition. 6 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evMagnitude", core, parent)

	@property
	def rms(self):
		"""rms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .EvMagnitude_.Rms import Rms
			self._rms = Rms(self._core, self._base)
		return self._rms

	@property
	def peak(self):
		"""peak commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_peak'):
			from .EvMagnitude_.Peak import Peak
			self._peak = Peak(self._core, self._base)
		return self._peak

	@property
	def chip(self):
		"""chip commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_chip'):
			from .EvMagnitude_.Chip import Chip
			self._chip = Chip(self._core, self._base)
		return self._chip

	def clone(self) -> 'EvMagnitude':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EvMagnitude(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
