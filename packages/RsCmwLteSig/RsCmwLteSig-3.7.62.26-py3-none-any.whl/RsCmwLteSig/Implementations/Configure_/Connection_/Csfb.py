from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csfb:
	"""Csfb commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("csfb", core, parent)

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.CsbfDestination:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:DESTination \n
		Snippet: value: enums.CsbfDestination = driver.configure.connection.csfb.get_destination() \n
		Selects the target radio access technology for MO CSFB. \n
			:return: destination: GSM | WCDMa | TDSCdma | NONE
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.CsbfDestination)

	def set_destination(self, destination: enums.CsbfDestination) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:DESTination \n
		Snippet: driver.configure.connection.csfb.set_destination(destination = enums.CsbfDestination.CDMA) \n
		Selects the target radio access technology for MO CSFB. \n
			:param destination: GSM | WCDMa | TDSCdma | NONE
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.CsbfDestination)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:DESTination {param}')

	# noinspection PyTypeChecker
	class GsmStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.GsmBand: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
			- Dl_Channel: int: Channel number used for the broadcast control channel (BCCH) Range: 0 to 1023, depending on GSM band, see table below
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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:GSM \n
		Snippet: value: GsmStruct = driver.configure.connection.csfb.get_gsm() \n
		Configures the GSM target for MO CSFB. \n
			:return: structure: for return value, see the help for GsmStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:GSM?', self.__class__.GsmStruct())

	def set_gsm(self, value: GsmStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:GSM \n
		Snippet: driver.configure.connection.csfb.set_gsm(value = GsmStruct()) \n
		Configures the GSM target for MO CSFB. \n
			:param value: see the help for GsmStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:GSM', value)

	# noinspection PyTypeChecker
	class WcdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperatingBandB: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB19 | OB20 | OB21 | OB22 | OB25 | OBS1 | OBS2 | OBS3 | OBL1 | OB26 OB1, ..., OB14: band I to XIV OB19, ..., OB22: band XIX to XXII OB25, OB26: band XXV, XXVI OBS1: band S OBS2: band S 170 MHz OBS3: band S 190 MHz OBL1: band L
			- Dl_Channel: int: Downlink channel number Range: 412 to 11000, depending on operating band, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperatingBandB),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperatingBandB = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_wcdma(self) -> WcdmaStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:WCDMa \n
		Snippet: value: WcdmaStruct = driver.configure.connection.csfb.get_wcdma() \n
		Configures the WCDMA target for MO CSFB. \n
			:return: structure: for return value, see the help for WcdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:WCDMa?', self.__class__.WcdmaStruct())

	def set_wcdma(self, value: WcdmaStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:WCDMa \n
		Snippet: driver.configure.connection.csfb.set_wcdma(value = WcdmaStruct()) \n
		Configures the WCDMA target for MO CSFB. \n
			:param value: see the help for WcdmaStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:WCDMa', value)

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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:TDSCdma \n
		Snippet: value: TdscdmaStruct = driver.configure.connection.csfb.get_tdscdma() \n
		Configures the TD-SCDMA target for MO CSFB. \n
			:return: structure: for return value, see the help for TdscdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:TDSCdma?', self.__class__.TdscdmaStruct())

	def set_tdscdma(self, value: TdscdmaStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CSFB:TDSCdma \n
		Snippet: driver.configure.connection.csfb.set_tdscdma(value = TdscdmaStruct()) \n
		Configures the TD-SCDMA target for MO CSFB. \n
			:param value: see the help for TdscdmaStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:CSFB:TDSCdma', value)
