from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdChannels:
	"""UdChannels commands group definition. 12 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("udChannels", core, parent)

	@property
	def mcluster(self):
		"""mcluster commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcluster'):
			from .UdChannels_.Mcluster import Mcluster
			self._mcluster = Mcluster(self._core, self._base)
		return self._mcluster

	@property
	def emtc(self):
		"""emtc commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_emtc'):
			from .UdChannels_.Emtc import Emtc
			self._emtc = Emtc(self._core, self._base)
		return self._emtc

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .UdChannels_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	# noinspection PyTypeChecker
	class UplinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: int: Number of allocated resource blocks
			- Start_Rb: int: Position of first resource block
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM
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

	def get_uplink(self) -> UplinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:UL \n
		Snippet: value: UplinkStruct = driver.configure.connection.pcc.udChannels.get_uplink() \n
		Configures a user-defined uplink channel with contiguous allocation (no LAA, no eMTC) . The allowed input ranges have
		dependencies and are described in the background information, see 'User-Defined Channels'. \n
			:return: structure: for return value, see the help for UplinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:UL?', self.__class__.UplinkStruct())

	def set_uplink(self, value: UplinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:UL \n
		Snippet: driver.configure.connection.pcc.udChannels.set_uplink(value = UplinkStruct()) \n
		Configures a user-defined uplink channel with contiguous allocation (no LAA, no eMTC) . The allowed input ranges have
		dependencies and are described in the background information, see 'User-Defined Channels'. \n
			:param value: see the help for UplinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:UL', value)

	def clone(self) -> 'UdChannels':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UdChannels(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
