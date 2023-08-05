from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcc:
	"""Pcc commands group definition. 14 total commands, 10 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcc", core, parent)

	@property
	def rsepre(self):
		"""rsepre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsepre'):
			from .Pcc_.Rsepre import Rsepre
			self._rsepre = Rsepre(self._core, self._base)
		return self._rsepre

	@property
	def pss(self):
		"""pss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pss'):
			from .Pcc_.Pss import Pss
			self._pss = Pss(self._core, self._base)
		return self._pss

	@property
	def sss(self):
		"""sss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sss'):
			from .Pcc_.Sss import Sss
			self._sss = Sss(self._core, self._base)
		return self._sss

	@property
	def pbch(self):
		"""pbch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbch'):
			from .Pcc_.Pbch import Pbch
			self._pbch = Pbch(self._core, self._base)
		return self._pbch

	@property
	def pcfich(self):
		"""pcfich commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcfich'):
			from .Pcc_.Pcfich import Pcfich
			self._pcfich = Pcfich(self._core, self._base)
		return self._pcfich

	@property
	def phich(self):
		"""phich commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phich'):
			from .Pcc_.Phich import Phich
			self._phich = Phich(self._core, self._base)
		return self._phich

	@property
	def pdcch(self):
		"""pdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pcc_.Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._base)
		return self._pdcch

	@property
	def pdsch(self):
		"""pdsch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pdsch'):
			from .Pcc_.Pdsch import Pdsch
			self._pdsch = Pdsch(self._core, self._base)
		return self._pdsch

	@property
	def csirs(self):
		"""csirs commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_csirs'):
			from .Pcc_.Csirs import Csirs
			self._csirs = Csirs(self._core, self._base)
		return self._csirs

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Pcc_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	def get_ocng(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:OCNG \n
		Snippet: value: bool = driver.configure.downlink.pcc.get_ocng() \n
		Enables or disables the OFDMA channel noise generator (OCNG) . \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:OCNG?')
		return Conversions.str_to_bool(response)

	def set_ocng(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:OCNG \n
		Snippet: driver.configure.downlink.pcc.set_ocng(enable = False) \n
		Enables or disables the OFDMA channel noise generator (OCNG) . \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:OCNG {param}')

	def get_awgn(self) -> float or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:AWGN \n
		Snippet: value: float or bool = driver.configure.downlink.pcc.get_awgn() \n
		Specifies the total level of the additional white Gaussian noise (AWGN) interferer. The unit dBm/15 kHz indicates the
		spectral density integrated across one subcarrier. The range depends on several parameters. It either equals the range of
		the RS EPRE or is a part of this range. \n
			:return: awgn: Range: depends on many parameters , Unit: dBm/15kHz Additional parameters: OFF | ON (disables | enables the AWGN interferer)
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:AWGN?')
		return Conversions.str_to_float_or_bool(response)

	def set_awgn(self, awgn: float or bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:AWGN \n
		Snippet: driver.configure.downlink.pcc.set_awgn(awgn = 1.0) \n
		Specifies the total level of the additional white Gaussian noise (AWGN) interferer. The unit dBm/15 kHz indicates the
		spectral density integrated across one subcarrier. The range depends on several parameters. It either equals the range of
		the RS EPRE or is a part of this range. \n
			:param awgn: Range: depends on many parameters , Unit: dBm/15kHz Additional parameters: OFF | ON (disables | enables the AWGN interferer)
		"""
		param = Conversions.decimal_or_bool_value_to_str(awgn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:AWGN {param}')

	def clone(self) -> 'Pcc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
