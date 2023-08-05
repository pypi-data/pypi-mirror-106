from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DedBearer:
	"""DedBearer commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dedBearer", core, parent)

	# noinspection PyTypeChecker
	class SeparateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Def_Bearer_Id: str: Bearer ID string, selecting the default bearer, to which the dedicated bearer is mapped. String example: '5 (cmw500.rohde-schwarz.com) ' To query a list of IDs for all established default bearers, see [CMDLINK: CATalog:LTE:SIGNi:CONNection:DEFBearer CMDLINK].
			- Profile: enums.DedBearerProfile: VOICe | VIDeo | DRAM | DRUM Selects a dedicated bearer profile VOICe: for voice connections VIDeo: for video connections DRAM: for data connections with RLC acknowledged mode DRUM: for data connections with RLC unacknowledged mode
			- Tft_Port_Low_Dl: int: Selects the lower end of the port range for downlink traffic Range: 1 to 65535
			- Tft_Port_High_Dl: int: Selects the upper end of the port range for downlink traffic Range: 1 to 65535
			- Tft_Port_Low_Ul: int: Selects the lower end of the port range for uplink traffic Range: 1 to 65535
			- Tft_Port_High_Ul: int: Selects the upper end of the port range for uplink traffic Range: 1 to 65535"""
		__meta_args_list = [
			ArgStruct.scalar_str('Def_Bearer_Id'),
			ArgStruct.scalar_enum('Profile', enums.DedBearerProfile),
			ArgStruct.scalar_int('Tft_Port_Low_Dl'),
			ArgStruct.scalar_int('Tft_Port_High_Dl'),
			ArgStruct.scalar_int('Tft_Port_Low_Ul'),
			ArgStruct.scalar_int('Tft_Port_High_Ul')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Def_Bearer_Id: str = None
			self.Profile: enums.DedBearerProfile = None
			self.Tft_Port_Low_Dl: int = None
			self.Tft_Port_High_Dl: int = None
			self.Tft_Port_Low_Ul: int = None
			self.Tft_Port_High_Ul: int = None

	def get_separate(self) -> SeparateStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:CONNection:DEDBearer:SEParate \n
		Snippet: value: SeparateStruct = driver.prepare.connection.dedBearer.get_separate() \n
		Configures dedicated bearer settings as a preparation for a bearer setup via CALL:LTE:SIGN:PSWitched:ACTion CONNect.
		Different port ranges can be set for the uplink and for the downlink. \n
			:return: structure: for return value, see the help for SeparateStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:CONNection:DEDBearer:SEParate?', self.__class__.SeparateStruct())

	def set_separate(self, value: SeparateStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:CONNection:DEDBearer:SEParate \n
		Snippet: driver.prepare.connection.dedBearer.set_separate(value = SeparateStruct()) \n
		Configures dedicated bearer settings as a preparation for a bearer setup via CALL:LTE:SIGN:PSWitched:ACTion CONNect.
		Different port ranges can be set for the uplink and for the downlink. \n
			:param value: see the help for SeparateStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:CONNection:DEDBearer:SEParate', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Def_Bearer_Id: str: Bearer ID string, selecting the default bearer, to which the dedicated bearer is mapped. String example: '5 (cmw500.rohde-schwarz.com) ' To query a list of IDs for all established default bearers, see [CMDLINK: CATalog:LTE:SIGNi:CONNection:DEFBearer CMDLINK].
			- Profile: enums.DedBearerProfile: VOICe | VIDeo | DRAM | DRUM Selects a dedicated bearer profile VOICe: for voice connections VIDeo: for video connections DRAM: for data connections with RLC acknowledged mode DRUM: for data connections with RLC unacknowledged mode
			- Tft_Port_Low: int: Selects the lower end of the port range, for which traffic is routed to the dedicated bearer Range: 1 to 65535
			- Tft_Port_High: int: Selects the upper end of the port range Range: 1 to 65535"""
		__meta_args_list = [
			ArgStruct.scalar_str('Def_Bearer_Id'),
			ArgStruct.scalar_enum('Profile', enums.DedBearerProfile),
			ArgStruct.scalar_int('Tft_Port_Low'),
			ArgStruct.scalar_int('Tft_Port_High')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Def_Bearer_Id: str = None
			self.Profile: enums.DedBearerProfile = None
			self.Tft_Port_Low: int = None
			self.Tft_Port_High: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:CONNection:DEDBearer \n
		Snippet: value: ValueStruct = driver.prepare.connection.dedBearer.get_value() \n
		Configures dedicated bearer settings as a preparation for a bearer setup via CALL:LTE:SIGN:PSWitched:ACTion CONNect. The
		same port range is used for the uplink and for the downlink. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:CONNection:DEDBearer?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:CONNection:DEDBearer \n
		Snippet: driver.prepare.connection.dedBearer.set_value(value = ValueStruct()) \n
		Configures dedicated bearer settings as a preparation for a bearer setup via CALL:LTE:SIGN:PSWitched:ACTion CONNect. The
		same port range is used for the uplink and for the downlink. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:CONNection:DEDBearer', value)
