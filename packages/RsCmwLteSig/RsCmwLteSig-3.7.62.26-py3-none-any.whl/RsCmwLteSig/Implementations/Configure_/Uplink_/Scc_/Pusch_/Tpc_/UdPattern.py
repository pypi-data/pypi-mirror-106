from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdPattern:
	"""UdPattern commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("udPattern", core, parent)

	# noinspection PyTypeChecker
	class UdPatternStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Pattern_Length: int: Number of values to be considered for the pattern Range: 1 to 20
			- Value_1: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_2: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_3: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_4: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_5: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_6: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_7: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_8: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_9: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_10: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_11: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_12: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_13: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_14: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_15: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_16: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_17: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_18: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_19: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB
			- Value_20: int: Optional setting parameter. Range: -1 dB to 3 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Pattern_Length'),
			ArgStruct.scalar_int('Value_1'),
			ArgStruct.scalar_int('Value_2'),
			ArgStruct.scalar_int('Value_3'),
			ArgStruct.scalar_int('Value_4'),
			ArgStruct.scalar_int('Value_5'),
			ArgStruct.scalar_int('Value_6'),
			ArgStruct.scalar_int('Value_7'),
			ArgStruct.scalar_int('Value_8'),
			ArgStruct.scalar_int('Value_9'),
			ArgStruct.scalar_int('Value_10'),
			ArgStruct.scalar_int('Value_11'),
			ArgStruct.scalar_int('Value_12'),
			ArgStruct.scalar_int('Value_13'),
			ArgStruct.scalar_int('Value_14'),
			ArgStruct.scalar_int('Value_15'),
			ArgStruct.scalar_int('Value_16'),
			ArgStruct.scalar_int('Value_17'),
			ArgStruct.scalar_int('Value_18'),
			ArgStruct.scalar_int('Value_19'),
			ArgStruct.scalar_int('Value_20')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pattern_Length: int = None
			self.Value_1: int = None
			self.Value_2: int = None
			self.Value_3: int = None
			self.Value_4: int = None
			self.Value_5: int = None
			self.Value_6: int = None
			self.Value_7: int = None
			self.Value_8: int = None
			self.Value_9: int = None
			self.Value_10: int = None
			self.Value_11: int = None
			self.Value_12: int = None
			self.Value_13: int = None
			self.Value_14: int = None
			self.Value_15: int = None
			self.Value_16: int = None
			self.Value_17: int = None
			self.Value_18: int = None
			self.Value_19: int = None
			self.Value_20: int = None

	def set(self, structure: UdPatternStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:UDPattern \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.udPattern.set(value = [PROPERTY_STRUCT_NAME](), secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines a pattern for power control of the PUSCH with the TPC setup UDSingle or UDContinuous. The pattern consists of 1
		to 20 TPC commands. To configure the pattern, specify the pattern length and a corresponding number of TPC commands.
		If you specify fewer TPC commands than required according to the pattern length, the previously defined values are used
		for the remaining commands. If you specify more TPC commands than required according to the pattern length, all values
		are set, but only the values corresponding to the pattern length are used. \n
			:param structure: for set value, see the help for UdPatternStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:UDPattern', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> UdPatternStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:UDPattern \n
		Snippet: value: UdPatternStruct = driver.configure.uplink.scc.pusch.tpc.udPattern.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines a pattern for power control of the PUSCH with the TPC setup UDSingle or UDContinuous. The pattern consists of 1
		to 20 TPC commands. To configure the pattern, specify the pattern length and a corresponding number of TPC commands.
		If you specify fewer TPC commands than required according to the pattern length, the previously defined values are used
		for the remaining commands. If you specify more TPC commands than required according to the pattern length, all values
		are set, but only the values corresponding to the pattern length are used. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for UdPatternStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:UDPattern?', self.__class__.UdPatternStruct())
