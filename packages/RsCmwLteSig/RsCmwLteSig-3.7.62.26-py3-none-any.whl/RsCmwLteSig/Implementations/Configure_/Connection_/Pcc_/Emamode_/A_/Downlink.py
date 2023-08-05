from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def anb(self):
		"""anb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_anb'):
			from .Downlink_.Anb import Anb
			self._anb = Anb(self._core, self._base)
		return self._anb

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: enums.NumberRb: ZERO | N1 | N2 | N3 | N4 | N5 | N6 Number of allocated resource blocks
			- Start_Rb: int: Position of first resource block Range: 0 to 6
			- Narrow_Band: int: Narrowband for the first transmission Range: 0 to 15
			- Modulation: enums.Modulation: QPSK | Q16 Modulation type QPSK | 16-QAM
			- Transp_Block_Size_Idx: int: Transport block size index Range: 0 to 14"""
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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:EMAMode:A:DL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.emamode.a.downlink.get_all() \n
		Configures the eMTC auto mode, downlink, for CE mode A. The indicated input ranges list all possible values. The ranges
		have dependencies described in the background information, see Table 'eMTC auto mode settings'. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:EMAMode:A:DL:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:EMAMode:A:DL:ALL \n
		Snippet: driver.configure.connection.pcc.emamode.a.downlink.set_all(value = AllStruct()) \n
		Configures the eMTC auto mode, downlink, for CE mode A. The indicated input ranges list all possible values. The ranges
		have dependencies described in the background information, see Table 'eMTC auto mode settings'. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:EMAMode:A:DL:ALL', value)

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
