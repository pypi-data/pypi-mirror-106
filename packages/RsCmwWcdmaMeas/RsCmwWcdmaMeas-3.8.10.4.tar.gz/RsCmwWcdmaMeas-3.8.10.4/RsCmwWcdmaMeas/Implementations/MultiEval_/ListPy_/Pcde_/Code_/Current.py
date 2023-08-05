from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:PCDE:CODE:CURRent \n
		Snippet: value: List[int] = driver.multiEval.listPy.pcde.code.current.fetch() \n
		Return the code number for which the peak code domain error was measured, for all measured list mode segments. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: pcd_error_code_nr: decimal Comma-separated list of values, one per measured segment Range: 0 to 255"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:PCDE:CODE:CURRent?', suppressed)
		return response
