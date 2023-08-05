from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zp:
	"""Zp commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("zp", core, parent)

	@property
	def csirs(self):
		"""csirs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csirs'):
			from .Zp_.Csirs import Csirs
			self._csirs = Csirs(self._core, self._base)
		return self._csirs

	def get_bits(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:ZP:BITS \n
		Snippet: value: str = driver.configure.connection.pcc.tm.zp.get_bits() \n
		Specifies the bitmap 'ZeroPowerCSI-RS'. \n
			:return: bits: 16-bit value Range: #B0000000000000000 to #B1111111111111111
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:ZP:BITS?')
		return trim_str_response(response)

	def set_bits(self, bits: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:ZP:BITS \n
		Snippet: driver.configure.connection.pcc.tm.zp.set_bits(bits = r1) \n
		Specifies the bitmap 'ZeroPowerCSI-RS'. \n
			:param bits: 16-bit value Range: #B0000000000000000 to #B1111111111111111
		"""
		param = Conversions.value_to_str(bits)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:ZP:BITS {param}')

	def clone(self) -> 'Zp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Zp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
