from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefined:
	"""UserDefined commands group definition. 10 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("userDefined", core, parent)

	@property
	def channel(self):
		"""channel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .UserDefined_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .UserDefined_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	def get_ud_separation(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:UDSeparation \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.get_ud_separation() \n
		Configures the UL/DL separation FDL - FUL for the user-defined band. The allowed range depends on the remaining
		user-defined band settings: The resulting uplink carrier center frequencies must be within the allowed frequency range.
		For calculations, see CONFigure:LTE:SIGN<i>:UDEFined:FREQuency:DL:MINimum. \n
			:return: frequency: Depending on the other settings, only a part of the following range is allowed. Range: -5930 MHz to 5930 MHz , Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:UDSeparation?')
		return Conversions.str_to_int(response)

	def set_ud_separation(self, frequency: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:UDSeparation \n
		Snippet: driver.configure.rfSettings.pcc.userDefined.set_ud_separation(frequency = 1) \n
		Configures the UL/DL separation FDL - FUL for the user-defined band. The allowed range depends on the remaining
		user-defined band settings: The resulting uplink carrier center frequencies must be within the allowed frequency range.
		For calculations, see CONFigure:LTE:SIGN<i>:UDEFined:FREQuency:DL:MINimum. \n
			:param frequency: Depending on the other settings, only a part of the following range is allowed. Range: -5930 MHz to 5930 MHz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:UDSeparation {param}')

	def get_bindicator(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:BINDicator \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.get_bindicator() \n
		Configures the frequency band indicator, identifying the user-defined band in signaling messages. \n
			:return: band_indicator: Range: 1 to 256
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:BINDicator?')
		return Conversions.str_to_int(response)

	def set_bindicator(self, band_indicator: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:BINDicator \n
		Snippet: driver.configure.rfSettings.pcc.userDefined.set_bindicator(band_indicator = 1) \n
		Configures the frequency band indicator, identifying the user-defined band in signaling messages. \n
			:param band_indicator: Range: 1 to 256
		"""
		param = Conversions.decimal_value_to_str(band_indicator)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:BINDicator {param}')

	def clone(self) -> 'UserDefined':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefined(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
