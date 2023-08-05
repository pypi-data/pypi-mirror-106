from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 14 total commands, 12 Sub-groups, 0 group commands
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
	def rsepre(self):
		"""rsepre commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsepre'):
			from .Scc_.Rsepre import Rsepre
			self._rsepre = Rsepre(self._core, self._base)
		return self._rsepre

	@property
	def pss(self):
		"""pss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pss'):
			from .Scc_.Pss import Pss
			self._pss = Pss(self._core, self._base)
		return self._pss

	@property
	def sss(self):
		"""sss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sss'):
			from .Scc_.Sss import Sss
			self._sss = Sss(self._core, self._base)
		return self._sss

	@property
	def pbch(self):
		"""pbch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pbch'):
			from .Scc_.Pbch import Pbch
			self._pbch = Pbch(self._core, self._base)
		return self._pbch

	@property
	def pcfich(self):
		"""pcfich commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcfich'):
			from .Scc_.Pcfich import Pcfich
			self._pcfich = Pcfich(self._core, self._base)
		return self._pcfich

	@property
	def phich(self):
		"""phich commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phich'):
			from .Scc_.Phich import Phich
			self._phich = Phich(self._core, self._base)
		return self._phich

	@property
	def pdcch(self):
		"""pdcch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Scc_.Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._base)
		return self._pdcch

	@property
	def pdsch(self):
		"""pdsch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Scc_.Pdsch import Pdsch
			self._pdsch = Pdsch(self._core, self._base)
		return self._pdsch

	@property
	def csirs(self):
		"""csirs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Scc_.Csirs import Csirs
			self._csirs = Csirs(self._core, self._base)
		return self._csirs

	@property
	def ocng(self):
		"""ocng commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ocng'):
			from .Scc_.Ocng import Ocng
			self._ocng = Ocng(self._core, self._base)
		return self._ocng

	@property
	def awgn(self):
		"""awgn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_awgn'):
			from .Scc_.Awgn import Awgn
			self._awgn = Awgn(self._core, self._base)
		return self._awgn

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Scc_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
