from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fwbcqi:
	"""Fwbcqi commands group definition. 4 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fwbcqi", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Fwbcqi_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	def clone(self) -> 'Fwbcqi':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fwbcqi(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
