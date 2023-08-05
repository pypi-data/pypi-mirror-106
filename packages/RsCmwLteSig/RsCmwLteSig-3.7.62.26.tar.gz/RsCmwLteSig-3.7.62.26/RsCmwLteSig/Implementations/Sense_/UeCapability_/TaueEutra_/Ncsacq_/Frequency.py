from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	def get_intra(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:TAUeeutra:NCSacq:FREQuency:INTRa \n
		Snippet: value: bool = driver.sense.ueCapability.taueEutra.ncsacq.frequency.get_intra() \n
		Returns whether the UE supports system information acquisition for intra-frequency neighbor cells or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:TAUeeutra:NCSacq:FREQuency:INTRa?')
		return Conversions.str_to_bool(response)

	def get_inter(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:TAUeeutra:NCSacq:FREQuency:INTer \n
		Snippet: value: bool = driver.sense.ueCapability.taueEutra.ncsacq.frequency.get_inter() \n
		Returns whether the UE supports system information acquisition for inter-frequency neighbor cells or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:TAUeeutra:NCSacq:FREQuency:INTer?')
		return Conversions.str_to_bool(response)
