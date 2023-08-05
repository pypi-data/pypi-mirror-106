from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 55 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connection", core, parent)

	@property
	def pcc(self):
		"""pcc commands group. 9 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcc'):
			from .Connection_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	@property
	def scc(self):
		"""scc commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Connection_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def ethroughput(self):
		"""ethroughput commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ethroughput'):
			from .Connection_.Ethroughput import Ethroughput
			self._ethroughput = Ethroughput(self._core, self._base)
		return self._ethroughput

	def clone(self) -> 'Connection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Connection(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
