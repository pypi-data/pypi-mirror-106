from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 28 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def uePower(self):
		"""uePower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_uePower'):
			from .Trace_.UePower import UePower
			self._uePower = UePower(self._core, self._base)
		return self._uePower

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .Trace_.EvMagnitude import EvMagnitude
			self._evMagnitude = EvMagnitude(self._core, self._base)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Trace_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Trace_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def freqError(self):
		"""freqError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .Trace_.FreqError import FreqError
			self._freqError = FreqError(self._core, self._base)
		return self._freqError

	@property
	def psteps(self):
		"""psteps commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_psteps'):
			from .Trace_.Psteps import Psteps
			self._psteps = Psteps(self._core, self._base)
		return self._psteps

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Trace_.Iq import Iq
			self._iq = Iq(self._core, self._base)
		return self._iq

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
