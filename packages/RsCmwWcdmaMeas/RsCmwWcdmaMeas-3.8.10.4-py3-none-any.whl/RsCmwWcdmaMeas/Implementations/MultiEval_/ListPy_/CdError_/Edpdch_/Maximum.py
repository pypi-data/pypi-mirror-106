from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	def fetch(self, edpdChannel=repcap.EdpdChannel.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:CDERror:EDPDch<nr>:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.listPy.cdError.edpdch.maximum.fetch(edpdChannel = repcap.EdpdChannel.Default) \n
		Return RMS CDP and CDE vs. slot values for a selected E-DPDCH for all measured list mode segments. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: edpdch: float Comma-separated list of values, one per measured segment Range: -100 dB to 0 dB, Unit: dB"""
		edpdChannel_cmd_val = self._base.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:CDERror:EDPDch{edpdChannel_cmd_val}:MAXimum?', suppressed)
		return response
