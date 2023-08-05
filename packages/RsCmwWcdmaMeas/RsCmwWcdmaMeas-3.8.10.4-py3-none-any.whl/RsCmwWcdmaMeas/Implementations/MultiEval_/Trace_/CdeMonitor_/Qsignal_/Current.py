from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:TRACe:CDEMonitor:QSIGnal:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.cdeMonitor.qsignal.current.fetch() \n
		Returns the values of the code domain error traces of the code domain monitor. The results of the I-Signal and Q-Signal
		traces can be retrieved. See also 'Detailed Views: CD Monitor' \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qsignal: float One value per code channel. The number of values/channels corresponds to the spreading factor (e.g. 8 values/channels for SF8) . Range: -100 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:TRACe:CDEMonitor:QSIGnal:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:TRACe:CDEMonitor:QSIGnal:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.cdeMonitor.qsignal.current.read() \n
		Returns the values of the code domain error traces of the code domain monitor. The results of the I-Signal and Q-Signal
		traces can be retrieved. See also 'Detailed Views: CD Monitor' \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qsignal: float One value per code channel. The number of values/channels corresponds to the spreading factor (e.g. 8 values/channels for SF8) . Range: -100 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:TRACe:CDEMonitor:QSIGnal:CURRent?', suppressed)
		return response
