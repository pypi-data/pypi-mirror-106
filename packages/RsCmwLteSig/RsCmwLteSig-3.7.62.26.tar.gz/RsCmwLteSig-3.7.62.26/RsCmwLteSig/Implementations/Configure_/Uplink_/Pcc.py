from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcc:
	"""Pcc commands group definition. 17 total commands, 3 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcc", core, parent)

	@property
	def pusch(self):
		"""pusch commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pusch'):
			from .Pcc_.Pusch import Pusch
			self._pusch = Pusch(self._core, self._base)
		return self._pusch

	@property
	def apPower(self):
		"""apPower commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_apPower'):
			from .Pcc_.ApPower import ApPower
			self._apPower = ApPower(self._core, self._base)
		return self._apPower

	@property
	def pucch(self):
		"""pucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pucch'):
			from .Pcc_.Pucch import Pucch
			self._pucch = Pucch(self._core, self._base)
		return self._pucch

	def get_pmax(self) -> float or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:PMAX \n
		Snippet: value: float or bool = driver.configure.uplink.pcc.get_pmax() \n
		Specifies the maximum allowed UE power. \n
			:return: power: Range: -30 dBm to 33 dBm, Unit: dBm Additional parameters: OFF | ON (disables | enables signaling of the value to the UE)
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:PCC:PMAX?')
		return Conversions.str_to_float_or_bool(response)

	def set_pmax(self, power: float or bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:PMAX \n
		Snippet: driver.configure.uplink.pcc.set_pmax(power = 1.0) \n
		Specifies the maximum allowed UE power. \n
			:param power: Range: -30 dBm to 33 dBm, Unit: dBm Additional parameters: OFF | ON (disables | enables signaling of the value to the UE)
		"""
		param = Conversions.decimal_or_bool_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:PCC:PMAX {param}')

	def get_ju_power(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:JUPower \n
		Snippet: value: bool = driver.configure.uplink.pcc.get_ju_power() \n
		Enables or disables joint uplink power control for uplink carrier aggregation. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:PCC:JUPower?')
		return Conversions.str_to_bool(response)

	def set_ju_power(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:JUPower \n
		Snippet: driver.configure.uplink.pcc.set_ju_power(enable = False) \n
		Enables or disables joint uplink power control for uplink carrier aggregation. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:PCC:JUPower {param}')

	def clone(self) -> 'Pcc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
