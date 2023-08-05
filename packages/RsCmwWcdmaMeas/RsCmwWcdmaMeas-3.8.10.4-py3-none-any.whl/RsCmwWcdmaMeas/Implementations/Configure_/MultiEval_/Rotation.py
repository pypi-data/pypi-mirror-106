from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rotation:
	"""Rotation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rotation", core, parent)

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:ROTation:MODulation \n
		Snippet: value: int = driver.configure.multiEval.rotation.get_modulation() \n
		Defines the initial phase reference (φ=0) for I/Q constellation diagrams of QPSK signals. \n
			:return: rotation: numeric The entered value is rounded to 0 deg or 45 deg. 0 deg: constellation points on I- and Q-axes 45 deg: constellation points on angle bisectors between I- and Q-axes Range: 0 deg to 45 deg, Unit: deg
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:ROTation:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, rotation: int) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:ROTation:MODulation \n
		Snippet: driver.configure.multiEval.rotation.set_modulation(rotation = 1) \n
		Defines the initial phase reference (φ=0) for I/Q constellation diagrams of QPSK signals. \n
			:param rotation: numeric The entered value is rounded to 0 deg or 45 deg. 0 deg: constellation points on I- and Q-axes 45 deg: constellation points on angle bisectors between I- and Q-axes Range: 0 deg to 45 deg, Unit: deg
		"""
		param = Conversions.decimal_value_to_str(rotation)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:ROTation:MODulation {param}')
