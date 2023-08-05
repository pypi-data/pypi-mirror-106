from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpc:
	"""Tpc commands group definition. 8 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tpc", core, parent)

	@property
	def pexecute(self):
		"""pexecute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pexecute'):
			from .Tpc_.Pexecute import Pexecute
			self._pexecute = Pexecute(self._core, self._base)
		return self._pexecute

	@property
	def cltPower(self):
		"""cltPower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cltPower'):
			from .Tpc_.CltPower import CltPower
			self._cltPower = CltPower(self._core, self._base)
		return self._cltPower

	# noinspection PyTypeChecker
	def get_set(self) -> enums.SetType:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:SET \n
		Snippet: value: enums.SetType = driver.configure.uplink.setc.pusch.tpc.get_set() \n
		Selects the active TPC setup to be executed for power control of the PUSCH. For some TPC setups, the execution must be
		explicitly triggered via CONFigure:LTE:SIGN<i>:PUSCh:TPC:PEXecute. \n
			:return: set_type: MINPower | MAXPower | CONStant | SINGle | UDSingle | UDContinuous | ALT0 | CLOop | RPControl | FULPower MINPower: command the UE to minimum power MAXPower: command the UE to maximum power CONStant: command the UE to keep the power constant SINGle: send a pattern once (only one type of TPC command) UDSingle: send a pattern once (mixed TPC commands allowed) UDContinuous: send a pattern continuously ALT0: send an alternating pattern continuously CLOop: command the UE to a configurable target power RPControl: patterns for 3GPP relative power control test FULPower: flexible uplink power
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:SET?')
		return Conversions.str_to_scalar_enum(response, enums.SetType)

	def set_set(self, set_type: enums.SetType) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:SET \n
		Snippet: driver.configure.uplink.setc.pusch.tpc.set_set(set_type = enums.SetType.ALT0) \n
		Selects the active TPC setup to be executed for power control of the PUSCH. For some TPC setups, the execution must be
		explicitly triggered via CONFigure:LTE:SIGN<i>:PUSCh:TPC:PEXecute. \n
			:param set_type: MINPower | MAXPower | CONStant | SINGle | UDSingle | UDContinuous | ALT0 | CLOop | RPControl | FULPower MINPower: command the UE to minimum power MAXPower: command the UE to maximum power CONStant: command the UE to keep the power constant SINGle: send a pattern once (only one type of TPC command) UDSingle: send a pattern once (mixed TPC commands allowed) UDContinuous: send a pattern continuously ALT0: send an alternating pattern continuously CLOop: command the UE to a configurable target power RPControl: patterns for 3GPP relative power control test FULPower: flexible uplink power
		"""
		param = Conversions.enum_scalar_to_str(set_type, enums.SetType)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:SET {param}')

	# noinspection PyTypeChecker
	def get_rp_control(self) -> enums.RpControlPattern:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:RPControl \n
		Snippet: value: enums.RpControlPattern = driver.configure.uplink.setc.pusch.tpc.get_rp_control() \n
		Selects a TPC pattern for 3GPP relative power control tests with the TPC setup RPControl. \n
			:return: pattern: RUA | RDA | RUB | RDB | RUC | RDC RUA | RUB | RUC: ramping up A | B | C RDA | RDB | RDC: ramping down A | B | C
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:RPControl?')
		return Conversions.str_to_scalar_enum(response, enums.RpControlPattern)

	def set_rp_control(self, pattern: enums.RpControlPattern) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:RPControl \n
		Snippet: driver.configure.uplink.setc.pusch.tpc.set_rp_control(pattern = enums.RpControlPattern.RDA) \n
		Selects a TPC pattern for 3GPP relative power control tests with the TPC setup RPControl. \n
			:param pattern: RUA | RDA | RUB | RDB | RUC | RDC RUA | RUB | RUC: ramping up A | B | C RDA | RDB | RDC: ramping down A | B | C
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.RpControlPattern)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:RPControl {param}')

	# noinspection PyTypeChecker
	class SingleStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- No_Of_Steps: int: Range: 1 to 35
			- Step_Direction: enums.UpDownDirection: UP | DOWN"""
		__meta_args_list = [
			ArgStruct.scalar_int('No_Of_Steps'),
			ArgStruct.scalar_enum('Step_Direction', enums.UpDownDirection)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.No_Of_Steps: int = None
			self.Step_Direction: enums.UpDownDirection = None

	def get_single(self) -> SingleStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:SINGle \n
		Snippet: value: SingleStruct = driver.configure.uplink.setc.pusch.tpc.get_single() \n
		Defines a pattern for power control of the PUSCH with the TPC setup SINGle. The pattern consists of 1 to 35 up (+1 dB) or
		down (-1 dB) commands, followed by 'constant power' commands (0 dB) . \n
			:return: structure: for return value, see the help for SingleStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:SINGle?', self.__class__.SingleStruct())

	def set_single(self, value: SingleStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:SINGle \n
		Snippet: driver.configure.uplink.setc.pusch.tpc.set_single(value = SingleStruct()) \n
		Defines a pattern for power control of the PUSCH with the TPC setup SINGle. The pattern consists of 1 to 35 up (+1 dB) or
		down (-1 dB) commands, followed by 'constant power' commands (0 dB) . \n
			:param value: see the help for SingleStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:SINGle', value)

	def get_tpower(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:TPOWer \n
		Snippet: value: float = driver.configure.uplink.setc.pusch.tpc.get_tpower() \n
		Defines the target powers for power control with the TPC setup FULPower. \n
			:return: power: Range: -50 dBm to 33 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:TPOWer?')
		return Conversions.str_to_float(response)

	def set_tpower(self, power: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:TPOWer \n
		Snippet: driver.configure.uplink.setc.pusch.tpc.set_tpower(power = 1.0) \n
		Defines the target powers for power control with the TPC setup FULPower. \n
			:param power: Range: -50 dBm to 33 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:TPOWer {param}')

	# noinspection PyTypeChecker
	class UdPatternStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Pattern_Length: int: Number of values to be considered for the pattern Range: 1 to 20
			- Value_1: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_2: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_3: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_4: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_5: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_6: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_7: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_8: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_9: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_10: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_11: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_12: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_13: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_14: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_15: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_16: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_17: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_18: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_19: int: Range: -1 dB to 3 dB, Unit: dB
			- Value_20: int: Range: -1 dB to 3 dB, Unit: dB"""
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

	def get_ud_pattern(self) -> UdPatternStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:UDPattern \n
		Snippet: value: UdPatternStruct = driver.configure.uplink.setc.pusch.tpc.get_ud_pattern() \n
		Defines a pattern for power control of the PUSCH with the TPC setup UDSingle or UDContinuous. The pattern consists of 1
		to 20 TPC commands. To configure the pattern, specify the pattern length and a corresponding number of TPC commands.
		If you specify fewer TPC commands than required according to the pattern length, the previously defined values are used
		for the remaining commands. If you specify more TPC commands than required according to the pattern length, all values
		are set, but only the values corresponding to the pattern length are used. \n
			:return: structure: for return value, see the help for UdPatternStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:UDPattern?', self.__class__.UdPatternStruct())

	def set_ud_pattern(self, value: UdPatternStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:UDPattern \n
		Snippet: driver.configure.uplink.setc.pusch.tpc.set_ud_pattern(value = UdPatternStruct()) \n
		Defines a pattern for power control of the PUSCH with the TPC setup UDSingle or UDContinuous. The pattern consists of 1
		to 20 TPC commands. To configure the pattern, specify the pattern length and a corresponding number of TPC commands.
		If you specify fewer TPC commands than required according to the pattern length, the previously defined values are used
		for the remaining commands. If you specify more TPC commands than required according to the pattern length, all values
		are set, but only the values corresponding to the pattern length are used. \n
			:param value: see the help for UdPatternStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:UDPattern', value)

	def clone(self) -> 'Tpc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tpc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
