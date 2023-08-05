from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcc:
	"""Pcc commands group definition. 29 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcc", core, parent)

	@property
	def fadingSimulator(self):
		"""fadingSimulator commands group. 8 Sub-classes, 3 commands."""
		if not hasattr(self, '_fadingSimulator'):
			from .Pcc_.FadingSimulator import FadingSimulator
			self._fadingSimulator = FadingSimulator(self._core, self._base)
		return self._fadingSimulator

	@property
	def awgn(self):
		"""awgn commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_awgn'):
			from .Pcc_.Awgn import Awgn
			self._awgn = Awgn(self._core, self._base)
		return self._awgn

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_power'):
			from .Pcc_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	def clone(self) -> 'Pcc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
