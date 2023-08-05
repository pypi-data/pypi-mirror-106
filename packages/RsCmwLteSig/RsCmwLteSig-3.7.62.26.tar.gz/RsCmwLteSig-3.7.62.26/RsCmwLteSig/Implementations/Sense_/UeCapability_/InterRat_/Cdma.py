from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdma:
	"""Cdma commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cdma", core, parent)

	def get_nw_sharing(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:CDMA<2000>:NWSHaring \n
		Snippet: value: bool = driver.sense.ueCapability.interRat.cdma.get_nw_sharing() \n
		Returns whether the UE supports network sharing for CDMA2000. \n
			:return: sharing: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:CDMA2000:NWSHaring?')
		return Conversions.str_to_bool(response)
