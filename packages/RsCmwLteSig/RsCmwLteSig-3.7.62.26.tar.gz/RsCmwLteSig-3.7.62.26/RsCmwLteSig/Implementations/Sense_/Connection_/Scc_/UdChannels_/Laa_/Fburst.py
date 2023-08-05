from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fburst:
	"""Fburst commands group definition. 3 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fburst", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Fburst_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	def clone(self) -> 'Fburst':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fburst(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
