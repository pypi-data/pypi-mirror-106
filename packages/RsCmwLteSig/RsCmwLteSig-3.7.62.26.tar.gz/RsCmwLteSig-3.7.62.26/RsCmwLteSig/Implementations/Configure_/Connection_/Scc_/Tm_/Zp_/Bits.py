from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bits:
	"""Bits commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bits", core, parent)

	def set(self, bits: str, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:ZP:BITS \n
		Snippet: driver.configure.connection.scc.tm.zp.bits.set(bits = r1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the bitmap 'ZeroPowerCSI-RS'. \n
			:param bits: 16-bit value Range: #B0000000000000000 to #B1111111111111111
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		param = Conversions.value_to_str(bits)
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:ZP:BITS {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:ZP:BITS \n
		Snippet: value: str = driver.configure.connection.scc.tm.zp.bits.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the bitmap 'ZeroPowerCSI-RS'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: bits: 16-bit value Range: #B0000000000000000 to #B1111111111111111"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:ZP:BITS?')
		return trim_str_response(response)
