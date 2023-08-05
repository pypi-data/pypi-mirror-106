from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sib:
	"""Sib commands group definition. 5 total commands, 4 Sub-groups, 0 group commands
	Repeated Capability: SystemInfoBlock, default value after init: SystemInfoBlock.Sib8"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sib", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_systemInfoBlock_get', 'repcap_systemInfoBlock_set', repcap.SystemInfoBlock.Sib8)

	def repcap_systemInfoBlock_set(self, enum_value: repcap.SystemInfoBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SystemInfoBlock.Default
		Default value after init: SystemInfoBlock.Sib8"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_systemInfoBlock_get(self) -> repcap.SystemInfoBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Sib_.Update import Update
			self._update = Update(self._core, self._base)
		return self._update

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Sib_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def syst(self):
		"""syst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_syst'):
			from .Sib_.Syst import Syst
			self._syst = Syst(self._core, self._base)
		return self._syst

	@property
	def tnfo(self):
		"""tnfo commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tnfo'):
			from .Sib_.Tnfo import Tnfo
			self._tnfo = Tnfo(self._core, self._base)
		return self._tnfo

	def clone(self) -> 'Sib':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sib(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
