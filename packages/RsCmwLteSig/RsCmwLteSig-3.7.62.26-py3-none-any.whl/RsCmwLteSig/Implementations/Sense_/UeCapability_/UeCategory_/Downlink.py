from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	def get_enhanced(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:UECategory:DL:ENHanced \n
		Snippet: value: str = driver.sense.ueCapability.ueCategory.downlink.get_enhanced() \n
		Returns the DL UE category according to the UE capability information. \n
			:return: ue_category: UE category as string
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:UECategory:DL:ENHanced?')
		return trim_str_response(response)
