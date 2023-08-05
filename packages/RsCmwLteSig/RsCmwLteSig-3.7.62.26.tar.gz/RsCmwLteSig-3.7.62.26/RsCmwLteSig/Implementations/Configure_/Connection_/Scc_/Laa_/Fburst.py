from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fburst:
	"""Fburst commands group definition. 4 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fburst", core, parent)

	@property
	def blength(self):
		"""blength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blength'):
			from .Fburst_.Blength import Blength
			self._blength = Blength(self._core, self._base)
		return self._blength

	@property
	def pbtr(self):
		"""pbtr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbtr'):
			from .Fburst_.Pbtr import Pbtr
			self._pbtr = Pbtr(self._core, self._base)
		return self._pbtr

	@property
	def spfSubframe(self):
		"""spfSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spfSubframe'):
			from .Fburst_.SpfSubframe import SpfSubframe
			self._spfSubframe = SpfSubframe(self._core, self._base)
		return self._spfSubframe

	@property
	def oslSubframe(self):
		"""oslSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oslSubframe'):
			from .Fburst_.OslSubframe import OslSubframe
			self._oslSubframe = OslSubframe(self._core, self._base)
		return self._oslSubframe

	def clone(self) -> 'Fburst':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fburst(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
