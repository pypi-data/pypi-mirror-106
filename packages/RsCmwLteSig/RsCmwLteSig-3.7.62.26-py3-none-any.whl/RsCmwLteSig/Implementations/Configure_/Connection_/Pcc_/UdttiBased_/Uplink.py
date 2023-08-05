from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	def set(self, tti: float, number_rb: int, start_rb: int, modulation: enums.Modulation, trans_block_size_idx: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL \n
		Snippet: driver.configure.connection.pcc.udttiBased.uplink.set(tti = 1.0, number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1) \n
		Configures a selected uplink subframe for all scheduling types with a TTI-based UL definition. The allowed input ranges
		have dependencies and are described in the background information, see 'User-Defined Channels'. A query for TDD can also
		return OFF,OFF,OFF,OFF, indicating that the queried subframe is no UL subframe. For UL-DL configuration 0, use the
		command method RsCmwLteSig.Configure.Connection.Scc.UdttiBased.Uplink.All.set. \n
			:param tti: Number of the subframe to be configured/queried. Range: 0 to 9
			:param number_rb: Number of allocated resource blocks
			:param start_rb: Position of first resource block
			:param modulation: QPSK | Q16 | Q64 | Q256 | OFF Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM | no UL subframe
			:param trans_block_size_idx: Transport block size index
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tti', tti, DataType.Float), ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: int: Number of allocated resource blocks
			- Start_Rb: int: Position of first resource block
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 | OFF Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM | no UL subframe
			- Trans_Block_Size_Idx: int: Transport block size index"""
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

	def get(self, tti: float) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL \n
		Snippet: value: GetStruct = driver.configure.connection.pcc.udttiBased.uplink.get(tti = 1.0) \n
		Configures a selected uplink subframe for all scheduling types with a TTI-based UL definition. The allowed input ranges
		have dependencies and are described in the background information, see 'User-Defined Channels'. A query for TDD can also
		return OFF,OFF,OFF,OFF, indicating that the queried subframe is no UL subframe. For UL-DL configuration 0, use the
		command method RsCmwLteSig.Configure.Connection.Scc.UdttiBased.Uplink.All.set. \n
			:param tti: Number of the subframe to be configured/queried. Range: 0 to 9
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(tti)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL? {param}', self.__class__.GetStruct())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: List[int]: Number of allocated resource blocks
			- Start_Rb: List[int]: Position of first resource block
			- Modulation: List[enums.Modulation]: QPSK | Q16 | Q64 | Q256 | OFF Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM | no UL subframe
			- Trans_Block_Size_Idx: List[int]: Transport block size index"""
		__meta_args_list = [
			ArgStruct('Number_Rb', DataType.IntegerList, None, False, False, 10),
			ArgStruct('Start_Rb', DataType.IntegerList, None, False, False, 10),
			ArgStruct('Modulation', DataType.EnumList, enums.Modulation, False, False, 10),
			ArgStruct('Trans_Block_Size_Idx', DataType.IntegerList, None, False, False, 10)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: List[int] = None
			self.Start_Rb: List[int] = None
			self.Modulation: List[enums.Modulation] = None
			self.Trans_Block_Size_Idx: List[int] = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.udttiBased.uplink.get_all() \n
		Configures the uplink channel for all scheduling types with a TTI-based UL definition. The parameters are entered 10
		times, so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ...
		, <NumberRB>9, <StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ...
		, <TransBlockSizeIdx>9 The allowed input ranges have dependencies and are described in the background information, see
		'User-Defined Channels'. For TDD DL and special subframes, you can set OFF or specify a number from the allowed input
		range. The effect is the same. A query returns OFF for non-UL subframes. For UL-DL configuration 0, the settings
		specified for subframe number 2 are automatically applied to all UL subframes. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL:ALL \n
		Snippet: driver.configure.connection.pcc.udttiBased.uplink.set_all(value = AllStruct()) \n
		Configures the uplink channel for all scheduling types with a TTI-based UL definition. The parameters are entered 10
		times, so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ...
		, <NumberRB>9, <StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ...
		, <TransBlockSizeIdx>9 The allowed input ranges have dependencies and are described in the background information, see
		'User-Defined Channels'. For TDD DL and special subframes, you can set OFF or specify a number from the allowed input
		range. The effect is the same. A query returns OFF for non-UL subframes. For UL-DL configuration 0, the settings
		specified for subframe number 2 are automatically applied to all UL subframes. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL:ALL', value)
