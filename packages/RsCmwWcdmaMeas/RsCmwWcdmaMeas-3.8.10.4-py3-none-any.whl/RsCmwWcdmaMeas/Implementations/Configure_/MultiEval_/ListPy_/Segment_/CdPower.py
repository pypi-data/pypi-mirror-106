from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdPower:
	"""CdPower commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cdPower", core, parent)

	# noinspection PyTypeChecker
	class CdPowerStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Mod_Statistics: int: integer The statistical length is limited by the length of the segment (see [CMDLINK: CONFigure:WCDMa:MEASi:MEValuation:LIST:SEGMentno:SETup CMDLINK]) . Range: 1 to 1000
			- Enable_Cdp: bool: OFF | ON OFF: Disable measurement ON: Enable measurement of code domain power
			- Enable_Cde: bool: OFF | ON Disable or enable measurement of code domain error
			- Enable_Pcde: bool: Optional setting parameter. OFF | ON Disable or enable measurement of peak code domain error"""
		__meta_args_list = [
			ArgStruct.scalar_int('Mod_Statistics'),
			ArgStruct.scalar_bool('Enable_Cdp'),
			ArgStruct.scalar_bool('Enable_Cde'),
			ArgStruct.scalar_bool('Enable_Pcde')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Statistics: int = None
			self.Enable_Cdp: bool = None
			self.Enable_Cde: bool = None
			self.Enable_Pcde: bool = None

	def set(self, structure: CdPowerStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CDPower \n
		Snippet: driver.configure.multiEval.listPy.segment.cdPower.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage, MINimum, MAXimum and SDEViation calculation and enables the calculation
		of the different code domain results in segment no. <no>; see 'Multi-Evaluation List Mode'. The statistical length for
		CDP, CDE, PCDE and modulation results is identical (see also method RsCmwWcdmaMeas.Configure.MultiEval.ListPy.Segment.
		Modulation.set) . \n
			:param structure: for set value, see the help for CdPowerStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CDPower', structure)

	def get(self, segment=repcap.Segment.Default) -> CdPowerStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CDPower \n
		Snippet: value: CdPowerStruct = driver.configure.multiEval.listPy.segment.cdPower.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage, MINimum, MAXimum and SDEViation calculation and enables the calculation
		of the different code domain results in segment no. <no>; see 'Multi-Evaluation List Mode'. The statistical length for
		CDP, CDE, PCDE and modulation results is identical (see also method RsCmwWcdmaMeas.Configure.MultiEval.ListPy.Segment.
		Modulation.set) . \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CdPowerStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CDPower?', self.__class__.CdPowerStruct())
