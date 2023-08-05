from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ulcm:
	"""Ulcm commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ulcm", core, parent)

	# noinspection PyTypeChecker
	class PaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Initial_Pwr_Step: float or bool: numeric | ON | OFF Symmetrical tolerance value for UE TX power in the first slot after the gap Range: 0 dB to 10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit)
			- Power_Step: float or bool: numeric | ON | OFF Symmetrical tolerance value for UE TX power in a recovery period Range: 0 dB to 10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit)
			- Power_Step_Group: float or bool: numeric | ON | OFF Symmetrical tolerance value for the aggregate UE TX power in the recovery period comprising the 7 rising or falling power steps after each gap Range: 0 dB to 10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Initial_Pwr_Step'),
			ArgStruct.scalar_float_ext('Power_Step'),
			ArgStruct.scalar_float_ext('Power_Step_Group')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Initial_Pwr_Step: float or bool = None
			self.Power_Step: float or bool = None
			self.Power_Step_Group: float or bool = None

	def get_pa(self) -> PaStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ULCM:PA \n
		Snippet: value: PaStruct = driver.configure.tpc.limit.ulcm.get_pa() \n
		Configures a power step limit for the measurement mode 'UL Compressed Mode', CM pattern A. \n
			:return: structure: for return value, see the help for PaStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ULCM:PA?', self.__class__.PaStruct())

	def set_pa(self, value: PaStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ULCM:PA \n
		Snippet: driver.configure.tpc.limit.ulcm.set_pa(value = PaStruct()) \n
		Configures a power step limit for the measurement mode 'UL Compressed Mode', CM pattern A. \n
			:param value: see the help for PaStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ULCM:PA', value)

	# noinspection PyTypeChecker
	class PbStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Initial_Pwr_Step: float or bool: numeric | ON | OFF Symmetrical tolerance value for the UE TX power in the first slot after the gap Range: 0 dB to 10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit)
			- Power_Step: float or bool: numeric | ON | OFF Symmetrical tolerance value for the UE TX power in the nonCM - CM and CM - nonCM power step Range: 0 dB to 10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Initial_Pwr_Step'),
			ArgStruct.scalar_float_ext('Power_Step')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Initial_Pwr_Step: float or bool = None
			self.Power_Step: float or bool = None

	def get_pb(self) -> PbStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ULCM:PB \n
		Snippet: value: PbStruct = driver.configure.tpc.limit.ulcm.get_pb() \n
		Configures a power step limit for the measurement mode 'UL Compressed Mode', CM pattern B. \n
			:return: structure: for return value, see the help for PbStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ULCM:PB?', self.__class__.PbStruct())

	def set_pb(self, value: PbStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ULCM:PB \n
		Snippet: driver.configure.tpc.limit.ulcm.set_pb(value = PbStruct()) \n
		Configures a power step limit for the measurement mode 'UL Compressed Mode', CM pattern B. \n
			:param value: see the help for PbStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ULCM:PB', value)
