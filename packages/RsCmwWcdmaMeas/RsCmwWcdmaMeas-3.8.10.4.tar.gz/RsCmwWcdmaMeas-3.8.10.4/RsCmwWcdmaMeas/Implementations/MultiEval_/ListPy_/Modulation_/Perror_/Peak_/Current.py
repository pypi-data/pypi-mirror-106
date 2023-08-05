from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:MODulation:PERRor:PEAK:CURRent \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.perror.peak.current.fetch() \n
		Return phase error peak values for all measured list mode segments. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: phase_error_peak: float Comma-separated list of values, one per measured segment Range: -180 deg to 180 deg (AVERage: 0 deg to 180 deg, SDEViation: 0 deg to 90 deg) , Unit: deg"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:MODulation:PERRor:PEAK:CURRent?', suppressed)
		return response
