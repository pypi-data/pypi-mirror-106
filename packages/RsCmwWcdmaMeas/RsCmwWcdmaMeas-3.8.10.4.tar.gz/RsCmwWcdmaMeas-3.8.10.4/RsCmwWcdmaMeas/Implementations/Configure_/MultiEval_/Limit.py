from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 23 total commands, 4 Sub-groups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def rcdError(self):
		"""rcdError commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcdError'):
			from .Limit_.RcdError import RcdError
			self._rcdError = RcdError(self._core, self._base)
		return self._rcdError

	@property
	def pcontrol(self):
		"""pcontrol commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pcontrol'):
			from .Limit_.Pcontrol import Pcontrol
			self._pcontrol = Pcontrol(self._core, self._base)
		return self._pcontrol

	@property
	def emask(self):
		"""emask commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_emask'):
			from .Limit_.Emask import Emask
			self._emask = Emask(self._core, self._base)
		return self._emask

	@property
	def aclr(self):
		"""aclr commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_aclr'):
			from .Limit_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	# noinspection PyTypeChecker
	class PhsDpcchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Measure_Point_A: float: numeric Range: 0.5 slots to 119.5 slots, Unit: slot
			- Measure_Point_B: float: numeric Range: 0.5 slots to 119.5 slots, Unit: slot
			- Dynamic: float: numeric Range: 0 deg to 90 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Measure_Point_A'),
			ArgStruct.scalar_float('Measure_Point_B'),
			ArgStruct.scalar_float('Dynamic')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Measure_Point_A: float = None
			self.Measure_Point_B: float = None
			self.Dynamic: float = None

	def get_phs_dpcch(self) -> PhsDpcchStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PHSDpcch \n
		Snippet: value: PhsDpcchStruct = driver.configure.multiEval.limit.get_phs_dpcch() \n
		Defines a dynamic limit for the phase discontinuity determined by half-slot measurements (signals with HS-DPCCH) .
		The limit is checked at point A and point B. As the phase discontinuity is measured at half-slot boundaries (x.5, not x.
		0) points A and B have to be set to half-slot positions. \n
			:return: structure: for return value, see the help for PhsDpcchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PHSDpcch?', self.__class__.PhsDpcchStruct())

	def set_phs_dpcch(self, value: PhsDpcchStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PHSDpcch \n
		Snippet: driver.configure.multiEval.limit.set_phs_dpcch(value = PhsDpcchStruct()) \n
		Defines a dynamic limit for the phase discontinuity determined by half-slot measurements (signals with HS-DPCCH) .
		The limit is checked at point A and point B. As the phase discontinuity is measured at half-slot boundaries (x.5, not x.
		0) points A and B have to be set to half-slot positions. \n
			:param value: see the help for PhsDpcchStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PHSDpcch', value)

	# noinspection PyTypeChecker
	class PhdStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Upper: float: numeric Range: 0 deg to 90 deg, Unit: deg
			- Dynamic: float: numeric Range: 0 deg to 90 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Upper'),
			ArgStruct.scalar_float('Dynamic')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Upper: float = None
			self.Dynamic: float = None

	def get_phd(self) -> PhdStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PHD \n
		Snippet: value: PhdStruct = driver.configure.multiEval.limit.get_phd() \n
		Defines upper and dynamic limits for the phase discontinuity determined by full-slot measurements (signals without HSPA
		channels) . \n
			:return: structure: for return value, see the help for PhdStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PHD?', self.__class__.PhdStruct())

	def set_phd(self, value: PhdStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PHD \n
		Snippet: driver.configure.multiEval.limit.set_phd(value = PhdStruct()) \n
		Defines upper and dynamic limits for the phase discontinuity determined by full-slot measurements (signals without HSPA
		channels) . \n
			:param value: see the help for PhdStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PHD', value)

	# noinspection PyTypeChecker
	class EvMagnitudeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: numeric | ON | OFF Range: 0 % to 100 %, Unit: % Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Peak: float or bool: numeric | ON | OFF Range: 0 % to 99 %, Unit: % Additional OFF | ON disables/enables the limit check using the previous/default limit values"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_ev_magnitude(self) -> EvMagnitudeStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.multiEval.limit.get_ev_magnitude() \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) . \n
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EVMagnitude?', self.__class__.EvMagnitudeStruct())

	def set_ev_magnitude(self, value: EvMagnitudeStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EVMagnitude \n
		Snippet: driver.configure.multiEval.limit.set_ev_magnitude(value = EvMagnitudeStruct()) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) . \n
			:param value: see the help for EvMagnitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EVMagnitude', value)

	# noinspection PyTypeChecker
	class MerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: numeric | ON | OFF Range: 0 % to 100 %, Unit: % Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Peak: float or bool: numeric | ON | OFF Range: 0 % to 99 %, Unit: % Additional OFF | ON disables/enables the limit check using the previous/default limit values"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_merror(self) -> MerrorStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.multiEval.limit.get_merror() \n
		Defines upper limits for the RMS and peak values of the magnitude error. \n
			:return: structure: for return value, see the help for MerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:MERRor?', self.__class__.MerrorStruct())

	def set_merror(self, value: MerrorStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:MERRor \n
		Snippet: driver.configure.multiEval.limit.set_merror(value = MerrorStruct()) \n
		Defines upper limits for the RMS and peak values of the magnitude error. \n
			:param value: see the help for MerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:MERRor', value)

	# noinspection PyTypeChecker
	class PerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: numeric | ON | OFF Range: 0 deg to 45 deg, Unit: deg Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Peak: float or bool: numeric | ON | OFF Range: 0 deg to 45 deg, Unit: deg Additional OFF | ON disables/enables the limit check using the previous/default limit values"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_perror(self) -> PerrorStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.multiEval.limit.get_perror() \n
		Defines symmetric limits for the RMS and peak values of the phase error. The limit check fails if the absolute value of
		the measured phase error exceeds the specified values. \n
			:return: structure: for return value, see the help for PerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PERRor?', self.__class__.PerrorStruct())

	def set_perror(self, value: PerrorStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:PERRor \n
		Snippet: driver.configure.multiEval.limit.set_perror(value = PerrorStruct()) \n
		Defines symmetric limits for the RMS and peak values of the phase error. The limit check fails if the absolute value of
		the measured phase error exceeds the specified values. \n
			:param value: see the help for PerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:PERRor', value)

	def get_iq_offset(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:IQOFfset \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_iq_offset() \n
		Defines an upper limit for the I/Q origin offset. \n
			:return: iq_offset: numeric | ON | OFF Range: -80 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:IQOFfset?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_offset(self, iq_offset: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.set_iq_offset(iq_offset = 1.0) \n
		Defines an upper limit for the I/Q origin offset. \n
			:param iq_offset: numeric | ON | OFF Range: -80 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_offset)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:IQOFfset {param}')

	def get_iq_imbalance(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:IQIMbalance \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_iq_imbalance() \n
		Defines an upper limit for the I/Q imbalance. \n
			:return: iq_imbalance: numeric | ON | OFF Range: -99 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_imbalance(self, iq_imbalance: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:IQIMbalance \n
		Snippet: driver.configure.multiEval.limit.set_iq_imbalance(iq_imbalance = 1.0) \n
		Defines an upper limit for the I/Q imbalance. \n
			:param iq_imbalance: numeric | ON | OFF Range: -99 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_imbalance)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:CFERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cf_error() \n
		Defines an upper limit for the carrier frequency error. \n
			:return: frequency_error: numeric | ON | OFF Range: 0 Hz to 4000 Hz, Unit: Hz Additional OFF | ON disables/enables the limit check using the previous/default limit values
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, frequency_error: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:CFERror \n
		Snippet: driver.configure.multiEval.limit.set_cf_error(frequency_error = 1.0) \n
		Defines an upper limit for the carrier frequency error. \n
			:param frequency_error: numeric | ON | OFF Range: 0 Hz to 4000 Hz, Unit: Hz Additional OFF | ON disables/enables the limit check using the previous/default limit values
		"""
		param = Conversions.decimal_or_bool_value_to_str(frequency_error)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:CFERror {param}')

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
