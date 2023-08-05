from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Return_Code: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Evm_Rms: List[float]: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: List[float]: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: List[float]: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: List[float]: float Magnitude error peak value Range: -100 % to 100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Phase_Error_Rms: List[float]: No parameter help available
			- Phase_Error_Peak: List[float]: No parameter help available
			- Iq_Offset: List[float]: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: List[float]: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Carrier_Freq_Err: List[float]: float Carrier frequency error Range: -60000 Hz to 60000 Hz, Unit: Hz
			- Transmit_Time_Err: List[float]: No parameter help available
			- Ue_Power: List[float]: float User equipment power Range: -100 dBm to 55 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Return_Code', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Evm_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Mag_Error_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Mag_Error_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Offset', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Imbalance', DataType.FloatList, None, False, True, 1),
			ArgStruct('Carrier_Freq_Err', DataType.FloatList, None, False, True, 1),
			ArgStruct('Transmit_Time_Err', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ue_Power', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Return_Code: List[int] = None
			self.Evm_Rms: List[float] = None
			self.Evm_Peak: List[float] = None
			self.Mag_Error_Rms: List[float] = None
			self.Mag_Error_Peak: List[float] = None
			self.Phase_Error_Rms: List[float] = None
			self.Phase_Error_Peak: List[float] = None
			self.Iq_Offset: List[float] = None
			self.Iq_Imbalance: List[float] = None
			self.Carrier_Freq_Err: List[float] = None
			self.Transmit_Time_Err: List[float] = None
			self.Ue_Power: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:WCDMa:MEASurement<instance>:MEValuation:LIST:MODulation:SDEViation \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.modulation.standardDev.fetch() \n
		Return modulation single value results in list mode. The values listed below in curly brackets {} are returned for the
		segments {...}seg 1, {...}seg 2, ..., {...}seg n, with n determined by method RsCmwWcdmaMeas.Configure.MultiEval.ListPy.
		count. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:MEASurement<Instance>:MEValuation:LIST:MODulation:SDEViation?', self.__class__.FetchStruct())
