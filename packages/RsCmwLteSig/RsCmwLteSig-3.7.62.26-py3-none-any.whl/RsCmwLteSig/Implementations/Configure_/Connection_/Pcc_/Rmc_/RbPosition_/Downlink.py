from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


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

	def set(self, position: enums.DownlinkRsrcBlockPosition, stream=repcap.Stream.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:RBPosition:DL<Stream> \n
		Snippet: driver.configure.connection.pcc.rmc.rbPosition.downlink.set(position = enums.DownlinkRsrcBlockPosition.HIGH, stream = repcap.Stream.Default) \n
		Selects the position of the allocated downlink resource blocks within the cell bandwidth. Set the same value for both
		streams of a carrier. The RBs can always be at the lower end, starting with RB number 0, or at the upper end of the
		channel. The other values are only allowed for certain configurations with one TX antenna, see 'DL RMCs, One TX Antenna
		(TM 1) '. \n
			:param position: LOW | HIGH | P5 | P10 | P23 | P35 | P48
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')"""
		param = Conversions.enum_scalar_to_str(position, enums.DownlinkRsrcBlockPosition)
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:RBPosition:DL{stream_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, stream=repcap.Stream.Default) -> enums.DownlinkRsrcBlockPosition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:RMC:RBPosition:DL<Stream> \n
		Snippet: value: enums.DownlinkRsrcBlockPosition = driver.configure.connection.pcc.rmc.rbPosition.downlink.get(stream = repcap.Stream.Default) \n
		Selects the position of the allocated downlink resource blocks within the cell bandwidth. Set the same value for both
		streams of a carrier. The RBs can always be at the lower end, starting with RB number 0, or at the upper end of the
		channel. The other values are only allowed for certain configurations with one TX antenna, see 'DL RMCs, One TX Antenna
		(TM 1) '. \n
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
			:return: position: LOW | HIGH | P5 | P10 | P23 | P35 | P48"""
		stream_cmd_val = self._base.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:RMC:RBPosition:DL{stream_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.DownlinkRsrcBlockPosition)

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
