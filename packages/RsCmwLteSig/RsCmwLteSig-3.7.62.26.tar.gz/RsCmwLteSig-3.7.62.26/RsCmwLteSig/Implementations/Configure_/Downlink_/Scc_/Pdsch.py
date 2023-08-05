from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdsch:
	"""Pdsch commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdsch", core, parent)

	@property
	def pa(self):
		"""pa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pa'):
			from .Pdsch_.Pa import Pa
			self._pa = Pa(self._core, self._base)
		return self._pa

	@property
	def rindex(self):
		"""rindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rindex'):
			from .Pdsch_.Rindex import Rindex
			self._rindex = Rindex(self._core, self._base)
		return self._rindex

	def clone(self) -> 'Pdsch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdsch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
