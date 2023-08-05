from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApPower:
	"""ApPower commands group definition. 8 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("apPower", core, parent)

	@property
	def rsPower(self):
		"""rsPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsPower'):
			from .ApPower_.RsPower import RsPower
			self._rsPower = RsPower(self._core, self._base)
		return self._rsPower

	@property
	def pirPower(self):
		"""pirPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pirPower'):
			from .ApPower_.PirPower import PirPower
			self._pirPower = PirPower(self._core, self._base)
		return self._pirPower

	@property
	def pnpusch(self):
		"""pnpusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pnpusch'):
			from .ApPower_.Pnpusch import Pnpusch
			self._pnpusch = Pnpusch(self._core, self._base)
		return self._pnpusch

	@property
	def pcAlpha(self):
		"""pcAlpha commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcAlpha'):
			from .ApPower_.PcAlpha import PcAlpha
			self._pcAlpha = PcAlpha(self._core, self._base)
		return self._pcAlpha

	@property
	def tprrcSetup(self):
		"""tprrcSetup commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tprrcSetup'):
			from .ApPower_.TprrcSetup import TprrcSetup
			self._tprrcSetup = TprrcSetup(self._core, self._base)
		return self._tprrcSetup

	@property
	def pathloss(self):
		"""pathloss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pathloss'):
			from .ApPower_.Pathloss import Pathloss
			self._pathloss = Pathloss(self._core, self._base)
		return self._pathloss

	@property
	def eppPower(self):
		"""eppPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eppPower'):
			from .ApPower_.EppPower import EppPower
			self._eppPower = EppPower(self._core, self._base)
		return self._eppPower

	@property
	def eoPower(self):
		"""eoPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eoPower'):
			from .ApPower_.EoPower import EoPower
			self._eoPower = EoPower(self._core, self._base)
		return self._eoPower

	def clone(self) -> 'ApPower':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApPower(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
