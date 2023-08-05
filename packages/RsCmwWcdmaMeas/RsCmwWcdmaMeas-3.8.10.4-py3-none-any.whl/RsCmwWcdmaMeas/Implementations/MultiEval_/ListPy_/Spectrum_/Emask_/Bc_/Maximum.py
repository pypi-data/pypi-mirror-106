from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SPECtrum:EMASk:BC:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.listPy.spectrum.emask.bc.maximum.fetch() \n
		Return the limit line margin values in the 4 emission mask areas below the carrier frequency for all measured list mode
		segments. A positive result indicates that the trace is located above the limit line, i.e. the limit is exceeded. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: emask_margin: float Comma-separated list of values, one per measured segment Range: -100 dB to 90 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SPECtrum:EMASk:BC:MAXimum?', suppressed)
		return response
