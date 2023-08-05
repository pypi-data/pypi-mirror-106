from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 39 total commands, 4 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prach", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Prach_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Prach_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def offPower(self):
		"""offPower commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_offPower'):
			from .Prach_.OffPower import OffPower
			self._offPower = OffPower(self._core, self._base)
		return self._offPower

	@property
	def preamble(self):
		"""preamble commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamble'):
			from .Prach_.Preamble import Preamble
			self._preamble = Preamble(self._core, self._base)
		return self._preamble

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:PRACh \n
		Snippet: driver.prach.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:MEASurement<Instance>:PRACh')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:PRACh \n
		Snippet: driver.prach.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:MEASurement<Instance>:PRACh')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:PRACh \n
		Snippet: driver.prach.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:MEASurement<Instance>:PRACh')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:PRACh \n
		Snippet: driver.prach.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:MEASurement<Instance>:PRACh')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:PRACh \n
		Snippet: driver.prach.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:MEASurement<Instance>:PRACh')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:PRACh \n
		Snippet: driver.prach.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:MEASurement<Instance>:PRACh')

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
