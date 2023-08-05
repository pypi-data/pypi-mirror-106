from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UePower:
	"""UePower commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uePower", core, parent)

	def set(self, enable_ue_power: bool, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:UEPower \n
		Snippet: driver.configure.multiEval.listPy.segment.uePower.set(enable_ue_power = False, segment = repcap.Segment.Default) \n
		Enables the calculation of the current UE power vs. slot results in segment no. <no>; see 'Multi-Evaluation List Mode'. \n
			:param enable_ue_power: OFF | ON OFF: Disable measurement ON: Enable measurement of UE power
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		param = Conversions.bool_to_str(enable_ue_power)
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:UEPower {param}')

	def get(self, segment=repcap.Segment.Default) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:UEPower \n
		Snippet: value: bool = driver.configure.multiEval.listPy.segment.uePower.get(segment = repcap.Segment.Default) \n
		Enables the calculation of the current UE power vs. slot results in segment no. <no>; see 'Multi-Evaluation List Mode'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: enable_ue_power: OFF | ON OFF: Disable measurement ON: Enable measurement of UE power"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:UEPower?')
		return Conversions.str_to_bool(response)
