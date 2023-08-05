from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpcch:
	"""Dpcch commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpcch", core, parent)

	def fetch(self, carrier=repcap.Carrier.Default) -> List[int]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:TRACe:RCDerror:SF:DPCCh \n
		Snippet: value: List[int] = driver.multiEval.carrier.trace.rcdError.sf.dpcch.fetch(carrier = repcap.Carrier.Default) \n
		Returns the current spreading factors for the DPCCH and the DPDCH. Each value refers to a half-slot or a full-slot,
		depending on the measurement period (method RsCmwWcdmaMeas.Configure.MultiEval.Mperiod.modulation) . The number of
		results depends on the measurement length (method RsCmwWcdmaMeas.Configure.MultiEval.msCount) . \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: dpcch: No help available"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:TRACe:RCDerror:SF:DPCCh?', suppressed)
		return response

	def read(self, carrier=repcap.Carrier.Default) -> List[int]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:TRACe:RCDerror:SF:DPCCh \n
		Snippet: value: List[int] = driver.multiEval.carrier.trace.rcdError.sf.dpcch.read(carrier = repcap.Carrier.Default) \n
		Returns the current spreading factors for the DPCCH and the DPDCH. Each value refers to a half-slot or a full-slot,
		depending on the measurement period (method RsCmwWcdmaMeas.Configure.MultiEval.Mperiod.modulation) . The number of
		results depends on the measurement length (method RsCmwWcdmaMeas.Configure.MultiEval.msCount) . \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: dpcch: No help available"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:TRACe:RCDerror:SF:DPCCh?', suppressed)
		return response
