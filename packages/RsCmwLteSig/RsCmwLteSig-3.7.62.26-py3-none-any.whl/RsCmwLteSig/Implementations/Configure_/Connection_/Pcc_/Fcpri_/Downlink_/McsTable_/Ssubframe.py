from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssubframe:
	"""Ssubframe commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ssubframe", core, parent)

	def get_user_defined(self) -> List[int]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FCPRi:DL:MCSTable:SSUBframe:UDEFined \n
		Snippet: value: List[int] = driver.configure.connection.pcc.fcpri.downlink.mcsTable.ssubframe.get_user_defined() \n
		Configures a user-defined mapping table for special subframes that assigns an MCS index value to each possible reported
		wideband CQI index value. The table is used for the scheduling type 'Follow WB CQI-PMI-RI' if the table mode is set to
		UDEFined. \n
			:return: mcs: Comma-separated list of 15 MCS values, for reported CQI index value 1 to 15 Range: 0 to 28
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FCPRi:DL:MCSTable:SSUBframe:UDEFined?')
		return response

	def set_user_defined(self, mcs: List[int]) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FCPRi:DL:MCSTable:SSUBframe:UDEFined \n
		Snippet: driver.configure.connection.pcc.fcpri.downlink.mcsTable.ssubframe.set_user_defined(mcs = [1, 2, 3]) \n
		Configures a user-defined mapping table for special subframes that assigns an MCS index value to each possible reported
		wideband CQI index value. The table is used for the scheduling type 'Follow WB CQI-PMI-RI' if the table mode is set to
		UDEFined. \n
			:param mcs: Comma-separated list of 15 MCS values, for reported CQI index value 1 to 15 Range: 0 to 28
		"""
		param = Conversions.list_to_csv_str(mcs)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FCPRi:DL:MCSTable:SSUBframe:UDEFined {param}')
