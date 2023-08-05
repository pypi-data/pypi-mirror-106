from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpcch:
	"""Dpcch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpcch", core, parent)

	def set(self, enable: bool, beta_factor: int, spreading_factor: int, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier>:DPCCh \n
		Snippet: driver.configure.multiEval.limit.rcdError.eecdp.carrier.dpcch.set(enable = False, beta_factor = 1, spreading_factor = 1, carrier = repcap.Carrier.Default) \n
		Specifies the presence of a DPCCH in the uplink signal and the beta factor and spreading factor of the channel. A query
		returns also the nominal CDP and effective CDP resulting from these settings. \n
			:param enable: OFF | ON Channel disabled | enabled
			:param beta_factor: numeric Range: 1 to 15
			:param spreading_factor: numeric Range: 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('beta_factor', beta_factor, DataType.Integer), ArgSingle('spreading_factor', spreading_factor, DataType.Integer))
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}:DPCCh {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF | ON Channel disabled | enabled
			- Beta_Factor: int: numeric Range: 1 to 15
			- Spreading_Factor: int: numeric Range: 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256
			- Nominal_Cdp: float: float Range: -60 dB to 0 dB, Unit: dB
			- Effective_Cdp: float: float Range: -80 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Beta_Factor'),
			ArgStruct.scalar_int('Spreading_Factor'),
			ArgStruct.scalar_float('Nominal_Cdp'),
			ArgStruct.scalar_float('Effective_Cdp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Beta_Factor: int = None
			self.Spreading_Factor: int = None
			self.Nominal_Cdp: float = None
			self.Effective_Cdp: float = None

	def get(self, carrier=repcap.Carrier.Default) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier>:DPCCh \n
		Snippet: value: GetStruct = driver.configure.multiEval.limit.rcdError.eecdp.carrier.dpcch.get(carrier = repcap.Carrier.Default) \n
		Specifies the presence of a DPCCH in the uplink signal and the beta factor and spreading factor of the channel. A query
		returns also the nominal CDP and effective CDP resulting from these settings. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}:DPCCh?', self.__class__.GetStruct())
