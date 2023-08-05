from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Evm_Rms: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: float: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: float: float Magnitude error peak value Range: -100 % to 100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Phase_Error_Rms: float: No parameter help available
			- Phase_Error_Peak: float: No parameter help available
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Carrier_Freq_Err: float: No parameter help available
			- Transmit_Time_Err: float: No parameter help available
			- Ue_Power: float: float User equipment power Range: -100 dBm to 55 dBm, Unit: dBm
			- Power_Steps: float: float User equipment power step Range: -50 dB to 50 dB, Unit: dB
			- Phase_Disc: enums.ResultStatus2: float Phase discontinuity Range: -180 deg to 180 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Mag_Error_Rms'),
			ArgStruct.scalar_float('Mag_Error_Peak'),
			ArgStruct.scalar_float('Phase_Error_Rms'),
			ArgStruct.scalar_float('Phase_Error_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Carrier_Freq_Err'),
			ArgStruct.scalar_float('Transmit_Time_Err'),
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Power_Steps'),
			ArgStruct.scalar_enum('Phase_Disc', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Mag_Error_Rms: float = None
			self.Mag_Error_Peak: float = None
			self.Phase_Error_Rms: float = None
			self.Phase_Error_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Carrier_Freq_Err: float = None
			self.Transmit_Time_Err: float = None
			self.Ue_Power: float = None
			self.Power_Steps: float = None
			self.Phase_Disc: enums.ResultStatus2 = None

	def calculate(self, carrier=repcap.Carrier.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:MODulation:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.carrier.modulation.average.calculate(carrier = repcap.Carrier.Default) \n
		Return the current, average, maximum and standard deviation single value results. The return values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each of the
		first 14 results listed below. The TX time alignment is only returned by FETCh and READ commands. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:MODulation:AVERage?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Evm_Rms: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: float: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: float: float Magnitude error peak value Range: -100 % to 100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Phase_Error_Rms: float: No parameter help available
			- Phase_Error_Peak: float: No parameter help available
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Carrier_Freq_Err: float: No parameter help available
			- Transmit_Time_Err: float: No parameter help available
			- Ue_Power: float: float User equipment power Range: -100 dBm to 55 dBm, Unit: dBm
			- Power_Steps: float: float User equipment power step Range: -50 dB to 50 dB, Unit: dB
			- Phase_Disc: float: float Phase discontinuity Range: -180 deg to 180 deg, Unit: deg
			- Tx_Time_Alignment: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Mag_Error_Rms'),
			ArgStruct.scalar_float('Mag_Error_Peak'),
			ArgStruct.scalar_float('Phase_Error_Rms'),
			ArgStruct.scalar_float('Phase_Error_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Carrier_Freq_Err'),
			ArgStruct.scalar_float('Transmit_Time_Err'),
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Power_Steps'),
			ArgStruct.scalar_float('Phase_Disc'),
			ArgStruct.scalar_float('Tx_Time_Alignment')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Mag_Error_Rms: float = None
			self.Mag_Error_Peak: float = None
			self.Phase_Error_Rms: float = None
			self.Phase_Error_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Carrier_Freq_Err: float = None
			self.Transmit_Time_Err: float = None
			self.Ue_Power: float = None
			self.Power_Steps: float = None
			self.Phase_Disc: float = None
			self.Tx_Time_Alignment: float = None

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:MODulation:AVERage \n
		Snippet: value: ResultData = driver.multiEval.carrier.modulation.average.fetch(carrier = repcap.Carrier.Default) \n
		Return the current, average, maximum and standard deviation single value results. The return values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each of the
		first 14 results listed below. The TX time alignment is only returned by FETCh and READ commands. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:MODulation:AVERage?', self.__class__.ResultData())

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:MODulation:AVERage \n
		Snippet: value: ResultData = driver.multiEval.carrier.modulation.average.read(carrier = repcap.Carrier.Default) \n
		Return the current, average, maximum and standard deviation single value results. The return values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each of the
		first 14 results listed below. The TX time alignment is only returned by FETCh and READ commands. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:MODulation:AVERage?', self.__class__.ResultData())
