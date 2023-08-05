from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:TRACe:PSTeps:CURRent \n
		Snippet: value: List[float] = driver.prach.trace.psteps.current.read() \n
		Return the values of the power steps bar graph. See also 'Detailed Views: UE Power and Power Steps' \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_steps: float Comma-separated list of values, one result per measured preamble (see method RsCmwWcdmaMeas.Configure.Prach.mpreamble) For the first preamble NCAP is returned. Range: -10 dB to 50 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:PRACh:TRACe:PSTeps:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:TRACe:PSTeps:CURRent \n
		Snippet: value: List[float] = driver.prach.trace.psteps.current.fetch() \n
		Return the values of the power steps bar graph. See also 'Detailed Views: UE Power and Power Steps' \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_steps: float Comma-separated list of values, one result per measured preamble (see method RsCmwWcdmaMeas.Configure.Prach.mpreamble) For the first preamble NCAP is returned. Range: -10 dB to 50 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:TRACe:PSTeps:CURRent?', suppressed)
		return response
