from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpc:
	"""Tpc commands group definition. 54 total commands, 4 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tpc", core, parent)

	@property
	def dhib(self):
		"""dhib commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dhib'):
			from .Tpc_.Dhib import Dhib
			self._dhib = Dhib(self._core, self._base)
		return self._dhib

	@property
	def carrier(self):
		"""carrier commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Tpc_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def total(self):
		"""total commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_total'):
			from .Tpc_.Total import Total
			self._total = Total(self._core, self._base)
		return self._total

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Tpc_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:TPC \n
		Snippet: driver.tpc.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:MEASurement<Instance>:TPC')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:TPC \n
		Snippet: driver.tpc.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:MEASurement<Instance>:TPC')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:TPC \n
		Snippet: driver.tpc.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:MEASurement<Instance>:TPC')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:TPC \n
		Snippet: driver.tpc.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:MEASurement<Instance>:TPC')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:TPC \n
		Snippet: driver.tpc.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:MEASurement<Instance>:TPC')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:TPC \n
		Snippet: driver.tpc.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:MEASurement<Instance>:TPC')

	def clone(self) -> 'Tpc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tpc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
