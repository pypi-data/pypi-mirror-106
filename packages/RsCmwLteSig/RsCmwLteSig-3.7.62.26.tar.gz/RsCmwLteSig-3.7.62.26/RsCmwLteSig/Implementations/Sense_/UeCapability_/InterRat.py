from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InterRat:
	"""InterRat commands group definition. 18 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("interRat", core, parent)

	@property
	def ufdd(self):
		"""ufdd commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ufdd'):
			from .InterRat_.Ufdd import Ufdd
			self._ufdd = Ufdd(self._core, self._base)
		return self._ufdd

	@property
	def utdd(self):
		"""utdd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_utdd'):
			from .InterRat_.Utdd import Utdd
			self._utdd = Utdd(self._core, self._base)
		return self._utdd

	@property
	def geran(self):
		"""geran commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_geran'):
			from .InterRat_.Geran import Geran
			self._geran = Geran(self._core, self._base)
		return self._geran

	@property
	def chrpd(self):
		"""chrpd commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_chrpd'):
			from .InterRat_.Chrpd import Chrpd
			self._chrpd = Chrpd(self._core, self._base)
		return self._chrpd

	@property
	def cxrtt(self):
		"""cxrtt commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_cxrtt'):
			from .InterRat_.Cxrtt import Cxrtt
			self._cxrtt = Cxrtt(self._core, self._base)
		return self._cxrtt

	@property
	def cdma(self):
		"""cdma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdma'):
			from .InterRat_.Cdma import Cdma
			self._cdma = Cdma(self._core, self._base)
		return self._cdma

	def clone(self) -> 'InterRat':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InterRat(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
