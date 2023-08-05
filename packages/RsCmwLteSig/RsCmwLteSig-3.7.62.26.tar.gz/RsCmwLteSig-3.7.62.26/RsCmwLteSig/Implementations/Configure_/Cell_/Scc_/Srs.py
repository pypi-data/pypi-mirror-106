from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Srs:
	"""Srs commands group definition. 9 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("srs", core, parent)

	@property
	def dconfig(self):
		"""dconfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dconfig'):
			from .Srs_.Dconfig import Dconfig
			self._dconfig = Dconfig(self._core, self._base)
		return self._dconfig

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Srs_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def bwConfig(self):
		"""bwConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwConfig'):
			from .Srs_.BwConfig import BwConfig
			self._bwConfig = BwConfig(self._core, self._base)
		return self._bwConfig

	@property
	def hbandwidth(self):
		"""hbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hbandwidth'):
			from .Srs_.Hbandwidth import Hbandwidth
			self._hbandwidth = Hbandwidth(self._core, self._base)
		return self._hbandwidth

	@property
	def mcEnable(self):
		"""mcEnable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcEnable'):
			from .Srs_.McEnable import McEnable
			self._mcEnable = McEnable(self._core, self._base)
		return self._mcEnable

	@property
	def sfConfig(self):
		"""sfConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfConfig'):
			from .Srs_.SfConfig import SfConfig
			self._sfConfig = SfConfig(self._core, self._base)
		return self._sfConfig

	@property
	def scIndex(self):
		"""scIndex commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scIndex'):
			from .Srs_.ScIndex import ScIndex
			self._scIndex = ScIndex(self._core, self._base)
		return self._scIndex

	@property
	def poffset(self):
		"""poffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_poffset'):
			from .Srs_.Poffset import Poffset
			self._poffset = Poffset(self._core, self._base)
		return self._poffset

	def clone(self) -> 'Srs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Srs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
