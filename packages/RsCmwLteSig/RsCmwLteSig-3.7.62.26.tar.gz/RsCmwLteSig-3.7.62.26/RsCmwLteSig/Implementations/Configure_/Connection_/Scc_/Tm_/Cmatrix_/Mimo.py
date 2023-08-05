from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mimo:
	"""Mimo commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mimo", core, parent)

	@property
	def mselection(self):
		"""mselection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mselection'):
			from .Mimo_.Mselection import Mselection
			self._mselection = Mselection(self._core, self._base)
		return self._mselection

	@property
	def line(self):
		"""line commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_line'):
			from .Mimo_.Line import Line
			self._line = Line(self._core, self._base)
		return self._line

	def clone(self) -> 'Mimo':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mimo(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
