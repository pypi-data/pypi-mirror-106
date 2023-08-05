from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmtc:
	"""Rmtc commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rmtc", core, parent)

	@property
	def period(self):
		"""period commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_period'):
			from .Rmtc_.Period import Period
			self._period = Period(self._core, self._base)
		return self._period

	@property
	def soffset(self):
		"""soffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soffset'):
			from .Rmtc_.Soffset import Soffset
			self._soffset = Soffset(self._core, self._base)
		return self._soffset

	def clone(self) -> 'Rmtc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rmtc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
