from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stream:
	"""Stream commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Stream, default value after init: Stream.S1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("stream", core, parent)
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
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Cqi_Median: int: Median reported CQI value Range: 0 to 15
			- Range_Absolute: int: Number of reports received for the range from median CQI - 1 to median CQI + 1 Range: 0 to 2E+9
			- Range_Relative: float: RangeAbsolute as percentage of total number of received reports Range: 0 % to 100 %, Unit: %
			- Bler: float: Block error ratio (percentage of sent scheduled subframes for which no ACK has been received) Range: 0 % to 100 %, Unit: %
			- Total_Number: int: Total number of received CQI reports Range: 0 to 2E+9
			- Expired_Subframes: int: Number of already sent scheduled subframes Range: 0 to 2E+9"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Cqi_Median'),
			ArgStruct.scalar_int('Range_Absolute'),
			ArgStruct.scalar_float('Range_Relative'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_int('Total_Number'),
			ArgStruct.scalar_int('Expired_Subframes')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cqi_Median: int = None
			self.Range_Absolute: int = None
			self.Range_Relative: float = None
			self.Bler: float = None
			self.Total_Number: int = None
			self.Expired_Subframes: int = None

	def fetch(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:SCC<Carrier>:CQIReporting:STReam<Stream> \n
		Snippet: value: FetchStruct = driver.ebler.scc.cqiReporting.stream.fetch(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Returns the single results of the CQI reporting view for one downlink stream of one carrier. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Stream')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:SCC{secondaryCompCarrier_cmd_val}:CQIReporting:STReam{stream_cmd_val}?', self.__class__.FetchStruct())

	def clone(self) -> 'Stream':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stream(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
