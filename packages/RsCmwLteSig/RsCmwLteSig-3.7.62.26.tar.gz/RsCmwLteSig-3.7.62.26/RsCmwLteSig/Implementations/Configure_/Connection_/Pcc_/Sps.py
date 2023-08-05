from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sps:
	"""Sps commands group definition. 5 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sps", core, parent)

	@property
	def sinterval(self):
		"""sinterval commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sinterval'):
			from .Sps_.Sinterval import Sinterval
			self._sinterval = Sinterval(self._core, self._base)
		return self._sinterval

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Sps_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	def get_ti_config(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:TIConfig \n
		Snippet: value: bool = driver.configure.connection.pcc.sps.get_ti_config() \n
		Configures the parameter 'twoIntervalsConfig', signaled to the UE for the scheduling type SPS in TDD mode. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:TIConfig?')
		return Conversions.str_to_bool(response)

	def set_ti_config(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:TIConfig \n
		Snippet: driver.configure.connection.pcc.sps.set_ti_config(enable = False) \n
		Configures the parameter 'twoIntervalsConfig', signaled to the UE for the scheduling type SPS in TDD mode. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:TIConfig {param}')

	# noinspection PyTypeChecker
	class UplinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: int: Number of allocated resource blocks
			- Start_Rb: int: Position of first resource block
			- Modulation: enums.Modulation: QPSK | Q16 Modulation type QPSK | 16-QAM
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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:UL \n
		Snippet: value: UplinkStruct = driver.configure.connection.pcc.sps.get_uplink() \n
		Configures the uplink RB allocation for the scheduling type SPS. The allowed input ranges have dependencies and are
		described in the background information, see 'Semi-Persistent Scheduling (SPS) '. \n
			:return: structure: for return value, see the help for UplinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:UL?', self.__class__.UplinkStruct())

	def set_uplink(self, value: UplinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:UL \n
		Snippet: driver.configure.connection.pcc.sps.set_uplink(value = UplinkStruct()) \n
		Configures the uplink RB allocation for the scheduling type SPS. The allowed input ranges have dependencies and are
		described in the background information, see 'Semi-Persistent Scheduling (SPS) '. \n
			:param value: see the help for UplinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:UL', value)

	def clone(self) -> 'Sps':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sps(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
