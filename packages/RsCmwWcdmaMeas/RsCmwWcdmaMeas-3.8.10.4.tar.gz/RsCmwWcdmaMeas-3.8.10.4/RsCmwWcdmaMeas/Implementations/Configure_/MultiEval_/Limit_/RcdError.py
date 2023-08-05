from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RcdError:
	"""RcdError commands group definition. 8 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rcdError", core, parent)

	@property
	def eecdp(self):
		"""eecdp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eecdp'):
			from .RcdError_.Eecdp import Eecdp
			self._eecdp = Eecdp(self._core, self._base)
		return self._eecdp

	# noinspection PyTypeChecker
	class EcdpStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Threshold_Bpsk_1: float: numeric Lower ECDP threshold for BPSK requirement 1 Range: -50 dB to 0 dB, Unit: dB
			- Threshold_Bpsk_2: float: numeric Lower ECDP threshold for BPSK requirement 2 Range: -50 dB to 0 dB, Unit: dB
			- Limit_Bpsk_1: float: numeric RCDE limit for BPSK requirement 1 Range: -50 dB to 0 dB, Unit: dB
			- Limit_Bpks_2: float: numeric RCDE limit for BPSK requirement 2 (limit = this value minus ECDP) Range: -50 dB to 0 dB, Unit: dB
			- Threshold_4_Pam_1: float: numeric Lower ECDP threshold for 4PAM requirement 1 Range: -50 dB to 0 dB, Unit: dB
			- Threshold_4_Pam_2: float: numeric Lower ECDP threshold for 4PAM requirement 2 Range: -50 dB to 0 dB, Unit: dB
			- Limit_4_Pam_1: float: numeric RCDE limit for 4PAM requirement 1 Range: -50 dB to 0 dB, Unit: dB
			- Limit_4_Pam_2: float: numeric RCDE limit for 4PAM requirement 2 (limit = this value minus ECDP) Range: -50 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Threshold_Bpsk_1'),
			ArgStruct.scalar_float('Threshold_Bpsk_2'),
			ArgStruct.scalar_float('Limit_Bpsk_1'),
			ArgStruct.scalar_float('Limit_Bpks_2'),
			ArgStruct.scalar_float('Threshold_4_Pam_1'),
			ArgStruct.scalar_float('Threshold_4_Pam_2'),
			ArgStruct.scalar_float('Limit_4_Pam_1'),
			ArgStruct.scalar_float('Limit_4_Pam_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Threshold_Bpsk_1: float = None
			self.Threshold_Bpsk_2: float = None
			self.Limit_Bpsk_1: float = None
			self.Limit_Bpks_2: float = None
			self.Threshold_4_Pam_1: float = None
			self.Threshold_4_Pam_2: float = None
			self.Limit_4_Pam_1: float = None
			self.Limit_4_Pam_2: float = None

	def get_ecdp(self) -> EcdpStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:ECDP \n
		Snippet: value: EcdpStruct = driver.configure.multiEval.limit.rcdError.get_ecdp() \n
		Defines upper limits for the relative CDE (RCDE) of BPSK and 4PAM modulated channels. For each modulation type, two
		requirements are defined. \n
			:return: structure: for return value, see the help for EcdpStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:ECDP?', self.__class__.EcdpStruct())

	def set_ecdp(self, value: EcdpStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:RCDerror:ECDP \n
		Snippet: driver.configure.multiEval.limit.rcdError.set_ecdp(value = EcdpStruct()) \n
		Defines upper limits for the relative CDE (RCDE) of BPSK and 4PAM modulated channels. For each modulation type, two
		requirements are defined. \n
			:param value: see the help for EcdpStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:RCDerror:ECDP', value)

	def clone(self) -> 'RcdError':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RcdError(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
