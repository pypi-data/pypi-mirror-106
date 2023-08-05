from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcde:
	"""Pcde commands group definition. 8 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcde", core, parent)

	@property
	def code(self):
		"""code commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_code'):
			from .Pcde_.Code import Code
			self._code = Code(self._core, self._base)
		return self._code

	@property
	def phase(self):
		"""phase commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_phase'):
			from .Pcde_.Phase import Phase
			self._phase = Phase(self._core, self._base)
		return self._phase

	@property
	def error(self):
		"""error commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_error'):
			from .Pcde_.Error import Error
			self._error = Error(self._core, self._base)
		return self._error

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Pcde_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Pcde_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	def clone(self) -> 'Pcde':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcde(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
