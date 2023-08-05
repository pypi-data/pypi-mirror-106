from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("absolute", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Sent: List[int]: Number of sent subframes Range: 0 to 2E+9
			- Ack: List[int]: Number of received acknowledgments Range: 0 to 2E+9
			- Nack: List[int]: Number of received negative acknowledgments Range: 0 to 2E+9
			- Dtx: List[int]: Number of sent subframes for which no ACK and no NACK has been received Range: 0 to 2E+9"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Sent', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Ack', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Nack', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dtx', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Sent: List[int] = None
			self.Ack: List[int] = None
			self.Nack: List[int] = None
			self.Dtx: List[int] = None

	def fetch(self, stream=repcap.Stream.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer[:PCC]:HARQ:STReam<Stream>:TRANsmission:ABSolute \n
		Snippet: value: FetchStruct = driver.ebler.pcc.harq.stream.transmission.absolute.fetch(stream = repcap.Stream.Default) \n
		Returns absolute HARQ results for one downlink stream. All columns of the 'HARQ per Transmissions' result table are
		returned: <Reliability>, {<Sent>, <ACK>, <NACK>, <DTX>}column 1, {...}col. 2, {...}col. 3, {...}col. 4 \n
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Stream')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:PCC:HARQ:STReam{stream_cmd_val}:TRANsmission:ABSolute?', self.__class__.FetchStruct())
