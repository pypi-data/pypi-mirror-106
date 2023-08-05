from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edpdch:
	"""Edpdch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: EdpdChannel, default value after init: EdpdChannel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("edpdch", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_edpdChannel_get', 'repcap_edpdChannel_set', repcap.EdpdChannel.Nr1)

	def repcap_edpdChannel_set(self, enum_value: repcap.EdpdChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to EdpdChannel.Default
		Default value after init: EdpdChannel.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_edpdChannel_get(self) -> repcap.EdpdChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, enable: bool, beta_factor: int, spreading_factor: int, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier>:EDPDch<nr> \n
		Snippet: driver.configure.multiEval.limit.rcdError.eecdp.carrier.edpdch.set(enable = False, beta_factor = 1, spreading_factor = 1, carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Specifies the presence of a selected E-DPDCH (1 to 4) in the uplink signal and the beta factor and spreading factor of
		the channel. A query returns also the nominal CDP and effective CDP resulting from these settings. \n
			:param enable: OFF | ON Channel disabled | enabled
			:param beta_factor: numeric Range: 5 to 5655
			:param spreading_factor: numeric Range: 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('beta_factor', beta_factor, DataType.Integer), ArgSingle('spreading_factor', spreading_factor, DataType.Integer))
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._base.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}:EDPDch{edpdChannel_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF | ON Channel disabled | enabled
			- Beta_Factor: int: numeric Range: 5 to 5655
			- Spreading_Factor: int: numeric Range: 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256
			- Nominal_Cdp: float: float Range: -70 dB to 0 dB, Unit: dB
			- Effective_Cdp: float: float Range: -90 dB to 0 dB, Unit: dB"""
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

	def get(self, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier<carrier>:EDPDch<nr> \n
		Snippet: value: GetStruct = driver.configure.multiEval.limit.rcdError.eecdp.carrier.edpdch.get(carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Specifies the presence of a selected E-DPDCH (1 to 4) in the uplink signal and the beta factor and spreading factor of
		the channel. A query returns also the nominal CDP and effective CDP resulting from these settings. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._base.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:EECDp:CARRier{carrier_cmd_val}:EDPDch{edpdChannel_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'Edpdch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Edpdch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
