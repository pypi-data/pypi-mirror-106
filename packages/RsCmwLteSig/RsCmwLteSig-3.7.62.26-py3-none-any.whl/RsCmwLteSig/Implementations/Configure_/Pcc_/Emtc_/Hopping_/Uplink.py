from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 4 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def b(self):
		"""b commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_b'):
			from .Uplink_.B import B
			self._b = B(self._core, self._base)
		return self._b

	@property
	def a(self):
		"""a commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_a'):
			from .Uplink_.A import A
			self._a = A(self._core, self._base)
		return self._a

	def get_hoffset(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:HOPPing:UL:HOFFset \n
		Snippet: value: int = driver.configure.pcc.emtc.hopping.uplink.get_hoffset() \n
		Specifies the size of one frequency hop, DL or UL. For the number of narrowbands per cell bandwidth, see Table
		'Narrowbands and resource blocks per cell BW'. \n
			:return: offset: Hop size in narrowbands Range: 1 to 16 (depends on cell BW)
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:HOPPing:UL:HOFFset?')
		return Conversions.str_to_int(response)

	def set_hoffset(self, offset: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:HOPPing:UL:HOFFset \n
		Snippet: driver.configure.pcc.emtc.hopping.uplink.set_hoffset(offset = 1) \n
		Specifies the size of one frequency hop, DL or UL. For the number of narrowbands per cell bandwidth, see Table
		'Narrowbands and resource blocks per cell BW'. \n
			:param offset: Hop size in narrowbands Range: 1 to 16 (depends on cell BW)
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:HOPPing:UL:HOFFset {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:HOPPing:UL:ENABle \n
		Snippet: value: bool = driver.configure.pcc.emtc.hopping.uplink.get_enable() \n
		Enables or disables frequency hopping for eMTC, DL or UL. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:HOPPing:UL:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:HOPPing:UL:ENABle \n
		Snippet: driver.configure.pcc.emtc.hopping.uplink.set_enable(enable = False) \n
		Enables or disables frequency hopping for eMTC, DL or UL. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:HOPPing:UL:ENABle {param}')

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
