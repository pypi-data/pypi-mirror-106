from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setup:
	"""Setup commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("setup", core, parent)

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Segment_Length: int: integer Number of measured timeslots in the segment. The sum of the length of all active segments must not exceed 6000. Ignoring this limit results in NCAPs for the remaining slots. The statistical length for result calculation covers at most the first 1000 slots of a segment. The sum of the length of all segments (active plus inactive) must not exceed 12000. 'Inactive' means that no measurement at all is enabled for the segment. Range: 1 to 12000, Unit: slot
			- Level: float: numeric Expected nominal power in the segment. The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
			- Frequency: float: numeric Range: 100 MHz to 6 GHz, Unit: Hz
			- Retrigger: enums.Retrigger: Optional setting parameter. OFF | ON | IFPower | IFPSync Specifies whether a trigger event is required for the segment or not. The setting is ignored for the first segment of a measurement and for trigger mode ONCE (see [CMDLINK: TRIGger:WCDMa:MEASi:MEValuation:LIST:MODE CMDLINK]) . OFF: measure the segment without retrigger ON: trigger event required, trigger source configured via [CMDLINK: TRIGger:WCDMa:MEASi:MEValuation:SOURce CMDLINK] IFPower: trigger event required, 'IF Power' trigger IFPSync: trigger event required, 'IF Power (Sync) ' trigger"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Retrigger', enums.Retrigger)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Frequency: float = None
			self.Retrigger: enums.Retrigger = None

	def set(self, structure: SetupStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: driver.configure.multiEval.listPy.segment.setup.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of a selected segment. In general, this command must be sent for all segments
		measured. \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup', structure)

	def get(self, segment=repcap.Segment.Default) -> SetupStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: value: SetupStruct = driver.configure.multiEval.listPy.segment.setup.get(segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of a selected segment. In general, this command must be sent for all segments
		measured. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup?', self.__class__.SetupStruct())
