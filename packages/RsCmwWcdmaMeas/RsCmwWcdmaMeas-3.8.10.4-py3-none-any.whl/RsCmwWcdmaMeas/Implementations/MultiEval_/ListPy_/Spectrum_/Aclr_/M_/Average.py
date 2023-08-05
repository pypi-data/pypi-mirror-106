from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self, aclr_mode: enums.AclrMode = None, minus=repcap.Minus.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SPECtrum:ACLR:M<nr>:AVERage \n
		Snippet: value: List[float] = driver.multiEval.listPy.spectrum.aclr.m.average.fetch(aclr_mode = enums.AclrMode.ABSolute, minus = repcap.Minus.Default) \n
		Return the power of the adjacent channels for all measured list mode segments.
			INTRO_CMD_HELP: The adjacent channel selected via M<no>/P<no> is at the following frequency relative to the carrier frequency: \n
			- M1 = -5 MHz, M2 = -10 MHz
			- P1 = +5 MHz, P2 = +10 MHz \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:param aclr_mode: ABSolute | RELative ABSolute: ACLR power displayed in dBm as absolute value RELative: ACLR power displayed in dB relative to carrier power
			:param minus: optional repeated capability selector. Default value: Ch1 (settable in the interface 'M')
			:return: aclr: float Comma-separated list of values, one per measured segment Range: -100 dBm to 55 dBm, Unit: dBm"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aclr_mode', aclr_mode, DataType.Enum, True))
		minus_cmd_val = self._base.get_repcap_cmd_value(minus, repcap.Minus)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SPECtrum:ACLR:M{minus_cmd_val}:AVERage? {param}'.rstrip(), suppressed)
		return response
