from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpc:
	"""Tpc commands group definition. 8 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tpc", core, parent)

	@property
	def set(self):
		"""set commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_set'):
			from .Tpc_.Set import Set
			self._set = Set(self._core, self._base)
		return self._set

	@property
	def pexecute(self):
		"""pexecute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pexecute'):
			from .Tpc_.Pexecute import Pexecute
			self._pexecute = Pexecute(self._core, self._base)
		return self._pexecute

	@property
	def rpControl(self):
		"""rpControl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpControl'):
			from .Tpc_.RpControl import RpControl
			self._rpControl = RpControl(self._core, self._base)
		return self._rpControl

	@property
	def single(self):
		"""single commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_single'):
			from .Tpc_.Single import Single
			self._single = Single(self._core, self._base)
		return self._single

	@property
	def cltPower(self):
		"""cltPower commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cltPower'):
			from .Tpc_.CltPower import CltPower
			self._cltPower = CltPower(self._core, self._base)
		return self._cltPower

	@property
	def udPattern(self):
		"""udPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udPattern'):
			from .Tpc_.UdPattern import UdPattern
			self._udPattern = UdPattern(self._core, self._base)
		return self._udPattern

	@property
	def tpower(self):
		"""tpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpower'):
			from .Tpc_.Tpower import Tpower
			self._tpower = Tpower(self._core, self._base)
		return self._tpower

	def clone(self) -> 'Tpc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tpc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
