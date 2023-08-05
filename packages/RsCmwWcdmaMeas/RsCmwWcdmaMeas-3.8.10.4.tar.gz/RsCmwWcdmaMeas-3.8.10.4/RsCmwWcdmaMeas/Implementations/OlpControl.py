from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OlpControl:
	"""OlpControl commands group definition. 10 total commands, 2 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("olpControl", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .OlpControl_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .OlpControl_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.olpControl.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:MEASurement<Instance>:OLPControl')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.olpControl.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:MEASurement<Instance>:OLPControl')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.olpControl.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:MEASurement<Instance>:OLPControl')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.olpControl.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:MEASurement<Instance>:OLPControl')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.olpControl.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:MEASurement<Instance>:OLPControl')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: driver.olpControl.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:MEASurement<Instance>:OLPControl')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Ue_Pwr_C_1: float: float UE power of carrier one during measurement of the ramp up of carrier two Range: -100 dBm to 100 dBm
			- Olpc_1: float: float UE power in DPCCH power control preamble of carrier one during measurement of the ramp up of carrier one Range: -100 dBm to 100 dBm
			- Slot_No_C_1: int: decimal Slot where the power ramp up of carrier one has been detected Range: 0 slots to 14 slots
			- Olpc_2: float: float UE power in DPCCH power control preamble of carrier two during measurement of the ramp up of carrier two Range: -100 dBm to 100 dBm
			- Slot_No_C_2: int: decimal Slot where the power ramp up of carrier two has been detected Range: 0 slots to 14 slots"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ue_Pwr_C_1'),
			ArgStruct.scalar_float('Olpc_1'),
			ArgStruct.scalar_int('Slot_No_C_1'),
			ArgStruct.scalar_float('Olpc_2'),
			ArgStruct.scalar_int('Slot_No_C_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ue_Pwr_C_1: float = None
			self.Olpc_1: float = None
			self.Slot_No_C_1: int = None
			self.Olpc_2: float = None
			self.Slot_No_C_2: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: value: ResultData = driver.olpControl.read() \n
		Return the single value results for open loop power control measurements. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:OLPControl?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: value: ResultData = driver.olpControl.fetch() \n
		Return the single value results for open loop power control measurements. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:OLPControl?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Olpc_1: float: float UE power in DPCCH power control preamble of carrier one during measurement of the ramp up of carrier one Range: -100 dBm to 100 dBm
			- Olpc_2: float: float UE power in DPCCH power control preamble of carrier two during measurement of the ramp up of carrier two Range: -100 dBm to 100 dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Olpc_1'),
			ArgStruct.scalar_float('Olpc_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Olpc_1: float = None
			self.Olpc_2: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:OLPControl \n
		Snippet: value: CalculateStruct = driver.olpControl.calculate() \n
		Return the single value results for open loop power control measurements. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:OLPControl?', self.__class__.CalculateStruct())

	def clone(self) -> 'OlpControl':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OlpControl(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
