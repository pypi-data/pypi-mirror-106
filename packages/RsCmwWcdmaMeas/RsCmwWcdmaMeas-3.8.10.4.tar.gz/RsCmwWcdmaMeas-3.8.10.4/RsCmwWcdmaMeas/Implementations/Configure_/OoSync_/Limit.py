from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	def get_pon_upper(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:PONupper \n
		Snippet: value: float = driver.configure.ooSync.limit.get_pon_upper() \n
		Specifies the transmitted power of the UE above which the UE's transmitter is considered to be on. \n
			:return: pon_lower: numeric Range: -70 dBm to 34 dBm
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:PONupper?')
		return Conversions.str_to_float(response)

	def set_pon_upper(self, pon_lower: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:PONupper \n
		Snippet: driver.configure.ooSync.limit.set_pon_upper(pon_lower = 1.0) \n
		Specifies the transmitted power of the UE above which the UE's transmitter is considered to be on. \n
			:param pon_lower: numeric Range: -70 dBm to 34 dBm
		"""
		param = Conversions.decimal_value_to_str(pon_lower)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:PONupper {param}')

	def get_poff_upper(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:POFFupper \n
		Snippet: value: float = driver.configure.ooSync.limit.get_poff_upper() \n
		Specifies the transmitted power of the UE below which the UE's transmitter is considered to be off. \n
			:return: po_ulimit: numeric Range: -90 dBm to 53 dBm
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:POFFupper?')
		return Conversions.str_to_float(response)

	def set_poff_upper(self, po_ulimit: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:POFFupper \n
		Snippet: driver.configure.ooSync.limit.set_poff_upper(po_ulimit = 1.0) \n
		Specifies the transmitted power of the UE below which the UE's transmitter is considered to be off. \n
			:param po_ulimit: numeric Range: -90 dBm to 53 dBm
		"""
		param = Conversions.decimal_value_to_str(po_ulimit)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:POFFupper {param}')

	def get_threshold(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:THReshold \n
		Snippet: value: float = driver.configure.ooSync.limit.get_threshold() \n
		Specifies the reliability of results for 'RX Level Strategy'≠'Max A off F Max'. If the UE transmitter is expected to be
		on and the UE power is below the limit, results are not reliable. \n
			:return: threshold_level: numeric Range: -65 dB to 0 dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold_level: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:OOSYnc:LIMit:THReshold \n
		Snippet: driver.configure.ooSync.limit.set_threshold(threshold_level = 1.0) \n
		Specifies the reliability of results for 'RX Level Strategy'≠'Max A off F Max'. If the UE transmitter is expected to be
		on and the UE power is below the limit, results are not reliable. \n
			:param threshold_level: numeric Range: -65 dB to 0 dB
		"""
		param = Conversions.decimal_value_to_str(threshold_level)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:OOSYnc:LIMit:THReshold {param}')
