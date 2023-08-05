from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handover:
	"""Handover commands group definition. 13 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handover", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Handover_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def external(self):
		"""external commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_external'):
			from .Handover_.External import External
			self._external = External(self._core, self._base)
		return self._external

	# noinspection PyTypeChecker
	class EnhancedStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Duplex_Mode: enums.DuplexMode: FDD | TDD Duplex mode of the handover destination
			- Band: enums.OperatingBandC: FDD: UDEFined | OB1 | ... | OB28 | OB30 | OB31 | OB65 | OB66 | OB68 | OB70 | ... | OB74 | OB85 TDD: UDEFined | OB33 | ... | OB45 | OB48 | OB50 | ... | OB53 | OB250 Operating band of the handover destination
			- Dl_Channel: int: DL channel number valid for the selected operating band. The related UL channel number is calculated and set automatically. For channel numbers depending on operating bands, see 'Operating Bands'. Range: depends on operating band
			- Dl_Bandwidth: enums.Bandwidth: B014 | B030 | B050 | B100 | B150 | B200 DL cell bandwidth (also used for UL) 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, 20 MHz
			- Add_Spec_Emission: enums.AddSpectrumEmission: NS01 | ... | NS288 Value signaled to the UE as additional ACLR and spectrum emission requirement"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexMode),
			ArgStruct.scalar_enum('Band', enums.OperatingBandC),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum('Dl_Bandwidth', enums.Bandwidth),
			ArgStruct.scalar_enum('Add_Spec_Emission', enums.AddSpectrumEmission)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Duplex_Mode: enums.DuplexMode = None
			self.Band: enums.OperatingBandC = None
			self.Dl_Channel: int = None
			self.Dl_Bandwidth: enums.Bandwidth = None
			self.Add_Spec_Emission: enums.AddSpectrumEmission = None

	# noinspection PyTypeChecker
	def get_enhanced(self) -> EnhancedStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:ENHanced \n
		Snippet: value: EnhancedStruct = driver.prepare.handover.get_enhanced() \n
		Configures the destination parameters for an intra-RAT handover within the LTE signaling application. The duplex mode of
		the destination is configurable. \n
			:return: structure: for return value, see the help for EnhancedStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:ENHanced?', self.__class__.EnhancedStruct())

	def set_enhanced(self, value: EnhancedStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:ENHanced \n
		Snippet: driver.prepare.handover.set_enhanced(value = EnhancedStruct()) \n
		Configures the destination parameters for an intra-RAT handover within the LTE signaling application. The duplex mode of
		the destination is configurable. \n
			:param value: see the help for EnhancedStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:ENHanced', value)

	def get_destination(self) -> str:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:DESTination \n
		Snippet: value: str = driver.prepare.handover.get_destination() \n
		Selects the handover destination. A complete list of all supported values can be displayed using method RsCmwLteSig.
		Prepare.Handover.Catalog.destination. \n
			:return: destination: Destination as string
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:DESTination?')
		return trim_str_response(response)

	def set_destination(self, destination: str) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:DESTination \n
		Snippet: driver.prepare.handover.set_destination(destination = '1') \n
		Selects the handover destination. A complete list of all supported values can be displayed using method RsCmwLteSig.
		Prepare.Handover.Catalog.destination. \n
			:param destination: Destination as string
		"""
		param = Conversions.value_to_quoted_str(destination)
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:DESTination {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.HandoverMode:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:MMODe \n
		Snippet: value: enums.HandoverMode = driver.prepare.handover.get_mmode() \n
		Selects the mechanism to be used for handover to another signaling application. \n
			:return: mode: REDirection | MTCSfallback | HANDover
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.HandoverMode)

	def set_mmode(self, mode: enums.HandoverMode) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:MMODe \n
		Snippet: driver.prepare.handover.set_mmode(mode = enums.HandoverMode.HANDover) \n
		Selects the mechanism to be used for handover to another signaling application. \n
			:param mode: REDirection | MTCSfallback | HANDover
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HandoverMode)
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:MMODe {param}')

	# noinspection PyTypeChecker
	def get_ctype(self) -> enums.VolteHandoverType:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:CTYPe \n
		Snippet: value: enums.VolteHandoverType = driver.prepare.handover.get_ctype() \n
		Selects the call type to be set up at the destination, for handover of VoLTE calls. \n
			:return: type_py: PSData | PSVolte PSData: E2E packet data connection PSVolte: Voice call, use handover with SRVCC
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.VolteHandoverType)

	def set_ctype(self, type_py: enums.VolteHandoverType) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:CTYPe \n
		Snippet: driver.prepare.handover.set_ctype(type_py = enums.VolteHandoverType.PSData) \n
		Selects the call type to be set up at the destination, for handover of VoLTE calls. \n
			:param type_py: PSData | PSVolte PSData: E2E packet data connection PSVolte: Voice call, use handover with SRVCC
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.VolteHandoverType)
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:CTYPe {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperatingBandC: FDD: UDEFined | OB1 | ... | OB28 | OB30 | OB31 | OB65 | OB66 | OB68 | OB70 | ... | OB74 | OB85 TDD: UDEFined | OB33 | ... | OB45 | OB48 | OB50 | ... | OB53 | OB250 Operating band of the handover destination
			- Dl_Channel: int: DL channel number valid for the selected operating band. The related UL channel number is calculated and set automatically. For channel numbers depending on operating bands, see 'Operating Bands'. Range: depends on operating band
			- Dl_Bandwidth: enums.Bandwidth: B014 | B030 | B050 | B100 | B150 | B200 DL cell bandwidth (also used for UL) 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, 20 MHz
			- Add_Spec_Emission: enums.AddSpectrumEmission: NS01 | ... | NS288 Value signaled to the UE as additional ACLR and spectrum emission requirement"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandC),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum('Dl_Bandwidth', enums.Bandwidth),
			ArgStruct.scalar_enum('Add_Spec_Emission', enums.AddSpectrumEmission)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandC = None
			self.Dl_Channel: int = None
			self.Dl_Bandwidth: enums.Bandwidth = None
			self.Add_Spec_Emission: enums.AddSpectrumEmission = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover \n
		Snippet: value: ValueStruct = driver.prepare.handover.get_value() \n
		Configures the destination parameters for an intra-RAT handover within the LTE signaling application. The duplex mode of
		the destination is the same as the duplex mode of the source. For a handover with duplex mode change, see method
		RsCmwLteSig.Prepare.Handover.enhanced. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:HANDover?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover \n
		Snippet: driver.prepare.handover.set_value(value = ValueStruct()) \n
		Configures the destination parameters for an intra-RAT handover within the LTE signaling application. The duplex mode of
		the destination is the same as the duplex mode of the source. For a handover with duplex mode change, see method
		RsCmwLteSig.Prepare.Handover.enhanced. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:HANDover', value)

	def clone(self) -> 'Handover':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Handover(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
