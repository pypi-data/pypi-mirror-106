from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IlpControl:
	"""IlpControl commands group definition. 8 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ilpControl", core, parent)

	@property
	def maxPower(self):
		"""maxPower commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_maxPower'):
			from .IlpControl_.MaxPower import MaxPower
			self._maxPower = MaxPower(self._core, self._base)
		return self._maxPower

	# noinspection PyTypeChecker
	class MinPowerStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Upper_Limit: float: numeric Range: -70 dBm to 34 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper_Limit: float = None

	def get_min_power(self) -> MinPowerStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MINPower \n
		Snippet: value: MinPowerStruct = driver.configure.tpc.limit.ilpControl.get_min_power() \n
		Defines an 'Inner Loop Power Control' limit: upper limit for the minimum UE output power. Also enables or disables the
		limit check. \n
			:return: structure: for return value, see the help for MinPowerStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MINPower?', self.__class__.MinPowerStruct())

	def set_min_power(self, value: MinPowerStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:MINPower \n
		Snippet: driver.configure.tpc.limit.ilpControl.set_min_power(value = MinPowerStruct()) \n
		Defines an 'Inner Loop Power Control' limit: upper limit for the minimum UE output power. Also enables or disables the
		limit check. \n
			:param value: see the help for MinPowerStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:MINPower', value)

	# noinspection PyTypeChecker
	class PstepStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Step_0_Db: float: numeric Limit for steps with expected step size 0 dB Range: 0 dB to 5 dB, Unit: dB
			- Step_1_Db: float: numeric Limit for steps with expected step size ±1 dB Range: 0 dB to 5 dB, Unit: dB
			- Step_2_Db: float: numeric Limit for steps with expected step size ±2 dB Range: 0 dB to 5 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Step_0_Db'),
			ArgStruct.scalar_float('Step_1_Db'),
			ArgStruct.scalar_float('Step_2_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Step_0_Db: float = None
			self.Step_1_Db: float = None
			self.Step_2_Db: float = None

	def get_pstep(self) -> PstepStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:PSTep \n
		Snippet: value: PstepStruct = driver.configure.tpc.limit.ilpControl.get_pstep() \n
		Defines 'Inner Loop Power Control' limits: upper limits for the absolute value of the power step error, depending on the
		expected step size. Also enables or disables the limit check. \n
			:return: structure: for return value, see the help for PstepStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:PSTep?', self.__class__.PstepStruct())

	def set_pstep(self, value: PstepStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:PSTep \n
		Snippet: driver.configure.tpc.limit.ilpControl.set_pstep(value = PstepStruct()) \n
		Defines 'Inner Loop Power Control' limits: upper limits for the absolute value of the power step error, depending on the
		expected step size. Also enables or disables the limit check. \n
			:param value: see the help for PstepStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:PSTep', value)

	# noinspection PyTypeChecker
	class EpStepStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON
			- Max_Count: int: numeric Maximum allowed exceptions for sections BC, EF and GH Range: 1 to 10
			- Step_1_Db: float: numeric Exceptional limit for step size 1 dB Range: 0 dB to 5 dB
			- Step_2_Db: float: numeric Exceptional limit for step size 2 dB Range: 0 dB to 5 dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Max_Count'),
			ArgStruct.scalar_float('Step_1_Db'),
			ArgStruct.scalar_float('Step_2_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Max_Count: int = None
			self.Step_1_Db: float = None
			self.Step_2_Db: float = None

	def get_ep_step(self) -> EpStepStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:EPSTep \n
		Snippet: value: EpStepStruct = driver.configure.tpc.limit.ilpControl.get_ep_step() \n
		Defines 'Inner Loop Power Control' limits for exceptions and enables or disables the limit check. \n
			:return: structure: for return value, see the help for EpStepStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:EPSTep?', self.__class__.EpStepStruct())

	def set_ep_step(self, value: EpStepStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:EPSTep \n
		Snippet: driver.configure.tpc.limit.ilpControl.set_ep_step(value = EpStepStruct()) \n
		Defines 'Inner Loop Power Control' limits for exceptions and enables or disables the limit check. \n
			:param value: see the help for EpStepStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:EPSTep', value)

	# noinspection PyTypeChecker
	class PsGroupStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Group_10_X_0_Db: float: numeric Limit for groups with expected step size 10 x 0 dB (algorithm 2) Range: 0 dB to 9 dB, Unit: dB
			- Group_10_X_1_Dba_Lg_2: float: numeric Limit for groups with expected step size 10 x ±1 dB + 40 x 0 dB (algorithm 2) Range: 0 dB to 9 dB, Unit: dB
			- Group_10_X_1_Db: float: numeric Limit for groups with expected step size 10 x ±1 dB (algorithm 1) Range: 0 dB to 9 dB, Unit: dB
			- Group_10_X_2_Db: float: numeric Limit for groups with expected step size 10 x ±2 dB (algorithm 1) Range: 0 dB to 9 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Group_10_X_0_Db'),
			ArgStruct.scalar_float('Group_10_X_1_Dba_Lg_2'),
			ArgStruct.scalar_float('Group_10_X_1_Db'),
			ArgStruct.scalar_float('Group_10_X_2_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Group_10_X_0_Db: float = None
			self.Group_10_X_1_Dba_Lg_2: float = None
			self.Group_10_X_1_Db: float = None
			self.Group_10_X_2_Db: float = None

	def get_ps_group(self) -> PsGroupStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:PSGRoup \n
		Snippet: value: PsGroupStruct = driver.configure.tpc.limit.ilpControl.get_ps_group() \n
		Defines 'Inner Loop Power Control' limits: upper limits for the absolute value of the power step group error, depending
		on the expected step size. Also enables or disables the limit check. \n
			:return: structure: for return value, see the help for PsGroupStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:PSGRoup?', self.__class__.PsGroupStruct())

	def set_ps_group(self, value: PsGroupStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:ILPControl:PSGRoup \n
		Snippet: driver.configure.tpc.limit.ilpControl.set_ps_group(value = PsGroupStruct()) \n
		Defines 'Inner Loop Power Control' limits: upper limits for the absolute value of the power step group error, depending
		on the expected step size. Also enables or disables the limit check. \n
			:param value: see the help for PsGroupStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:ILPControl:PSGRoup', value)

	def clone(self) -> 'IlpControl':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IlpControl(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
