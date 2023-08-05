from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CpIndication:
	"""CpIndication commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cpIndication", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .CpIndication_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	def get_utran(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:CPINdication:UTRan \n
		Snippet: value: bool = driver.sense.ueCapability.cpIndication.get_utran() \n
		Returns whether the UE supports proximity indications for UTRAN CSG member cells or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:CPINdication:UTRan?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'CpIndication':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CpIndication(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
