from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCategory:
	"""UeCategory commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueCategory", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .UeCategory_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .UeCategory_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	def get_value(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:UECategory \n
		Snippet: value: int = driver.sense.ueCapability.ueCategory.get_value() \n
		Returns the UE category according to the UE capability information. \n
			:return: ue_category: Range: 1 to 12
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:UECategory?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'UeCategory':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCategory(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
