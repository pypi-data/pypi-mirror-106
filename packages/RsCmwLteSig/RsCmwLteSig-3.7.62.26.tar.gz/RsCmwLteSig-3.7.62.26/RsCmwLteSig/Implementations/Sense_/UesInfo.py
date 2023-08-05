from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UesInfo:
	"""UesInfo commands group definition. 7 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uesInfo", core, parent)

	@property
	def ueAddress(self):
		"""ueAddress commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueAddress'):
			from .UesInfo_.UeAddress import UeAddress
			self._ueAddress = UeAddress(self._core, self._base)
		return self._ueAddress

	# noinspection PyTypeChecker
	def get_ue_usage(self) -> enums.UeUsage:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UESinfo:UEUSage \n
		Snippet: value: enums.UeUsage = driver.sense.uesInfo.get_ue_usage() \n
		Queries the usage setting of the UE. \n
			:return: usage: VCENtric | DCENtric VCENtric: Voice centric DCENtric: Data centric
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UESinfo:UEUSage?')
		return Conversions.str_to_scalar_enum(response, enums.UeUsage)

	# noinspection PyTypeChecker
	def get_vd_preference(self) -> enums.VdPreference:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UESinfo:VDPReference \n
		Snippet: value: enums.VdPreference = driver.sense.uesInfo.get_vd_preference() \n
		Queries the voice domain preference of the UE. \n
			:return: value: CVONly | IPVonly | CVPRefered | IPVPrefered CVONly: CS voice only IPVonly: IMS PS voice only CVPRefered: CS voice preferred, IMS PS voice as secondary IPVPrefered: IMS PS voice preferred, CS voice as secondary
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UESinfo:VDPReference?')
		return Conversions.str_to_scalar_enum(response, enums.VdPreference)

	def get_imei(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UESinfo:IMEI \n
		Snippet: value: str = driver.sense.uesInfo.get_imei() \n
		Queries the IMEI of the UE. \n
			:return: imei: IMEI as string with up to 18 digits
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UESinfo:IMEI?')
		return trim_str_response(response)

	def get_imsi(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UESinfo:IMSI \n
		Snippet: value: str = driver.sense.uesInfo.get_imsi() \n
		Queries the IMSI of the UE. \n
			:return: imsi: IMSI as string with up to 16 digits
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UESinfo:IMSI?')
		return trim_str_response(response)

	def clone(self) -> 'UesInfo':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UesInfo(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
