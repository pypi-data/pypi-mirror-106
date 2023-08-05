from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Monitor:
	"""Monitor commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("monitor", core, parent)

	def get_mlength(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:MONitor:MLENgth \n
		Snippet: value: int = driver.configure.tpc.monitor.get_mlength() \n
		Defines the number of slots to be measured in 'Monitor' mode. \n
			:return: meas_length: numeric Range: 1 slot to 341 slots, Unit: slots
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:MONitor:MLENgth?')
		return Conversions.str_to_int(response)

	def set_mlength(self, meas_length: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:MONitor:MLENgth \n
		Snippet: driver.configure.tpc.monitor.set_mlength(meas_length = 1) \n
		Defines the number of slots to be measured in 'Monitor' mode. \n
			:param meas_length: numeric Range: 1 slot to 341 slots, Unit: slots
		"""
		param = Conversions.decimal_value_to_str(meas_length)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:MONitor:MLENgth {param}')
