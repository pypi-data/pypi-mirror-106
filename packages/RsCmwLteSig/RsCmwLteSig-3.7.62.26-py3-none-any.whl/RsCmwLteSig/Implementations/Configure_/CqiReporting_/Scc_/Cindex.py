from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cindex:
	"""Cindex commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cindex", core, parent)

	@property
	def laa(self):
		"""laa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_laa'):
			from .Cindex_.Laa import Laa
			self._laa = Laa(self._core, self._base)
		return self._laa

	@property
	def fdd(self):
		"""fdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdd'):
			from .Cindex_.Fdd import Fdd
			self._fdd = Fdd(self._core, self._base)
		return self._fdd

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdd'):
			from .Cindex_.Tdd import Tdd
			self._tdd = Tdd(self._core, self._base)
		return self._tdd

	def clone(self) -> 'Cindex':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cindex(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
