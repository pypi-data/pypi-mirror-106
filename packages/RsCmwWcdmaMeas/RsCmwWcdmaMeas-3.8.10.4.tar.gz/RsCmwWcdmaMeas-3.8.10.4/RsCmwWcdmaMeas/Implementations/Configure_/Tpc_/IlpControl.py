from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IlpControl:
	"""IlpControl commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ilpControl", core, parent)

	def get_mlength(self) -> int:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:MLENgth \n
		Snippet: value: int = driver.configure.tpc.ilpControl.get_mlength() \n
		Query the number of slots measured in 'Inner Loop Power Control' mode. The value depends on the selected TPC setup and
		the test step settings. It can only be determined while the 'Inner Loop Power Control' mode is active. In other modes INV
		is returned. \n
			:return: meas_length: decimal Range: 101 slots to 341 slots, Unit: slots
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:MLENgth?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	class TsefStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Length: int: numeric Number of TPC bits per test step Range: 100 to 170
			- Statistics: int: numeric Number of slots at the end of test step E (F) , where the minimum (maximum) output power results are measured. Range: 1 slot to 20 slots, Unit: slots"""
		__meta_args_list = [
			ArgStruct.scalar_int('Length'),
			ArgStruct.scalar_int('Statistics')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length: int = None
			self.Statistics: int = None

	def get_tsef(self) -> TsefStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSEF \n
		Snippet: value: TsefStruct = driver.configure.tpc.ilpControl.get_tsef() \n
		Configures the inner loop power control test steps E and F. For the combined signal path scenario,
		useCONFigure:WCDMa:SIGN<i>:UL:TPCSet:PCONfig:TSEF. \n
			:return: structure: for return value, see the help for TsefStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSEF?', self.__class__.TsefStruct())

	def set_tsef(self, value: TsefStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSEF \n
		Snippet: driver.configure.tpc.ilpControl.set_tsef(value = TsefStruct()) \n
		Configures the inner loop power control test steps E and F. For the combined signal path scenario,
		useCONFigure:WCDMa:SIGN<i>:UL:TPCSet:PCONfig:TSEF. \n
			:param value: see the help for TsefStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSEF', value)

	# noinspection PyTypeChecker
	class TsghStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Length: int: numeric Number of TPC bits per test step Range: 60 to 170
			- Statistics: int: numeric Number of slots at the end of test step G (H) , where the minimum (maximum) output power results are measured. Range: 1 slot to 20 slots, Unit: slots"""
		__meta_args_list = [
			ArgStruct.scalar_int('Length'),
			ArgStruct.scalar_int('Statistics')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length: int = None
			self.Statistics: int = None

	def get_tsgh(self) -> TsghStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSGH \n
		Snippet: value: TsghStruct = driver.configure.tpc.ilpControl.get_tsgh() \n
		Configures the inner loop power control test steps G and H. For the combined signal path scenario, usemethod
		RsCmwWcdmaMeas.Configure.Tpc.IlpControl.tsgh. \n
			:return: structure: for return value, see the help for TsghStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSGH?', self.__class__.TsghStruct())

	def set_tsgh(self, value: TsghStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSGH \n
		Snippet: driver.configure.tpc.ilpControl.set_tsgh(value = TsghStruct()) \n
		Configures the inner loop power control test steps G and H. For the combined signal path scenario, usemethod
		RsCmwWcdmaMeas.Configure.Tpc.IlpControl.tsgh. \n
			:param value: see the help for TsghStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSGH', value)

	def get_ts_segment(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSSegment \n
		Snippet: value: bool = driver.configure.tpc.ilpControl.get_ts_segment() \n
		Enables or disables segmentation for test steps E, F, G and H. For the combined signal path scenario,
		use CONFigure:WCDMa:SIGN<i>:UL:TPCSet:PCONfig:TSSegment. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSSegment?')
		return Conversions.str_to_bool(response)

	def set_ts_segment(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:TSSegment \n
		Snippet: driver.configure.tpc.ilpControl.set_ts_segment(enable = False) \n
		Enables or disables segmentation for test steps E, F, G and H. For the combined signal path scenario,
		use CONFigure:WCDMa:SIGN<i>:UL:TPCSet:PCONfig:TSSegment. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:TSSegment {param}')

	def get_aexecution(self) -> bool:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:AEXecution \n
		Snippet: value: bool = driver.configure.tpc.ilpControl.get_aexecution() \n
		Enables or disables automatic execution of the TPC setup for combined signal path measurements in 'Inner Loop Power
		Control' mode. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:AEXecution?')
		return Conversions.str_to_bool(response)

	def set_aexecution(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:TPC:ILPControl:AEXecution \n
		Snippet: driver.configure.tpc.ilpControl.set_aexecution(enable = False) \n
		Enables or disables automatic execution of the TPC setup for combined signal path measurements in 'Inner Loop Power
		Control' mode. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:TPC:ILPControl:AEXecution {param}')
