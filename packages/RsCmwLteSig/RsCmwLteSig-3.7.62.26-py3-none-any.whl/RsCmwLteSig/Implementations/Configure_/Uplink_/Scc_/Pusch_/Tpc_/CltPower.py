from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CltPower:
	"""CltPower commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cltPower", core, parent)

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .CltPower_.Offset import Offset
			self._offset = Offset(self._core, self._base)
		return self._offset

	def set(self, power: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:CLTPower \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.cltPower.set(power = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the target power for power control with the TPC setup CLOop. \n
			:param power: Range: -50 dBm to 33 dBm, Unit: dBm
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		param = Conversions.decimal_value_to_str(power)
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:CLTPower {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:CLTPower \n
		Snippet: value: float = driver.configure.uplink.scc.pusch.tpc.cltPower.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the target power for power control with the TPC setup CLOop. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: power: Range: -50 dBm to 33 dBm, Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:CLTPower?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'CltPower':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CltPower(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
