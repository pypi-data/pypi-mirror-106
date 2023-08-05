from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:MODulation:EVM:PEAK:AVERage \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.evm.peak.average.fetch() \n
		Return error vector magnitude peak values for all measured list mode segments. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: evm_peak: float Comma-separated list of values, one per measured segment Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:MODulation:EVM:PEAK:AVERage?', suppressed)
		return response
