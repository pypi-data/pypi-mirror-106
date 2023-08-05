from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Ue_Power: float: float UE power Range: -100 dBm to 55 dBm, Unit: dBm
			- Max_Output_Power: float: float Maximum output power Range: -100 dBm to 55 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Max_Output_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ue_Power: float = None
			self.Max_Output_Power: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:TOTal:UEPower:AVERage \n
		Snippet: value: ResultData = driver.tpc.total.uePower.average.fetch() \n
		Return the UE power and maximum output power single value results over all carriers. The minimum, maximum and average
		values of these results can be retrieved. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:TPC:TOTal:UEPower:AVERage?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:TOTal:UEPower:AVERage \n
		Snippet: value: ResultData = driver.tpc.total.uePower.average.read() \n
		Return the UE power and maximum output power single value results over all carriers. The minimum, maximum and average
		values of these results can be retrieved. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:TPC:TOTal:UEPower:AVERage?', self.__class__.ResultData())
