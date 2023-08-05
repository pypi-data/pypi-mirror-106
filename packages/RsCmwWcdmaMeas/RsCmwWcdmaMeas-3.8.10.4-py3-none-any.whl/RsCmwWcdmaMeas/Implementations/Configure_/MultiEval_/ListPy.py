from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 12 total commands, 2 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def segment(self):
		"""segment commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	@property
	def singleCmw(self):
		"""singleCmw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .ListPy_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	def get_eoffset(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:EOFFset \n
		Snippet: value: int = driver.configure.multiEval.listPy.get_eoffset() \n
		Defines the evaluation offset. The specified number of slots at the beginning of each segment is excluded from the
		evaluation. Set the trigger delay to 0 when using an evaluation offset (see method RsCmwWcdmaMeas.Trigger.MultiEval.
		delay) . \n
			:return: offset: numeric Range: 0 slots to 1024 slots
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:EOFFset?')
		return Conversions.str_to_int(response)

	def set_eoffset(self, offset: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:EOFFset \n
		Snippet: driver.configure.multiEval.listPy.set_eoffset(offset = 1) \n
		Defines the evaluation offset. The specified number of slots at the beginning of each segment is excluded from the
		evaluation. Set the trigger delay to 0 when using an evaluation offset (see method RsCmwWcdmaMeas.Trigger.MultiEval.
		delay) . \n
			:param offset: numeric Range: 0 slots to 1024 slots
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:EOFFset {param}')

	def get_count(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:COUNt \n
		Snippet: value: int = driver.configure.multiEval.listPy.get_count() \n
		Defines the number of segments in the entire measurement interval, including active and inactive segments. \n
			:return: segments: numeric Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, segments: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:COUNt \n
		Snippet: driver.configure.multiEval.listPy.set_count(segments = 1) \n
		Defines the number of segments in the entire measurement interval, including active and inactive segments. \n
			:param segments: numeric Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(segments)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:COUNt {param}')

	def get_os_index(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:OSINdex \n
		Snippet: value: int = driver.configure.multiEval.listPy.get_os_index() \n
		No command help available \n
			:return: index: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:OSINdex?')
		return Conversions.str_to_int(response)

	def set_os_index(self, index: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:OSINdex \n
		Snippet: driver.configure.multiEval.listPy.set_os_index(index = 1) \n
		No command help available \n
			:param index: No help available
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:OSINdex {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST \n
		Snippet: value: bool = driver.configure.multiEval.listPy.get_value() \n
		Enables or disables the list mode. \n
			:return: enable: OFF | ON OFF: Disable list mode ON: Enable list mode
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST \n
		Snippet: driver.configure.multiEval.listPy.set_value(enable = False) \n
		Enables or disables the list mode. \n
			:param enable: OFF | ON OFF: Disable list mode ON: Enable list mode
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
