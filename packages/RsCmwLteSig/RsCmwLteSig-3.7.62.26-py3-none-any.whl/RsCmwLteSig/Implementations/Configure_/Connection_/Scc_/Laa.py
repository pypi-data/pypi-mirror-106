from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Laa:
	"""Laa commands group definition. 10 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("laa", core, parent)

	@property
	def tbursts(self):
		"""tbursts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbursts'):
			from .Laa_.Tbursts import Tbursts
			self._tbursts = Tbursts(self._core, self._base)
		return self._tbursts

	@property
	def rburst(self):
		"""rburst commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_rburst'):
			from .Laa_.Rburst import Rburst
			self._rburst = Rburst(self._core, self._base)
		return self._rburst

	@property
	def fburst(self):
		"""fburst commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fburst'):
			from .Laa_.Fburst import Fburst
			self._fburst = Fburst(self._core, self._base)
		return self._fburst

	def clone(self) -> 'Laa':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Laa(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
