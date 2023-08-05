from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsdpcch:
	"""Hsdpcch commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsdpcch", core, parent)

	@property
	def config(self):
		"""config commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_config'):
			from .Hsdpcch_.Config import Config
			self._config = Config(self._core, self._base)
		return self._config

	# noinspection PyTypeChecker
	class HsdpcchStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF | ON Channel disabled | enabled
			- Beta_Factor: int: numeric Range: 5 to 570
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

	def set(self, structure: HsdpcchStruct, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:HSDPcch \n
		Snippet: driver.configure.ueChannels.carrier.hsdpcch.set(value = [PROPERTY_STRUCT_NAME](), carrier = repcap.Carrier.Default) \n
		Specifies the presence of an HS-DPCCH in the uplink signal and the beta factor and spreading factor of the channel. For
		the HS-DPCCH three sets of beta factor and spreading factor can be configured, depending on whether it transports an ACK,
		NACK or CQI. This command configures/returns the values related to the currently active set. For selection of the active
		set, see method RsCmwWcdmaMeas.Configure.UeChannels.Carrier.Hsdpcch.Config.set.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- Beta factor setting: CONFigure:WCDMa:SIGN<i>:UL:GFACtor:HSDPa
			- Setting of spreading factor via automatic configuration depending on connection configuration \n
			:param structure: for set value, see the help for HsdpcchStruct structure arguments.
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:HSDPcch', structure)

	def get(self, carrier=repcap.Carrier.Default) -> HsdpcchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:HSDPcch \n
		Snippet: value: HsdpcchStruct = driver.configure.ueChannels.carrier.hsdpcch.get(carrier = repcap.Carrier.Default) \n
		Specifies the presence of an HS-DPCCH in the uplink signal and the beta factor and spreading factor of the channel. For
		the HS-DPCCH three sets of beta factor and spreading factor can be configured, depending on whether it transports an ACK,
		NACK or CQI. This command configures/returns the values related to the currently active set. For selection of the active
		set, see method RsCmwWcdmaMeas.Configure.UeChannels.Carrier.Hsdpcch.Config.set.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- Beta factor setting: CONFigure:WCDMa:SIGN<i>:UL:GFACtor:HSDPa
			- Setting of spreading factor via automatic configuration depending on connection configuration \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for HsdpcchStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:HSDPcch?', self.__class__.HsdpcchStruct())

	def clone(self) -> 'Hsdpcch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsdpcch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
