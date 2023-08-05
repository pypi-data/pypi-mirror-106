from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PipSubFrames:
	"""PipSubFrames commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pipSubFrames", core, parent)

	@property
	def mcluster(self):
		"""mcluster commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcluster'):
			from .PipSubFrames_.Mcluster import Mcluster
			self._mcluster = Mcluster(self._core, self._base)
		return self._mcluster

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .PipSubFrames_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	def clone(self) -> 'PipSubFrames':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PipSubFrames(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
