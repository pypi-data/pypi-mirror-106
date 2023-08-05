from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OoSync:
	"""OoSync commands group definition. 7 total commands, 1 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ooSync", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .OoSync_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	def get_delay(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:DELay \n
		Snippet: value: float = driver.trigger.ooSync.get_delay() \n
		Defines a time delaying the start of the measurement relative to the trigger event. The delay is useful if the trigger
		event and the uplink DPCH slot border are not synchronous. A measurement starts always at an uplink DPCH slot border.
		Triggering a measurement at another time can yield a synchronization error. For internal trigger sources aligned to the
		downlink DPCH, an additional delay of 1024 chips is automatically applied. It corresponds to the assumed delay between
		downlink and uplink slot. This setting has no influence on 'Free Run' measurements. \n
			:return: delay: numeric Range: -666.7E-6 s to 0.24 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:DELay \n
		Snippet: driver.trigger.ooSync.set_delay(delay = 1.0) \n
		Defines a time delaying the start of the measurement relative to the trigger event. The delay is useful if the trigger
		event and the uplink DPCH slot border are not synchronous. A measurement starts always at an uplink DPCH slot border.
		Triggering a measurement at another time can yield a synchronization error. For internal trigger sources aligned to the
		downlink DPCH, an additional delay of 1024 chips is automatically applied. It corresponds to the assumed delay between
		downlink and uplink slot. This setting has no influence on 'Free Run' measurements. \n
			:param delay: numeric Range: -666.7E-6 s to 0.24 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:DELay {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:MGAP \n
		Snippet: value: float = driver.trigger.ooSync.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: minimum_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:MGAP \n
		Snippet: driver.trigger.ooSync.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param minimum_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:MGAP {param}')

	def get_source(self) -> str:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:SOURce \n
		Snippet: value: str = driver.trigger.ooSync.get_source() \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:return: source: string 'Free Run (Standard) ': Free run (standard synchronization) 'Free Run (Fast Sync) ': Free run (fast synchronization) 'IF Power': Power trigger (normal synchronization) 'IF Power (Sync) ': Power trigger (extended synchronization)
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:SOURce \n
		Snippet: driver.trigger.ooSync.set_source(source = '1') \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:param source: string 'Free Run (Standard) ': Free run (standard synchronization) 'Free Run (Fast Sync) ': Free run (fast synchronization) 'IF Power': Power trigger (normal synchronization) 'IF Power (Sync) ': Power trigger (extended synchronization)
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:SOURce {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:THReshold \n
		Snippet: value: float = driver.trigger.ooSync.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: level: numeric Range: -47 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, level: float) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:THReshold \n
		Snippet: driver.trigger.ooSync.set_threshold(level = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param level: numeric Range: -47 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlope:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:SLOPe \n
		Snippet: value: enums.SignalSlope = driver.trigger.ooSync.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: slope: REDGe | FEDGe REDGe: Rising edge FEDGe: Falling edge
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlope)

	def set_slope(self, slope: enums.SignalSlope) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:SLOPe \n
		Snippet: driver.trigger.ooSync.set_slope(slope = enums.SignalSlope.FEDGe) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param slope: REDGe | FEDGe REDGe: Rising edge FEDGe: Falling edge
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlope)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:SLOPe {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:TOUT \n
		Snippet: value: float or bool = driver.trigger.ooSync.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:return: timeout: numeric | ON | OFF Range: 0.01 s to 60 s, Unit: s Additional parameters: OFF | ON (disables | enables the timeout)
		"""
		response = self._core.io.query_str('TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:WCDMa:MEASurement<instance>:OOSYnc:TOUT \n
		Snippet: driver.trigger.ooSync.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:param timeout: numeric | ON | OFF Range: 0.01 s to 60 s, Unit: s Additional parameters: OFF | ON (disables | enables the timeout)
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:WCDMa:MEASurement<Instance>:OOSYnc:TOUT {param}')

	def clone(self) -> 'OoSync':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OoSync(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
