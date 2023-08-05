from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Last:
	"""Last commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("last", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Timestamp: str: Timestamp of the entry as string
			- Category: enums.LogCategory: INFO | WARNing | ERRor | CONTinue Category of the entry, as indicated in the main view by an icon
			- Event: str: Text string describing the event, e.g. 'RRC Connection Established'"""
		__meta_args_list = [
			ArgStruct.scalar_str('Timestamp'),
			ArgStruct.scalar_enum('Category', enums.LogCategory),
			ArgStruct.scalar_str('Event')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamp: str = None
			self.Category: enums.LogCategory = None
			self.Event: str = None

	def get(self, hres: enums.TimeResolution = None) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:ELOG:LAST \n
		Snippet: value: GetStruct = driver.sense.elog.last.get(hres = enums.TimeResolution.HRES) \n
		Queries the latest entry of the event log. \n
			:param hres: HRES If you omit this parameter, the timestamp resolution is 1 s (format 'hh:mm:ss') . If you send the value HRES, the timestamp resolution is 1 ms (format 'hh:mm:ss.sss') .
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hres', hres, DataType.Enum, True))
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:ELOG:LAST? {param}'.rstrip(), self.__class__.GetStruct())
