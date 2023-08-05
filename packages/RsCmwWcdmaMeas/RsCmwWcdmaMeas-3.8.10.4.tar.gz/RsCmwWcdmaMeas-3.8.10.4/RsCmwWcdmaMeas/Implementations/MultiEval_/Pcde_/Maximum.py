from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Pcd_Error: float: float Peak code domain error Range: -100 dB to 0 dB, Unit: dB
			- Pcd_Error_Phase: enums.PcdErrorPhase: IPHase | QPHase Phase where the peak code domain error was measured IPHase: I-Signal QPHase: Q-Signal
			- Pcd_Error_Code_Nr: int: decimal Code number for which the PCDE was measured Range: 0 to 255"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Pcd_Error'),
			ArgStruct.scalar_enum('Pcd_Error_Phase', enums.PcdErrorPhase),
			ArgStruct.scalar_int('Pcd_Error_Code_Nr')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pcd_Error: float = None
			self.Pcd_Error_Phase: enums.PcdErrorPhase = None
			self.Pcd_Error_Code_Nr: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:PCDE:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.pcde.maximum.read() \n
		Returns the peak code domain error (PCDE) results. In addition to the current PCDE value, the maximum PCDE value can be
		retrieved. See also 'Detailed Views: CD Monitor' \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:PCDE:MAXimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:PCDE:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.pcde.maximum.fetch() \n
		Returns the peak code domain error (PCDE) results. In addition to the current PCDE value, the maximum PCDE value can be
		retrieved. See also 'Detailed Views: CD Monitor' \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:PCDE:MAXimum?', self.__class__.ResultData())
