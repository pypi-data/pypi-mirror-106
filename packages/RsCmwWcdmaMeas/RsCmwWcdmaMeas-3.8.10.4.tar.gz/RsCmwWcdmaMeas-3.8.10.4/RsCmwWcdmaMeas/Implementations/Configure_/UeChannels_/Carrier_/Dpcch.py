from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpcch:
	"""Dpcch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpcch", core, parent)

	# noinspection PyTypeChecker
	class DpcchStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF | ON Channel disabled | enabled
			- Beta_Factor: int: numeric Range: 1 to 15
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

	def set(self, structure: DpcchStruct, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:DPCCh \n
		Snippet: driver.configure.ueChannels.carrier.dpcch.set(value = [PROPERTY_STRUCT_NAME](), carrier = repcap.Carrier.Default) \n
		Specifies the presence of a DPCCH in the uplink signal and the beta factor and spreading factor of the channel.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- Beta factor setting:
			Table Header:  \n
			- CONFigure:WCDMa:SIGN<i>:UL:GFACtor:PDATa<no>
			- CONFigure:WCDMa:SIGN<i>:UL:GFACtor:RMC<no>
			- CONFigure:WCDMa:SIGN<i>:UL:GFACtor:VIDeo
			- CONFigure:WCDMa:SIGN<i>:UL:GFACtor:VOICe
			- Setting of spreading factor via automatic configuration depending on connection
		configuration \n
			:param structure: for set value, see the help for DpcchStruct structure arguments.
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:DPCCh', structure)

	def get(self, carrier=repcap.Carrier.Default) -> DpcchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:DPCCh \n
		Snippet: value: DpcchStruct = driver.configure.ueChannels.carrier.dpcch.get(carrier = repcap.Carrier.Default) \n
		Specifies the presence of a DPCCH in the uplink signal and the beta factor and spreading factor of the channel.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- Beta factor setting:
			Table Header:  \n
			- CONFigure:WCDMa:SIGN<i>:UL:GFACtor:PDATa<no>
			- CONFigure:WCDMa:SIGN<i>:UL:GFACtor:RMC<no>
			- CONFigure:WCDMa:SIGN<i>:UL:GFACtor:VIDeo
			- CONFigure:WCDMa:SIGN<i>:UL:GFACtor:VOICe
			- Setting of spreading factor via automatic configuration depending on connection
		configuration \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for DpcchStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:DPCCh?', self.__class__.DpcchStruct())
