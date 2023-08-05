from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Message:
	"""Message commands group definition. 19 total commands, 3 Sub-groups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("message", core, parent)

	@property
	def dcScheme(self):
		"""dcScheme commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dcScheme'):
			from .Message_.DcScheme import DcScheme
			self._dcScheme = DcScheme(self._core, self._base)
		return self._dcScheme

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .Message_.File import File
			self._file = File(self._core, self._base)
		return self._file

	@property
	def etws(self):
		"""etws commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_etws'):
			from .Message_.Etws import Etws
			self._etws = Etws(self._core, self._base)
		return self._etws

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:ENABle \n
		Snippet: value: bool = driver.configure.cbs.message.get_enable() \n
		Enables the transmission of cell broadcast messages. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:ENABle \n
		Snippet: driver.configure.cbs.message.set_enable(enable = False) \n
		Enables the transmission of cell broadcast messages. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:ENABle {param}')

	def get_id(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:ID \n
		Snippet: value: int = driver.configure.cbs.message.get_id() \n
		Specifies the message ID as decimal value. The related message type is set automatically. \n
			:return: idn: Range: 0 to 65535
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:ID?')
		return Conversions.str_to_int(response)

	def set_id(self, idn: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:ID \n
		Snippet: driver.configure.cbs.message.set_id(idn = 1) \n
		Specifies the message ID as decimal value. The related message type is set automatically. \n
			:param idn: Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(idn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:ID {param}')

	# noinspection PyTypeChecker
	def get_id_type(self) -> enums.MessageType:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:IDTYpe \n
		Snippet: value: enums.MessageType = driver.configure.cbs.message.get_id_type() \n
		Selects the message type. The related message ID is set automatically. For user-defined CMAS/ETWS, specify the message ID
		via method RsCmwLteSig.Configure.Cbs.Message.id. \n
			:return: type_py: APResidentia | AEXTreme | ASEVere | AAMBer | EARThquake | TSUNami | ETWarning | ETWTest | UDCMas | UDETws APResidentia: presidential alert AEXTreme: extreme alert ASEVere: severe alert AAMBer: amber alert EARThquake: earthquake TSUNami: tsunami ETWarning: earthquake + tsunami ETWTest: ETWS test UDCMas: user-defined CMAS UDETws: user-defined ETWS
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:IDTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.MessageType)

	def set_id_type(self, type_py: enums.MessageType) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:IDTYpe \n
		Snippet: driver.configure.cbs.message.set_id_type(type_py = enums.MessageType.AAMBer) \n
		Selects the message type. The related message ID is set automatically. For user-defined CMAS/ETWS, specify the message ID
		via method RsCmwLteSig.Configure.Cbs.Message.id. \n
			:param type_py: APResidentia | AEXTreme | ASEVere | AAMBer | EARThquake | TSUNami | ETWarning | ETWTest | UDCMas | UDETws APResidentia: presidential alert AEXTreme: extreme alert ASEVere: severe alert AAMBer: amber alert EARThquake: earthquake TSUNami: tsunami ETWarning: earthquake + tsunami ETWTest: ETWS test UDCMas: user-defined CMAS UDETws: user-defined ETWS
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.MessageType)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:IDTYpe {param}')

	# noinspection PyTypeChecker
	class SerialStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Geo_Scope: enums.GeoScope: CIMMediate | PLMN | LOCation | CNORmal Geographical scope CIMMediate: cell immediate PLMN: PLMN normal LOCation: tracking area normal CNORmal: cell normal
			- Message_Code: int: Range: 0 to 1023
			- Auto_Incr: bool: OFF | ON OFF: UpdateNumber is not changed automatically ON: UpdateNumber is increased if message is changed
			- Update_Number: int: Range: 0 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Geo_Scope', enums.GeoScope),
			ArgStruct.scalar_int('Message_Code'),
			ArgStruct.scalar_bool('Auto_Incr'),
			ArgStruct.scalar_int('Update_Number')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Geo_Scope: enums.GeoScope = None
			self.Message_Code: int = None
			self.Auto_Incr: bool = None
			self.Update_Number: int = None

	# noinspection PyTypeChecker
	def get_serial(self) -> SerialStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:SERial \n
		Snippet: value: SerialStruct = driver.configure.cbs.message.get_serial() \n
		Specifies the serial number, consisting of the geographical scope, the message code and the update number. \n
			:return: structure: for return value, see the help for SerialStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:SERial?', self.__class__.SerialStruct())

	def set_serial(self, value: SerialStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:SERial \n
		Snippet: driver.configure.cbs.message.set_serial(value = SerialStruct()) \n
		Specifies the serial number, consisting of the geographical scope, the message code and the update number. \n
			:param value: see the help for SerialStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:SERial', value)

	def get_cgroup(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:CGRoup \n
		Snippet: value: int = driver.configure.cbs.message.get_cgroup() \n
		Queries the coding group of the message. \n
			:return: coding_group: 0: used for internal data source 1: used for file data source
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:CGRoup?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	class LanguageStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Language: int: Range: 0 to 15
			- Lng_Indication: str: Language indication as string"""
		__meta_args_list = [
			ArgStruct.scalar_int('Language'),
			ArgStruct.scalar_str('Lng_Indication')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Language: int = None
			self.Lng_Indication: str = None

	def get_language(self) -> LanguageStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:LANGuage \n
		Snippet: value: LanguageStruct = driver.configure.cbs.message.get_language() \n
		Specifies the language of the message. Setting a language is only possible for the internal data source. For a file data
		source, the value is fixed (1,'UCS-2') . The mapping of language codes to language indication strings is listed in the
		table below. If you specify a value pair that does not match, the specified code is used and the correct string is set
		automatically. \n
			:return: structure: for return value, see the help for LanguageStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:LANGuage?', self.__class__.LanguageStruct())

	def set_language(self, value: LanguageStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:LANGuage \n
		Snippet: driver.configure.cbs.message.set_language(value = LanguageStruct()) \n
		Specifies the language of the message. Setting a language is only possible for the internal data source. For a file data
		source, the value is fixed (1,'UCS-2') . The mapping of language codes to language indication strings is listed in the
		table below. If you specify a value pair that does not match, the specified code is used and the correct string is set
		automatically. \n
			:param value: see the help for LanguageStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:LANGuage', value)

	# noinspection PyTypeChecker
	def get_category(self) -> enums.Priority:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:CATegory \n
		Snippet: value: enums.Priority = driver.configure.cbs.message.get_category() \n
		No command help available \n
			:return: category: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:CATegory?')
		return Conversions.str_to_scalar_enum(response, enums.Priority)

	def set_category(self, category: enums.Priority) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:CATegory \n
		Snippet: driver.configure.cbs.message.set_category(category = enums.Priority.BACKground) \n
		No command help available \n
			:param category: No help available
		"""
		param = Conversions.enum_scalar_to_str(category, enums.Priority)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:CATegory {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.MessageHandling:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:SOURce \n
		Snippet: value: enums.MessageHandling = driver.configure.cbs.message.get_source() \n
		Selects the source of the message text. \n
			:return: message_handling: INTernal | FILE INTernal: message text defined via method RsCmwLteSig.Configure.Cbs.Message.data FILE: message text read from file, selected via method RsCmwLteSig.Configure.Cbs.Message.File.value
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.MessageHandling)

	def set_source(self, message_handling: enums.MessageHandling) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:SOURce \n
		Snippet: driver.configure.cbs.message.set_source(message_handling = enums.MessageHandling.FILE) \n
		Selects the source of the message text. \n
			:param message_handling: INTernal | FILE INTernal: message text defined via method RsCmwLteSig.Configure.Cbs.Message.data FILE: message text read from file, selected via method RsCmwLteSig.Configure.Cbs.Message.File.value
		"""
		param = Conversions.enum_scalar_to_str(message_handling, enums.MessageHandling)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:SOURce {param}')

	def get_data(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:DATA \n
		Snippet: value: str = driver.configure.cbs.message.get_data() \n
		Defines the message text for the data source INTernal. \n
			:return: data: String with up to 1395 characters
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:DATA?')
		return trim_str_response(response)

	def set_data(self, data: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:DATA \n
		Snippet: driver.configure.cbs.message.set_data(data = '1') \n
		Defines the message text for the data source INTernal. \n
			:param data: String with up to 1395 characters
		"""
		param = Conversions.value_to_quoted_str(data)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:DATA {param}')

	def get_ucoded(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:UCODed \n
		Snippet: value: float = driver.configure.cbs.message.get_ucoded() \n
		No command help available \n
			:return: user_coded: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:UCODed?')
		return Conversions.str_to_float(response)

	def set_ucoded(self, user_coded: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:UCODed \n
		Snippet: driver.configure.cbs.message.set_ucoded(user_coded = 1.0) \n
		No command help available \n
			:param user_coded: No help available
		"""
		param = Conversions.decimal_value_to_str(user_coded)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:UCODed {param}')

	def get_wa_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:WAENable \n
		Snippet: value: bool = driver.configure.cbs.message.get_wa_enable() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WAENable?')
		return Conversions.str_to_bool(response)

	def set_wa_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:WAENable \n
		Snippet: driver.configure.cbs.message.set_wa_enable(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WAENable {param}')

	def get_wa_coordinate(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WACoordinate \n
		Snippet: value: float = driver.configure.cbs.message.get_wa_coordinate() \n
		No command help available \n
			:return: wa_coordinates: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WACoordinate?')
		return Conversions.str_to_float(response)

	def set_wa_coordinate(self, wa_coordinates: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WACoordinate \n
		Snippet: driver.configure.cbs.message.set_wa_coordinate(wa_coordinates = 1.0) \n
		No command help available \n
			:param wa_coordinates: No help available
		"""
		param = Conversions.decimal_value_to_str(wa_coordinates)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:WACoordinate {param}')

	def get_period(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:PERiod \n
		Snippet: value: float = driver.configure.cbs.message.get_period() \n
		No command help available \n
			:return: interval: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, interval: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:PERiod \n
		Snippet: driver.configure.cbs.message.set_period(interval = 1.0) \n
		No command help available \n
			:param interval: No help available
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:PERiod {param}')

	def clone(self) -> 'Message':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Message(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
