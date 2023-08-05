from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeChannels:
	"""UeChannels commands group definition. 7 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueChannels", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .UeChannels_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	# noinspection PyTypeChecker
	def get_bsf_selection(self) -> enums.AutoManualMode:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:BSFSelection \n
		Snippet: value: enums.AutoManualMode = driver.configure.ueChannels.get_bsf_selection() \n
		Specifies the application controlling beta factor and spreading factor configuration in combined signal path. \n
			:return: selection: AUTO | MANual AUTO: settings controlled by WCDMA signaling MAN: settings controlled by WCDMA UE TX measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:UECHannels:BSFSelection?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_bsf_selection(self, selection: enums.AutoManualMode) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:UECHannels:BSFSelection \n
		Snippet: driver.configure.ueChannels.set_bsf_selection(selection = enums.AutoManualMode.AUTO) \n
		Specifies the application controlling beta factor and spreading factor configuration in combined signal path. \n
			:param selection: AUTO | MANual AUTO: settings controlled by WCDMA signaling MAN: settings controlled by WCDMA UE TX measurement
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.AutoManualMode)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:UECHannels:BSFSelection {param}')

	def clone(self) -> 'UeChannels':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeChannels(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
