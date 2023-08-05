from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TaueEutra:
	"""TaueEutra commands group definition. 22 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("taueEutra", core, parent)

	@property
	def player(self):
		"""player commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_player'):
			from .TaueEutra_.Player import Player
			self._player = Player(self._core, self._base)
		return self._player

	@property
	def fgIndicators(self):
		"""fgIndicators commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_fgIndicators'):
			from .TaueEutra_.FgIndicators import FgIndicators
			self._fgIndicators = FgIndicators(self._core, self._base)
		return self._fgIndicators

	@property
	def interRat(self):
		"""interRat commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_interRat'):
			from .TaueEutra_.InterRat import InterRat
			self._interRat = InterRat(self._core, self._base)
		return self._interRat

	@property
	def ncsacq(self):
		"""ncsacq commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncsacq'):
			from .TaueEutra_.Ncsacq import Ncsacq
			self._ncsacq = Ncsacq(self._core, self._base)
		return self._ncsacq

	def clone(self) -> 'TaueEutra':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TaueEutra(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
