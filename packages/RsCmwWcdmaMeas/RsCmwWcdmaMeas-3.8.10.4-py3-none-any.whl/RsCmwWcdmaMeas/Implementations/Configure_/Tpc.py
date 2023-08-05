from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpc:
	"""Tpc commands group definition. 32 total commands, 7 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tpc", core, parent)

	@property
	def ilpControl(self):
		"""ilpControl commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_ilpControl'):
			from .Tpc_.IlpControl import IlpControl
			self._ilpControl = IlpControl(self._core, self._base)
		return self._ilpControl

	@property
	def monitor(self):
		"""monitor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_monitor'):
			from .Tpc_.Monitor import Monitor
			self._monitor = Monitor(self._core, self._base)
		return self._monitor

	@property
	def mpedch(self):
		"""mpedch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mpedch'):
			from .Tpc_.Mpedch import Mpedch
			self._mpedch = Mpedch(self._core, self._base)
		return self._mpedch

	@property
	def ctfc(self):
		"""ctfc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ctfc'):
			from .Tpc_.Ctfc import Ctfc
			self._ctfc = Ctfc(self._core, self._base)
		return self._ctfc

	@property
	def ulcm(self):
		"""ulcm commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ulcm'):
			from .Tpc_.Ulcm import Ulcm
			self._ulcm = Ulcm(self._core, self._base)
		return self._ulcm

	@property
	def dhib(self):
		"""dhib commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_dhib'):
			from .Tpc_.Dhib import Dhib
			self._dhib = Dhib(self._core, self._base)
		return self._dhib

	@property
	def limit(self):
		"""limit commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_limit'):
			from .Tpc_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	# noinspection PyTypeChecker
	def get_cselection(self) -> enums.Carrier:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:CSELection \n
		Snippet: value: enums.Carrier = driver.configure.tpc.get_cselection() \n
		Selects the uplink carrier to be measured. This parameter is relevant only for the dual uplink carrier configuration. \n
			:return: carrier: C1 | C2 C1: primary uplink carrier C2: secondary uplink carrier
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:CSELection?')
		return Conversions.str_to_scalar_enum(response, enums.Carrier)

	def set_cselection(self, carrier: enums.Carrier) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:CSELection \n
		Snippet: driver.configure.tpc.set_cselection(carrier = enums.Carrier.C1) \n
		Selects the uplink carrier to be measured. This parameter is relevant only for the dual uplink carrier configuration. \n
			:param carrier: C1 | C2 C1: primary uplink carrier C2: secondary uplink carrier
		"""
		param = Conversions.enum_scalar_to_str(carrier, enums.Carrier)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:CSELection {param}')

	# noinspection PyTypeChecker
	def get_setup(self) -> enums.SetType:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:SETup \n
		Snippet: value: enums.SetType = driver.configure.tpc.get_setup() \n
		Selects the TPC setup (expected) to be executed during the measurement. For the combined signal path scenario,
		useCONFigure:WCDMa:SIGN<i>:UL:TPC:SET. \n
			:return: set_type: CLOop | ALTernating | ALL1 | ALL0 | SALT | SAL1 | SAL0 | CONTinuous | TSE | TSF | PHUP | PHDown | TSABc | TSEF | TSGH | MPEDch | ULCM | CTFC | DHIB CLOop: 'Closed Loop' ALTernating: 'Alternating' ALL1: 'All 1' ALL0: 'All 0' SALT: 'Single Pattern + Alternating' SAL1: 'Single Pattern + All 1' SAL0: 'Single Pattern + All 0' CONTinuous: 'Continuous Pattern' TSE: 'TPC Test Step E' TSF: 'TPC Test Step F' PHUP: 'Phase Discontinuity Up' PHDown: 'Phase Discontinuity Down' TSABc: 'TPC Test Step ABC' TSEF: 'TPC Test Step EF' TSGH: 'TPC Test Step GH' MPEDch:'Max. Power E-DCH' ULCM: 'TPC Test Step UL CM' CTFC: 'Change of TFC' DHIB: 'DC HSPA In-Band Emission'
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:SETup?')
		return Conversions.str_to_scalar_enum(response, enums.SetType)

	def set_setup(self, set_type: enums.SetType) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:SETup \n
		Snippet: driver.configure.tpc.set_setup(set_type = enums.SetType.ALL0) \n
		Selects the TPC setup (expected) to be executed during the measurement. For the combined signal path scenario,
		useCONFigure:WCDMa:SIGN<i>:UL:TPC:SET. \n
			:param set_type: CLOop | ALTernating | ALL1 | ALL0 | SALT | SAL1 | SAL0 | CONTinuous | TSE | TSF | PHUP | PHDown | TSABc | TSEF | TSGH | MPEDch | ULCM | CTFC | DHIB CLOop: 'Closed Loop' ALTernating: 'Alternating' ALL1: 'All 1' ALL0: 'All 0' SALT: 'Single Pattern + Alternating' SAL1: 'Single Pattern + All 1' SAL0: 'Single Pattern + All 0' CONTinuous: 'Continuous Pattern' TSE: 'TPC Test Step E' TSF: 'TPC Test Step F' PHUP: 'Phase Discontinuity Up' PHDown: 'Phase Discontinuity Down' TSABc: 'TPC Test Step ABC' TSEF: 'TPC Test Step EF' TSGH: 'TPC Test Step GH' MPEDch:'Max. Power E-DCH' ULCM: 'TPC Test Step UL CM' CTFC: 'Change of TFC' DHIB: 'DC HSPA In-Band Emission'
		"""
		param = Conversions.enum_scalar_to_str(set_type, enums.SetType)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:SETup {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.MeasMode:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:MODE \n
		Snippet: value: enums.MeasMode = driver.configure.tpc.get_mode() \n
		Queries the active measurement mode resulting from the currently selected TPC setup. \n
			:return: meas_mode: MONitor | ILPControl | MPEDch | CTFC | ULCM | DHIB MONitor: 'Monitor' ILPControl: 'Inner Loop Power Contro'l MPEDch: 'Max. Power E-DCH' CTFC: 'Change of TFC' ULCM: 'UL Commpressed Mode' DHIB: 'DC HSPA In-Band Emission'
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MeasMode)

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:MOEXception \n
		Snippet: value: bool = driver.configure.tpc.get_mo_exception() \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF | ON OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:MOEXception \n
		Snippet: driver.configure.tpc.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF | ON OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:MOEXception {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:TOUT \n
		Snippet: value: float = driver.configure.tpc.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: numeric Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:TOUT \n
		Snippet: driver.configure.tpc.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: numeric Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:TOUT {param}')

	def clone(self) -> 'Tpc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tpc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
