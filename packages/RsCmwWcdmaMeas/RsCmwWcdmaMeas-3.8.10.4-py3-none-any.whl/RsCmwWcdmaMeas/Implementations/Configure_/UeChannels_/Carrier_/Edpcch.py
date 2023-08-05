from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edpcch:
	"""Edpcch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("edpcch", core, parent)

	# noinspection PyTypeChecker
	class EdpcchStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF | ON Channel disabled | enabled
			- Beta_Factor: int: numeric Range: 5 to 3585
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

	def set(self, structure: EdpcchStruct, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:EDPCch \n
		Snippet: driver.configure.ueChannels.carrier.edpcch.set(value = [PROPERTY_STRUCT_NAME](), carrier = repcap.Carrier.Default) \n
		Specifies the presence of an E-DPCCH in the uplink signal and the beta factor and spreading factor of the channel.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- Beta factor setting: CONFigure:WCDMa:SIGN<i>:UL:GFACtor:HSUPa:EDPCch
			- Setting of spreading factor via automatic configuration depending on connection configuration \n
			:param structure: for set value, see the help for EdpcchStruct structure arguments.
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:EDPCch', structure)

	def get(self, carrier=repcap.Carrier.Default) -> EdpcchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:CARRier<carrier>:EDPCch \n
		Snippet: value: EdpcchStruct = driver.configure.ueChannels.carrier.edpcch.get(carrier = repcap.Carrier.Default) \n
		Specifies the presence of an E-DPCCH in the uplink signal and the beta factor and spreading factor of the channel.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- Beta factor setting: CONFigure:WCDMa:SIGN<i>:UL:GFACtor:HSUPa:EDPCch
			- Setting of spreading factor via automatic configuration depending on connection configuration \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for EdpcchStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:CARRier{carrier_cmd_val}:EDPCch?', self.__class__.EdpcchStruct())
