from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


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

	# noinspection PyTypeChecker
	class EdpdchStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF | ON Channel disabled | enabled
			- Beta_Factor: int: numeric Range: 5 to 5655
			- Spreading_Factor: int: numeric Range: 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Beta_Factor'),
			ArgStruct.scalar_int('Spreading_Factor')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Beta_Factor: int = None
			self.Spreading_Factor: int = None

	def set(self, structure: EdpdchStruct, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:EDPDch<nr> \n
		Snippet: driver.configure.ueChannels.carrier.edpdch.set(value = [PROPERTY_STRUCT_NAME](), carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Specifies the presence of a selected E-DPDCH (1 to 4) in the uplink signal and the beta factor and spreading factor of
		the channel.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- Beta factor setting: CONFigure:WCDMa:SIGN<i>:UL:GFACtor:HSUPa:EDPCch
			- Setting of spreading factor via automatic configuration depending on connection configuration \n
			:param structure: for set value, see the help for EdpdchStruct structure arguments.
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._base.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:EDPDch{edpdChannel_cmd_val}', structure)

	def get(self, carrier=repcap.Carrier.Default, edpdChannel=repcap.EdpdChannel.Default) -> EdpdchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:EDPDch<nr> \n
		Snippet: value: EdpdchStruct = driver.configure.ueChannels.carrier.edpdch.get(carrier = repcap.Carrier.Default, edpdChannel = repcap.EdpdChannel.Default) \n
		Specifies the presence of a selected E-DPDCH (1 to 4) in the uplink signal and the beta factor and spreading factor of
		the channel.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- Beta factor setting: CONFigure:WCDMa:SIGN<i>:UL:GFACtor:HSUPa:EDPCch
			- Setting of spreading factor via automatic configuration depending on connection configuration \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:param edpdChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Edpdch')
			:return: structure: for return value, see the help for EdpdchStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		edpdChannel_cmd_val = self._base.get_repcap_cmd_value(edpdChannel, repcap.EdpdChannel)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:EDPDch{edpdChannel_cmd_val}?', self.__class__.EdpdchStruct())

	def clone(self) -> 'Edpdch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Edpdch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
