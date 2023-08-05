from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Determined:
	"""Determined commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("determined", core, parent)

	def get(self, table_name: enums.Table = None) -> List[int]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:FWBCqi:DL:MCSTable:CSIRs:DETermined \n
		Snippet: value: List[int] = driver.sense.connection.pcc.fwbcqi.downlink.mcsTable.csirs.determined.get(table_name = enums.Table.ANY) \n
		Queries the automatically determined mapping table for subframes with CSI-RS. The table is used for the scheduling type
		'Follow WB CQI' if the table mode is set to DETermined. \n
			:param table_name: ANY | CW1 | CW2 | OTLC1 | OTLC2 | TFLC1 | TFLC2
			:return: mcs: Comma-separated list of 15 MCS values, for reported CQI index value 1 to 15 Range: 0 to 31"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('table_name', table_name, DataType.Enum, True))
		response = self._core.io.query_bin_or_ascii_int_list(f'SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:FWBCqi:DL:MCSTable:CSIRs:DETermined? {param}'.rstrip())
		return response
