from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Ue_Power: float: float Mean preamble power Range: -100 dBm to 55 dBm, Unit: dBm
			- Power_Steps: float: float Mean preamble power minus mean power of previous preamble For first preamble NCAP is returned. Range: -10 dB to 50 dB, Unit: dB
			- Carrier_Freq_Err: float: float Carrier frequency error Range: -60000 Hz to 60000 Hz, Unit: Hz
			- Evm_Rms: float: float Error vector magnitude RMS value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: float: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: float: float Magnitude error peak value Range: -100 % to 100 %, Unit: %
			- Phase_Error_Rms: float: No parameter help available
			- Phase_Error_Peak: float: No parameter help available
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Signature: int: decimal Detected preamble signature Range: 0 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Power_Steps'),
			ArgStruct.scalar_float('Carrier_Freq_Err'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Mag_Error_Rms'),
			ArgStruct.scalar_float('Mag_Error_Peak'),
			ArgStruct.scalar_float('Phase_Error_Rms'),
			ArgStruct.scalar_float('Phase_Error_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_int('Signature')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ue_Power: float = None
			self.Power_Steps: float = None
			self.Carrier_Freq_Err: float = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Mag_Error_Rms: float = None
			self.Mag_Error_Peak: float = None
			self.Phase_Error_Rms: float = None
			self.Phase_Error_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Signature: int = None

	def read(self, preamble=repcap.Preamble.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:PRACh:PREamble<nr>:CURRent \n
		Snippet: value: ResultData = driver.prach.preamble.current.read(preamble = repcap.Preamble.Default) \n
		Return the single value results for a selected preamble. See also 'Detailed Views: TX Measurement' \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		preamble_cmd_val = self._base.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:PRACh:PREamble{preamble_cmd_val}:CURRent?', self.__class__.ResultData())

	def fetch(self, preamble=repcap.Preamble.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:PRACh:PREamble<nr>:CURRent \n
		Snippet: value: ResultData = driver.prach.preamble.current.fetch(preamble = repcap.Preamble.Default) \n
		Return the single value results for a selected preamble. See also 'Detailed Views: TX Measurement' \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		preamble_cmd_val = self._base.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:PRACh:PREamble{preamble_cmd_val}:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Ue_Power: float: float Mean preamble power Range: -100 dBm to 55 dBm, Unit: dBm
			- Power_Steps: float: float Mean preamble power minus mean power of previous preamble For first preamble NCAP is returned. Range: -10 dB to 50 dB, Unit: dB
			- Carrier_Freq_Err: float: float Carrier frequency error Range: -60000 Hz to 60000 Hz, Unit: Hz
			- Evm_Rms: float: float Error vector magnitude RMS value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: float: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: float: float Magnitude error peak value Range: -100 % to 100 %, Unit: %
			- Phase_Error_Rms: float: No parameter help available
			- Phase_Error_Peak: float: No parameter help available
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ue_Power'),
			ArgStruct.scalar_float('Power_Steps'),
			ArgStruct.scalar_float('Carrier_Freq_Err'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Mag_Error_Rms'),
			ArgStruct.scalar_float('Mag_Error_Peak'),
			ArgStruct.scalar_float('Phase_Error_Rms'),
			ArgStruct.scalar_float('Phase_Error_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ue_Power: float = None
			self.Power_Steps: float = None
			self.Carrier_Freq_Err: float = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Mag_Error_Rms: float = None
			self.Mag_Error_Peak: float = None
			self.Phase_Error_Rms: float = None
			self.Phase_Error_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None

	def calculate(self, preamble=repcap.Preamble.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:PRACh:PREamble<nr>:CURRent \n
		Snippet: value: CalculateStruct = driver.prach.preamble.current.calculate(preamble = repcap.Preamble.Default) \n
		Return the single value results for a selected preamble. See also 'Detailed Views: TX Measurement' \n
		Use RsCmwWcdmaMeas.reliability.last_value to read the updated reliability indicator. \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		preamble_cmd_val = self._base.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:PRACh:PREamble{preamble_cmd_val}:CURRent?', self.__class__.CalculateStruct())
