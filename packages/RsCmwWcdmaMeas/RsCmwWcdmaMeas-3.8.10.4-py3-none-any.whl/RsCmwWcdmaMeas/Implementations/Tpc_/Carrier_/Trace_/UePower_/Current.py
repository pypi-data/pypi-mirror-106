from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self, carrier=repcap.Carrier.Default) -> List[float]:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:TRACe:UEPower:CURRent \n
		Snippet: value: List[float] = driver.tpc.carrier.trace.uePower.current.fetch(carrier = repcap.Carrier.Default) \n
		Return the values of the UE power vs slot trace per carrier. You can query the number of measured slots using the
		CONFigure:WCDMa:MEAS:TPC:...:MLENgth? command of the used measurement mode. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: ue_power: float N power results, one per measured slot Range: -100 dBm to 55 dBm, Unit: dBm"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:TRACe:UEPower:CURRent?', suppressed)
		return response

	def read(self, carrier=repcap.Carrier.Default) -> List[float]:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:TRACe:UEPower:CURRent \n
		Snippet: value: List[float] = driver.tpc.carrier.trace.uePower.current.read(carrier = repcap.Carrier.Default) \n
		Return the values of the UE power vs slot trace per carrier. You can query the number of measured slots using the
		CONFigure:WCDMa:MEAS:TPC:...:MLENgth? command of the used measurement mode. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: ue_power: float N power results, one per measured slot Range: -100 dBm to 55 dBm, Unit: dBm"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:TRACe:UEPower:CURRent?', suppressed)
		return response

	def calculate(self, carrier=repcap.Carrier.Default) -> List[float]:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:TRACe:UEPower:CURRent \n
		Snippet: value: List[float] = driver.tpc.carrier.trace.uePower.current.calculate(carrier = repcap.Carrier.Default) \n
		Return the values of the UE power vs slot trace per carrier. You can query the number of measured slots using the
		CONFigure:WCDMa:MEAS:TPC:...:MLENgth? command of the used measurement mode. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: ue_power: float N power results, one per measured slot Range: -100 dBm to 55 dBm, Unit: dBm"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:TRACe:UEPower:CURRent?', suppressed)
		return response
