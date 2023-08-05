from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 13 total commands, 9 Sub-groups, 0 group commands
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
	def confidence(self):
		"""confidence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_confidence'):
			from .Scc_.Confidence import Confidence
			self._confidence = Confidence(self._core, self._base)
		return self._confidence

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Scc_.Absolute import Absolute
			self._absolute = Absolute(self._core, self._base)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Scc_.Relative import Relative
			self._relative = Relative(self._core, self._base)
		return self._relative

	@property
	def stream(self):
		"""stream commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_stream'):
			from .Scc_.Stream import Stream
			self._stream = Stream(self._core, self._base)
		return self._stream

	@property
	def harq(self):
		"""harq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Scc_.Harq import Harq
			self._harq = Harq(self._core, self._base)
		return self._harq

	@property
	def cqiReporting(self):
		"""cqiReporting commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqiReporting'):
			from .Scc_.CqiReporting import CqiReporting
			self._cqiReporting = CqiReporting(self._core, self._base)
		return self._cqiReporting

	@property
	def ri(self):
		"""ri commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ri'):
			from .Scc_.Ri import Ri
			self._ri = Ri(self._core, self._base)
		return self._ri

	@property
	def pmi(self):
		"""pmi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmi'):
			from .Scc_.Pmi import Pmi
			self._pmi = Pmi(self._core, self._base)
		return self._pmi

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Scc_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
