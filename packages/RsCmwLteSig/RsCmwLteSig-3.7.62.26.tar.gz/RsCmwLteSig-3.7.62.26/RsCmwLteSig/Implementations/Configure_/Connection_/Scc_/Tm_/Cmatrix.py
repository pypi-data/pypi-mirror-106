from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmatrix:
	"""Cmatrix commands group definition. 5 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cmatrix", core, parent)

	@property
	def eight(self):
		"""eight commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eight'):
			from .Cmatrix_.Eight import Eight
			self._eight = Eight(self._core, self._base)
		return self._eight

	@property
	def four(self):
		"""four commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_four'):
			from .Cmatrix_.Four import Four
			self._four = Four(self._core, self._base)
		return self._four

	@property
	def two(self):
		"""two commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_two'):
			from .Cmatrix_.Two import Two
			self._two = Two(self._core, self._base)
		return self._two

	@property
	def mimo(self):
		"""mimo commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Cmatrix_.Mimo import Mimo
			self._mimo = Mimo(self._core, self._base)
		return self._mimo

	def clone(self) -> 'Cmatrix':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cmatrix(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
