from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeReport:
	"""UeReport commands group definition. 24 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueReport", core, parent)

	@property
	def pcc(self):
		"""pcc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcc'):
			from .UeReport_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	@property
	def scc(self):
		"""scc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .UeReport_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def ncell(self):
		"""ncell commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ncell'):
			from .UeReport_.Ncell import Ncell
			self._ncell = Ncell(self._core, self._base)
		return self._ncell

	def clone(self) -> 'UeReport':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeReport(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
