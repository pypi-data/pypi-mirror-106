from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 9 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pusch", core, parent)

	@property
	def tpc(self):
		"""tpc commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_tpc'):
			from .Pusch_.Tpc import Tpc
			self._tpc = Tpc(self._core, self._base)
		return self._tpc

	@property
	def olnPower(self):
		"""olnPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_olnPower'):
			from .Pusch_.OlnPower import OlnPower
			self._olnPower = OlnPower(self._core, self._base)
		return self._olnPower

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
