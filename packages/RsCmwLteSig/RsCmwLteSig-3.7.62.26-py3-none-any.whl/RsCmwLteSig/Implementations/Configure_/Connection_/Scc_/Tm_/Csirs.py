from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csirs:
	"""Csirs commands group definition. 4 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("csirs", core, parent)

	@property
	def aports(self):
		"""aports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aports'):
			from .Csirs_.Aports import Aports
			self._aports = Aports(self._core, self._base)
		return self._aports

	@property
	def subframe(self):
		"""subframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subframe'):
			from .Csirs_.Subframe import Subframe
			self._subframe = Subframe(self._core, self._base)
		return self._subframe

	@property
	def resource(self):
		"""resource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resource'):
			from .Csirs_.Resource import Resource
			self._resource = Resource(self._core, self._base)
		return self._resource

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Csirs_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	def clone(self) -> 'Csirs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Csirs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
