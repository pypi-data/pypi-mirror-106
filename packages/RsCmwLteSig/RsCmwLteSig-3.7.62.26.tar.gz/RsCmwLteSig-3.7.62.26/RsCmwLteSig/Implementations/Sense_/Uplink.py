from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 40 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def scc(self):
		"""scc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Uplink_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def seta(self):
		"""seta commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_seta'):
			from .Uplink_.Seta import Seta
			self._seta = Seta(self._core, self._base)
		return self._seta

	@property
	def setb(self):
		"""setb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_setb'):
			from .Uplink_.Setb import Setb
			self._setb = Setb(self._core, self._base)
		return self._setb

	@property
	def setc(self):
		"""setc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_setc'):
			from .Uplink_.Setc import Setc
			self._setc = Setc(self._core, self._base)
		return self._setc

	@property
	def pcc(self):
		"""pcc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcc'):
			from .Uplink_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
