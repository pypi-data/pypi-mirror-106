from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbPosition:
	"""RbPosition commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rbPosition", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .RbPosition_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	# noinspection PyTypeChecker
	def get_uplink(self) -> enums.RbPosition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:RBPosition:UL \n
		Snippet: value: enums.RbPosition = driver.configure.connection.pcc.rmc.rbPosition.get_uplink() \n
		Selects the position of the allocated uplink resource blocks within the cell bandwidth, for contiguous allocation.
		The RBs can always be at the lower end, starting with RB number 0 (LOW) , or at the upper end of the channel (HIGH) .
		Other values are only allowed for certain RMC configurations, see 'Scheduling Type RMC'. \n
			:return: position: LOW | HIGH | MID | P0 | P1 | P2 | P3 | P4 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P19 | P20 | P21 | P22 | P24 | P25 | P28 | P30 | P31 | P33 | P36 | P37 | P39 | P40 | P43 | P44 | P45 | P48 | P49 | P50 | P51 | P52 | P54 | P56 | P57 | P58 | P62 | P63 | P66 | P68 | P70 | P74 | P75 | P83 | P96 | P99
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:RBPosition:UL?')
		return Conversions.str_to_scalar_enum(response, enums.RbPosition)

	def set_uplink(self, position: enums.RbPosition) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:RBPosition:UL \n
		Snippet: driver.configure.connection.pcc.rmc.rbPosition.set_uplink(position = enums.RbPosition.FULL) \n
		Selects the position of the allocated uplink resource blocks within the cell bandwidth, for contiguous allocation.
		The RBs can always be at the lower end, starting with RB number 0 (LOW) , or at the upper end of the channel (HIGH) .
		Other values are only allowed for certain RMC configurations, see 'Scheduling Type RMC'. \n
			:param position: LOW | HIGH | MID | P0 | P1 | P2 | P3 | P4 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P19 | P20 | P21 | P22 | P24 | P25 | P28 | P30 | P31 | P33 | P36 | P37 | P39 | P40 | P43 | P44 | P45 | P48 | P49 | P50 | P51 | P52 | P54 | P56 | P57 | P58 | P62 | P63 | P66 | P68 | P70 | P74 | P75 | P83 | P96 | P99
		"""
		param = Conversions.enum_scalar_to_str(position, enums.RbPosition)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:RBPosition:UL {param}')

	def clone(self) -> 'RbPosition':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RbPosition(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
