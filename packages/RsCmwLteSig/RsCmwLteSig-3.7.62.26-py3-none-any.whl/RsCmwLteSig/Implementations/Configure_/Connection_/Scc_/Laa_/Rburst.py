from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rburst:
	"""Rburst commands group definition. 5 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rburst", core, parent)

	@property
	def psfConfig(self):
		"""psfConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psfConfig'):
			from .Rburst_.PsfConfig import PsfConfig
			self._psfConfig = PsfConfig(self._core, self._base)
		return self._psfConfig

	@property
	def blength(self):
		"""blength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blength'):
			from .Rburst_.Blength import Blength
			self._blength = Blength(self._core, self._base)
		return self._blength

	@property
	def lsConfig(self):
		"""lsConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lsConfig'):
			from .Rburst_.LsConfig import LsConfig
			self._lsConfig = LsConfig(self._core, self._base)
		return self._lsConfig

	@property
	def ipSubframe(self):
		"""ipSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipSubframe'):
			from .Rburst_.IpSubframe import IpSubframe
			self._ipSubframe = IpSubframe(self._core, self._base)
		return self._ipSubframe

	@property
	def tprobability(self):
		"""tprobability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tprobability'):
			from .Rburst_.Tprobability import Tprobability
			self._tprobability = Tprobability(self._core, self._base)
		return self._tprobability

	def clone(self) -> 'Rburst':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rburst(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
