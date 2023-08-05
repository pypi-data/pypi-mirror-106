from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	@property
	def noise(self):
		"""noise commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_noise'):
			from .Power_.Noise import Noise
			self._noise = Noise(self._core, self._base)
		return self._noise

	def get_signal(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:POWer:SIGNal \n
		Snippet: value: float = driver.configure.fading.pcc.power.get_signal() \n
		No command help available \n
			:return: signal_power: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:POWer:SIGNal?')
		return Conversions.str_to_float(response)

	def get_sum(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:POWer:SUM \n
		Snippet: value: float = driver.configure.fading.pcc.power.get_sum() \n
		Queries the calculated total power (signal + noise) on the DL channel, i.e. within the cell bandwidth. \n
			:return: power: Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:POWer:SUM?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
