from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class B:
	"""B commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("b", core, parent)

	# noinspection PyTypeChecker
	class UplinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Modulation: enums.Modulation: No parameter help available
			- Trans_Block_Size_Idx: int: No parameter help available"""
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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:B:UL \n
		Snippet: value: UplinkStruct = driver.configure.connection.pcc.udChannels.emtc.b.get_uplink() \n
		No command help available \n
			:return: structure: for return value, see the help for UplinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:B:UL?', self.__class__.UplinkStruct())

	def set_uplink(self, value: UplinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:B:UL \n
		Snippet: driver.configure.connection.pcc.udChannels.emtc.b.set_uplink(value = UplinkStruct()) \n
		No command help available \n
			:param value: see the help for UplinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:B:UL', value)

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Modulation: enums.Modulation: No parameter help available
			- Trans_Block_Size_Idx: int: No parameter help available"""
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

	def get_downlink(self) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:B:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.pcc.udChannels.emtc.b.get_downlink() \n
		No command help available \n
			:return: structure: for return value, see the help for DownlinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:B:DL?', self.__class__.DownlinkStruct())

	def set_downlink(self, value: DownlinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:B:DL \n
		Snippet: driver.configure.connection.pcc.udChannels.emtc.b.set_downlink(value = DownlinkStruct()) \n
		No command help available \n
			:param value: see the help for DownlinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:B:DL', value)
