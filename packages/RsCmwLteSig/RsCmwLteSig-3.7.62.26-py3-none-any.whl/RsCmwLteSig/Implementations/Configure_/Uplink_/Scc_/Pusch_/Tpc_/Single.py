from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Single:
	"""Single commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("single", core, parent)

	# noinspection PyTypeChecker
	class SingleStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- No_Of_Steps: int: Range: 1 to 35
			- Step_Direction: enums.UpDownDirection: UP | DOWN"""
		__meta_args_list = [
			ArgStruct.scalar_int('No_Of_Steps'),
			ArgStruct.scalar_enum('Step_Direction', enums.UpDownDirection)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.No_Of_Steps: int = None
			self.Step_Direction: enums.UpDownDirection = None

	def set(self, structure: SingleStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:SINGle \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.single.set(value = [PROPERTY_STRUCT_NAME](), secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines a pattern for power control of the PUSCH with the TPC setup SINGle. The pattern consists of 1 to 35 up (+1 dB) or
		down (-1 dB) commands, followed by 'constant power' commands (0 dB) . \n
			:param structure: for set value, see the help for SingleStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:SINGle', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> SingleStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:SINGle \n
		Snippet: value: SingleStruct = driver.configure.uplink.scc.pusch.tpc.single.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines a pattern for power control of the PUSCH with the TPC setup SINGle. The pattern consists of 1 to 35 up (+1 dB) or
		down (-1 dB) commands, followed by 'constant power' commands (0 dB) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for SingleStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:SINGle?', self.__class__.SingleStruct())
