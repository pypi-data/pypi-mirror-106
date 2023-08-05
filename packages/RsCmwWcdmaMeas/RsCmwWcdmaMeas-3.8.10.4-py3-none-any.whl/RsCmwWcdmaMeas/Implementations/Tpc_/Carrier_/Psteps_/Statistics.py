from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Statistics:
	"""Statistics commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("statistics", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Pwr_Steps_0_Db: int: No parameter help available
			- Pwr_Steps_B_1_Db: int: No parameter help available
			- Pwr_Steps_Cm_1_Db: int: No parameter help available
			- Pwr_Steps_Group_A: int: No parameter help available
			- Pwr_Steps_Eg: int: No parameter help available
			- Pwr_Steps_Fh: int: No parameter help available
			- Pwr_Steps_Group_Eg: int: No parameter help available
			- Pwr_Steps_Group_Fh: int: No parameter help available
			- Pwr_Steps_Up: int: float Power steps up result of 'Change of TFC' mode Range: 0 to 5
			- Pwr_Steps_Down: int: float Power steps down result of 'Change of TFC' mode Range: 0 to 5
			- Rpwr_Steps: int: decimal Recovery power steps result of 'UL Compressed Mode' - pattern A
			- Epwr_Steps_B_1_D_B: int: No parameter help available
			- Epwr_Steps_Cm_1_D_B: int: No parameter help available
			- Epwr_Steps_Eg: int: No parameter help available
			- Epwr_Steps_Fh: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Pwr_Steps_0_Db'),
			ArgStruct.scalar_int('Pwr_Steps_B_1_Db'),
			ArgStruct.scalar_int('Pwr_Steps_Cm_1_Db'),
			ArgStruct.scalar_int('Pwr_Steps_Group_A'),
			ArgStruct.scalar_int('Pwr_Steps_Eg'),
			ArgStruct.scalar_int('Pwr_Steps_Fh'),
			ArgStruct.scalar_int('Pwr_Steps_Group_Eg'),
			ArgStruct.scalar_int('Pwr_Steps_Group_Fh'),
			ArgStruct.scalar_int('Pwr_Steps_Up'),
			ArgStruct.scalar_int('Pwr_Steps_Down'),
			ArgStruct.scalar_int('Rpwr_Steps'),
			ArgStruct.scalar_int('Epwr_Steps_B_1_D_B'),
			ArgStruct.scalar_int('Epwr_Steps_Cm_1_D_B'),
			ArgStruct.scalar_int('Epwr_Steps_Eg'),
			ArgStruct.scalar_int('Epwr_Steps_Fh')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pwr_Steps_0_Db: int = None
			self.Pwr_Steps_B_1_Db: int = None
			self.Pwr_Steps_Cm_1_Db: int = None
			self.Pwr_Steps_Group_A: int = None
			self.Pwr_Steps_Eg: int = None
			self.Pwr_Steps_Fh: int = None
			self.Pwr_Steps_Group_Eg: int = None
			self.Pwr_Steps_Group_Fh: int = None
			self.Pwr_Steps_Up: int = None
			self.Pwr_Steps_Down: int = None
			self.Rpwr_Steps: int = None
			self.Epwr_Steps_B_1_D_B: int = None
			self.Epwr_Steps_Cm_1_D_B: int = None
			self.Epwr_Steps_Eg: int = None
			self.Epwr_Steps_Fh: int = None

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:PSTeps:STATistics \n
		Snippet: value: ResultData = driver.tpc.carrier.psteps.statistics.read(carrier = repcap.Carrier.Default) \n
		Return the 'Statistics' values per carrier, indicating how many trace values have been considered to derive the maximum,
		minimum and average power step and power step group results. The command returns all parameters listed below, independent
		of the selected TPC setup. However, only for some of the parameters result values are available. For the other parameters,
		only an indicator is returned (e.g. NAV) . 'Step A' to 'step H' refer to the test steps of the 'Inner Loop Power Control'
		mode (results <2_Step0dB_ABC> to <9_GroupFH> and <13_EPStepsB1dB> to <16_EPStepsFH>) . \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:PSTeps:STATistics?', self.__class__.ResultData())

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:TPC:CARRier<carrier>:PSTeps:STATistics \n
		Snippet: value: ResultData = driver.tpc.carrier.psteps.statistics.fetch(carrier = repcap.Carrier.Default) \n
		Return the 'Statistics' values per carrier, indicating how many trace values have been considered to derive the maximum,
		minimum and average power step and power step group results. The command returns all parameters listed below, independent
		of the selected TPC setup. However, only for some of the parameters result values are available. For the other parameters,
		only an indicator is returned (e.g. NAV) . 'Step A' to 'step H' refer to the test steps of the 'Inner Loop Power Control'
		mode (results <2_Step0dB_ABC> to <9_GroupFH> and <13_EPStepsB1dB> to <16_EPStepsFH>) . \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:TPC:CARRier{carrier_cmd_val}:PSTeps:STATistics?', self.__class__.ResultData())
