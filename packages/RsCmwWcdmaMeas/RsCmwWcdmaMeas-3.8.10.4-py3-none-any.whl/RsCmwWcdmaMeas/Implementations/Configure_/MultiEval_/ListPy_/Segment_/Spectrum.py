from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrum:
	"""Spectrum commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("spectrum", core, parent)

	# noinspection PyTypeChecker
	class SpectrumStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Spec_Statistics: int: integer The statistical length is limited by the length of the segment (see [CMDLINK: CONFigure:WCDMa:MEASi:MEValuation:LIST:SEGMentno:SETup CMDLINK]) . Range: 1 to 1000
			- Enable_Aclr: bool: OFF | ON OFF: Disable measurement ON: Enable measurement of ACLR
			- Enable_Emask: bool: OFF | ON Disable or enable measurement of spectrum emission mask
			- Enable_Obw: bool: OFF | ON Disable or enable measurement of occupied bandwidth"""
		__meta_args_list = [
			ArgStruct.scalar_int('Spec_Statistics'),
			ArgStruct.scalar_bool('Enable_Aclr'),
			ArgStruct.scalar_bool('Enable_Emask'),
			ArgStruct.scalar_bool('Enable_Obw')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spec_Statistics: int = None
			self.Enable_Aclr: bool = None
			self.Enable_Emask: bool = None
			self.Enable_Obw: bool = None

	def set(self, structure: SpectrumStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SPECtrum \n
		Snippet: driver.configure.multiEval.listPy.segment.spectrum.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage and MAXimum calculation and enables the calculation of the different
		spectrum results in segment no. <no>; see 'Multi-Evaluation List Mode'. \n
			:param structure: for set value, see the help for SpectrumStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SPECtrum', structure)

	def get(self, segment=repcap.Segment.Default) -> SpectrumStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SPECtrum \n
		Snippet: value: SpectrumStruct = driver.configure.multiEval.listPy.segment.spectrum.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage and MAXimum calculation and enables the calculation of the different
		spectrum results in segment no. <no>; see 'Multi-Evaluation List Mode'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SpectrumStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SPECtrum?', self.__class__.SpectrumStruct())
