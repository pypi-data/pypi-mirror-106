from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrum:
	"""Spectrum commands group definition. 48 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("spectrum", core, parent)

	@property
	def uePower(self):
		"""uePower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_uePower'):
			from .Spectrum_.UePower import UePower
			self._uePower = UePower(self._core, self._base)
		return self._uePower

	@property
	def emask(self):
		"""emask commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_emask'):
			from .Spectrum_.Emask import Emask
			self._emask = Emask(self._core, self._base)
		return self._emask

	@property
	def cpower(self):
		"""cpower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpower'):
			from .Spectrum_.Cpower import Cpower
			self._cpower = Cpower(self._core, self._base)
		return self._cpower

	@property
	def aclr(self):
		"""aclr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .Spectrum_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	@property
	def obw(self):
		"""obw commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_obw'):
			from .Spectrum_.Obw import Obw
			self._obw = Obw(self._core, self._base)
		return self._obw

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Spectrum_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Spectrum_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Spectrum_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	def clone(self) -> 'Spectrum':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spectrum(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
