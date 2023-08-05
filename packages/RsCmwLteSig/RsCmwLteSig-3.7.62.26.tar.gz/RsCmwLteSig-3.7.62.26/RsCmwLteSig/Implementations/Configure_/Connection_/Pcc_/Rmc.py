from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmc:
	"""Rmc commands group definition. 9 total commands, 5 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rmc", core, parent)

	@property
	def mcluster(self):
		"""mcluster commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcluster'):
			from .Rmc_.Mcluster import Mcluster
			self._mcluster = Mcluster(self._core, self._base)
		return self._mcluster

	@property
	def emtc(self):
		"""emtc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_emtc'):
			from .Rmc_.Emtc import Emtc
			self._emtc = Emtc(self._core, self._base)
		return self._emtc

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Rmc_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def rbPosition(self):
		"""rbPosition commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbPosition'):
			from .Rmc_.RbPosition import RbPosition
			self._rbPosition = RbPosition(self._core, self._base)
		return self._rbPosition

	@property
	def version(self):
		"""version commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_version'):
			from .Rmc_.Version import Version
			self._version = Version(self._core, self._base)
		return self._version

	# noinspection PyTypeChecker
	class UplinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: enums.NumberRb: ZERO | N1 | N2 | N3 | N4 | N5 | N6 | N7 | N8 | N9 | N10 | N12 | N15 | N16 | N17 | N18 | N20 | N24 | N25 | N27 | N30 | N32 | N36 | N40 | N42 | N45 | N48 | N50 | N54 | N60 | N64 | N72 | N75 | N80 | N81 | N83 | N90 | N92 | N96 | N100 Number of allocated resource blocks
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM
			- Trans_Block_Size_Idx: enums.TransBlockSizeIdx: ZERO | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T10 | T11 | T12 | T13 | T14 | T15 | T17 | T18 | T19 | T21 | T22 | T23 | T24 | T25 | T30 | T31 | T32 | T8 | T9 | T16 | T20 | T26 | T27 | T28 | T29 Transport block size index. Use KEEP to select a compatible value."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Number_Rb', enums.NumberRb),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_enum('Trans_Block_Size_Idx', enums.TransBlockSizeIdx)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: enums.NumberRb = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: enums.TransBlockSizeIdx = None

	# noinspection PyTypeChecker
	def get_uplink(self) -> UplinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:UL \n
		Snippet: value: UplinkStruct = driver.configure.connection.pcc.rmc.get_uplink() \n
		Configures an uplink reference measurement channel (RMC) with contiguous allocation. Only certain value combinations are
		accepted, see 'Scheduling Type RMC'. \n
			:return: structure: for return value, see the help for UplinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:UL?', self.__class__.UplinkStruct())

	def set_uplink(self, value: UplinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:UL \n
		Snippet: driver.configure.connection.pcc.rmc.set_uplink(value = UplinkStruct()) \n
		Configures an uplink reference measurement channel (RMC) with contiguous allocation. Only certain value combinations are
		accepted, see 'Scheduling Type RMC'. \n
			:param value: see the help for UplinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:UL', value)

	def clone(self) -> 'Rmc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rmc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
