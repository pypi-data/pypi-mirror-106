from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcluster:
	"""Mcluster commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mcluster", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Mcluster_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	# noinspection PyTypeChecker
	class UplinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb_1: int: Number of allocated resource blocks, cluster 1
			- Start_Rb_1: int: Position of first RB, cluster 1
			- Number_Rb_2: int: Number of allocated resource blocks, cluster 2
			- Start_Rb_2: int: Position of first RB, cluster 2
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM
			- Trans_Block_Size_Idx: int: Transport block size index"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Rb_1'),
			ArgStruct.scalar_int('Start_Rb_1'),
			ArgStruct.scalar_int('Number_Rb_2'),
			ArgStruct.scalar_int('Start_Rb_2'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int('Trans_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb_1: int = None
			self.Start_Rb_1: int = None
			self.Number_Rb_2: int = None
			self.Start_Rb_2: int = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: int = None

	def get_uplink(self) -> UplinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:MCLuster:UL \n
		Snippet: value: UplinkStruct = driver.configure.connection.pcc.udChannels.mcluster.get_uplink() \n
		Configures a user-defined uplink channel with multi-cluster allocation. The allowed input ranges have dependencies and
		are described in the background information, see 'User-Defined Channels'. \n
			:return: structure: for return value, see the help for UplinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:MCLuster:UL?', self.__class__.UplinkStruct())

	def set_uplink(self, value: UplinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:MCLuster:UL \n
		Snippet: driver.configure.connection.pcc.udChannels.mcluster.set_uplink(value = UplinkStruct()) \n
		Configures a user-defined uplink channel with multi-cluster allocation. The allowed input ranges have dependencies and
		are described in the background information, see 'User-Defined Channels'. \n
			:param value: see the help for UplinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:MCLuster:UL', value)

	def clone(self) -> 'Mcluster':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mcluster(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
