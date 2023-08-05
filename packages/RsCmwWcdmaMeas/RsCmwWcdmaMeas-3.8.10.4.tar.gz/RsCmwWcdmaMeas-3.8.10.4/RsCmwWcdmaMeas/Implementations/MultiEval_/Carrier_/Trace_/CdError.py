from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdError:
	"""CdError commands group definition. 40 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cdError", core, parent)

	@property
	def dpcch(self):
		"""dpcch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpcch'):
			from .CdError_.Dpcch import Dpcch
			self._dpcch = Dpcch(self._core, self._base)
		return self._dpcch

	@property
	def dpdch(self):
		"""dpdch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpdch'):
			from .CdError_.Dpdch import Dpdch
			self._dpdch = Dpdch(self._core, self._base)
		return self._dpdch

	@property
	def hsdpcch(self):
		"""hsdpcch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsdpcch'):
			from .CdError_.Hsdpcch import Hsdpcch
			self._hsdpcch = Hsdpcch(self._core, self._base)
		return self._hsdpcch

	@property
	def edpcch(self):
		"""edpcch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_edpcch'):
			from .CdError_.Edpcch import Edpcch
			self._edpcch = Edpcch(self._core, self._base)
		return self._edpcch

	@property
	def edpdch(self):
		"""edpdch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_edpdch'):
			from .CdError_.Edpdch import Edpdch
			self._edpdch = Edpdch(self._core, self._base)
		return self._edpdch

	def clone(self) -> 'CdError':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CdError(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
