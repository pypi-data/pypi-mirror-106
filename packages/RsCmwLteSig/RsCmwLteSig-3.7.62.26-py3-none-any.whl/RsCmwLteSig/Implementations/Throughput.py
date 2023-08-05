from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 15 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Throughput_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Throughput_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def stop(self) -> None:
		"""SCPI: STOP:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:LTE:SIGNaling<Instance>:THRoughput')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:LTE:SIGNaling<Instance>:THRoughput')

	def abort(self) -> None:
		"""SCPI: ABORt:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:LTE:SIGNaling<Instance>:THRoughput')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:LTE:SIGNaling<Instance>:THRoughput')

	def initiate(self) -> None:
		"""SCPI: INITiate:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:LTE:SIGNaling<Instance>:THRoughput')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:LTE:SIGNaling<Instance>:THRoughput')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Curr_Dl_Pdu: float: Current downlink throughput Unit: bit/s
			- Avg_Dl_Pdu: float: Average downlink throughput Unit: bit/s
			- Max_Dl_Pdu: float: Maximum downlink throughput Unit: bit/s
			- Min_Dl_Pdu: float: Minimum downlink throughput Unit: bit/s
			- Bytes_Dl_Pdu: int: Number of bytes transmitted in the downlink
			- Curr_Ul_Pdu: float: Current uplink throughput Unit: bit/s
			- Avg_Ul_Pdu: float: Average uplink throughput Unit: bit/s
			- Max_Ul_Pdu: float: Maximum uplink throughput Unit: bit/s
			- Min_Ul_Pdu: float: Minimum uplink throughput Unit: bit/s
			- Bytes_Ul_Pdu: float: Number of bytes received in the uplink"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Curr_Dl_Pdu'),
			ArgStruct.scalar_float('Avg_Dl_Pdu'),
			ArgStruct.scalar_float('Max_Dl_Pdu'),
			ArgStruct.scalar_float('Min_Dl_Pdu'),
			ArgStruct.scalar_int('Bytes_Dl_Pdu'),
			ArgStruct.scalar_float('Curr_Ul_Pdu'),
			ArgStruct.scalar_float('Avg_Ul_Pdu'),
			ArgStruct.scalar_float('Max_Ul_Pdu'),
			ArgStruct.scalar_float('Min_Ul_Pdu'),
			ArgStruct.scalar_float('Bytes_Ul_Pdu')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Curr_Dl_Pdu: float = None
			self.Avg_Dl_Pdu: float = None
			self.Max_Dl_Pdu: float = None
			self.Min_Dl_Pdu: float = None
			self.Bytes_Dl_Pdu: int = None
			self.Curr_Ul_Pdu: float = None
			self.Avg_Ul_Pdu: float = None
			self.Max_Ul_Pdu: float = None
			self.Min_Ul_Pdu: float = None
			self.Bytes_Ul_Pdu: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: value: ResultData = driver.throughput.fetch() \n
		Returns the contents of the RLC throughput result table. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:LTE:SIGNaling<Instance>:THRoughput?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:LTE:SIGNaling<instance>:THRoughput \n
		Snippet: value: ResultData = driver.throughput.read() \n
		Returns the contents of the RLC throughput result table. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:LTE:SIGNaling<Instance>:THRoughput?', self.__class__.ResultData())

	def clone(self) -> 'Throughput':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Throughput(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
