from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:PHD:CURRent \n
		Snippet: value: List[float] = driver.multiEval.listPy.phd.current.fetch() \n
		Returns the phase discontinuity vs. slot results in list mode. Each value indicates the phase discontinuity at the
		boundary between the slot and the previous slot. If the slot or the previous slot is not measured, NCAP is returned. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: phd: float Comma-separated list of phase discontinuity results, one value per slot. The list contains results for all active segments (segments for which any measurement has been enabled) . If another measurement has been enabled for a segment, but the phase discontinuity measurement is disabled, NCAPs are returned for that segment. Example: segment 1 with 10 slots active, segment 2 with 50 slots inactive, segment 3 with 12 slots active. 22 phase discontinuity results are returned. Range: -180 deg to 180 deg, Unit: deg"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:PHD:CURRent?', suppressed)
		return response
