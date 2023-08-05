from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 9 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pusch", core, parent)

	@property
	def tpc(self):
		"""tpc commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_tpc'):
			from .Pusch_.Tpc import Tpc
			self._tpc = Tpc(self._core, self._base)
		return self._tpc

	def get_oln_power(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:PUSCh:OLNPower \n
		Snippet: value: float = driver.configure.uplink.setb.pusch.get_oln_power() \n
		Defines a cell-specific nominal power value for full resource block allocation in the UL (entire cell bandwidth used) .
		From this value, the cell-specific nominal power value PO_NOMINAL_PUSCH related to one resource block is determined and
		sent to all UEs via broadcast. This command is only relevant for basic configuration and rejected if advanced
		configuration is active. \n
			:return: power: Range: -50 dBm to 23 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETB:PUSCh:OLNPower?')
		return Conversions.str_to_float(response)

	def set_oln_power(self, power: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:PUSCh:OLNPower \n
		Snippet: driver.configure.uplink.setb.pusch.set_oln_power(power = 1.0) \n
		Defines a cell-specific nominal power value for full resource block allocation in the UL (entire cell bandwidth used) .
		From this value, the cell-specific nominal power value PO_NOMINAL_PUSCH related to one resource block is determined and
		sent to all UEs via broadcast. This command is only relevant for basic configuration and rejected if advanced
		configuration is active. \n
			:param power: Range: -50 dBm to 23 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETB:PUSCh:OLNPower {param}')

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
