from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 7 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Level_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def qrxlevmin(self):
		"""qrxlevmin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qrxlevmin'):
			from .Level_.Qrxlevmin import Qrxlevmin
			self._qrxlevmin = Qrxlevmin(self._core, self._base)
		return self._qrxlevmin

	@property
	def prach(self):
		"""prach commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_prach'):
			from .Level_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
