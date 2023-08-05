from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcc:
	"""Pcc commands group definition. 6 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcc", core, parent)

	@property
	def rsrp(self):
		"""rsrp commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rsrp'):
			from .Pcc_.Rsrp import Rsrp
			self._rsrp = Rsrp(self._core, self._base)
		return self._rsrp

	@property
	def rsrq(self):
		"""rsrq commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rsrq'):
			from .Pcc_.Rsrq import Rsrq
			self._rsrq = Rsrq(self._core, self._base)
		return self._rsrq

	@property
	def scell(self):
		"""scell commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scell'):
			from .Pcc_.Scell import Scell
			self._scell = Scell(self._core, self._base)
		return self._scell

	def clone(self) -> 'Pcc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
