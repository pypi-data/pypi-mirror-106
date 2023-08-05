from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmc:
	"""Rmc commands group definition. 6 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rmc", core, parent)

	@property
	def mcluster(self):
		"""mcluster commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcluster'):
			from .Rmc_.Mcluster import Mcluster
			self._mcluster = Mcluster(self._core, self._base)
		return self._mcluster

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Rmc_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def rbPosition(self):
		"""rbPosition commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rbPosition'):
			from .Rmc_.RbPosition import RbPosition
			self._rbPosition = RbPosition(self._core, self._base)
		return self._rbPosition

	@property
	def version(self):
		"""version commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_version'):
			from .Rmc_.Version import Version
			self._version = Version(self._core, self._base)
		return self._version

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Rmc_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	def clone(self) -> 'Rmc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rmc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
