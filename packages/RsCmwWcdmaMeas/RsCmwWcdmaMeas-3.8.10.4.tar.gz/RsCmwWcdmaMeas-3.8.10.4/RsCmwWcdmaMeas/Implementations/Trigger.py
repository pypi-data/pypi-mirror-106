from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 36 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trigger", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 2 Sub-classes, 6 commands."""
		if not hasattr(self, '_multiEval'):
			from .Trigger_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	@property
	def tpc(self):
		"""tpc commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_tpc'):
			from .Trigger_.Tpc import Tpc
			self._tpc = Tpc(self._core, self._base)
		return self._tpc

	@property
	def prach(self):
		"""prach commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_prach'):
			from .Trigger_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	@property
	def ooSync(self):
		"""ooSync commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_ooSync'):
			from .Trigger_.OoSync import OoSync
			self._ooSync = OoSync(self._core, self._base)
		return self._ooSync

	@property
	def olpControl(self):
		"""olpControl commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_olpControl'):
			from .Trigger_.OlpControl import OlpControl
			self._olpControl = OlpControl(self._core, self._base)
		return self._olpControl

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
