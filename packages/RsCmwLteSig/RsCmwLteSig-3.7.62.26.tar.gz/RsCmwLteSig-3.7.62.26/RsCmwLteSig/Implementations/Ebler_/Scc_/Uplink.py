from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Bler: int: Block error ratio (percentage of received uplink subframes with failed CRC check) Range: 0 % to 100 %, Unit: %
			- Throughput: int: Average uplink throughput Unit: bit/s
			- Crc_Pass: int: Number of received subframes with passed CRC check Range: 0 to 2E+9
			- Crc_Fail: int: Number of received subframes with failed CRC check Range: 0 to 2E+9
			- Dtx: int: Number of scheduled UL subframes not sent by the UE Range: 0 to 2E+9
			- Skipped: int: 1..7"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Bler'),
			ArgStruct.scalar_int('Throughput'),
			ArgStruct.scalar_int('Crc_Pass'),
			ArgStruct.scalar_int('Crc_Fail'),
			ArgStruct.scalar_int('Dtx'),
			ArgStruct.scalar_int('Skipped')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bler: int = None
			self.Throughput: int = None
			self.Crc_Pass: int = None
			self.Crc_Fail: int = None
			self.Dtx: int = None
			self.Skipped: int = None

	def fetch(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:SCC<Carrier>:UPLink \n
		Snippet: value: FetchStruct = driver.ebler.scc.uplink.fetch(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the uplink results of the BLER measurement. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:EBLer:SCC{secondaryCompCarrier_cmd_val}:UPLink?', self.__class__.FetchStruct())
