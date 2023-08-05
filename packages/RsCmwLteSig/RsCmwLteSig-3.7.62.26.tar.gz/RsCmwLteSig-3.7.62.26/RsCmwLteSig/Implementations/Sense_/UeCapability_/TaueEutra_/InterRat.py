from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InterRat:
	"""InterRat commands group definition. 7 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("interRat", core, parent)

	@property
	def eredirection(self):
		"""eredirection commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eredirection'):
			from .InterRat_.Eredirection import Eredirection
			self._eredirection = Eredirection(self._core, self._base)
		return self._eredirection

	@property
	def geran(self):
		"""geran commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_geran'):
			from .InterRat_.Geran import Geran
			self._geran = Geran(self._core, self._base)
		return self._geran

	@property
	def cxrtt(self):
		"""cxrtt commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_cxrtt'):
			from .InterRat_.Cxrtt import Cxrtt
			self._cxrtt = Cxrtt(self._core, self._base)
		return self._cxrtt

	def clone(self) -> 'InterRat':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InterRat(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
