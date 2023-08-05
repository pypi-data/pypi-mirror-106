from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ber:
	"""Ber commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ber", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Ber: float: float Percentage of received data bits that were erroneous Range: 0 % to 100 %, Unit: %
			- Bler: float: float Percentage of received transport data blocks containing at least one erroneous bit Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ber'),
			ArgStruct.scalar_float('Bler')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ber: float = None
			self.Bler: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:BER \n
		Snippet: value: ResultData = driver.multiEval.ber.read() \n
		Returns the bit error rate and the block error ratio. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:BER?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:BER \n
		Snippet: value: ResultData = driver.multiEval.ber.fetch() \n
		Returns the bit error rate and the block error ratio. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:BER?', self.__class__.ResultData())
