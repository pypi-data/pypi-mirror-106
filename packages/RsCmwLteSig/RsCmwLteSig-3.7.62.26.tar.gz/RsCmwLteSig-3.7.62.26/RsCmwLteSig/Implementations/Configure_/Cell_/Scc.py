from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 21 total commands, 10 Sub-groups, 0 group commands
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
	def pcid(self):
		"""pcid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcid'):
			from .Scc_.Pcid import Pcid
			self._pcid = Pcid(self._core, self._base)
		return self._pcid

	@property
	def ulDl(self):
		"""ulDl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDl'):
			from .Scc_.UlDl import UlDl
			self._ulDl = UlDl(self._core, self._base)
		return self._ulDl

	@property
	def ssubframe(self):
		"""ssubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssubframe'):
			from .Scc_.Ssubframe import Ssubframe
			self._ssubframe = Ssubframe(self._core, self._base)
		return self._ssubframe

	@property
	def csat(self):
		"""csat commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_csat'):
			from .Scc_.Csat import Csat
			self._csat = Csat(self._core, self._base)
		return self._csat

	@property
	def scMuting(self):
		"""scMuting commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_scMuting'):
			from .Scc_.ScMuting import ScMuting
			self._scMuting = ScMuting(self._core, self._base)
		return self._scMuting

	@property
	def ulSupport(self):
		"""ulSupport commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulSupport'):
			from .Scc_.UlSupport import UlSupport
			self._ulSupport = UlSupport(self._core, self._base)
		return self._ulSupport

	@property
	def srs(self):
		"""srs commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Scc_.Srs import Srs
			self._srs = Srs(self._core, self._base)
		return self._srs

	@property
	def dbandwidth(self):
		"""dbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbandwidth'):
			from .Scc_.Dbandwidth import Dbandwidth
			self._dbandwidth = Dbandwidth(self._core, self._base)
		return self._dbandwidth

	@property
	def cid(self):
		"""cid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cid'):
			from .Scc_.Cid import Cid
			self._cid = Cid(self._core, self._base)
		return self._cid

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Scc_.Sync import Sync
			self._sync = Sync(self._core, self._base)
		return self._sync

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
