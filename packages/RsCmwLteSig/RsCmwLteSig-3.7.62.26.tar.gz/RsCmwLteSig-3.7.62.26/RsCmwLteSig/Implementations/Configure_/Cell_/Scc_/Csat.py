from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csat:
	"""Csat commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("csat", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Csat_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def dmtcPeriod(self):
		"""dmtcPeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmtcPeriod'):
			from .Csat_.DmtcPeriod import DmtcPeriod
			self._dmtcPeriod = DmtcPeriod(self._core, self._base)
		return self._dmtcPeriod

	def clone(self) -> 'Csat':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Csat(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
