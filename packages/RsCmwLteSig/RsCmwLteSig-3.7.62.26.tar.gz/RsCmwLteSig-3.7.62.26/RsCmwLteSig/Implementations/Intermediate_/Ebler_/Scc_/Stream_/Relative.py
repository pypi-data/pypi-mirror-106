from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("relative", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Ack: float: Received acknowledgments (percentage of sent scheduled subframes) Range: 0 % to 100 %, Unit: %
			- Nack: float: Received negative acknowledgments (percentage of sent scheduled subframes) Range: 0 % to 100 %, Unit: %
			- Bler: float: Block error ratio (percentage of sent scheduled subframes for which no ACK has been received) Range: 0 % to 100 %, Unit: %
			- Throughput: float: Average DL throughput (percentage of maximum reachable throughput) Range: 0 % to 100 %, Unit: %
			- Dtx: float: Percentage of sent scheduled subframes for which no ACK and no NACK has been received Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ack'),
			ArgStruct.scalar_float('Nack'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_float('Throughput'),
			ArgStruct.scalar_float('Dtx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ack: float = None
			self.Nack: float = None
			self.Bler: float = None
			self.Throughput: float = None
			self.Dtx: float = None

	def fetch(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> FetchStruct:
		"""SCPI: FETCh:INTermediate:LTE:SIGNaling<instance>:EBLer:SCC<Carrier>:STReam<Stream>:RELative \n
		Snippet: value: FetchStruct = driver.intermediate.ebler.scc.stream.relative.fetch(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Returns the relative results of the BLER measurement for one downlink stream of one carrier. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Stream')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'FETCh:INTermediate:LTE:SIGNaling<Instance>:EBLer:SCC{secondaryCompCarrier_cmd_val}:STReam{stream_cmd_val}:RELative?', self.__class__.FetchStruct())
