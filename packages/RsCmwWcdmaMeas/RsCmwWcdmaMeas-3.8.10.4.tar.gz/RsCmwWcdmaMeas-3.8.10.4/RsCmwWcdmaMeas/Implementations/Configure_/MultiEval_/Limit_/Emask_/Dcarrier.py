from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dcarrier:
	"""Dcarrier commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dcarrier", core, parent)

	# noinspection PyTypeChecker
	class AbsoluteStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Point_Ij: float or bool: numeric | ON | OFF Absolute limit line I-J referenced to a 1 MHz filter. Range: -80 dBm to 33 dBm, Unit: dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Point_Jk: float or bool: numeric | ON | OFF Absolute limit line J-K referenced to a 1 MHz filter. Range: -80 dBm to 33 dBm, Unit: dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Point_Kl: float or bool: numeric | ON | OFF Absolute limit line K-L referenced to a 1 MHz filter. Range: -80 dBm to 33 dBm, Unit: dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values
			- Point_Mn: float or bool: numeric | ON | OFF Absolute limit line M-N referenced to a 30 kHz filter. Range: -80 dBm to 33 dBm, Unit: dBm Additional OFF | ON disables/enables the limit check using the previous/default limit values"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Point_Ij'),
			ArgStruct.scalar_float_ext('Point_Jk'),
			ArgStruct.scalar_float_ext('Point_Kl'),
			ArgStruct.scalar_float_ext('Point_Mn')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Point_Ij: float or bool = None
			self.Point_Jk: float or bool = None
			self.Point_Kl: float or bool = None
			self.Point_Mn: float or bool = None

	def get_absolute(self) -> AbsoluteStruct:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:DCARrier:ABSolute \n
		Snippet: value: AbsoluteStruct = driver.configure.multiEval.limit.emask.dcarrier.get_absolute() \n
		Defines absolute limits for the spectrum emission curves of DC HSPA connections. \n
			:return: structure: for return value, see the help for AbsoluteStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:DCARrier:ABSolute?', self.__class__.AbsoluteStruct())

	def set_absolute(self, value: AbsoluteStruct) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:MEValuation:LIMit:EMASk:DCARrier:ABSolute \n
		Snippet: driver.configure.multiEval.limit.emask.dcarrier.set_absolute(value = AbsoluteStruct()) \n
		Defines absolute limits for the spectrum emission curves of DC HSPA connections. \n
			:param value: see the help for AbsoluteStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:MEASurement<Instance>:MEValuation:LIMit:EMASk:DCARrier:ABSolute', value)
