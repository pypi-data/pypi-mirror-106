from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCapability:
	"""UeCapability commands group definition. 6 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueCapability", core, parent)

	@property
	def rfBands(self):
		"""rfBands commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfBands'):
			from .UeCapability_.RfBands import RfBands
			self._rfBands = RfBands(self._core, self._base)
		return self._rfBands

	def get_rutra(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RUTRa \n
		Snippet: value: bool = driver.configure.ueCapability.get_rutra() \n
		Selects whether UTRA capabilities are requested from the UE (entry 'utra' in field 'ue-CapabilityRequest' of
		'ueCapabilityEnquiry' message) . \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UECapability:RUTRa?')
		return Conversions.str_to_bool(response)

	def set_rutra(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RUTRa \n
		Snippet: driver.configure.ueCapability.set_rutra(enable = False) \n
		Selects whether UTRA capabilities are requested from the UE (entry 'utra' in field 'ue-CapabilityRequest' of
		'ueCapabilityEnquiry' message) . \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UECapability:RUTRa {param}')

	def get_rgcs(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RGCS \n
		Snippet: value: bool = driver.configure.ueCapability.get_rgcs() \n
		Selects whether GERAN CS capabilities are requested from the UE (entry 'geran-cs' in field 'ue-CapabilityRequest' of
		'ueCapabilityEnquiry' message) . \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UECapability:RGCS?')
		return Conversions.str_to_bool(response)

	def set_rgcs(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RGCS \n
		Snippet: driver.configure.ueCapability.set_rgcs(enable = False) \n
		Selects whether GERAN CS capabilities are requested from the UE (entry 'geran-cs' in field 'ue-CapabilityRequest' of
		'ueCapabilityEnquiry' message) . \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UECapability:RGCS {param}')

	def get_rgps(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RGPS \n
		Snippet: value: bool = driver.configure.ueCapability.get_rgps() \n
		Selects whether GERAN PS capabilities are requested from the UE (entry 'geran-ps' in field 'ue-CapabilityRequest' of
		'ueCapabilityEnquiry' message) . \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UECapability:RGPS?')
		return Conversions.str_to_bool(response)

	def set_rgps(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RGPS \n
		Snippet: driver.configure.ueCapability.set_rgps(enable = False) \n
		Selects whether GERAN PS capabilities are requested from the UE (entry 'geran-ps' in field 'ue-CapabilityRequest' of
		'ueCapabilityEnquiry' message) . \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UECapability:RGPS {param}')

	def get_rr_format(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RRFormat \n
		Snippet: value: bool = driver.configure.ueCapability.get_rr_format() \n
		Enables the optional field 'requestReducedFormat-r13' in the 'ueCapabilityEnquiry' message. \n
			:return: enable: OFF | ON OFF: field omitted ON: field included
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UECapability:RRFormat?')
		return Conversions.str_to_bool(response)

	def set_rr_format(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RRFormat \n
		Snippet: driver.configure.ueCapability.set_rr_format(enable = False) \n
		Enables the optional field 'requestReducedFormat-r13' in the 'ueCapabilityEnquiry' message. \n
			:param enable: OFF | ON OFF: field omitted ON: field included
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UECapability:RRFormat {param}')

	def get_sfc(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:SFC \n
		Snippet: value: bool = driver.configure.ueCapability.get_sfc() \n
		Enables the optional field 'requestSkipFallbackComb-r13' in the 'ueCapabilityEnquiry' message. \n
			:return: enable: OFF | ON OFF: field omitted ON: field included
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UECapability:SFC?')
		return Conversions.str_to_bool(response)

	def set_sfc(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:SFC \n
		Snippet: driver.configure.ueCapability.set_sfc(enable = False) \n
		Enables the optional field 'requestSkipFallbackComb-r13' in the 'ueCapabilityEnquiry' message. \n
			:param enable: OFF | ON OFF: field omitted ON: field included
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UECapability:SFC {param}')

	def clone(self) -> 'UeCapability':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCapability(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
