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
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:TRACe:EVMagnitude:PEAK:CURRent \n
		Snippet: value: List[float] = driver.prach.trace.evMagnitude.peak.current.fetch() \n
		Return the EVM RMS and peak values for each measured preamble. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: evm: float Comma-separated list of values, one result per measured preamble (see method RsCmwWcdmaMeas.Configure.Prach.mpreamble) Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:TRACe:EVMagnitude:PEAK:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:TRACe:EVMagnitude:PEAK:CURRent \n
		Snippet: value: List[float] = driver.prach.trace.evMagnitude.peak.current.read() \n
		Return the EVM RMS and peak values for each measured preamble. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: evm: float Comma-separated list of values, one result per measured preamble (see method RsCmwWcdmaMeas.Configure.Prach.mpreamble) Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:PRACh:TRACe:EVMagnitude:PEAK:CURRent?', suppressed)
		return response
