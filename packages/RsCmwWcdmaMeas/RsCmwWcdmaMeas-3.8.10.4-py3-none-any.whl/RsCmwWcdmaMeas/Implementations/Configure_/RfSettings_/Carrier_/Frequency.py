from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:CARRier<carrier>:FREQuency \n
		Snippet: driver.configure.rfSettings.carrier.frequency.set(frequency = 1.0, carrier = repcap.Carrier.Default) \n
		Selects the center frequency of the RF analyzer.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:WCDMa:SIGN<i>:RFSettings:CARRier<c>:FREQuency:UL
			- CONFigure:WCDMa:SIGN<i>:RFSettings:CARRier<c>:FOFFset:UL
			- CONFigure:WCDMa:SIGN<i>:RFSettings:CARRier<c>:CHANnel:UL
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param frequency: numeric Range: 70 MHz to 6 GHz, Unit: Hz Using the unit CH the frequency can be set via the channel number. The allowed channel number range depends on the operating band, see 'Operating Bands'.
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		param = Conversions.decimal_value_to_str(frequency)
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:CARRier{carrier_cmd_val}:FREQuency {param}')

	def get(self, carrier=repcap.Carrier.Default) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:CARRier<carrier>:FREQuency \n
		Snippet: value: float = driver.configure.rfSettings.carrier.frequency.get(carrier = repcap.Carrier.Default) \n
		Selects the center frequency of the RF analyzer.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:WCDMa:SIGN<i>:RFSettings:CARRier<c>:FREQuency:UL
			- CONFigure:WCDMa:SIGN<i>:RFSettings:CARRier<c>:FOFFset:UL
			- CONFigure:WCDMa:SIGN<i>:RFSettings:CARRier<c>:CHANnel:UL
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: frequency: numeric Range: 70 MHz to 6 GHz, Unit: Hz Using the unit CH the frequency can be set via the channel number. The allowed channel number range depends on the operating band, see 'Operating Bands'."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:CARRier{carrier_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)
