from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Return_Code: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Dpcch: float: float RMS CDP values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Dpdch: float: float RMS CDP values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Hsdpcch: float: float RMS CDP values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpcch: float: float RMS CDP values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_1: float: float RMS CDP values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_2: float: float RMS CDP values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_3: float: float RMS CDP values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_4: float: float RMS CDP values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Return_Code'),
			ArgStruct.scalar_float('Dpcch'),
			ArgStruct.scalar_float('Dpdch'),
			ArgStruct.scalar_float('Hsdpcch'),
			ArgStruct.scalar_float('Edpcch'),
			ArgStruct.scalar_float('Edpdch_1'),
			ArgStruct.scalar_float('Edpdch_2'),
			ArgStruct.scalar_float('Edpdch_3'),
			ArgStruct.scalar_float('Edpdch_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Return_Code: int = None
			self.Dpcch: float = None
			self.Dpdch: float = None
			self.Hsdpcch: float = None
			self.Edpcch: float = None
			self.Edpdch_1: float = None
			self.Edpdch_2: float = None
			self.Edpdch_3: float = None
			self.Edpdch_4: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CDPower:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.cdPower.current.fetch(segment = repcap.Segment.Default) \n
		Returns the RMS CDP vs. slot results for segment <no> in list mode. The number to the left of each result parameter is
		provided for easy identification of the parameter position within the result array. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CDPower:CURRent?', self.__class__.FetchStruct())
