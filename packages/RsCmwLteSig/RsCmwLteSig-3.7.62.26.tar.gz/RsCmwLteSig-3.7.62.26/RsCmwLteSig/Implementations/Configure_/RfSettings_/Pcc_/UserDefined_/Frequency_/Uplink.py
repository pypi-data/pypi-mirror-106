from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	def get_minimum(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:FREQuency:UL:MINimum \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.frequency.uplink.get_minimum() \n
		Query the minimum and maximum uplink carrier center frequencies resulting from the user-defined band settings.
		For calculations, see CONFigure:LTE:SIGN<i>:UDEFined:FREQuency:DL:MINimum. \n
			:return: frequency: Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:FREQuency:UL:MINimum?')
		return Conversions.str_to_int(response)

	def get_maximum(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:FREQuency:UL:MAXimum \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.frequency.uplink.get_maximum() \n
		Query the minimum and maximum uplink carrier center frequencies resulting from the user-defined band settings.
		For calculations, see CONFigure:LTE:SIGN<i>:UDEFined:FREQuency:DL:MINimum. \n
			:return: frequency: Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:FREQuency:UL:MAXimum?')
		return Conversions.str_to_int(response)
