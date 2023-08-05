from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Determined:
	"""Determined commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("determined", core, parent)

	def get(self, table_name: enums.Table = None, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[int]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FCRI:DL:MCSTable:SSUBframe:DETermined \n
		Snippet: value: List[int] = driver.sense.connection.scc.fcri.downlink.mcsTable.ssubframe.determined.get(table_name = enums.Table.ANY, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the automatically determined mapping table for special subframes. The table is used for the scheduling type
		'Follow WB CQI-RI' if the table mode is set to DETermined. \n
			:param table_name: ANY | CW1 | CW2 | OTLC1 | OTLC2 | TFLC1 | TFLC2
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mcs: Comma-separated list of 15 MCS values, for reported CQI index value 1 to 15 Range: 0 to 31"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('table_name', table_name, DataType.Enum, True))
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_bin_or_ascii_int_list(f'SENSe:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FCRI:DL:MCSTable:SSUBframe:DETermined? {param}'.rstrip())
		return response
