from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hopping:
	"""Hopping commands group definition. 8 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hopping", core, parent)

	@property
	def uplink(self):
		"""uplink commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_uplink'):
			from .Hopping_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_downlink'):
			from .Hopping_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	def clone(self) -> 'Hopping':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hopping(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
