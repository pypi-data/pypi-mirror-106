from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 103 total commands, 29 Sub-groups, 0 group commands
	Repeated Capability: SecondaryCompCarrier, default value after init: SecondaryCompCarrier.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_secondaryCompCarrier_get', 'repcap_secondaryCompCarrier_set', repcap.SecondaryCompCarrier.CC1)

	def repcap_secondaryCompCarrier_set(self, enum_value: repcap.SecondaryCompCarrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCompCarrier.Default
		Default value after init: SecondaryCompCarrier.CC1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_secondaryCompCarrier_get(self) -> repcap.SecondaryCompCarrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def mcluster(self):
		"""mcluster commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcluster'):
			from .Scc_.Mcluster import Mcluster
			self._mcluster = Mcluster(self._core, self._base)
		return self._mcluster

	@property
	def stype(self):
		"""stype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stype'):
			from .Scc_.Stype import Stype
			self._stype = Stype(self._core, self._base)
		return self._stype

	@property
	def asEmission(self):
		"""asEmission commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_asEmission'):
			from .Scc_.AsEmission import AsEmission
			self._asEmission = AsEmission(self._core, self._base)
		return self._asEmission

	@property
	def sexecute(self):
		"""sexecute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sexecute'):
			from .Scc_.Sexecute import Sexecute
			self._sexecute = Sexecute(self._core, self._base)
		return self._sexecute

	@property
	def cexecute(self):
		"""cexecute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cexecute'):
			from .Scc_.Cexecute import Cexecute
			self._cexecute = Cexecute(self._core, self._base)
		return self._cexecute

	@property
	def hpusch(self):
		"""hpusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hpusch'):
			from .Scc_.Hpusch import Hpusch
			self._hpusch = Hpusch(self._core, self._base)
		return self._hpusch

	@property
	def laa(self):
		"""laa commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_laa'):
			from .Scc_.Laa import Laa
			self._laa = Laa(self._core, self._base)
		return self._laa

	@property
	def tia(self):
		"""tia commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tia'):
			from .Scc_.Tia import Tia
			self._tia = Tia(self._core, self._base)
		return self._tia

	@property
	def pzero(self):
		"""pzero commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pzero'):
			from .Scc_.Pzero import Pzero
			self._pzero = Pzero(self._core, self._base)
		return self._pzero

	@property
	def tm(self):
		"""tm commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_tm'):
			from .Scc_.Tm import Tm
			self._tm = Tm(self._core, self._base)
		return self._tm

	@property
	def dlEqual(self):
		"""dlEqual commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlEqual'):
			from .Scc_.DlEqual import DlEqual
			self._dlEqual = DlEqual(self._core, self._base)
		return self._dlEqual

	@property
	def transmission(self):
		"""transmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transmission'):
			from .Scc_.Transmission import Transmission
			self._transmission = Transmission(self._core, self._base)
		return self._transmission

	@property
	def dciFormat(self):
		"""dciFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dciFormat'):
			from .Scc_.DciFormat import DciFormat
			self._dciFormat = DciFormat(self._core, self._base)
		return self._dciFormat

	@property
	def nenbAntennas(self):
		"""nenbAntennas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nenbAntennas'):
			from .Scc_.NenbAntennas import NenbAntennas
			self._nenbAntennas = NenbAntennas(self._core, self._base)
		return self._nenbAntennas

	@property
	def noLayers(self):
		"""noLayers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noLayers'):
			from .Scc_.NoLayers import NoLayers
			self._noLayers = NoLayers(self._core, self._base)
		return self._noLayers

	@property
	def beamforming(self):
		"""beamforming commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_beamforming'):
			from .Scc_.Beamforming import Beamforming
			self._beamforming = Beamforming(self._core, self._base)
		return self._beamforming

	@property
	def pmatrix(self):
		"""pmatrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmatrix'):
			from .Scc_.Pmatrix import Pmatrix
			self._pmatrix = Pmatrix(self._core, self._base)
		return self._pmatrix

	@property
	def schModel(self):
		"""schModel commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_schModel'):
			from .Scc_.SchModel import SchModel
			self._schModel = SchModel(self._core, self._base)
		return self._schModel

	@property
	def rmc(self):
		"""rmc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmc'):
			from .Scc_.Rmc import Rmc
			self._rmc = Rmc(self._core, self._base)
		return self._rmc

	@property
	def udChannels(self):
		"""udChannels commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_udChannels'):
			from .Scc_.UdChannels import UdChannels
			self._udChannels = UdChannels(self._core, self._base)
		return self._udChannels

	@property
	def udttiBased(self):
		"""udttiBased commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_udttiBased'):
			from .Scc_.UdttiBased import UdttiBased
			self._udttiBased = UdttiBased(self._core, self._base)
		return self._udttiBased

	@property
	def qam(self):
		"""qam commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qam'):
			from .Scc_.Qam import Qam
			self._qam = Qam(self._core, self._base)
		return self._qam

	@property
	def fcttiBased(self):
		"""fcttiBased commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcttiBased'):
			from .Scc_.FcttiBased import FcttiBased
			self._fcttiBased = FcttiBased(self._core, self._base)
		return self._fcttiBased

	@property
	def fwbcqi(self):
		"""fwbcqi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fwbcqi'):
			from .Scc_.Fwbcqi import Fwbcqi
			self._fwbcqi = Fwbcqi(self._core, self._base)
		return self._fwbcqi

	@property
	def fpmi(self):
		"""fpmi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpmi'):
			from .Scc_.Fpmi import Fpmi
			self._fpmi = Fpmi(self._core, self._base)
		return self._fpmi

	@property
	def fcri(self):
		"""fcri commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcri'):
			from .Scc_.Fcri import Fcri
			self._fcri = Fcri(self._core, self._base)
		return self._fcri

	@property
	def fcpri(self):
		"""fcpri commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcpri'):
			from .Scc_.Fcpri import Fcpri
			self._fcpri = Fcpri(self._core, self._base)
		return self._fcpri

	@property
	def fpri(self):
		"""fpri commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpri'):
			from .Scc_.Fpri import Fpri
			self._fpri = Fpri(self._core, self._base)
		return self._fpri

	@property
	def pdcch(self):
		"""pdcch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Scc_.Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._base)
		return self._pdcch

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
