from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prepare:
	"""Prepare commands group definition. 15 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prepare", core, parent)

	@property
	def handover(self):
		"""handover commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_handover'):
			from .Prepare_.Handover import Handover
			self._handover = Handover(self._core, self._base)
		return self._handover

	@property
	def connection(self):
		"""connection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Prepare_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	def clone(self) -> 'Prepare':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prepare(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
