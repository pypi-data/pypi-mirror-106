from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OoSync:
	"""OoSync commands group definition. 5 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ooSync", core, parent)

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_limit'):
			from .OoSync_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_aa_dpch_level(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:AADPchlevel \n
		Snippet: value: bool = driver.configure.ooSync.get_aa_dpch_level() \n
		Enables or disables automatic activation of DPCH level sequence, provided by WCDMA signaling application.
		With auto execution, the sequence is activated by starting the measurement. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:AADPchlevel?')
		return Conversions.str_to_bool(response)

	def set_aa_dpch_level(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:AADPchlevel \n
		Snippet: driver.configure.ooSync.set_aa_dpch_level(enable = False) \n
		Enables or disables automatic activation of DPCH level sequence, provided by WCDMA signaling application.
		With auto execution, the sequence is activated by starting the measurement. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:AADPchlevel {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:TOUT \n
		Snippet: value: float = driver.configure.ooSync.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:TOUT \n
		Snippet: driver.configure.ooSync.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:TOUT {param}')

	def clone(self) -> 'OoSync':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OoSync(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
