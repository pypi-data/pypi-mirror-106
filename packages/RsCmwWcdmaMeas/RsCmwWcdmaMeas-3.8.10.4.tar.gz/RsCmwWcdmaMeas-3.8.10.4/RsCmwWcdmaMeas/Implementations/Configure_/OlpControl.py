from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OlpControl:
	"""OlpControl commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("olpControl", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:TOUT \n
		Snippet: value: float = driver.configure.olpControl.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OLPControl:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:TOUT \n
		Snippet: driver.configure.olpControl.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OLPControl:TOUT {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:MOEXception \n
		Snippet: value: bool = driver.configure.olpControl.get_mo_exception() \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF | ON OFF: faulty results are rejected ON: results are never rejected
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OLPControl:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:MOEXception \n
		Snippet: driver.configure.olpControl.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF | ON OFF: faulty results are rejected ON: results are never rejected
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OLPControl:MOEXception {param}')

	def get_limit(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:LIMit \n
		Snippet: value: float = driver.configure.olpControl.get_limit() \n
		Sets the maximum deviation at any carrier regarding the expected nominal UE TX power. \n
			:return: olp_limit: numeric Upper limit for DPCCH preamble power Range: 0 dB to 15 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OLPControl:LIMit?')
		return Conversions.str_to_float(response)

	def set_limit(self, olp_limit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OLPControl:LIMit \n
		Snippet: driver.configure.olpControl.set_limit(olp_limit = 1.0) \n
		Sets the maximum deviation at any carrier regarding the expected nominal UE TX power. \n
			:param olp_limit: numeric Upper limit for DPCCH preamble power Range: 0 dB to 15 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(olp_limit)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OLPControl:LIMit {param}')
