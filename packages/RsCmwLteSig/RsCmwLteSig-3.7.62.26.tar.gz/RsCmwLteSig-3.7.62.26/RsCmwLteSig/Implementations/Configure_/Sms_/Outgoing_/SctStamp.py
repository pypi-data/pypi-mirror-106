from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SctStamp:
	"""SctStamp commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sctStamp", core, parent)

	# noinspection PyTypeChecker
	def get_tsource(self) -> enums.SourceTime:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TSOurce \n
		Snippet: value: enums.SourceTime = driver.configure.sms.outgoing.sctStamp.get_tsource() \n
		Selects the source for the service center time stamp.
			INTRO_CMD_HELP: The date and time for the source DATE is configured via the following commands: \n
			- method RsCmwLteSig.Configure.Sms.Outgoing.SctStamp.date
			- method RsCmwLteSig.Configure.Sms.Outgoing.SctStamp.time \n
			:return: source_time: CMWTime | DATE CMWTime: Current date and time of the operation system DATE: Date and time specified via remote commands
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TSOurce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceTime)

	def set_tsource(self, source_time: enums.SourceTime) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TSOurce \n
		Snippet: driver.configure.sms.outgoing.sctStamp.set_tsource(source_time = enums.SourceTime.CMWTime) \n
		Selects the source for the service center time stamp.
			INTRO_CMD_HELP: The date and time for the source DATE is configured via the following commands: \n
			- method RsCmwLteSig.Configure.Sms.Outgoing.SctStamp.date
			- method RsCmwLteSig.Configure.Sms.Outgoing.SctStamp.time \n
			:param source_time: CMWTime | DATE CMWTime: Current date and time of the operation system DATE: Date and time specified via remote commands
		"""
		param = Conversions.enum_scalar_to_str(source_time, enums.SourceTime)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TSOurce {param}')

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Day: int: Range: 1 to 31
			- Month: int: Range: 1 to 12
			- Year: int: Range: 2011 to 9999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Day'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Year')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Day: int = None
			self.Month: int = None
			self.Year: int = None

	def get_date(self) -> DateStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:DATE \n
		Snippet: value: DateStruct = driver.configure.sms.outgoing.sctStamp.get_date() \n
		Specifies the date of the service center time stamp for the time source DATE (see method RsCmwLteSig.Configure.Sms.
		Outgoing.SctStamp.tsource) . \n
			:return: structure: for return value, see the help for DateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:DATE?', self.__class__.DateStruct())

	def set_date(self, value: DateStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:DATE \n
		Snippet: driver.configure.sms.outgoing.sctStamp.set_date(value = DateStruct()) \n
		Specifies the date of the service center time stamp for the time source DATE (see method RsCmwLteSig.Configure.Sms.
		Outgoing.SctStamp.tsource) . \n
			:param value: see the help for DateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:DATE', value)

	# noinspection PyTypeChecker
	class TimeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hour: int: Range: 0 to 23
			- Minute: int: Range: 0 to 59
			- Second: int: Range: 0 to 59"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_int('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None
			self.Second: int = None

	def get_time(self) -> TimeStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TIME \n
		Snippet: value: TimeStruct = driver.configure.sms.outgoing.sctStamp.get_time() \n
		Specifies the time of the service center time stamp for the time source DATE (see method RsCmwLteSig.Configure.Sms.
		Outgoing.SctStamp.tsource) . \n
			:return: structure: for return value, see the help for TimeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TIME?', self.__class__.TimeStruct())

	def set_time(self, value: TimeStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TIME \n
		Snippet: driver.configure.sms.outgoing.sctStamp.set_time(value = TimeStruct()) \n
		Specifies the time of the service center time stamp for the time source DATE (see method RsCmwLteSig.Configure.Sms.
		Outgoing.SctStamp.tsource) . \n
			:param value: see the help for TimeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TIME', value)
