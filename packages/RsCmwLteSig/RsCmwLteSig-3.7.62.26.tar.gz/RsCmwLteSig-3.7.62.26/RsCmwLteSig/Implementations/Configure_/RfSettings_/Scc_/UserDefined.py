from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefined:
	"""UserDefined commands group definition. 10 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("userDefined", core, parent)

	@property
	def bindicator(self):
		"""bindicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bindicator'):
			from .UserDefined_.Bindicator import Bindicator
			self._bindicator = Bindicator(self._core, self._base)
		return self._bindicator

	@property
	def channel(self):
		"""channel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .UserDefined_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .UserDefined_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def udSeparation(self):
		"""udSeparation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udSeparation'):
			from .UserDefined_.UdSeparation import UdSeparation
			self._udSeparation = UdSeparation(self._core, self._base)
		return self._udSeparation

	def clone(self) -> 'UserDefined':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefined(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
