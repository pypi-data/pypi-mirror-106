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

	def set(self, structure: AllStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDTTibased:UL:ALL \n
		Snippet: driver.configure.connection.scc.udttiBased.uplink.all.set(value = [PROPERTY_STRUCT_NAME](), secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the uplink channel for all scheduling types with a TTI-based UL definition. The parameters are entered 10
		times, so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ...
		, <NumberRB>9, <StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ...
		, <TransBlockSizeIdx>9 The allowed input ranges have dependencies and are described in the background information, see
		'User-Defined Channels'. For TDD DL and special subframes, you can set OFF or specify a number from the allowed input
		range. The effect is the same. A query returns OFF for non-UL subframes. For UL-DL configuration 0, the settings
		specified for subframe number 2 are automatically applied to all UL subframes. \n
			:param structure: for set value, see the help for AllStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDTTibased:UL:ALL', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDTTibased:UL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.scc.udttiBased.uplink.all.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the uplink channel for all scheduling types with a TTI-based UL definition. The parameters are entered 10
		times, so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ...
		, <NumberRB>9, <StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ...
		, <TransBlockSizeIdx>9 The allowed input ranges have dependencies and are described in the background information, see
		'User-Defined Channels'. For TDD DL and special subframes, you can set OFF or specify a number from the allowed input
		range. The effect is the same. A query returns OFF for non-UL subframes. For UL-DL configuration 0, the settings
		specified for subframe number 2 are automatically applied to all UL subframes. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDTTibased:UL:ALL?', self.__class__.AllStruct())
