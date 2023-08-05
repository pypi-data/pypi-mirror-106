from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 13 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def ilpControl(self):
		"""ilpControl commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_ilpControl'):
			from .Limit_.IlpControl import IlpControl
			self._ilpControl = IlpControl(self._core, self._base)
		return self._ilpControl

	@property
	def ulcm(self):
		"""ulcm commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ulcm'):
			from .Limit_.Ulcm import Ulcm
			self._ulcm = Ulcm(self._core, self._base)
		return self._ulcm

	# noinspection PyTypeChecker
	class MpedchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Nom_Max_Power: float: numeric Nominal maximum UE power Range: -47 dBm to 34 dBm, Unit: dBm
			- Upper_Limit: float: numeric Upper limit = nominal power + this value Range: 0 dB to 10 dB, Unit: dB
			- Lower_Limit: float: numeric Lower limit = nominal power + this value Range: -10 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Nom_Max_Power'),
			ArgStruct.scalar_float('Upper_Limit'),
			ArgStruct.scalar_float('Lower_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Nom_Max_Power: float = None
			self.Upper_Limit: float = None
			self.Lower_Limit: float = None

	def get_mpedch(self) -> MpedchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:MPEDch \n
		Snippet: value: MpedchStruct = driver.configure.tpc.limit.get_mpedch() \n
		Configures UE power limits for the measurement mode 'Max. Power E-DCH'. \n
			:return: structure: for return value, see the help for MpedchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:MPEDch?', self.__class__.MpedchStruct())

	def set_mpedch(self, value: MpedchStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:MPEDch \n
		Snippet: driver.configure.tpc.limit.set_mpedch(value = MpedchStruct()) \n
		Configures UE power limits for the measurement mode 'Max. Power E-DCH'. \n
			:param value: see the help for MpedchStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:MPEDch', value)

	# noinspection PyTypeChecker
	class CtfcStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Power_Step_Limit: float: numeric Symmetrical tolerance value for the power step size Range: 0 dB to 10 dB, Unit: dB
			- Calc_Beta_Factors: bool: OFF | ON Enables or disables the automatic calculation of the expected power step size from the configured beta factors
			- Power_Step_Size: float: numeric Expected power step size applicable if the automatic calculation from beta factors is disabled Range: 0 dB to 24 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Power_Step_Limit'),
			ArgStruct.scalar_bool('Calc_Beta_Factors'),
			ArgStruct.scalar_float('Power_Step_Size')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Power_Step_Limit: float = None
			self.Calc_Beta_Factors: bool = None
			self.Power_Step_Size: float = None

	def get_ctfc(self) -> CtfcStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:CTFC \n
		Snippet: value: CtfcStruct = driver.configure.tpc.limit.get_ctfc() \n
		Configures a power step limit for the measurement mode 'Change of TFC'. \n
			:return: structure: for return value, see the help for CtfcStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:CTFC?', self.__class__.CtfcStruct())

	def set_ctfc(self, value: CtfcStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:CTFC \n
		Snippet: driver.configure.tpc.limit.set_ctfc(value = CtfcStruct()) \n
		Configures a power step limit for the measurement mode 'Change of TFC'. \n
			:param value: see the help for CtfcStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:CTFC', value)

	def get_dhib(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:DHIB \n
		Snippet: value: float = driver.configure.tpc.limit.get_dhib() \n
		Defines a 'DC HSPA In-Band Emission' limit: upper limit for the ratio of the UE output power in one carrier to the UE
		output power in the other carrier. \n
			:return: min_power: numeric Range: -80 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:DHIB?')
		return Conversions.str_to_float(response)

	def set_dhib(self, min_power: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:LIMit:DHIB \n
		Snippet: driver.configure.tpc.limit.set_dhib(min_power = 1.0) \n
		Defines a 'DC HSPA In-Band Emission' limit: upper limit for the ratio of the UE output power in one carrier to the UE
		output power in the other carrier. \n
			:param min_power: numeric Range: -80 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(min_power)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:LIMit:DHIB {param}')

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
