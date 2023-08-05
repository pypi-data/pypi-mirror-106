from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 5 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prach", core, parent)

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_foffset'):
			from .Prach_.Foffset import Foffset
			self._foffset = Foffset(self._core, self._base)
		return self._foffset

	@property
	def mpAttempts(self):
		"""mpAttempts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpAttempts'):
			from .Prach_.MpAttempts import MpAttempts
			self._mpAttempts = MpAttempts(self._core, self._base)
		return self._mpAttempts

	@property
	def rpAttempt(self):
		"""rpAttempt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpAttempt'):
			from .Prach_.RpAttempt import RpAttempt
			self._rpAttempt = RpAttempt(self._core, self._base)
		return self._rpAttempt

	@property
	def mmrRepetition(self):
		"""mmrRepetition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmrRepetition'):
			from .Prach_.MmrRepetition import MmrRepetition
			self._mmrRepetition = MmrRepetition(self._core, self._base)
		return self._mmrRepetition

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cindex'):
			from .Prach_.Cindex import Cindex
			self._cindex = Cindex(self._core, self._base)
		return self._cindex

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
