from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 21 total commands, 9 Sub-groups, 0 group commands
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
	def userDefined(self):
		"""userDefined commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_userDefined'):
			from .Scc_.UserDefined import UserDefined
			self._userDefined = UserDefined(self._core, self._base)
		return self._userDefined

	@property
	def mixerLevelOffset(self):
		"""mixerLevelOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mixerLevelOffset'):
			from .Scc_.MixerLevelOffset import MixerLevelOffset
			self._mixerLevelOffset = MixerLevelOffset(self._core, self._base)
		return self._mixerLevelOffset

	@property
	def eattenuation(self):
		"""eattenuation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Scc_.Eattenuation import Eattenuation
			self._eattenuation = Eattenuation(self._core, self._base)
		return self._eattenuation

	@property
	def channel(self):
		"""channel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Scc_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def foffset(self):
		"""foffset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_foffset'):
			from .Scc_.Foffset import Foffset
			self._foffset = Foffset(self._core, self._base)
		return self._foffset

	@property
	def udSeparation(self):
		"""udSeparation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udSeparation'):
			from .Scc_.UdSeparation import UdSeparation
			self._udSeparation = UdSeparation(self._core, self._base)
		return self._udSeparation

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_envelopePower'):
			from .Scc_.EnvelopePower import EnvelopePower
			self._envelopePower = EnvelopePower(self._core, self._base)
		return self._envelopePower

	@property
	def enpMode(self):
		"""enpMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enpMode'):
			from .Scc_.EnpMode import EnpMode
			self._enpMode = EnpMode(self._core, self._base)
		return self._enpMode

	@property
	def umargin(self):
		"""umargin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_umargin'):
			from .Scc_.Umargin import Umargin
			self._umargin = Umargin(self._core, self._base)
		return self._umargin

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
