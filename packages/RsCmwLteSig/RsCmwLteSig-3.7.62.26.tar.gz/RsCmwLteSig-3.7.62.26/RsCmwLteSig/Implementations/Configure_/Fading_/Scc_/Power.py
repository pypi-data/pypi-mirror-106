from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 4 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	@property
	def signal(self):
		"""signal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_signal'):
			from .Power_.Signal import Signal
			self._signal = Signal(self._core, self._base)
		return self._signal

	@property
	def noise(self):
		"""noise commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_noise'):
			from .Power_.Noise import Noise
			self._noise = Noise(self._core, self._base)
		return self._noise

	@property
	def sum(self):
		"""sum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sum'):
			from .Power_.Sum import Sum
			self._sum = Sum(self._core, self._base)
		return self._sum

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
