from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emask:
	"""Emask commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("emask", core, parent)

	@property
	def dcarrier(self):
		"""dcarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcarrier'):
			from .Emask_.Dcarrier import Dcarrier
			self._dcarrier = Dcarrier(self._core, self._base)
		return self._dcarrier

	# noinspection PyTypeChecker
	class AbsoluteStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Limit_G_3_M_84: float or bool: numeric | ON | OFF Absolute limit line G referenced to a 3.84 MHz filter Range: -80 dBm to 33 dBm, Unit: dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Limit_H_1_Mhz: float or bool: numeric | ON | OFF Absolute limit line H referenced to a 1 MHz or 100 kHz filter, depending on the line H mode Range: -80 dBm to 33 dBm, Unit: dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Limit_H_30_Khz: float or bool: numeric | ON | OFF Absolute limit line H referenced to a 30 kHz filter Range: -80 dBm to 33 dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Limit_Hmode: enums.LimitHmode: A | B | C Line H mode"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Limit_G_3_M_84'),
			ArgStruct.scalar_float_ext('Limit_H_1_Mhz'),
			ArgStruct.scalar_float_ext('Limit_H_30_Khz'),
			ArgStruct.scalar_enum('Limit_Hmode', enums.LimitHmode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Limit_G_3_M_84: float or bool = None
			self.Limit_H_1_Mhz: float or bool = None
			self.Limit_H_30_Khz: float or bool = None
			self.Limit_Hmode: enums.LimitHmode = None

	def get_absolute(self) -> AbsoluteStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:ABSolute \n
		Snippet: value: AbsoluteStruct = driver.configure.multiEval.limit.emask.get_absolute() \n
		Defines absolute limits for the spectrum emission curves. \n
			:return: structure: for return value, see the help for AbsoluteStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:ABSolute?', self.__class__.AbsoluteStruct())

	def set_absolute(self, value: AbsoluteStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:ABSolute \n
		Snippet: driver.configure.multiEval.limit.emask.set_absolute(value = AbsoluteStruct()) \n
		Defines absolute limits for the spectrum emission curves. \n
			:param value: see the help for AbsoluteStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:ABSolute', value)

	# noinspection PyTypeChecker
	class RelativeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Point_A: float or bool: numeric | ON | OFF Range: -90 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Point_B: float or bool: numeric | ON | OFF Range: -90 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Point_C: float or bool: numeric | ON | OFF Range: -90 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Point_D: float or bool: numeric | ON | OFF Range: -90 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Point_E: float or bool: numeric | ON | OFF Range: -90 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Point_F: float or bool: numeric | ON | OFF Range: -90 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Point_A'),
			ArgStruct.scalar_float_ext('Point_B'),
			ArgStruct.scalar_float_ext('Point_C'),
			ArgStruct.scalar_float_ext('Point_D'),
			ArgStruct.scalar_float_ext('Point_E'),
			ArgStruct.scalar_float_ext('Point_F')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Point_A: float or bool = None
			self.Point_B: float or bool = None
			self.Point_C: float or bool = None
			self.Point_D: float or bool = None
			self.Point_E: float or bool = None
			self.Point_F: float or bool = None

	def get_relative(self) -> RelativeStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:RELative \n
		Snippet: value: RelativeStruct = driver.configure.multiEval.limit.emask.get_relative() \n
		Defines relative limits for the spectrum emission curves. \n
			:return: structure: for return value, see the help for RelativeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:RELative?', self.__class__.RelativeStruct())

	def set_relative(self, value: RelativeStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:RELative \n
		Snippet: driver.configure.multiEval.limit.emask.set_relative(value = RelativeStruct()) \n
		Defines relative limits for the spectrum emission curves. \n
			:param value: see the help for RelativeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:RELative', value)

	def clone(self) -> 'Emask':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emask(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
