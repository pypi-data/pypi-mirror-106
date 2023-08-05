from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emask:
	"""Emask commands group definition. 30 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("emask", core, parent)

	@property
	def mfLeft(self):
		"""mfLeft commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mfLeft'):
			from .Emask_.MfLeft import MfLeft
			self._mfLeft = MfLeft(self._core, self._base)
		return self._mfLeft

	@property
	def mfRight(self):
		"""mfRight commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mfRight'):
			from .Emask_.MfRight import MfRight
			self._mfRight = MfRight(self._core, self._base)
		return self._mfRight

	@property
	def hkfLeft(self):
		"""hkfLeft commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_hkfLeft'):
			from .Emask_.HkfLeft import HkfLeft
			self._hkfLeft = HkfLeft(self._core, self._base)
		return self._hkfLeft

	@property
	def hkfRight(self):
		"""hkfRight commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_hkfRight'):
			from .Emask_.HkfRight import HkfRight
			self._hkfRight = HkfRight(self._core, self._base)
		return self._hkfRight

	@property
	def kfilter(self):
		"""kfilter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_kfilter'):
			from .Emask_.Kfilter import Kfilter
			self._kfilter = Kfilter(self._core, self._base)
		return self._kfilter

	def clone(self) -> 'Emask':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emask(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
