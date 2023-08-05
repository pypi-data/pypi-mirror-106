from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 529 total commands, 8 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("multiEval", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .MultiEval_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .MultiEval_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def carrier(self):
		"""carrier commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .MultiEval_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def spectrum(self):
		"""spectrum commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .MultiEval_.Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._base)
		return self._spectrum

	@property
	def modulation(self):
		"""modulation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .MultiEval_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def ber(self):
		"""ber commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ber'):
			from .MultiEval_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	@property
	def pcde(self):
		"""pcde commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcde'):
			from .MultiEval_.Pcde import Pcde
			self._pcde = Pcde(self._core, self._base)
		return self._pcde

	@property
	def listPy(self):
		"""listPy commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .MultiEval_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:MEValuation \n
		Snippet: driver.multiEval.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:MEASurement<Instance>:MEValuation')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:MEASurement<instance>:MEValuation \n
		Snippet: driver.multiEval.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:MEASurement<Instance>:MEValuation')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:MEValuation \n
		Snippet: driver.multiEval.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:MEASurement<Instance>:MEValuation')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:MEASurement<instance>:MEValuation \n
		Snippet: driver.multiEval.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:MEASurement<Instance>:MEValuation')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:MEValuation \n
		Snippet: driver.multiEval.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:MEASurement<Instance>:MEValuation')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:MEASurement<instance>:MEValuation \n
		Snippet: driver.multiEval.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:MEASurement<Instance>:MEValuation')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
