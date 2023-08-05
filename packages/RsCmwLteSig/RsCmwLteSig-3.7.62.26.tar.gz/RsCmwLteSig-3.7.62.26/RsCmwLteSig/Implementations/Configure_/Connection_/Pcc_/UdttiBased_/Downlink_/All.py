from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Number_Rb: List[int]: Number of allocated resource blocks. The same value must be configured for all streams of the carrier.
			- Start_Rb: List[int]: Position of first resource block. The same value must be configured for all streams of the carrier.
			- Modulation: List[enums.Modulation]: QPSK | Q16 | Q64 | Q256 | OFF Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM | no DL subframe
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

	def set(self, structure: AllStruct, stream=repcap.Stream.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:DL<Stream>:ALL \n
		Snippet: driver.configure.connection.pcc.udttiBased.downlink.all.set(value = [PROPERTY_STRUCT_NAME](), stream = repcap.Stream.Default) \n
		Configures all downlink subframes for the scheduling type 'User-defined TTI-Based'. The parameters are entered 10 times,
		so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ..., <NumberRB>9,
		<StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ..., <TransBlockSizeIdx>9 The
		allowed input ranges have dependencies and are described in the background information, see 'User-Defined Channels'. For
		TDD UL and special subframes, you can set OFF or specify a number from the allowed input range. The effect is the same. A
		query returns OFF for non-DL subframes. \n
			:param structure: for set value, see the help for AllStruct structure arguments.
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')"""
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:DL{stream_cmd_val}:ALL', structure)

	def get(self, stream=repcap.Stream.Default) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:DL<Stream>:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.udttiBased.downlink.all.get(stream = repcap.Stream.Default) \n
		Configures all downlink subframes for the scheduling type 'User-defined TTI-Based'. The parameters are entered 10 times,
		so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ..., <NumberRB>9,
		<StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ..., <TransBlockSizeIdx>9 The
		allowed input ranges have dependencies and are described in the background information, see 'User-Defined Channels'. For
		TDD UL and special subframes, you can set OFF or specify a number from the allowed input range. The effect is the same. A
		query returns OFF for non-DL subframes. \n
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:DL{stream_cmd_val}:ALL?', self.__class__.AllStruct())
