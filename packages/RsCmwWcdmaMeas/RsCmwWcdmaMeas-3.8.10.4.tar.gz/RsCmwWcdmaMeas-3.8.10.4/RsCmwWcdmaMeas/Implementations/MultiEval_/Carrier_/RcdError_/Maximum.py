from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Dpcch: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Dpdch: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Hsdpcch: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpcch: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_1: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_2: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_3: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_4: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
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
			self.Dpcch: float = None
			self.Dpdch: float = None
			self.Hsdpcch: float = None
			self.Edpcch: float = None
			self.Edpdch_1: float = None
			self.Edpdch_2: float = None
			self.Edpdch_3: float = None
			self.Edpdch_4: float = None

	def calculate(self, carrier=repcap.Carrier.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:RCDerror:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.carrier.rcdError.maximum.calculate(carrier = repcap.Carrier.Default) \n
		Returns the RCDE vs. slot values measured in a selected slot. In addition to the current values, average, maximum and
		standard deviation values can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CALCulate:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:RCDerror:MAXimum?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Dpcch: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Dpdch: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Hsdpcch: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpcch: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_1: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_2: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_3: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB
			- Edpdch_4: float: float RCDE values for the indicated channels Range: -100 dB to 0 dB (SDEViation 0 dB to 50 dB) , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
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
			self.Dpcch: float = None
			self.Dpdch: float = None
			self.Hsdpcch: float = None
			self.Edpcch: float = None
			self.Edpdch_1: float = None
			self.Edpdch_2: float = None
			self.Edpdch_3: float = None
			self.Edpdch_4: float = None

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:RCDerror:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.carrier.rcdError.maximum.fetch(carrier = repcap.Carrier.Default) \n
		Returns the RCDE vs. slot values measured in a selected slot. In addition to the current values, average, maximum and
		standard deviation values can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:RCDerror:MAXimum?', self.__class__.ResultData())

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:MEValuation:CARRier<carrier>:RCDerror:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.carrier.rcdError.maximum.read(carrier = repcap.Carrier.Default) \n
		Returns the RCDE vs. slot values measured in a selected slot. In addition to the current values, average, maximum and
		standard deviation values can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:MEValuation:CARRier{carrier_cmd_val}:RCDerror:MAXimum?', self.__class__.ResultData())
