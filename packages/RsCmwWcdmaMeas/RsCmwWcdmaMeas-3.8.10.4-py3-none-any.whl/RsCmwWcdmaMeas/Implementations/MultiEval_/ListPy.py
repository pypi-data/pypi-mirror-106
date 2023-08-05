from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 181 total commands, 9 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def sreliability(self):
		"""sreliability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sreliability'):
			from .ListPy_.Sreliability import Sreliability
			self._sreliability = Sreliability(self._core, self._base)
		return self._sreliability

	@property
	def uePower(self):
		"""uePower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uePower'):
			from .ListPy_.UePower import UePower
			self._uePower = UePower(self._core, self._base)
		return self._uePower

	@property
	def segment(self):
		"""segment commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	@property
	def phd(self):
		"""phd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phd'):
			from .ListPy_.Phd import Phd
			self._phd = Phd(self._core, self._base)
		return self._phd

	@property
	def pcde(self):
		"""pcde commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcde'):
			from .ListPy_.Pcde import Pcde
			self._pcde = Pcde(self._core, self._base)
		return self._pcde

	@property
	def cdPower(self):
		"""cdPower commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdPower'):
			from .ListPy_.CdPower import CdPower
			self._cdPower = CdPower(self._core, self._base)
		return self._cdPower

	@property
	def spectrum(self):
		"""spectrum commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .ListPy_.Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._base)
		return self._spectrum

	@property
	def modulation(self):
		"""modulation commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .ListPy_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def cdError(self):
		"""cdError commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdError'):
			from .ListPy_.CdError import CdError
			self._cdError = CdError(self._core, self._base)
		return self._cdError

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
