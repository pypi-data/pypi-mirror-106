from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def stti(self):
		"""stti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stti'):
			from .Downlink_.Stti import Stti
			self._stti = Stti(self._core, self._base)
		return self._stti

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
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

	def set(self, structure: DownlinkStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FPRI:DL \n
		Snippet: driver.configure.connection.scc.fpri.downlink.set(value = [PROPERTY_STRUCT_NAME](), secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the downlink for the scheduling type 'Follow WB PMI-RI', with contiguous allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI Channels'. \n
			:param structure: for set value, see the help for DownlinkStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FPRI:DL', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FPRI:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.scc.fpri.downlink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the downlink for the scheduling type 'Follow WB PMI-RI', with contiguous allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI Channels'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FPRI:DL?', self.__class__.DownlinkStruct())

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
