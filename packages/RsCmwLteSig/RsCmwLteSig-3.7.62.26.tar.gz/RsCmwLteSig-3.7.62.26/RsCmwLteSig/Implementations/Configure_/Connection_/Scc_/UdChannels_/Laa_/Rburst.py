from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rburst:
	"""Rburst commands group definition. 6 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rburst", core, parent)

	@property
	def fullSubFrames(self):
		"""fullSubFrames commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fullSubFrames'):
			from .Rburst_.FullSubFrames import FullSubFrames
			self._fullSubFrames = FullSubFrames(self._core, self._base)
		return self._fullSubFrames

	@property
	def pipSubFrames(self):
		"""pipSubFrames commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pipSubFrames'):
			from .Rburst_.PipSubFrames import PipSubFrames
			self._pipSubFrames = PipSubFrames(self._core, self._base)
		return self._pipSubFrames

	@property
	def pepSubFrames(self):
		"""pepSubFrames commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pepSubFrames'):
			from .Rburst_.PepSubFrames import PepSubFrames
			self._pepSubFrames = PepSubFrames(self._core, self._base)
		return self._pepSubFrames

	def clone(self) -> 'Rburst':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rburst(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
