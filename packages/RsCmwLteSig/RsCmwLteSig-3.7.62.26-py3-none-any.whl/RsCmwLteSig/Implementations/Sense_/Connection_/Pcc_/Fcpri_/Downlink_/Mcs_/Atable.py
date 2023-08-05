from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Atable:
	"""Atable commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("atable", core, parent)

	# noinspection PyTypeChecker
	def get_list_py(self) -> List[enums.Table]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:FCPRi:DL:MCS:ATABle:LIST \n
		Snippet: value: List[enums.Table] = driver.sense.connection.pcc.fcpri.downlink.mcs.atable.get_list_py() \n
		No command help available \n
			:return: tables: No help available
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:FCPRi:DL:MCS:ATABle:LIST?')
		return Conversions.str_to_list_enum(response, enums.Table)
