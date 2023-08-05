from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uul:
	"""Uul commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uul", core, parent)

	# noinspection PyTypeChecker
	class UulStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Use_Uplink: bool: OFF | ON
			- Scc_Rx_Connector: enums.RxConnector: Optional setting parameter. RF connector for the SCC input path
			- Scc_Rx_Converter: enums.RxConverter: Optional setting parameter. RX module for the SCC input path"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Use_Uplink'),
			ArgStruct.scalar_enum('Scc_Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Scc_Rx_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Use_Uplink: bool = None
			self.Scc_Rx_Connector: enums.RxConnector = None
			self.Scc_Rx_Converter: enums.RxConverter = None

	def set(self, structure: UulStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:UUL \n
		Snippet: driver.configure.scc.uul.set(value = [PROPERTY_STRUCT_NAME](), secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Activates the uplink for the SCC number <c> and optionally selects the signal path. For possible connector and converter
		values, see 'Values for Signal Path Selection'. \n
			:param structure: for set value, see the help for UulStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:UUL', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> UulStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:UUL \n
		Snippet: value: UulStruct = driver.configure.scc.uul.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Activates the uplink for the SCC number <c> and optionally selects the signal path. For possible connector and converter
		values, see 'Values for Signal Path Selection'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for UulStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:UUL?', self.__class__.UulStruct())
