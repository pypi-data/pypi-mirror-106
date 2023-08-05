from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rssi:
	"""Rssi commands group definition. 5 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rssi", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Rssi_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def rmtc(self):
		"""rmtc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmtc'):
			from .Rssi_.Rmtc import Rmtc
			self._rmtc = Rmtc(self._core, self._base)
		return self._rmtc

	@property
	def coThreshold(self):
		"""coThreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coThreshold'):
			from .Rssi_.CoThreshold import CoThreshold
			self._coThreshold = CoThreshold(self._core, self._base)
		return self._coThreshold

	@property
	def mduration(self):
		"""mduration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mduration'):
			from .Rssi_.Mduration import Mduration
			self._mduration = Mduration(self._core, self._base)
		return self._mduration

	def clone(self) -> 'Rssi':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rssi(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
