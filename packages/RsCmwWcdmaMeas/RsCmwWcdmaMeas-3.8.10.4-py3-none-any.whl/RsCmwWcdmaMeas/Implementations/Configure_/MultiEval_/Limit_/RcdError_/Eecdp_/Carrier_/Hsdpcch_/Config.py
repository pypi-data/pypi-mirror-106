from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("config", core, parent)

	def set(self, type_py: enums.Type, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier>:HSDPcch:CONFig \n
		Snippet: driver.configure.multiEval.limit.rcdError.eecdp.carrier.hsdpcch.config.set(type_py = enums.Type.ACK, carrier = repcap.Carrier.Default) \n
		Selects whether the HS-DPCCH transports an ACK, NACK or CQI and thus which set of beta factor and spreading factor values
		is used. \n
			:param type_py: ACK | NACK | CQI
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		param = Conversions.enum_scalar_to_str(type_py, enums.Type)
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}:HSDPcch:CONFig {param}')

	# noinspection PyTypeChecker
	def get(self, carrier=repcap.Carrier.Default) -> enums.Type:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier>:HSDPcch:CONFig \n
		Snippet: value: enums.Type = driver.configure.multiEval.limit.rcdError.eecdp.carrier.hsdpcch.config.get(carrier = repcap.Carrier.Default) \n
		Selects whether the HS-DPCCH transports an ACK, NACK or CQI and thus which set of beta factor and spreading factor values
		is used. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: type_py: ACK | NACK | CQI"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}:HSDPcch:CONFig?')
		return Conversions.str_to_scalar_enum(response, enums.Type)
