from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcc:
	"""Pcc commands group definition. 22 total commands, 9 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcc", core, parent)

	@property
	def hpusch(self):
		"""hpusch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hpusch'):
			from .Pcc_.Hpusch import Hpusch
			self._hpusch = Hpusch(self._core, self._base)
		return self._hpusch

	@property
	def udChannels(self):
		"""udChannels commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_udChannels'):
			from .Pcc_.UdChannels import UdChannels
			self._udChannels = UdChannels(self._core, self._base)
		return self._udChannels

	@property
	def sps(self):
		"""sps commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sps'):
			from .Pcc_.Sps import Sps
			self._sps = Sps(self._core, self._base)
		return self._sps

	@property
	def udttiBased(self):
		"""udttiBased commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_udttiBased'):
			from .Pcc_.UdttiBased import UdttiBased
			self._udttiBased = UdttiBased(self._core, self._base)
		return self._udttiBased

	@property
	def fwbcqi(self):
		"""fwbcqi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fwbcqi'):
			from .Pcc_.Fwbcqi import Fwbcqi
			self._fwbcqi = Fwbcqi(self._core, self._base)
		return self._fwbcqi

	@property
	def fcri(self):
		"""fcri commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcri'):
			from .Pcc_.Fcri import Fcri
			self._fcri = Fcri(self._core, self._base)
		return self._fcri

	@property
	def fcpri(self):
		"""fcpri commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcpri'):
			from .Pcc_.Fcpri import Fcpri
			self._fcpri = Fcpri(self._core, self._base)
		return self._fcpri

	@property
	def pdcch(self):
		"""pdcch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pcc_.Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._base)
		return self._pdcch

	@property
	def pucch(self):
		"""pucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pucch'):
			from .Pcc_.Pucch import Pucch
			self._pucch = Pucch(self._core, self._base)
		return self._pucch

	# noinspection PyTypeChecker
	def get_tscheme(self) -> enums.TransmScheme:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:TSCHeme \n
		Snippet: value: enums.TransmScheme = driver.sense.connection.pcc.get_tscheme() \n
		Queries the transmission scheme. \n
			:return: scheme: SISO | SIMO | TXDiversity | OLSMultiplex | CLSMultiplex | CLSingle | SBF5 | SBF8 | DBF78 | FBF710 SISO: single input single output SIMO: single input multiple outputs (receive diversity) TXDiversity: transmit diversity OLSMultiplex: open loop spatial multiplexing CLSMultiplex: closed loop spatial multiplexing CLSingle: closed loop spatial multiplexing, single layer SBF5: single-layer beamforming (port 5) SBF8: single-layer beamforming (port 8) DBF78: dual-layer beamforming (ports 7, 8) FBF710: four-layer beamforming (ports 7 to 10)
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:TSCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.TransmScheme)

	def clone(self) -> 'Pcc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
