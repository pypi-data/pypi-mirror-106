from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Meas:
	"""Meas commands group definition. 15 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("meas", core, parent)

	@property
	def interFreqNgaps(self):
		"""interFreqNgaps commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_interFreqNgaps'):
			from .Meas_.InterFreqNgaps import InterFreqNgaps
			self._interFreqNgaps = InterFreqNgaps(self._core, self._base)
		return self._interFreqNgaps

	@property
	def irnGaps(self):
		"""irnGaps commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_irnGaps'):
			from .Meas_.IrnGaps import IrnGaps
			self._irnGaps = IrnGaps(self._core, self._base)
		return self._irnGaps

	def get_rm_wideband(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:RMWideband \n
		Snippet: value: bool = driver.sense.ueCapability.meas.get_rm_wideband() \n
		Returns whether the UE supports RSRQ measurements with wider bandwidth. \n
			:return: wideband: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:RMWideband?')
		return Conversions.str_to_bool(response)

	def get_bf_interrupt(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:BFINterrupt \n
		Snippet: value: bool = driver.sense.ueCapability.meas.get_bf_interrupt() \n
		Returns whether the UE power consumption can be reduced by allowing the UE to cause interruptions to serving cells during
		measurements. \n
			:return: benefits: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:BFINterrupt?')
		return Conversions.str_to_bool(response)

	def get_rco_reporting(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:RCOReporting \n
		Snippet: value: int = driver.sense.ueCapability.meas.get_rco_reporting() \n
		Returns whether the UE supports RSSI and channel occupancy measurements for LAA. \n
			:return: reporting: 0 | 1
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:RCOReporting?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Meas':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Meas(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
