from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("file", core, parent)

	# noinspection PyTypeChecker
	class InfoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Message_Encoding: str: Encoding of the message as string (7-bit 'ascii', 8-bit 'binary', 16-bit 'Unicode')
			- Message_Text: str: Message text as string
			- Message_Length: int: Number of characters in the message Range: 0 to 10E+3
			- Message_Segments: int: Number of segments Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_str('Message_Encoding'),
			ArgStruct.scalar_str('Message_Text'),
			ArgStruct.scalar_int('Message_Length'),
			ArgStruct.scalar_int('Message_Segments')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Message_Encoding: str = None
			self.Message_Text: str = None
			self.Message_Length: int = None
			self.Message_Segments: int = None

	def get_info(self) -> InfoStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:INComing:FILE:INFO \n
		Snippet: value: InfoStruct = driver.configure.sms.incoming.file.get_info() \n
		Displays information about the file selected via method RsCmwLteSig.Configure.Sms.Incoming.File.value. \n
			:return: structure: for return value, see the help for InfoStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:SMS:INComing:FILE:INFO?', self.__class__.InfoStruct())

	def get_value(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:INComing:FILE \n
		Snippet: value: str = driver.configure.sms.incoming.file.get_value() \n
		Selects the file of a received message. You can display information about the selected file via the command method
		RsCmwLteSig.Configure.Sms.Incoming.File.info. \n
			:return: sms_file: Path of the file as string, for example: '@USERDATA/sms/LTE/Received/rx_001.sms'
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:INComing:FILE?')
		return trim_str_response(response)

	def set_value(self, sms_file: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SMS:INComing:FILE \n
		Snippet: driver.configure.sms.incoming.file.set_value(sms_file = '1') \n
		Selects the file of a received message. You can display information about the selected file via the command method
		RsCmwLteSig.Configure.Sms.Incoming.File.info. \n
			:param sms_file: Path of the file as string, for example: '@USERDATA/sms/LTE/Received/rx_001.sms'
		"""
		param = Conversions.value_to_quoted_str(sms_file)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:INComing:FILE {param}')
