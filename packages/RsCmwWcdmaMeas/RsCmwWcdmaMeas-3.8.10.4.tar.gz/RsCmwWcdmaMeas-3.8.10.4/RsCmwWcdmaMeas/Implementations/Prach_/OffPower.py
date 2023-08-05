from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffPower:
	"""OffPower commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("offPower", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:OFFPower \n
		Snippet: value: List[float] = driver.prach.offPower.fetch() \n
		Return the OFF power results. See also 'Detailed Views: TX Measurement' \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: off_power: float OFF power before preamble, OFF power after preamble Range: -100 dBm to -24 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:OFFPower?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:OFFPower \n
		Snippet: value: List[float] = driver.prach.offPower.read() \n
		Return the OFF power results. See also 'Detailed Views: TX Measurement' \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: off_power: float OFF power before preamble, OFF power after preamble Range: -100 dBm to -24 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:PRACh:OFFPower?', suppressed)
		return response

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:PRACh:OFFPower \n
		Snippet: value: List[float] = driver.prach.offPower.calculate() \n
		Return the OFF power results. See also 'Detailed Views: TX Measurement' \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: off_power: float OFF power before preamble, OFF power after preamble Range: -100 dBm to -24 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:WCDMa:MEASurement<Instance>:PRACh:OFFPower?', suppressed)
		return response
