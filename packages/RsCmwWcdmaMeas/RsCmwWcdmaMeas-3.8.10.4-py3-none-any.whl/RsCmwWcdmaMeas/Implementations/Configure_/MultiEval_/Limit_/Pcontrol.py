from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcontrol:
	"""Pcontrol commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcontrol", core, parent)

	# noinspection PyTypeChecker
	class HsdpcchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Dtx_To_Nack: float: numeric Range: -10 dB to 10 dB, Unit: dB
			- Nack_To_Cqi: float: numeric Range: -10 dB to 10 dB, Unit: dB
			- Cqi_To_Dtx: float: numeric Range: -10 dB to 10 dB, Unit: dB
			- Test_Case: enums.TestCase: T0DB | T1DB T0DB: measurement below maximum UE power with TPC command = 0 dB T1DB: measurement at maximum UE power with TPC command = 1 dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Dtx_To_Nack'),
			ArgStruct.scalar_float('Nack_To_Cqi'),
			ArgStruct.scalar_float('Cqi_To_Dtx'),
			ArgStruct.scalar_enum('Test_Case', enums.TestCase)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Dtx_To_Nack: float = None
			self.Nack_To_Cqi: float = None
			self.Cqi_To_Dtx: float = None
			self.Test_Case: enums.TestCase = None

	def get_hsdpcch(self) -> HsdpcchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PCONtrol:HSDPcch \n
		Snippet: value: HsdpcchStruct = driver.configure.multiEval.limit.pcontrol.get_hsdpcch() \n
		Defines nominal power steps for the HS-DPCCH limit set. Measurements at maximum UE power and below maximum UE power are
		supported. Separate values can be defined for the boundaries DTX > (N) ACK, (N) ACK > CQI and CQI > DTX. Also the limit
		check can be enabled or disabled. See also 'Power Control Limits' \n
			:return: structure: for return value, see the help for HsdpcchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PCONtrol:HSDPcch?', self.__class__.HsdpcchStruct())

	def set_hsdpcch(self, value: HsdpcchStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PCONtrol:HSDPcch \n
		Snippet: driver.configure.multiEval.limit.pcontrol.set_hsdpcch(value = HsdpcchStruct()) \n
		Defines nominal power steps for the HS-DPCCH limit set. Measurements at maximum UE power and below maximum UE power are
		supported. Separate values can be defined for the boundaries DTX > (N) ACK, (N) ACK > CQI and CQI > DTX. Also the limit
		check can be enabled or disabled. See also 'Power Control Limits' \n
			:param value: see the help for HsdpcchStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PCONtrol:HSDPcch', value)

	# noinspection PyTypeChecker
	class EpStepStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Expected_0_Db: float: numeric Tolerance value for power step size 0 dB Range: 0 dB to 5 dB, Unit: dB
			- Expected_1_Db: float: numeric Tolerance value for power step size 1 dB Range: 0 dB to 5 dB, Unit: dB
			- Expected_2_Db: float: numeric Tolerance value for power step size 2 dB Range: 0 dB to 5 dB, Unit: dB
			- Expected_3_Db: float: numeric Tolerance value for power step size 3 dB Range: 0 dB to 5 dB, Unit: dB
			- Expected_4_To_7_Db: float: numeric Tolerance value for power step size 4 dB to 7 dB Range: 0 dB to 5 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Expected_0_Db'),
			ArgStruct.scalar_float('Expected_1_Db'),
			ArgStruct.scalar_float('Expected_2_Db'),
			ArgStruct.scalar_float('Expected_3_Db'),
			ArgStruct.scalar_float('Expected_4_To_7_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Expected_0_Db: float = None
			self.Expected_1_Db: float = None
			self.Expected_2_Db: float = None
			self.Expected_3_Db: float = None
			self.Expected_4_To_7_Db: float = None

	def get_ep_step(self) -> EpStepStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PCONtrol:EPSTep \n
		Snippet: value: EpStepStruct = driver.configure.multiEval.limit.pcontrol.get_ep_step() \n
		Defines tolerance values ('Expected Power Step Limits') depending on the nominal power step size. \n
			:return: structure: for return value, see the help for EpStepStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PCONtrol:EPSTep?', self.__class__.EpStepStruct())

	def set_ep_step(self, value: EpStepStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PCONtrol:EPSTep \n
		Snippet: driver.configure.multiEval.limit.pcontrol.set_ep_step(value = EpStepStruct()) \n
		Defines tolerance values ('Expected Power Step Limits') depending on the nominal power step size. \n
			:param value: see the help for EpStepStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PCONtrol:EPSTep', value)
