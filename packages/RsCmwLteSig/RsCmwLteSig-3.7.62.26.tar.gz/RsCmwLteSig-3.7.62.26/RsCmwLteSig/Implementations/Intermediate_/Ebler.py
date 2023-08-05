from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ebler:
	"""Ebler commands group definition. 10 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ebler", core, parent)

	@property
	def all(self):
		"""all commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .Ebler_.All import All
			self._all = All(self._core, self._base)
		return self._all

	@property
	def pcc(self):
		"""pcc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcc'):
			from .Ebler_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	@property
	def scc(self):
		"""scc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Ebler_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	def clone(self) -> 'Ebler':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ebler(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
