from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 20 total commands, 1 Sub-groups, 17 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("result", core, parent)

	@property
	def chip(self):
		"""chip commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_chip'):
			from .Result_.Chip import Chip
			self._chip = Chip(self._core, self._base)
		return self._chip

	def get_txm(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:TXM \n
		Snippet: value: bool = driver.configure.multiEval.result.get_txm() \n
		No command help available \n
			:return: enable_txm: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:TXM?')
		return Conversions.str_to_bool(response)

	def set_txm(self, enable_txm: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:TXM \n
		Snippet: driver.configure.multiEval.result.set_txm(enable_txm = False) \n
		No command help available \n
			:param enable_txm: No help available
		"""
		param = Conversions.bool_to_str(enable_txm)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:TXM {param}')

	def get_rcd_error(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:RCDerror \n
		Snippet: value: bool = driver.configure.multiEval.result.get_rcd_error() \n
		Enables or disables the evaluation of results and shows or hides the relative CDE view in the multi-evaluation
		measurement. \n
			:return: enable_rcde: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:RCDerror?')
		return Conversions.str_to_bool(response)

	def set_rcd_error(self, enable_rcde: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:RCDerror \n
		Snippet: driver.configure.multiEval.result.set_rcd_error(enable_rcde = False) \n
		Enables or disables the evaluation of results and shows or hides the relative CDE view in the multi-evaluation
		measurement. \n
			:param enable_rcde: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_rcde)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:RCDerror {param}')

	def get_iq(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:IQ \n
		Snippet: value: bool = driver.configure.multiEval.result.get_iq() \n
		Enables or disables the evaluation of results and shows or hides the I/Q constellation diagram view in the
		multi-evaluation measurement. \n
			:return: enable_iq: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:IQ?')
		return Conversions.str_to_bool(response)

	def set_iq(self, enable_iq: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:IQ \n
		Snippet: driver.configure.multiEval.result.set_iq(enable_iq = False) \n
		Enables or disables the evaluation of results and shows or hides the I/Q constellation diagram view in the
		multi-evaluation measurement. \n
			:param enable_iq: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_iq)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:IQ {param}')

	def get_ber(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:BER \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ber() \n
		Enables or disables the evaluation of results and shows or hides the bit error rate view in the multi-evaluation
		measurement. \n
			:return: enable_ber: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:BER?')
		return Conversions.str_to_bool(response)

	def set_ber(self, enable_ber: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:BER \n
		Snippet: driver.configure.multiEval.result.set_ber(enable_ber = False) \n
		Enables or disables the evaluation of results and shows or hides the bit error rate view in the multi-evaluation
		measurement. \n
			:param enable_ber: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_ber)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:BER {param}')

	def get_psteps(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PSTeps \n
		Snippet: value: bool = driver.configure.multiEval.result.get_psteps() \n
		Enables or disables the evaluation of results and shows or hides the power steps view in the multi-evaluation measurement. \n
			:return: enable_pow_steps: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PSTeps?')
		return Conversions.str_to_bool(response)

	def set_psteps(self, enable_pow_steps: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PSTeps \n
		Snippet: driver.configure.multiEval.result.set_psteps(enable_pow_steps = False) \n
		Enables or disables the evaluation of results and shows or hides the power steps view in the multi-evaluation measurement. \n
			:param enable_pow_steps: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_pow_steps)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PSTeps {param}')

	def get_phd(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PHD \n
		Snippet: value: bool = driver.configure.multiEval.result.get_phd() \n
		Enables or disables the evaluation of results and shows or hides the phase discontinuity view in the multi-evaluation
		measurement. \n
			:return: enable_phase_disc: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PHD?')
		return Conversions.str_to_bool(response)

	def set_phd(self, enable_phase_disc: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PHD \n
		Snippet: driver.configure.multiEval.result.set_phd(enable_phase_disc = False) \n
		Enables or disables the evaluation of results and shows or hides the phase discontinuity view in the multi-evaluation
		measurement. \n
			:param enable_phase_disc: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_phase_disc)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PHD {param}')

	def get_freq_error(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:FERRor \n
		Snippet: value: bool = driver.configure.multiEval.result.get_freq_error() \n
		Enables or disables the evaluation of results and shows or hides the frequency error view in the multi-evaluation
		measurement. \n
			:return: enable_freq_error: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:FERRor?')
		return Conversions.str_to_bool(response)

	def set_freq_error(self, enable_freq_error: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:FERRor \n
		Snippet: driver.configure.multiEval.result.set_freq_error(enable_freq_error = False) \n
		Enables or disables the evaluation of results and shows or hides the frequency error view in the multi-evaluation
		measurement. \n
			:param enable_freq_error: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_freq_error)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:FERRor {param}')

	def get_ue_power(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:UEPower \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ue_power() \n
		Enables or disables the evaluation of results and shows or hides the UE power view in the multi-evaluation measurement. \n
			:return: enable_ue_power: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:UEPower?')
		return Conversions.str_to_bool(response)

	def set_ue_power(self, enable_ue_power: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:UEPower \n
		Snippet: driver.configure.multiEval.result.set_ue_power(enable_ue_power = False) \n
		Enables or disables the evaluation of results and shows or hides the UE power view in the multi-evaluation measurement. \n
			:param enable_ue_power: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_ue_power)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:UEPower {param}')

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable_Evm: bool: OFF | ON Error vector magnitude OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
			- Enable_Mag_Error: bool: OFF | ON Magnitude error
			- Enable_Phase_Err: bool: OFF | ON Phase error
			- Enable_Aclr: bool: OFF | ON Adjacent channel leakage power ratio
			- Enable_Emask: bool: OFF | ON Spectrum emission mask
			- Enable_Cd_Monitor: bool: OFF | ON Code domain monitor
			- Enable_Cdp: bool: OFF | ON Code domain power
			- Enable_Cde: bool: OFF | ON Code domain error
			- Enable_Evm_Chip: bool: OFF | ON EVM vs. chip
			- Enable_Merr_Chip: bool: OFF | ON Magnitude error vs. chip
			- Enable_Ph_Err_Chip: bool: OFF | ON Phase error vs. chip
			- Enable_Ue_Power: bool: OFF | ON UE power
			- Enable_Freq_Error: bool: OFF | ON Frequency error
			- Enable_Phase_Disc: bool: OFF | ON Phase discontinuity
			- Enable_Pow_Steps: bool: OFF | ON Power steps
			- Enable_Ber: bool: OFF | ON Bit error rate
			- Enable_Iq: bool: OFF | ON I/Q constellation diagram
			- Enable_Rcde: bool: OFF | ON Relative CDE
			- Enable_Txm: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Evm'),
			ArgStruct.scalar_bool('Enable_Mag_Error'),
			ArgStruct.scalar_bool('Enable_Phase_Err'),
			ArgStruct.scalar_bool('Enable_Aclr'),
			ArgStruct.scalar_bool('Enable_Emask'),
			ArgStruct.scalar_bool('Enable_Cd_Monitor'),
			ArgStruct.scalar_bool('Enable_Cdp'),
			ArgStruct.scalar_bool('Enable_Cde'),
			ArgStruct.scalar_bool('Enable_Evm_Chip'),
			ArgStruct.scalar_bool('Enable_Merr_Chip'),
			ArgStruct.scalar_bool('Enable_Ph_Err_Chip'),
			ArgStruct.scalar_bool('Enable_Ue_Power'),
			ArgStruct.scalar_bool('Enable_Freq_Error'),
			ArgStruct.scalar_bool('Enable_Phase_Disc'),
			ArgStruct.scalar_bool('Enable_Pow_Steps'),
			ArgStruct.scalar_bool('Enable_Ber'),
			ArgStruct.scalar_bool('Enable_Iq'),
			ArgStruct.scalar_bool('Enable_Rcde'),
			ArgStruct.scalar_bool('Enable_Txm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Evm: bool = None
			self.Enable_Mag_Error: bool = None
			self.Enable_Phase_Err: bool = None
			self.Enable_Aclr: bool = None
			self.Enable_Emask: bool = None
			self.Enable_Cd_Monitor: bool = None
			self.Enable_Cdp: bool = None
			self.Enable_Cde: bool = None
			self.Enable_Evm_Chip: bool = None
			self.Enable_Merr_Chip: bool = None
			self.Enable_Ph_Err_Chip: bool = None
			self.Enable_Ue_Power: bool = None
			self.Enable_Freq_Error: bool = None
			self.Enable_Phase_Disc: bool = None
			self.Enable_Pow_Steps: bool = None
			self.Enable_Ber: bool = None
			self.Enable_Iq: bool = None
			self.Enable_Rcde: bool = None
			self.Enable_Txm: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.multiEval.result.get_all() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		This command combines all other CONFigure:WCDMa:MEAS<i>:MEValuation:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult[:ALL] \n
		Snippet: driver.configure.multiEval.result.set_all(value = AllStruct()) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		This command combines all other CONFigure:WCDMa:MEAS<i>:MEValuation:RESult... commands. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:ALL', value)

	def get_cd_error(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDERror \n
		Snippet: value: bool = driver.configure.multiEval.result.get_cd_error() \n
		Enables or disables the evaluation of results and shows or hides the code domain error view in the multi-evaluation
		measurement. \n
			:return: enable_cde: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDERror?')
		return Conversions.str_to_bool(response)

	def set_cd_error(self, enable_cde: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDERror \n
		Snippet: driver.configure.multiEval.result.set_cd_error(enable_cde = False) \n
		Enables or disables the evaluation of results and shows or hides the code domain error view in the multi-evaluation
		measurement. \n
			:param enable_cde: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_cde)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDERror {param}')

	def get_cd_power(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDPower \n
		Snippet: value: bool = driver.configure.multiEval.result.get_cd_power() \n
		Enables or disables the evaluation of results and shows or hides the code domain power view in the multi-evaluation
		measurement. \n
			:return: enable_cdp: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDPower?')
		return Conversions.str_to_bool(response)

	def set_cd_power(self, enable_cdp: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDPower \n
		Snippet: driver.configure.multiEval.result.set_cd_power(enable_cdp = False) \n
		Enables or disables the evaluation of results and shows or hides the code domain power view in the multi-evaluation
		measurement. \n
			:param enable_cdp: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_cdp)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDPower {param}')

	def get_cdp_monitor(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDPMonitor \n
		Snippet: value: bool = driver.configure.multiEval.result.get_cdp_monitor() \n
		Enables or disables the evaluation of results and shows or hides the code domain monitor view in the multi-evaluation
		measurement. \n
			:return: enable_cd_monitor: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDPMonitor?')
		return Conversions.str_to_bool(response)

	def set_cdp_monitor(self, enable_cd_monitor: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:CDPMonitor \n
		Snippet: driver.configure.multiEval.result.set_cdp_monitor(enable_cd_monitor = False) \n
		Enables or disables the evaluation of results and shows or hides the code domain monitor view in the multi-evaluation
		measurement. \n
			:param enable_cd_monitor: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_cd_monitor)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:CDPMonitor {param}')

	def get_emask(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:EMASk \n
		Snippet: value: bool = driver.configure.multiEval.result.get_emask() \n
		Enables or disables the evaluation of results and shows or hides the spectrum emission mask view in the multi-evaluation
		measurement. \n
			:return: enable_emask: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:EMASk?')
		return Conversions.str_to_bool(response)

	def set_emask(self, enable_emask: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:EMASk \n
		Snippet: driver.configure.multiEval.result.set_emask(enable_emask = False) \n
		Enables or disables the evaluation of results and shows or hides the spectrum emission mask view in the multi-evaluation
		measurement. \n
			:param enable_emask: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_emask)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:EMASk {param}')

	def get_aclr(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:ACLR \n
		Snippet: value: bool = driver.configure.multiEval.result.get_aclr() \n
		Enables or disables the evaluation of results and shows or hides the adjacent channel leakage power ratio view in the
		multi-evaluation measurement. \n
			:return: enable_aclr: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:ACLR?')
		return Conversions.str_to_bool(response)

	def set_aclr(self, enable_aclr: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:ACLR \n
		Snippet: driver.configure.multiEval.result.set_aclr(enable_aclr = False) \n
		Enables or disables the evaluation of results and shows or hides the adjacent channel leakage power ratio view in the
		multi-evaluation measurement. \n
			:param enable_aclr: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_aclr)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:ACLR {param}')

	def get_perror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PERRor \n
		Snippet: value: bool = driver.configure.multiEval.result.get_perror() \n
		Enables or disables the evaluation of results and shows or hides the phase error view in the multi-evaluation measurement. \n
			:return: enable_phase_err: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PERRor?')
		return Conversions.str_to_bool(response)

	def set_perror(self, enable_phase_err: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:PERRor \n
		Snippet: driver.configure.multiEval.result.set_perror(enable_phase_err = False) \n
		Enables or disables the evaluation of results and shows or hides the phase error view in the multi-evaluation measurement. \n
			:param enable_phase_err: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_phase_err)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:PERRor {param}')

	def get_ev_magnitude(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ev_magnitude() \n
		Enables or disables the evaluation of results and shows or hides the error vector magnitude view in the multi-evaluation
		measurement. \n
			:return: enable_evm: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:EVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_ev_magnitude(self, enable_evm: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: driver.configure.multiEval.result.set_ev_magnitude(enable_evm = False) \n
		Enables or disables the evaluation of results and shows or hides the error vector magnitude view in the multi-evaluation
		measurement. \n
			:param enable_evm: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_evm)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:EVMagnitude {param}')

	def get_merror(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:MERRor \n
		Snippet: value: bool = driver.configure.multiEval.result.get_merror() \n
		Enables or disables the evaluation of results and shows or hides the magnitude error view in the multi-evaluation
		measurement. \n
			:return: enable_mag_error: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:MERRor?')
		return Conversions.str_to_bool(response)

	def set_merror(self, enable_mag_error: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:RESult:MERRor \n
		Snippet: driver.configure.multiEval.result.set_merror(enable_mag_error = False) \n
		Enables or disables the evaluation of results and shows or hides the magnitude error view in the multi-evaluation
		measurement. \n
			:param enable_mag_error: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable_mag_error)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:RESult:MERRor {param}')

	def clone(self) -> 'Result':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Result(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
