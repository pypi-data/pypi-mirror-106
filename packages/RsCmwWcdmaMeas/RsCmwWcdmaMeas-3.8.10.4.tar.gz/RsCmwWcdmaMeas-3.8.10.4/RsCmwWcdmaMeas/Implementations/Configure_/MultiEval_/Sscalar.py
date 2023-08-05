from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sscalar:
	"""Sscalar commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sscalar", core, parent)

	def get_modulation(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SSCalar:MODulation \n
		Snippet: value: float = driver.configure.multiEval.sscalar.get_modulation() \n
		Selects a particular slot or half-slot within the measurement length where the R&S CMW evaluates the statistical
		measurement results for multislot measurements. The slot number must be smaller than the number of measured slots (see
		method RsCmwWcdmaMeas.Configure.MultiEval.msCount) . \n
			:return: slot_number: numeric Range: 0 to 119.5
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SSCalar:MODulation?')
		return Conversions.str_to_float(response)

	def set_modulation(self, slot_number: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:SSCalar:MODulation \n
		Snippet: driver.configure.multiEval.sscalar.set_modulation(slot_number = 1.0) \n
		Selects a particular slot or half-slot within the measurement length where the R&S CMW evaluates the statistical
		measurement results for multislot measurements. The slot number must be smaller than the number of measured slots (see
		method RsCmwWcdmaMeas.Configure.MultiEval.msCount) . \n
			:param slot_number: numeric Range: 0 to 119.5
		"""
		param = Conversions.decimal_value_to_str(slot_number)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:SSCalar:MODulation {param}')
