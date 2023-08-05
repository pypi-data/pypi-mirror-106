from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Stream, default value after init: Stream.S1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_stream_get', 'repcap_stream_set', repcap.Stream.S1)

	def repcap_stream_set(self, enum_value: repcap.Stream) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Stream.Default
		Default value after init: Stream.S1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_stream_get(self) -> repcap.Stream:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Number_Rb: enums.NumberRb: ZERO | N1 | N2 | N3 | N4 | N5 | N6 | N7 | N8 | N9 | N10 | N12 | N15 | N16 | N17 | N18 | N20 | N24 | N25 | N27 | N30 | N32 | N36 | N40 | N42 | N45 | N48 | N50 | N54 | N60 | N64 | N72 | N75 | N80 | N81 | N83 | N90 | N92 | N96 | N100 Number of allocated resource blocks. The same value must be configured for all streams of the carrier.
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

	def set(self, structure: DownlinkStruct, stream=repcap.Stream.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:DL<Stream> \n
		Snippet: driver.configure.connection.pcc.rmc.downlink.set(value = [PROPERTY_STRUCT_NAME](), stream = repcap.Stream.Default) \n
		Configures a downlink reference measurement channel (RMC) . Only certain value combinations are accepted, see 'Scheduling
		Type RMC'. \n
			:param structure: for set value, see the help for DownlinkStruct structure arguments.
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')"""
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:DL{stream_cmd_val}', structure)

	def get(self, stream=repcap.Stream.Default) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:DL<Stream> \n
		Snippet: value: DownlinkStruct = driver.configure.connection.pcc.rmc.downlink.get(stream = repcap.Stream.Default) \n
		Configures a downlink reference measurement channel (RMC) . Only certain value combinations are accepted, see 'Scheduling
		Type RMC'. \n
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:DL{stream_cmd_val}?', self.__class__.DownlinkStruct())

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
