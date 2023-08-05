from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcc:
	"""Pcc commands group definition. 24 total commands, 5 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcc", core, parent)

	@property
	def afBands(self):
		"""afBands commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_afBands'):
			from .Pcc_.AfBands import AfBands
			self._afBands = AfBands(self._core, self._base)
		return self._afBands

	@property
	def userDefined(self):
		"""userDefined commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_userDefined'):
			from .Pcc_.UserDefined import UserDefined
			self._userDefined = UserDefined(self._core, self._base)
		return self._userDefined

	@property
	def eattenuation(self):
		"""eattenuation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Pcc_.Eattenuation import Eattenuation
			self._eattenuation = Eattenuation(self._core, self._base)
		return self._eattenuation

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_channel'):
			from .Pcc_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def foffset(self):
		"""foffset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_foffset'):
			from .Pcc_.Foffset import Foffset
			self._foffset = Foffset(self._core, self._base)
		return self._foffset

	def get_mixer_level_offset(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:MLOFfset \n
		Snippet: value: int = driver.configure.rfSettings.pcc.get_mixer_level_offset() \n
		Varies the input level of the mixer in the analyzer path. \n
			:return: mix_lev_offset: Range: -10 dB to 10 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:MLOFfset?')
		return Conversions.str_to_int(response)

	def set_mixer_level_offset(self, mix_lev_offset: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:MLOFfset \n
		Snippet: driver.configure.rfSettings.pcc.set_mixer_level_offset(mix_lev_offset = 1) \n
		Varies the input level of the mixer in the analyzer path. \n
			:param mix_lev_offset: Range: -10 dB to 10 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(mix_lev_offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:MLOFfset {param}')

	def get_ud_separation(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDSeparation \n
		Snippet: value: int = driver.configure.rfSettings.pcc.get_ud_separation() \n
		Configures the UL/DL separation. For most operating bands, this setting is fixed. \n
			:return: frequency: UL/DL separation Range: see table , Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDSeparation?')
		return Conversions.str_to_int(response)

	def set_ud_separation(self, frequency: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDSeparation \n
		Snippet: driver.configure.rfSettings.pcc.set_ud_separation(frequency = 1) \n
		Configures the UL/DL separation. For most operating bands, this setting is fixed. \n
			:param frequency: UL/DL separation Range: see table , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDSeparation {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.pcc.get_envelope_power() \n
		Sets the expected nominal power of the UL signal in manual mode. If the expected nominal power is calculated
		automatically according to the UL power control settings, you can only query the result. To configure the expected
		nominal power mode, see CONFigure:LTE:SIGN<i>:ENPMode. \n
			:return: expected_power: In manual mode, the range of the expected nominal power can be calculated as follows: Range (expected nominal power) = range (input power) + external attenuation - margin The input power range is stated in the data sheet. Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, expected_power: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:ENPower \n
		Snippet: driver.configure.rfSettings.pcc.set_envelope_power(expected_power = 1.0) \n
		Sets the expected nominal power of the UL signal in manual mode. If the expected nominal power is calculated
		automatically according to the UL power control settings, you can only query the result. To configure the expected
		nominal power mode, see CONFigure:LTE:SIGN<i>:ENPMode. \n
			:param expected_power: In manual mode, the range of the expected nominal power can be calculated as follows: Range (expected nominal power) = range (input power) + external attenuation - margin The input power range is stated in the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(expected_power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:ENPower {param}')

	# noinspection PyTypeChecker
	def get_enp_mode(self) -> enums.NominalPowerMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:ENPMode \n
		Snippet: value: enums.NominalPowerMode = driver.configure.rfSettings.pcc.get_enp_mode() \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- CONFigure:LTE:SIGN<i>:ENPower
			- CONFigure:LTE:SIGN<i>:UMARgin
		For UL power control settings, see 'Uplink Power Control'. \n
			:return: mode: MANual | ULPC MANual The expected nominal power and margin are specified manually. ULPC The expected nominal power is calculated according to the UL power control settings. For the margin, 12 dB are applied.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:ENPMode?')
		return Conversions.str_to_scalar_enum(response, enums.NominalPowerMode)

	def set_enp_mode(self, mode: enums.NominalPowerMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:ENPMode \n
		Snippet: driver.configure.rfSettings.pcc.set_enp_mode(mode = enums.NominalPowerMode.AUToranging) \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- CONFigure:LTE:SIGN<i>:ENPower
			- CONFigure:LTE:SIGN<i>:UMARgin
		For UL power control settings, see 'Uplink Power Control'. \n
			:param mode: MANual | ULPC MANual The expected nominal power and margin are specified manually. ULPC The expected nominal power is calculated according to the UL power control settings. For the margin, 12 dB are applied.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NominalPowerMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:ENPMode {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.pcc.get_umargin() \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode.
		If the expected nominal power is calculated automatically according to the UL power control settings, a fix margin of 12
		dB is used instead. The reference level minus the external input attenuation must be within the power range of the
		selected input connector; refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- CONFigure:LTE:SIGN<i>:ENPMode
			- CONFigure:LTE:SIGN<i>:ENPower
			- CONFigure:LTE:SIGN<i>:EATTenuation:INPut \n
			:return: user_margin: Range: 0 dB to (42 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UMARgin \n
		Snippet: driver.configure.rfSettings.pcc.set_umargin(user_margin = 1.0) \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode.
		If the expected nominal power is calculated automatically according to the UL power control settings, a fix margin of 12
		dB is used instead. The reference level minus the external input attenuation must be within the power range of the
		selected input connector; refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- CONFigure:LTE:SIGN<i>:ENPMode
			- CONFigure:LTE:SIGN<i>:ENPower
			- CONFigure:LTE:SIGN<i>:EATTenuation:INPut \n
			:param user_margin: Range: 0 dB to (42 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UMARgin {param}')

	def clone(self) -> 'Pcc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
