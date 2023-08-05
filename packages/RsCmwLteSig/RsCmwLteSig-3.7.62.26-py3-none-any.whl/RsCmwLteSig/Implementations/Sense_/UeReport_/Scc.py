from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 8 total commands, 5 Sub-groups, 0 group commands
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
	def rsrp(self):
		"""rsrp commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsrp'):
			from .Scc_.Rsrp import Rsrp
			self._rsrp = Rsrp(self._core, self._base)
		return self._rsrp

	@property
	def rsrq(self):
		"""rsrq commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsrq'):
			from .Scc_.Rsrq import Rsrq
			self._rsrq = Rsrq(self._core, self._base)
		return self._rsrq

	@property
	def scell(self):
		"""scell commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_scell'):
			from .Scc_.Scell import Scell
			self._scell = Scell(self._core, self._base)
		return self._scell

	@property
	def cocc(self):
		"""cocc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cocc'):
			from .Scc_.Cocc import Cocc
			self._cocc = Cocc(self._core, self._base)
		return self._cocc

	@property
	def rresult(self):
		"""rresult commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rresult'):
			from .Scc_.Rresult import Rresult
			self._rresult = Rresult(self._core, self._base)
		return self._rresult

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
