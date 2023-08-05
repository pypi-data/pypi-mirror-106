from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 48 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	@property
	def pcc(self):
		"""pcc commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_pcc'):
			from .RfSettings_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	@property
	def scc(self):
		"""scc commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .RfSettings_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def edc(self):
		"""edc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_edc'):
			from .RfSettings_.Edc import Edc
			self._edc = Edc(self._core, self._base)
		return self._edc

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .RfSettings_.All import All
			self._all = All(self._core, self._base)
		return self._all

	def clone(self) -> 'RfSettings':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettings(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
