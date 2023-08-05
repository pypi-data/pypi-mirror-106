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
			- Number_Rb: enums.NumberRb: ZERO | N1 | N2 Number of allocated resource blocks
			- Start_Rb: int: Position of first resource block Range: 0 to 5
			- Narrow_Band: int: Narrowband for the first transmission Range: 0 to 15
			- Modulation: enums.Modulation: QPSK Modulation type QPSK
			- Transp_Block_Size_Idx: int: Transport block size index Range: 0 to 10"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Number_Rb', enums.NumberRb),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_int('Narrow_Band'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int('Transp_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: enums.NumberRb = None
			self.Start_Rb: int = None
			self.Narrow_Band: int = None
			self.Modulation: enums.Modulation = None
			self.Transp_Block_Size_Idx: int = None

	# noinspection PyTypeChecker
	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:EMAMode:B:UL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.emamode.b.uplink.get_all() \n
		Configures the eMTC auto mode, uplink, for CE mode B. The indicated input ranges list all possible values. The ranges
		have dependencies described in the background information, see Table 'eMTC auto mode settings'. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:EMAMode:B:UL:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:EMAMode:B:UL:ALL \n
		Snippet: driver.configure.connection.pcc.emamode.b.uplink.set_all(value = AllStruct()) \n
		Configures the eMTC auto mode, uplink, for CE mode B. The indicated input ranges list all possible values. The ranges
		have dependencies described in the background information, see Table 'eMTC auto mode settings'. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:EMAMode:B:UL:ALL', value)
