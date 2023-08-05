from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class A:
	"""A commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("a", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .A_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	# noinspection PyTypeChecker
	class UplinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: int: Number of allocated resource blocks Range: 0 to 6
			- Start_Rb: int: Range: 0 to 6
			- Modulation: enums.Modulation: QPSK | Q16 Modulation type QPSK | 16-QAM
			- Trans_Block_Size_Idx: int: Transport block size index Range: 0 to 14"""
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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:A:UL \n
		Snippet: value: UplinkStruct = driver.configure.connection.pcc.udChannels.emtc.a.get_uplink() \n
		Configures a user-defined uplink channel for eMTC, CE mode A. The ranges have dependencies described in the background
		information, see Table 'eMTC user-defined channel settings'. \n
			:return: structure: for return value, see the help for UplinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:A:UL?', self.__class__.UplinkStruct())

	def set_uplink(self, value: UplinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:A:UL \n
		Snippet: driver.configure.connection.pcc.udChannels.emtc.a.set_uplink(value = UplinkStruct()) \n
		Configures a user-defined uplink channel for eMTC, CE mode A. The ranges have dependencies described in the background
		information, see Table 'eMTC user-defined channel settings'. \n
			:param value: see the help for UplinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:A:UL', value)

	def clone(self) -> 'A':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = A(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
