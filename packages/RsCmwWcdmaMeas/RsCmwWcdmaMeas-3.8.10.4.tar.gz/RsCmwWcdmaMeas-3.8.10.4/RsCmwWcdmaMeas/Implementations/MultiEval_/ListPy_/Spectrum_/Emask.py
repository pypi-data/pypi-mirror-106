from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emask:
	"""Emask commands group definition. 30 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("emask", core, parent)

	@property
	def hda(self):
		"""hda commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_hda'):
			from .Emask_.Hda import Hda
			self._hda = Hda(self._core, self._base)
		return self._hda

	@property
	def had(self):
		"""had commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_had'):
			from .Emask_.Had import Had
			self._had = Had(self._core, self._base)
		return self._had

	@property
	def ab(self):
		"""ab commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ab'):
			from .Emask_.Ab import Ab
			self._ab = Ab(self._core, self._base)
		return self._ab

	@property
	def bc(self):
		"""bc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bc'):
			from .Emask_.Bc import Bc
			self._bc = Bc(self._core, self._base)
		return self._bc

	@property
	def cd(self):
		"""cd commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cd'):
			from .Emask_.Cd import Cd
			self._cd = Cd(self._core, self._base)
		return self._cd

	@property
	def ef(self):
		"""ef commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ef'):
			from .Emask_.Ef import Ef
			self._ef = Ef(self._core, self._base)
		return self._ef

	@property
	def fe(self):
		"""fe commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fe'):
			from .Emask_.Fe import Fe
			self._fe = Fe(self._core, self._base)
		return self._fe

	@property
	def dc(self):
		"""dc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dc'):
			from .Emask_.Dc import Dc
			self._dc = Dc(self._core, self._base)
		return self._dc

	@property
	def cb(self):
		"""cb commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cb'):
			from .Emask_.Cb import Cb
			self._cb = Cb(self._core, self._base)
		return self._cb

	@property
	def ba(self):
		"""ba commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ba'):
			from .Emask_.Ba import Ba
			self._ba = Ba(self._core, self._base)
		return self._ba

	def clone(self) -> 'Emask':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emask(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
