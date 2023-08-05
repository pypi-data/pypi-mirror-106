from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Beamforming:
	"""Beamforming commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("beamforming", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Beamforming_.Mode import Mode
			self._mode = Mode(self._core, self._base)
		return self._mode

	@property
	def noLayers(self):
		"""noLayers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noLayers'):
			from .Beamforming_.NoLayers import NoLayers
			self._noLayers = NoLayers(self._core, self._base)
		return self._noLayers

	@property
	def matrix(self):
		"""matrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_matrix'):
			from .Beamforming_.Matrix import Matrix
			self._matrix = Matrix(self._core, self._base)
		return self._matrix

	def clone(self) -> 'Beamforming':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Beamforming(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
