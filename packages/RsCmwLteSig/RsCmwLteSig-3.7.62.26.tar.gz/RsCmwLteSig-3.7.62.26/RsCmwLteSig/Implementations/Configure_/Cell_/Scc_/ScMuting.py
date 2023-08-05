from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScMuting:
	"""ScMuting commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scMuting", core, parent)

	@property
	def onsDuration(self):
		"""onsDuration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_onsDuration'):
			from .ScMuting_.OnsDuration import OnsDuration
			self._onsDuration = OnsDuration(self._core, self._base)
		return self._onsDuration

	@property
	def offsDuration(self):
		"""offsDuration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offsDuration'):
			from .ScMuting_.OffsDuration import OffsDuration
			self._offsDuration = OffsDuration(self._core, self._base)
		return self._offsDuration

	@property
	def pmac(self):
		"""pmac commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmac'):
			from .ScMuting_.Pmac import Pmac
			self._pmac = Pmac(self._core, self._base)
		return self._pmac

	def clone(self) -> 'ScMuting':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScMuting(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
