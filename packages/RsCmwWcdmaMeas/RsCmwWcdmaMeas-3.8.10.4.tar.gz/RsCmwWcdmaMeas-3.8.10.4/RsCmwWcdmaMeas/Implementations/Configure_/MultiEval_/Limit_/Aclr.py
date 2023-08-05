from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aclr:
	"""Aclr commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aclr", core, parent)

	# noinspection PyTypeChecker
	class RelativeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Channel_First: float or bool: numeric | ON | OFF For single uplink carrier: ±5 MHz from the center frequency For dual uplink carrier: ±7.5 MHz from the center frequency of both carriers Range: -80 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Channel_Second: float or bool: numeric | ON | OFF For single uplink carrier: ±10 MHz from the center frequency For dual uplink carrier: ±12.5 MHz from the center frequency of both carriers Range: -80 dB to 0 dB, Unit: dB Additional OFF | ON disables/enables the limit check using the previous/default limit values"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Channel_First'),
			ArgStruct.scalar_float_ext('Channel_Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Channel_First: float or bool = None
			self.Channel_Second: float or bool = None

	def get_relative(self) -> RelativeStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:ACLR:RELative \n
		Snippet: value: RelativeStruct = driver.configure.multiEval.limit.aclr.get_relative() \n
		Defines upper limits for the ACLR in channels one and two relative to the carrier power. Relative limits are only
		evaluated when the absolute limit is exceeded (method RsCmwWcdmaMeas.Configure.MultiEval.Limit.Aclr.absolute) . \n
			:return: structure: for return value, see the help for RelativeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:ACLR:RELative?', self.__class__.RelativeStruct())

	def set_relative(self, value: RelativeStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:ACLR:RELative \n
		Snippet: driver.configure.multiEval.limit.aclr.set_relative(value = RelativeStruct()) \n
		Defines upper limits for the ACLR in channels one and two relative to the carrier power. Relative limits are only
		evaluated when the absolute limit is exceeded (method RsCmwWcdmaMeas.Configure.MultiEval.Limit.Aclr.absolute) . \n
			:param value: see the help for RelativeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:ACLR:RELative', value)

	def get_absolute(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:ACLR:ABSolute \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.aclr.get_absolute() \n
		Defines an absolute upper limit for the ACLR. If the absolute upper limit is exceeded, relative limits are evaluated
		(method RsCmwWcdmaMeas.Configure.MultiEval.Limit.Aclr.relative) . \n
			:return: limit_3_m_84: numeric | ON | OFF Range: -80 dBm to 33 dBm, Unit: dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:ACLR:ABSolute?')
		return Conversions.str_to_float_or_bool(response)

	def set_absolute(self, limit_3_m_84: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:ACLR:ABSolute \n
		Snippet: driver.configure.multiEval.limit.aclr.set_absolute(limit_3_m_84 = 1.0) \n
		Defines an absolute upper limit for the ACLR. If the absolute upper limit is exceeded, relative limits are evaluated
		(method RsCmwWcdmaMeas.Configure.MultiEval.Limit.Aclr.relative) . \n
			:param limit_3_m_84: numeric | ON | OFF Range: -80 dBm to 33 dBm, Unit: dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit_3_m_84)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:ACLR:ABSolute {param}')
