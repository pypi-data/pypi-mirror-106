from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("external", core, parent)

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.HandoverDestination:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:DESTination \n
		Snippet: value: enums.HandoverDestination = driver.prepare.handover.external.get_destination() \n
		Selects the target radio access technology for handover to another instrument. \n
			:return: destination: LTE | EVDO | CDMA | GSM | WCDMa | TDSCdma
		"""
		response = self._core.io.query_str('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.HandoverDestination)

	def set_destination(self, destination: enums.HandoverDestination) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:DESTination \n
		Snippet: driver.prepare.handover.external.set_destination(destination = enums.HandoverDestination.CDMA) \n
		Selects the target radio access technology for handover to another instrument. \n
			:param destination: LTE | EVDO | CDMA | GSM | WCDMa | TDSCdma
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.HandoverDestination)
		self._core.io.write(f'PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:DESTination {param}')

	# noinspection PyTypeChecker
	class LteStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperatingBandC: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB250 | OB252 | OB255 Operating band
			- Dl_Channel: int: Downlink channel number Range: depends on operating band"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandC),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandC = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_lte(self) -> LteStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:LTE \n
		Snippet: value: LteStruct = driver.prepare.handover.external.get_lte() \n
		Configures the destination parameters for handover to an LTE destination at another instrument. For channel number ranges
		depending on operating bands, see 'Operating Bands'. \n
			:return: structure: for return value, see the help for LteStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:LTE?', self.__class__.LteStruct())

	def set_lte(self, value: LteStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:LTE \n
		Snippet: driver.prepare.handover.external.set_lte(value = LteStruct()) \n
		Configures the destination parameters for handover to an LTE destination at another instrument. For channel number ranges
		depending on operating bands, see 'Operating Bands'. \n
			:param value: see the help for LteStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:LTE', value)

	# noinspection PyTypeChecker
	class GsmStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.GsmBand: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
			- Dl_Channel: int: Channel number used for the BCCH Range: depends on GSM band, see table below
			- Band_Indicator: enums.BandIndicator: G18 | G19 Band indicator for distinction of GSM 1800 and GSM 1900 bands. The two bands partially use the same channel numbers for different frequencies."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.GsmBand),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum('Band_Indicator', enums.BandIndicator)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.GsmBand = None
			self.Dl_Channel: int = None
			self.Band_Indicator: enums.BandIndicator = None

	# noinspection PyTypeChecker
	def get_gsm(self) -> GsmStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:GSM \n
		Snippet: value: GsmStruct = driver.prepare.handover.external.get_gsm() \n
		Configures the destination parameters for handover to a GSM destination at another instrument. \n
			:return: structure: for return value, see the help for GsmStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:GSM?', self.__class__.GsmStruct())

	def set_gsm(self, value: GsmStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:GSM \n
		Snippet: driver.prepare.handover.external.set_gsm(value = GsmStruct()) \n
		Configures the destination parameters for handover to a GSM destination at another instrument. \n
			:param value: see the help for GsmStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:GSM', value)

	# noinspection PyTypeChecker
	class CdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band_Class: enums.BandClass: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | NA9C | PS7C | LO7C USC: BC 0, US cellular KCEL: BC 0, Korean cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS band JTAC: BC 3, JTACS band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, upper 700 MHz B18M: BC 8, 1800-MHz band NA9C: BC 9, North American 900 MHz NA8S: BC 10, secondary 800 MHz PA4M: BC 11, European 400-MHz PAMR PA8M: BC 12, 800-MHz PAMR IEXT: BC 13, IMT-2000 2.5-GHz extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS band U25B: BC 16, US 2.5-GHz band U25F: BC 17, US 2.5 GHz forward PS7C: BC 18, public safety band 700 MHz LO7C: BC 19, lower 700 MHz
			- Dl_Channel: int: Channel number Range: depends on the band class, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Class', enums.BandClass),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Class: enums.BandClass = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_cdma(self) -> CdmaStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:CDMA \n
		Snippet: value: CdmaStruct = driver.prepare.handover.external.get_cdma() \n
		Configures the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:return: structure: for return value, see the help for CdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:CDMA?', self.__class__.CdmaStruct())

	def set_cdma(self, value: CdmaStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:CDMA \n
		Snippet: driver.prepare.handover.external.set_cdma(value = CdmaStruct()) \n
		Configures the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:param value: see the help for CdmaStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:CDMA', value)

	# noinspection PyTypeChecker
	class EvdoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band_Class: enums.BandClass: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | NA9C | PS7C | LO7C USC: BC 0, US cellular KCEL: BC 0, Korean cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS band JTAC: BC 3, JTACS band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, upper 700 MHz B18M: BC 8, 1800-MHz band NA9C: BC 9, North American 900 MHz NA8S: BC 10, secondary 800 MHz PA4M: BC 11, European 400-MHz PAMR PA8M: BC 12, 800-MHz PAMR IEXT: BC 13, IMT-2000 2.5-GHz extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS band U25B: BC 16, US 2.5-GHz band U25F: BC 17, US 2.5 GHz forward PS7C: BC 18, public safety band 700 MHz LO7C: BC 19, lower 700 MHz
			- Dl_Channel: int: Channel number Range: depends on the band class, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Class', enums.BandClass),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Class: enums.BandClass = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_evdo(self) -> EvdoStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:EVDO \n
		Snippet: value: EvdoStruct = driver.prepare.handover.external.get_evdo() \n
		Configures the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:return: structure: for return value, see the help for EvdoStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:EVDO?', self.__class__.EvdoStruct())

	def set_evdo(self, value: EvdoStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:EVDO \n
		Snippet: driver.prepare.handover.external.set_evdo(value = EvdoStruct()) \n
		Configures the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:param value: see the help for EvdoStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:EVDO', value)

	# noinspection PyTypeChecker
	class WcdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperatingBandB: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB19 | OB20 | OB21 | OB22 | OB25 | OBS1 | OBS2 | OBS3 | OBL1 | OB26 OB1, ..., OB14: band I to XIV OB19, ..., OB22: band XIX to XXII OB25, OB26: band XXV, XXVI OBS1: band S OBS2: band S 170 MHz OBS3: band S 190 MHz OBL1: band L
			- Dl_Channel: int: Downlink channel number Range: Depends on operating band, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandB),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandB = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_wcdma(self) -> WcdmaStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:WCDMa \n
		Snippet: value: WcdmaStruct = driver.prepare.handover.external.get_wcdma() \n
		Configures the destination parameters for handover to a WCDMA destination at another instrument. \n
			:return: structure: for return value, see the help for WcdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:WCDMa?', self.__class__.WcdmaStruct())

	def set_wcdma(self, value: WcdmaStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:WCDMa \n
		Snippet: driver.prepare.handover.external.set_wcdma(value = WcdmaStruct()) \n
		Configures the destination parameters for handover to a WCDMA destination at another instrument. \n
			:param value: see the help for WcdmaStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:WCDMa', value)

	# noinspection PyTypeChecker
	class TdscdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperatingBandA: OB1 | OB2 | OB3 OB1: Band 1 (F) , 1880 MHz to 1920 MHz OB2: Band 2 (A) , 2010 MHz to 2025 MHz OB3: Band 3 (E) , 2300 MHz to 2400 MHz
			- Dl_Channel: int: Downlink channel number The allowed range depends on the frequency band: OB1: 9400 to 9600 OB2: 10050 to 10125 OB3: 11500 to 12000"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandA),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandA = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_tdscdma(self) -> TdscdmaStruct:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:TDSCdma \n
		Snippet: value: TdscdmaStruct = driver.prepare.handover.external.get_tdscdma() \n
		Configures the destination parameters for handover to a TD-SCDMA destination at another instrument. \n
			:return: structure: for return value, see the help for TdscdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:TDSCdma?', self.__class__.TdscdmaStruct())

	def set_tdscdma(self, value: TdscdmaStruct) -> None:
		"""SCPI: PREPare:LTE:SIGNaling<instance>:HANDover:EXTernal:TDSCdma \n
		Snippet: driver.prepare.handover.external.set_tdscdma(value = TdscdmaStruct()) \n
		Configures the destination parameters for handover to a TD-SCDMA destination at another instrument. \n
			:param value: see the help for TdscdmaStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:LTE:SIGNaling<Instance>:HANDover:EXTernal:TDSCdma', value)
