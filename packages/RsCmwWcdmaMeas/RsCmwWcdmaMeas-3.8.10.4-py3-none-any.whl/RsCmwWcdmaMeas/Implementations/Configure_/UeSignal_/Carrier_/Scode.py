from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scode:
	"""Scode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scode", core, parent)

	def set(self, code: float, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UESignal:CARRier<carrier>:SCODe \n
		Snippet: driver.configure.ueSignal.carrier.scode.set(code = 1.0, carrier = repcap.Carrier.Default) \n
		Selects the number of the long code that is used to scramble the received uplink WCDMA signal. For the combined signal
		path scenario, useCONFigure:WCDMa:SIGN<i>:UL:CARRier<c>:SCODe. \n
			:param code: numeric Range: #H0 to #HFFFFFF
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		param = Conversions.decimal_value_to_str(code)
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:UESignal:CARRier{carrier_cmd_val}:SCODe {param}')

	def get(self, carrier=repcap.Carrier.Default) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UESignal:CARRier<carrier>:SCODe \n
		Snippet: value: float = driver.configure.ueSignal.carrier.scode.get(carrier = repcap.Carrier.Default) \n
		Selects the number of the long code that is used to scramble the received uplink WCDMA signal. For the combined signal
		path scenario, useCONFigure:WCDMa:SIGN<i>:UL:CARRier<c>:SCODe. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: code: numeric Range: #H0 to #HFFFFFF"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'CONFigure:WCDMa:MEASurement<Instance>:UESignal:CARRier{carrier_cmd_val}:SCODe?')
		return Conversions.str_to_float(response)
