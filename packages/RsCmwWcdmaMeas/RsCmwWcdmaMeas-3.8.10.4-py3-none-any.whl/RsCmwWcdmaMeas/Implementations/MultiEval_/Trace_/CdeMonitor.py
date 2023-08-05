from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdeMonitor:
	"""CdeMonitor commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cdeMonitor", core, parent)

	@property
	def qsignal(self):
		"""qsignal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qsignal'):
			from .CdeMonitor_.Qsignal import Qsignal
			self._qsignal = Qsignal(self._core, self._base)
		return self._qsignal

	@property
	def isignal(self):
		"""isignal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_isignal'):
			from .CdeMonitor_.Isignal import Isignal
			self._isignal = Isignal(self._core, self._base)
		return self._isignal

	def clone(self) -> 'CdeMonitor':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CdeMonitor(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
