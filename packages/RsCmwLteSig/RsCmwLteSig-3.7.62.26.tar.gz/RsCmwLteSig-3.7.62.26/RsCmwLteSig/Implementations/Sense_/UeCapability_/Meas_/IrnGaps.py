from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IrnGaps:
	"""IrnGaps commands group definition. 10 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("irnGaps", core, parent)

	@property
	def ufdd(self):
		"""ufdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ufdd'):
			from .IrnGaps_.Ufdd import Ufdd
			self._ufdd = Ufdd(self._core, self._base)
		return self._ufdd

	@property
	def utdd(self):
		"""utdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_utdd'):
			from .IrnGaps_.Utdd import Utdd
			self._utdd = Utdd(self._core, self._base)
		return self._utdd

	@property
	def geran(self):
		"""geran commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_geran'):
			from .IrnGaps_.Geran import Geran
			self._geran = Geran(self._core, self._base)
		return self._geran

	@property
	def chrpd(self):
		"""chrpd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chrpd'):
			from .IrnGaps_.Chrpd import Chrpd
			self._chrpd = Chrpd(self._core, self._base)
		return self._chrpd

	@property
	def cxrtt(self):
		"""cxrtt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cxrtt'):
			from .IrnGaps_.Cxrtt import Cxrtt
			self._cxrtt = Cxrtt(self._core, self._base)
		return self._cxrtt

	@property
	def v(self):
		"""v commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_v'):
			from .IrnGaps_.V import V
			self._v = V(self._core, self._base)
		return self._v

	def clone(self) -> 'IrnGaps':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IrnGaps(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
