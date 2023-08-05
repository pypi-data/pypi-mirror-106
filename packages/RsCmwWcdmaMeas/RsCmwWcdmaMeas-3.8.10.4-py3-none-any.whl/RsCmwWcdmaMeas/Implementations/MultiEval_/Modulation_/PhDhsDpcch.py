from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhDhsDpcch:
	"""PhDhsDpcch commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("phDhsDpcch", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Overall_Max_Ph_D: float: No parameter help available
			- Measure_Points: float: No parameter help available
			- Count_Dyn_Limit: float: decimal Number of results exceeding the limit Range: 0 to 99999999
			- Ratio_Dyn_Limit: float: float Percentage of results exceeding the limit Range: 0 % to 100 %, Unit: %
			- Meas_Point_Acurr: float: No parameter help available
			- Meas_Point_Amax: float: No parameter help available
			- Meas_Point_Bcurr: float: No parameter help available
			- Meas_Point_Bmax: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Overall_Max_Ph_D'),
			ArgStruct.scalar_float('Measure_Points'),
			ArgStruct.scalar_float('Count_Dyn_Limit'),
			ArgStruct.scalar_float('Ratio_Dyn_Limit'),
			ArgStruct.scalar_float('Meas_Point_Acurr'),
			ArgStruct.scalar_float('Meas_Point_Amax'),
			ArgStruct.scalar_float('Meas_Point_Bcurr'),
			ArgStruct.scalar_float('Meas_Point_Bmax')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Overall_Max_Ph_D: float = None
			self.Measure_Points: float = None
			self.Count_Dyn_Limit: float = None
			self.Ratio_Dyn_Limit: float = None
			self.Meas_Point_Acurr: float = None
			self.Meas_Point_Amax: float = None
			self.Meas_Point_Bcurr: float = None
			self.Meas_Point_Bmax: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:MODulation:PHDHsdpcch \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.phDhsDpcch.calculate() \n
		Returns the phase discontinuity HS-DPCCH single value results for signals with HS-DPCCH. The results depend on the
		dynamic limit and points A and B (see method RsCmwWcdmaMeas.Configure.MultiEval.Limit.phsDpcch) . See also 'Detailed
		Views: Phase Discontinuity' The values described below are returned by FETCh and READ commands. CALCulate commands return
		limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:MODulation:PHDHsdpcch?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Overall_Max_Ph_D: float: No parameter help available
			- Measure_Points: int: No parameter help available
			- Count_Dyn_Limit: int: decimal Number of results exceeding the limit Range: 0 to 99999999
			- Ratio_Dyn_Limit: float: float Percentage of results exceeding the limit Range: 0 % to 100 %, Unit: %
			- Meas_Point_Acurr: float: No parameter help available
			- Meas_Point_Amax: float: No parameter help available
			- Meas_Point_Bcurr: float: No parameter help available
			- Meas_Point_Bmax: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Overall_Max_Ph_D'),
			ArgStruct.scalar_int('Measure_Points'),
			ArgStruct.scalar_int('Count_Dyn_Limit'),
			ArgStruct.scalar_float('Ratio_Dyn_Limit'),
			ArgStruct.scalar_float('Meas_Point_Acurr'),
			ArgStruct.scalar_float('Meas_Point_Amax'),
			ArgStruct.scalar_float('Meas_Point_Bcurr'),
			ArgStruct.scalar_float('Meas_Point_Bmax')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Overall_Max_Ph_D: float = None
			self.Measure_Points: int = None
			self.Count_Dyn_Limit: int = None
			self.Ratio_Dyn_Limit: float = None
			self.Meas_Point_Acurr: float = None
			self.Meas_Point_Amax: float = None
			self.Meas_Point_Bcurr: float = None
			self.Meas_Point_Bmax: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:MODulation:PHDHsdpcch \n
		Snippet: value: ResultData = driver.multiEval.modulation.phDhsDpcch.read() \n
		Returns the phase discontinuity HS-DPCCH single value results for signals with HS-DPCCH. The results depend on the
		dynamic limit and points A and B (see method RsCmwWcdmaMeas.Configure.MultiEval.Limit.phsDpcch) . See also 'Detailed
		Views: Phase Discontinuity' The values described below are returned by FETCh and READ commands. CALCulate commands return
		limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:MODulation:PHDHsdpcch?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:MODulation:PHDHsdpcch \n
		Snippet: value: ResultData = driver.multiEval.modulation.phDhsDpcch.fetch() \n
		Returns the phase discontinuity HS-DPCCH single value results for signals with HS-DPCCH. The results depend on the
		dynamic limit and points A and B (see method RsCmwWcdmaMeas.Configure.MultiEval.Limit.phsDpcch) . See also 'Detailed
		Views: Phase Discontinuity' The values described below are returned by FETCh and READ commands. CALCulate commands return
		limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:MODulation:PHDHsdpcch?', self.__class__.ResultData())
