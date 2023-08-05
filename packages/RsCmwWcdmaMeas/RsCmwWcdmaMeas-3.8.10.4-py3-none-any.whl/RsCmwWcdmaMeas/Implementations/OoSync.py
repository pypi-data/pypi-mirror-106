from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OoSync:
	"""OoSync commands group definition. 8 total commands, 1 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ooSync", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .OoSync_.State import State
			self._state = State(self._core, self._base)
		return self._state

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability Indicator'
			- Out_Pow_Ab_Max: enums.ResultStatus2: float Maximal output power measured in interval A-B Unit: dBm
			- Out_Pow_Ab_Min: enums.ResultStatus2: float Minimal output power measured in interval A-B Unit: dBm
			- Out_Pow_Ccurrent: enums.ResultStatus2: float Output power measured for point C Unit: dBm
			- Out_Pow_Cd_Max: enums.ResultStatus2: float Maximal output power measured in interval C-D Unit: dBm
			- Out_Pow_Cd_Min: enums.ResultStatus2: float Minimal output power measured in interval C-D Unit: dBm
			- Out_Pow_De_Max: enums.ResultStatus2: float Maximal output power measured in interval D-E Unit: dBm
			- Out_Pow_De_Min: enums.ResultStatus2: float Minimal output power measured in interval D-E Unit: dBm
			- Out_Pow_Fcurrent: enums.ResultStatus2: float Output power measured for point F Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Out_Pow_Ab_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Ab_Min', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Ccurrent', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Cd_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Cd_Min', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_De_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_De_Min', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Pow_Fcurrent', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Pow_Ab_Max: enums.ResultStatus2 = None
			self.Out_Pow_Ab_Min: enums.ResultStatus2 = None
			self.Out_Pow_Ccurrent: enums.ResultStatus2 = None
			self.Out_Pow_Cd_Max: enums.ResultStatus2 = None
			self.Out_Pow_Cd_Min: enums.ResultStatus2 = None
			self.Out_Pow_De_Max: enums.ResultStatus2 = None
			self.Out_Pow_De_Min: enums.ResultStatus2 = None
			self.Out_Pow_Fcurrent: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: value: CalculateStruct = driver.ooSync.calculate() \n
		Return the results of out-of-synchronization handling measurement. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:OOSYnc?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability Indicator'
			- Out_Pow_Ab_Max: float: float Maximal output power measured in interval A-B Unit: dBm
			- Out_Pow_Ab_Min: float: float Minimal output power measured in interval A-B Unit: dBm
			- Out_Pow_Ccurrent: float: float Output power measured for point C Unit: dBm
			- Out_Powc_State: enums.OutPowFstate: OFF | NOFF State of output power for point C OFF: UE transmitter off NOFF: UE transmitter not off
			- Out_Pow_Cd_Max: float: float Maximal output power measured in interval C-D Unit: dBm
			- Out_Pow_Cd_Min: float: float Minimal output power measured in interval C-D Unit: dBm
			- Out_Pow_De_Max: float: float Maximal output power measured in interval D-E Unit: dBm
			- Out_Pow_De_Min: float: float Minimal output power measured in interval D-E Unit: dBm
			- Out_Pow_Fcurrent: float: float Output power measured for point F Unit: dBm
			- Out_Pow_Fstate: enums.OutPowFstate: ON | NON State of output power for point F ON: UE transmitter on NON: UE transmitter not on"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Pow_Ab_Max'),
			ArgStruct.scalar_float('Out_Pow_Ab_Min'),
			ArgStruct.scalar_float('Out_Pow_Ccurrent'),
			ArgStruct.scalar_enum('Out_Powc_State', enums.OutPowFstate),
			ArgStruct.scalar_float('Out_Pow_Cd_Max'),
			ArgStruct.scalar_float('Out_Pow_Cd_Min'),
			ArgStruct.scalar_float('Out_Pow_De_Max'),
			ArgStruct.scalar_float('Out_Pow_De_Min'),
			ArgStruct.scalar_float('Out_Pow_Fcurrent'),
			ArgStruct.scalar_enum('Out_Pow_Fstate', enums.OutPowFstate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Pow_Ab_Max: float = None
			self.Out_Pow_Ab_Min: float = None
			self.Out_Pow_Ccurrent: float = None
			self.Out_Powc_State: enums.OutPowFstate = None
			self.Out_Pow_Cd_Max: float = None
			self.Out_Pow_Cd_Min: float = None
			self.Out_Pow_De_Max: float = None
			self.Out_Pow_De_Min: float = None
			self.Out_Pow_Fcurrent: float = None
			self.Out_Pow_Fstate: enums.OutPowFstate = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: value: ResultData = driver.ooSync.read() \n
		Return the results of out-of-synchronization handling measurement. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:OOSYnc?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: value: ResultData = driver.ooSync.fetch() \n
		Return the results of out-of-synchronization handling measurement. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:OOSYnc?', self.__class__.ResultData())

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.ooSync.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:MEASurement<Instance>:OOSYnc')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.ooSync.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:MEASurement<Instance>:OOSYnc')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.ooSync.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:MEASurement<Instance>:OOSYnc')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.ooSync.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:MEASurement<Instance>:OOSYnc')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.ooSync.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:MEASurement<Instance>:OOSYnc')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:OOSYnc \n
		Snippet: driver.ooSync.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:MEASurement<Instance>:OOSYnc')

	def clone(self) -> 'OoSync':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OoSync(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
