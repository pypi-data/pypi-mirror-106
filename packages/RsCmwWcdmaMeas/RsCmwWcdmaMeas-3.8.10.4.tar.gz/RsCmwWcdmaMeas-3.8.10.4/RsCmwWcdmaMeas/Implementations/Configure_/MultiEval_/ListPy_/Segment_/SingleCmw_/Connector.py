from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connector:
	"""Connector commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connector", core, parent)

	def set(self, cmws_connector: enums.CmwsConnector, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CMWS:CONNector \n
		Snippet: driver.configure.multiEval.listPy.segment.singleCmw.connector.set(cmws_connector = enums.CmwsConnector.R11, segment = repcap.Segment.Default) \n
		Selects the RF input connector for segment <no> for WCDMA list mode measurements with the R&S CMWS. This setting is only
		relevant for connector mode LIST, see method RsCmwWcdmaMeas.Configure.MultiEval.ListPy.SingleCmw.cmode. All segments of a
		list mode measurement must use connectors of the same bench. For possible connector values, see 'Values for RF Path
		Selection'. \n
			:param cmws_connector: Selects the input connector of the R&S CMWS
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		param = Conversions.enum_scalar_to_str(cmws_connector, enums.CmwsConnector)
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CMWS:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.CmwsConnector:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CMWS:CONNector \n
		Snippet: value: enums.CmwsConnector = driver.configure.multiEval.listPy.segment.singleCmw.connector.get(segment = repcap.Segment.Default) \n
		Selects the RF input connector for segment <no> for WCDMA list mode measurements with the R&S CMWS. This setting is only
		relevant for connector mode LIST, see method RsCmwWcdmaMeas.Configure.MultiEval.ListPy.SingleCmw.cmode. All segments of a
		list mode measurement must use connectors of the same bench. For possible connector values, see 'Values for RF Path
		Selection'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: cmws_connector: Selects the input connector of the R&S CMWS"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CMWS:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.CmwsConnector)
