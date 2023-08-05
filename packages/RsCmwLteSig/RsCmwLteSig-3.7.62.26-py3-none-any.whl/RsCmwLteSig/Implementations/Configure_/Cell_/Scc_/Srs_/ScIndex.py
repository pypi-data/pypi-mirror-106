from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScIndex:
	"""ScIndex commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scIndex", core, parent)

	@property
	def fdd(self):
		"""fdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdd'):
			from .ScIndex_.Fdd import Fdd
			self._fdd = Fdd(self._core, self._base)
		return self._fdd

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdd'):
			from .ScIndex_.Tdd import Tdd
			self._tdd = Tdd(self._core, self._base)
		return self._tdd

	def clone(self) -> 'ScIndex':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScIndex(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
