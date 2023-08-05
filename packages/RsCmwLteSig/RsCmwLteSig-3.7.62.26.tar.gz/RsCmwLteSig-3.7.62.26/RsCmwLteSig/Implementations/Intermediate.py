from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Intermediate:
	"""Intermediate commands group definition. 10 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("intermediate", core, parent)

	@property
	def ebler(self):
		"""ebler commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ebler'):
			from .Intermediate_.Ebler import Ebler
			self._ebler = Ebler(self._core, self._base)
		return self._ebler

	def clone(self) -> 'Intermediate':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Intermediate(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
