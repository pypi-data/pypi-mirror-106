from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApPower:
	"""ApPower commands group definition. 8 total commands, 5 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("apPower", core, parent)

	@property
	def rsPower(self):
		"""rsPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsPower'):
			from .ApPower_.RsPower import RsPower
			self._rsPower = RsPower(self._core, self._base)
		return self._rsPower

	@property
	def pirPower(self):
		"""pirPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pirPower'):
			from .ApPower_.PirPower import PirPower
			self._pirPower = PirPower(self._core, self._base)
		return self._pirPower

	@property
	def pnpusch(self):
		"""pnpusch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnpusch'):
			from .ApPower_.Pnpusch import Pnpusch
			self._pnpusch = Pnpusch(self._core, self._base)
		return self._pnpusch

	@property
	def pcAlpha(self):
		"""pcAlpha commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcAlpha'):
			from .ApPower_.PcAlpha import PcAlpha
			self._pcAlpha = PcAlpha(self._core, self._base)
		return self._pcAlpha

	@property
	def tprrcSetup(self):
		"""tprrcSetup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tprrcSetup'):
			from .ApPower_.TprrcSetup import TprrcSetup
			self._tprrcSetup = TprrcSetup(self._core, self._base)
		return self._tprrcSetup

	def get_pathloss(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETA:APPower:PATHloss \n
		Snippet: value: float = driver.sense.uplink.seta.apPower.get_pathloss() \n
		Queries the pathloss resulting from the advanced UL power settings. \n
			:return: pathloss: Unit: dB
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETA:APPower:PATHloss?')
		return Conversions.str_to_float(response)

	def get_epp_power(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETA:APPower:EPPPower \n
		Snippet: value: float = driver.sense.uplink.seta.apPower.get_epp_power() \n
		Queries the expected power of the first preamble, resulting from the advanced UL power settings. \n
			:return: power: Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETA:APPower:EPPPower?')
		return Conversions.str_to_float(response)

	def get_eo_power(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETA:APPower:EOPower \n
		Snippet: value: float = driver.sense.uplink.seta.apPower.get_eo_power() \n
		Queries the expected initial PUSCH power, resulting from the advanced UL power settings. \n
			:return: expected_ol_power: Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETA:APPower:EOPower?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'ApPower':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApPower(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
