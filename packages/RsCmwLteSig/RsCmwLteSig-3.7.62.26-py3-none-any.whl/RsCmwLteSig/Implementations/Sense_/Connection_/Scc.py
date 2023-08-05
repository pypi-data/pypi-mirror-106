from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 25 total commands, 8 Sub-groups, 0 group commands
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
	def hpusch(self):
		"""hpusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hpusch'):
			from .Scc_.Hpusch import Hpusch
			self._hpusch = Hpusch(self._core, self._base)
		return self._hpusch

	@property
	def tscheme(self):
		"""tscheme commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tscheme'):
			from .Scc_.Tscheme import Tscheme
			self._tscheme = Tscheme(self._core, self._base)
		return self._tscheme

	@property
	def udChannels(self):
		"""udChannels commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_udChannels'):
			from .Scc_.UdChannels import UdChannels
			self._udChannels = UdChannels(self._core, self._base)
		return self._udChannels

	@property
	def udttiBased(self):
		"""udttiBased commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_udttiBased'):
			from .Scc_.UdttiBased import UdttiBased
			self._udttiBased = UdttiBased(self._core, self._base)
		return self._udttiBased

	@property
	def fwbcqi(self):
		"""fwbcqi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fwbcqi'):
			from .Scc_.Fwbcqi import Fwbcqi
			self._fwbcqi = Fwbcqi(self._core, self._base)
		return self._fwbcqi

	@property
	def fcri(self):
		"""fcri commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcri'):
			from .Scc_.Fcri import Fcri
			self._fcri = Fcri(self._core, self._base)
		return self._fcri

	@property
	def fcpri(self):
		"""fcpri commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fcpri'):
			from .Scc_.Fcpri import Fcpri
			self._fcpri = Fcpri(self._core, self._base)
		return self._fcpri

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
