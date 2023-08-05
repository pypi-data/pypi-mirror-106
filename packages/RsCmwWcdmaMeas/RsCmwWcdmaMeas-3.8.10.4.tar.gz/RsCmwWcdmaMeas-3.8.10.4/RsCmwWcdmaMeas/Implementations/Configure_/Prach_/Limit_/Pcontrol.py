from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcontrol:
	"""Pcontrol commands group definition. 7 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcontrol", core, parent)

	@property
	def maxPower(self):
		"""maxPower commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_maxPower'):
			from .Pcontrol_.MaxPower import MaxPower
			self._maxPower = MaxPower(self._core, self._base)
		return self._maxPower

	# noinspection PyTypeChecker
	class PstepStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Preamble_Pwr_Step: float: numeric Expected preamble power step size Range: 0 dB to 15 dB, Unit: dB
			- Pwr_Step_Limit: float: numeric Preamble power step tolerance value Range: 0 dB to 15 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Preamble_Pwr_Step'),
			ArgStruct.scalar_float('Pwr_Step_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Preamble_Pwr_Step: float = None
			self.Pwr_Step_Limit: float = None

	def get_pstep(self) -> PstepStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:PSTep \n
		Snippet: value: PstepStruct = driver.configure.prach.limit.pcontrol.get_pstep() \n
		Enables or disables the check of the preamble power step limits and specifies these limits. \n
			:return: structure: for return value, see the help for PstepStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:PSTep?', self.__class__.PstepStruct())

	def set_pstep(self, value: PstepStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:PSTep \n
		Snippet: driver.configure.prach.limit.pcontrol.set_pstep(value = PstepStruct()) \n
		Enables or disables the check of the preamble power step limits and specifies these limits. \n
			:param value: see the help for PstepStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:PSTep', value)

	# noinspection PyTypeChecker
	class OlPowerStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Disables | enables the limit check
			- Init_Preamble_Pwr: float: numeric Initial preamble power Range: -50 dBm to 34 dBm, Unit: dBm
			- Olp_Limit: float: numeric Open loop power tolerance value Range: 0 dB to 15 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Init_Preamble_Pwr'),
			ArgStruct.scalar_float('Olp_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Init_Preamble_Pwr: float = None
			self.Olp_Limit: float = None

	def get_ol_power(self) -> OlPowerStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:OLPower \n
		Snippet: value: OlPowerStruct = driver.configure.prach.limit.pcontrol.get_ol_power() \n
		Enables or disables the check of the open loop power limits and specifies these limits. \n
			:return: structure: for return value, see the help for OlPowerStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:OLPower?', self.__class__.OlPowerStruct())

	def set_ol_power(self, value: OlPowerStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:OLPower \n
		Snippet: driver.configure.prach.limit.pcontrol.set_ol_power(value = OlPowerStruct()) \n
		Enables or disables the check of the open loop power limits and specifies these limits. \n
			:param value: see the help for OlPowerStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:OLPower', value)

	def get_off_power(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:OFFPower \n
		Snippet: value: float or bool = driver.configure.prach.limit.pcontrol.get_off_power() \n
		Defines an upper OFF power limit. Also enables or disables the limit check. \n
			:return: limit: numeric | ON | OFF Range: -90 dBm to 53 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:OFFPower?')
		return Conversions.str_to_float_or_bool(response)

	def set_off_power(self, limit: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:PRACh:LIMit:PCONtrol:OFFPower \n
		Snippet: driver.configure.prach.limit.pcontrol.set_off_power(limit = 1.0) \n
		Defines an upper OFF power limit. Also enables or disables the limit check. \n
			:param limit: numeric | ON | OFF Range: -90 dBm to 53 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:PRACh:LIMit:PCONtrol:OFFPower {param}')

	def clone(self) -> 'Pcontrol':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcontrol(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
