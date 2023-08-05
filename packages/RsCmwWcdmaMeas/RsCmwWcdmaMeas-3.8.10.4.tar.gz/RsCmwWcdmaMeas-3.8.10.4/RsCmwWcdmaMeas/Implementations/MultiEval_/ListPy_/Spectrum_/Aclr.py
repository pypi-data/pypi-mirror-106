from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aclr:
	"""Aclr commands group definition. 6 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aclr", core, parent)

	@property
	def m(self):
		"""m commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_m'):
			from .Aclr_.M import M
			self._m = M(self._core, self._base)
		return self._m

	@property
	def p(self):
		"""p commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_p'):
			from .Aclr_.P import P
			self._p = P(self._core, self._base)
		return self._p

	def clone(self) -> 'Aclr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Aclr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
