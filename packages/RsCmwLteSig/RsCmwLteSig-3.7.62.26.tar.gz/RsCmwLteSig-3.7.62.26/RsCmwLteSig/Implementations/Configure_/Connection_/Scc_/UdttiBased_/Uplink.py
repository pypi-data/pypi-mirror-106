from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .Uplink_.All import All
			self._all = All(self._core, self._base)
		return self._all

	def set(self, tti: float, number_rb: int, start_rb: int, modulation: enums.Modulation, trans_block_size_idx: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDTTibased:UL \n
		Snippet: driver.configure.connection.scc.udttiBased.uplink.set(tti = 1.0, number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures a selected uplink subframe for all scheduling types with a TTI-based UL definition. The allowed input ranges
		have dependencies and are described in the background information, see 'User-Defined Channels'. A query for TDD can also
		return OFF,OFF,OFF,OFF, indicating that the queried subframe is no UL subframe. For UL-DL configuration 0, use the
		command method RsCmwLteSig.Configure.Connection.Scc.UdttiBased.Uplink.All.set. \n
			:param tti: Number of the subframe to be configured/queried. Range: 0 to 9
			:param number_rb: Number of allocated resource blocks
			:param start_rb: Position of first resource block
			:param modulation: QPSK | Q16 | Q64 | Q256 | OFF Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM | no UL subframe
			:param trans_block_size_idx: Transport block size index
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tti', tti, DataType.Float), ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.Integer))
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDTTibased:UL {param}'.rstrip())

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

	def get(self, tti: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDTTibased:UL \n
		Snippet: value: GetStruct = driver.configure.connection.scc.udttiBased.uplink.get(tti = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures a selected uplink subframe for all scheduling types with a TTI-based UL definition. The allowed input ranges
		have dependencies and are described in the background information, see 'User-Defined Channels'. A query for TDD can also
		return OFF,OFF,OFF,OFF, indicating that the queried subframe is no UL subframe. For UL-DL configuration 0, use the
		command method RsCmwLteSig.Configure.Connection.Scc.UdttiBased.Uplink.All.set. \n
			:param tti: Number of the subframe to be configured/queried. Range: 0 to 9
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(tti)
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDTTibased:UL? {param}', self.__class__.GetStruct())

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
