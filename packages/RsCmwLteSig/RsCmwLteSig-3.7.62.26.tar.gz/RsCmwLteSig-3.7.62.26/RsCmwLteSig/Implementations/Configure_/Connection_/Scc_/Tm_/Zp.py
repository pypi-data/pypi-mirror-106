from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zp:
	"""Zp commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("zp", core, parent)

	@property
	def bits(self):
		"""bits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bits'):
			from .Zp_.Bits import Bits
			self._bits = Bits(self._core, self._base)
		return self._bits

	@property
	def csirs(self):
		"""csirs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Zp_.Csirs import Csirs
			self._csirs = Csirs(self._core, self._base)
		return self._csirs

	def clone(self) -> 'Zp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Zp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
