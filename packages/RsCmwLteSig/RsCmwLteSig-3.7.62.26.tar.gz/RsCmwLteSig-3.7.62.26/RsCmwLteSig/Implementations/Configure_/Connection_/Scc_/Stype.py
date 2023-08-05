from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stype:
	"""Stype commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("stype", core, parent)

	# noinspection PyTypeChecker
	class StypeStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Type_Py: enums.SchedulingType: RMC | UDCHannels | UDTTibased | CQI | SPS | EMAMode | EMCSched RMC: 3GPP-compliant reference measurement channel UDCHannels: user-defined channel UDTTibased: user-defined channel configurable per TTI CQI: CQI channel, as specified by next parameter SPS: semi-persistent scheduling (only PCC, not SCC) EMAMode: eMTC auto mode EMCSched: eMTC compact scheduling
			- Cqi_Mode: enums.CqiMode: Optional setting parameter. TTIBased | FWB | FPMI | FCPRi | FCRI | FPRI Only relevant for Type = CQI TTIBased: fixed CQI FWB: follow wideband CQI FPMI: follow wideband PMI FCPRi: follow wideband CQI-PMI-RI FCRI: follow wideband CQI-RI FPRI: follow wideband PMI-RI"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Type_Py', enums.SchedulingType),
			ArgStruct.scalar_enum('Cqi_Mode', enums.CqiMode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Type_Py: enums.SchedulingType = None
			self.Cqi_Mode: enums.CqiMode = None

	def set(self, structure: StypeStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:STYPe \n
		Snippet: driver.configure.connection.scc.stype.set(value = [PROPERTY_STRUCT_NAME](), secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the scheduling type. \n
			:param structure: for set value, see the help for StypeStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:STYPe', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> StypeStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:STYPe \n
		Snippet: value: StypeStruct = driver.configure.connection.scc.stype.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the scheduling type. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for StypeStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:STYPe?', self.__class__.StypeStruct())
