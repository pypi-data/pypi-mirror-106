from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 6 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	@property
	def uephd(self):
		"""uephd commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_uephd'):
			from .Modulation_.Uephd import Uephd
			self._uephd = Uephd(self._core, self._base)
		return self._uephd

	@property
	def phDhsDpcch(self):
		"""phDhsDpcch commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_phDhsDpcch'):
			from .Modulation_.PhDhsDpcch import PhDhsDpcch
			self._phDhsDpcch = PhDhsDpcch(self._core, self._base)
		return self._phDhsDpcch

	def clone(self) -> 'Modulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Modulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
