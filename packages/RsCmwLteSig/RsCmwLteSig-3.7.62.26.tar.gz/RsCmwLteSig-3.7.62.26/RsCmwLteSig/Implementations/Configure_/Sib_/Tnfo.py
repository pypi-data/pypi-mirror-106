from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tnfo:
	"""Tnfo commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tnfo", core, parent)

	@property
	def utc(self):
		"""utc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_utc'):
			from .Tnfo_.Utc import Utc
			self._utc = Utc(self._core, self._base)
		return self._utc

	@property
	def leap(self):
		"""leap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_leap'):
			from .Tnfo_.Leap import Leap
			self._leap = Leap(self._core, self._base)
		return self._leap

	def clone(self) -> 'Tnfo':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tnfo(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
