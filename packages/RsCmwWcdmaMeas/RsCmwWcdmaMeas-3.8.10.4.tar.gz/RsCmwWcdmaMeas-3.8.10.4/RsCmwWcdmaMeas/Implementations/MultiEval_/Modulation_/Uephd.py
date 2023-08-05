from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uephd:
	"""Uephd commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uephd", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Overall_Max_Ph_D: float: float Overall maximum phase discontinuity Range: -180 deg to 180 deg, Unit: deg
			- Overall_Min_Dist: float: decimal Overall minimum slot distance between two results exceeding the dynamic limit Unit: slots
			- Count_Upper_Limit: float: decimal Number of results exceeding the upper limit Range: 0 to 99999999
			- Count_Dyn_Limit: float: decimal Number of results exceeding the dynamic limit Range: 0 to 99999999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Overall_Max_Ph_D'),
			ArgStruct.scalar_float('Overall_Min_Dist'),
			ArgStruct.scalar_float('Count_Upper_Limit'),
			ArgStruct.scalar_float('Count_Dyn_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Overall_Max_Ph_D: float = None
			self.Overall_Min_Dist: float = None
			self.Count_Upper_Limit: float = None
			self.Count_Dyn_Limit: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:MODulation:UEPHd \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.uephd.calculate() \n
		Returns the UE phase discontinuity single value results for signals without HSPA channels. The results depend on the
		upper limit and the dynamic limit, see method RsCmwWcdmaMeas.Configure.MultiEval.Limit.phd. See also 'Detailed Views:
		Phase Discontinuity' The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:MODulation:UEPHd?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Overall_Max_Ph_D: float: float Overall maximum phase discontinuity Range: -180 deg to 180 deg, Unit: deg
			- Overall_Min_Dist: int: decimal Overall minimum slot distance between two results exceeding the dynamic limit Unit: slots
			- Count_Upper_Limit: int: decimal Number of results exceeding the upper limit Range: 0 to 99999999
			- Count_Dyn_Limit: int: decimal Number of results exceeding the dynamic limit Range: 0 to 99999999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Overall_Max_Ph_D'),
			ArgStruct.scalar_int('Overall_Min_Dist'),
			ArgStruct.scalar_int('Count_Upper_Limit'),
			ArgStruct.scalar_int('Count_Dyn_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Overall_Max_Ph_D: float = None
			self.Overall_Min_Dist: int = None
			self.Count_Upper_Limit: int = None
			self.Count_Dyn_Limit: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:MODulation:UEPHd \n
		Snippet: value: ResultData = driver.multiEval.modulation.uephd.read() \n
		Returns the UE phase discontinuity single value results for signals without HSPA channels. The results depend on the
		upper limit and the dynamic limit, see method RsCmwWcdmaMeas.Configure.MultiEval.Limit.phd. See also 'Detailed Views:
		Phase Discontinuity' The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:MODulation:UEPHd?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:MODulation:UEPHd \n
		Snippet: value: ResultData = driver.multiEval.modulation.uephd.fetch() \n
		Returns the UE phase discontinuity single value results for signals without HSPA channels. The results depend on the
		upper limit and the dynamic limit, see method RsCmwWcdmaMeas.Configure.MultiEval.Limit.phd. See also 'Detailed Views:
		Phase Discontinuity' The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:MODulation:UEPHd?', self.__class__.ResultData())
