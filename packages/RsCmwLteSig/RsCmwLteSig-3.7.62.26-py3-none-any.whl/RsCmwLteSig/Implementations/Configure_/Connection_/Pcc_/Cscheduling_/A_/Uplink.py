from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: int: Number of allocated resource blocks Range: 0 to 6
			- Start_Rb: int: Position of first resource block Range: 0 to 6
			- Modulation: enums.Modulation: QPSK | Q16 Modulation type QPSK | 16-QAM
			- Trans_Block_Size_Idx: int: Range: 0 to 14"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int('Trans_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: int = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:A:UL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.cscheduling.a.uplink.get_all() \n
		Configures eMTC compact scheduling, uplink, for CE mode A. The indicated input ranges list all possible values.
		The ranges have dependencies described in the background information, see Table 'eMTC compact scheduling settings'. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:A:UL:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:A:UL:ALL \n
		Snippet: driver.configure.connection.pcc.cscheduling.a.uplink.set_all(value = AllStruct()) \n
		Configures eMTC compact scheduling, uplink, for CE mode A. The indicated input ranges list all possible values.
		The ranges have dependencies described in the background information, see Table 'eMTC compact scheduling settings'. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:A:UL:ALL', value)
