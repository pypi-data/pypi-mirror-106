from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaxPower:
	"""MaxPower commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maxPower", core, parent)

	def get_urp_class(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower:URPClass \n
		Snippet: value: bool = driver.configure.tpc.limit.ilpControl.maxPower.get_urp_class() \n
		Enables or disables the use of the UE power class value reported by the UE in the capability report. This command is only
		relevant for combined signal path 'Inner Loop Power Control' measurements and only if the predefined limit sets are used. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower:URPClass?')
		return Conversions.str_to_bool(response)

	def set_urp_class(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower:URPClass \n
		Snippet: driver.configure.tpc.limit.ilpControl.maxPower.set_urp_class(enable = False) \n
		Enables or disables the use of the UE power class value reported by the UE in the capability report. This command is only
		relevant for combined signal path 'Inner Loop Power Control' measurements and only if the predefined limit sets are used. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower:URPClass {param}')

	# noinspection PyTypeChecker
	class ActiveStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Nominal_Max_Power: float: float Nominal maximum output power of the UE Range: -50 dBm to 34 dBm, Unit: dBm
			- Upper_Limit: float: float Tolerance value for too high maximum UE power Range: 0 dB to 5 dB, Unit: dB
			- Lower_Limit: float: float Tolerance value for too low maximum UE power Range: -5 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Nominal_Max_Power'),
			ArgStruct.scalar_float('Upper_Limit'),
			ArgStruct.scalar_float('Lower_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nominal_Max_Power: float = None
			self.Upper_Limit: float = None
			self.Lower_Limit: float = None

	def get_active(self) -> ActiveStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower:ACTive \n
		Snippet: value: ActiveStruct = driver.configure.tpc.limit.ilpControl.maxPower.get_active() \n
		Queries the active limit values for the 'Inner Loop Power Control' mode. These limit values result either from the
		configured UE power class or from the reported UE power class or have been defined manually. \n
			:return: structure: for return value, see the help for ActiveStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower:ACTive?', self.__class__.ActiveStruct())

	# noinspection PyTypeChecker
	class UserDefinedStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Nominal_Max_Power: float: numeric Nominal maximum output power of the UE Range: -50 dBm to 34 dBm, Unit: dBm
			- Upper_Limit: float: numeric Tolerance value for too high maximum UE power Range: 0 dB to 5 dB, Unit: dB
			- Lower_Limit: float: numeric Tolerance value for too low maximum UE power Range: -5 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Nominal_Max_Power'),
			ArgStruct.scalar_float('Upper_Limit'),
			ArgStruct.scalar_float('Lower_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nominal_Max_Power: float = None
			self.Upper_Limit: float = None
			self.Lower_Limit: float = None

	def get_user_defined(self) -> UserDefinedStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower:UDEFined \n
		Snippet: value: UserDefinedStruct = driver.configure.tpc.limit.ilpControl.maxPower.get_user_defined() \n
		Sets the user-defined maximum output power limits for the 'Inner Loop Power Control' mode. To activate the usage of this
		limit set, see method RsCmwWcdmaMeas.Configure.Tpc.Limit.IlpControl.MaxPower.value. \n
			:return: structure: for return value, see the help for UserDefinedStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower:UDEFined?', self.__class__.UserDefinedStruct())

	def set_user_defined(self, value: UserDefinedStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower:UDEFined \n
		Snippet: driver.configure.tpc.limit.ilpControl.maxPower.set_user_defined(value = UserDefinedStruct()) \n
		Sets the user-defined maximum output power limits for the 'Inner Loop Power Control' mode. To activate the usage of this
		limit set, see method RsCmwWcdmaMeas.Configure.Tpc.Limit.IlpControl.MaxPower.value. \n
			:param value: see the help for UserDefinedStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower:UDEFined', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Active_Limit: enums.ActiveLimit: USER | PC1 | PC2 | PC3 | PC3B | PC4 To use the limits defined by 3GPP, select the power class of the UE (PC1 to PC4 = power class 1, 2, 3, 3bis, 4) . To use the UE power class value reported by the UE in the capability report, see also [CMDLINK: CONFigure:WCDMa:MEASi:TPC:LIMit:ILPControl:MAXPower:URPClass CMDLINK]. For user-defined limit values, select USER and define the limits via [CMDLINK: CONFigure:WCDMa:MEASi:TPC:LIMit:ILPControl:MAXPower:UDEFined CMDLINK]."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Active_Limit', enums.ActiveLimit)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Active_Limit: enums.ActiveLimit = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower \n
		Snippet: value: ValueStruct = driver.configure.tpc.limit.ilpControl.maxPower.get_value() \n
		Enables or disables the check of the maximum UE output power limits for the 'Inner Loop Power Control' mode and selects
		the set of limit settings to be used. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MAXPower \n
		Snippet: driver.configure.tpc.limit.ilpControl.maxPower.set_value(value = ValueStruct()) \n
		Enables or disables the check of the maximum UE output power limits for the 'Inner Loop Power Control' mode and selects
		the set of limit settings to be used. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MAXPower', value)
