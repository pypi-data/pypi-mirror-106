from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eecdp:
	"""Eecdp commands group definition. 7 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eecdp", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_carrier'):
			from .Eecdp_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	def clone(self) -> 'Eecdp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eecdp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
