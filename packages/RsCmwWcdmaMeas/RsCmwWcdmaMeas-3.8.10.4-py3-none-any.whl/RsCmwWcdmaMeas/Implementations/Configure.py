from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 161 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Configure_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def cell(self):
		"""cell commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Configure_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	@property
	def ueSignal(self):
		"""ueSignal commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_ueSignal'):
			from .Configure_.UeSignal import UeSignal
			self._ueSignal = UeSignal(self._core, self._base)
		return self._ueSignal

	@property
	def ueChannels(self):
		"""ueChannels commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueChannels'):
			from .Configure_.UeChannels import UeChannels
			self._ueChannels = UeChannels(self._core, self._base)
		return self._ueChannels

	@property
	def rfSettings(self):
		"""rfSettings commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Configure_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def multiEval(self):
		"""multiEval commands group. 11 Sub-classes, 7 commands."""
		if not hasattr(self, '_multiEval'):
			from .Configure_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	@property
	def tpc(self):
		"""tpc commands group. 7 Sub-classes, 5 commands."""
		if not hasattr(self, '_tpc'):
			from .Configure_.Tpc import Tpc
			self._tpc = Tpc(self._core, self._base)
		return self._tpc

	@property
	def prach(self):
		"""prach commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_prach'):
			from .Configure_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	@property
	def ooSync(self):
		"""ooSync commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ooSync'):
			from .Configure_.OoSync import OoSync
			self._ooSync = OoSync(self._core, self._base)
		return self._ooSync

	@property
	def olpControl(self):
		"""olpControl commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_olpControl'):
			from .Configure_.OlpControl import OlpControl
			self._olpControl = OlpControl(self._core, self._base)
		return self._olpControl

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
