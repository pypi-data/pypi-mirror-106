from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Beamforming:
	"""Beamforming commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("beamforming", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BeamformingMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:BEAMforming:MODE \n
		Snippet: value: enums.BeamformingMode = driver.configure.connection.pcc.beamforming.get_mode() \n
		Selects the beamforming mode for TM 7 and 8.
			INTRO_CMD_HELP: Depending on other settings, only a subset of the values is allowed, see: \n
			- TM 7: 'Beamforming Mode'
			- TM 8: 'Beamforming Mode' \n
			:return: mode: OFF | ON | TSBF | PMAT OFF: Beamforming is disabled ON: Beamforming is enabled. The configured beamforming matrix is used. TSBF: Beamforming is enabled. The beamforming matrix is selected randomly as defined in 3GPP TS 36.521, annex B.4.1 and B.4.2. PMAT: Beamforming is enabled. A precoding matrix is used as beamforming matrix, see CONFigure:LTE:SIGNi:PMATrix.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:BEAMforming:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BeamformingMode)

	def set_mode(self, mode: enums.BeamformingMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:BEAMforming:MODE \n
		Snippet: driver.configure.connection.pcc.beamforming.set_mode(mode = enums.BeamformingMode.OFF) \n
		Selects the beamforming mode for TM 7 and 8.
			INTRO_CMD_HELP: Depending on other settings, only a subset of the values is allowed, see: \n
			- TM 7: 'Beamforming Mode'
			- TM 8: 'Beamforming Mode' \n
			:param mode: OFF | ON | TSBF | PMAT OFF: Beamforming is disabled ON: Beamforming is enabled. The configured beamforming matrix is used. TSBF: Beamforming is enabled. The beamforming matrix is selected randomly as defined in 3GPP TS 36.521, annex B.4.1 and B.4.2. PMAT: Beamforming is enabled. A precoding matrix is used as beamforming matrix, see CONFigure:LTE:SIGNi:PMATrix.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.BeamformingMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:BEAMforming:MODE {param}')

	# noinspection PyTypeChecker
	def get_no_layers(self) -> enums.BeamformingNoOfLayers:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:BEAMforming:NOLayers \n
		Snippet: value: enums.BeamformingNoOfLayers = driver.configure.connection.pcc.beamforming.get_no_layers() \n
		Selects the number of layers for transmission mode 8. \n
			:return: number: L1 | L2 L1: single-layer beamforming L2: dual-layer beamforming
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:BEAMforming:NOLayers?')
		return Conversions.str_to_scalar_enum(response, enums.BeamformingNoOfLayers)

	def set_no_layers(self, number: enums.BeamformingNoOfLayers) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:BEAMforming:NOLayers \n
		Snippet: driver.configure.connection.pcc.beamforming.set_no_layers(number = enums.BeamformingNoOfLayers.L1) \n
		Selects the number of layers for transmission mode 8. \n
			:param number: L1 | L2 L1: single-layer beamforming L2: dual-layer beamforming
		"""
		param = Conversions.enum_scalar_to_str(number, enums.BeamformingNoOfLayers)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:BEAMforming:NOLayers {param}')

	# noinspection PyTypeChecker
	class MatrixStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- B_11_Phi: int: Range: 0 deg to 345 deg, Unit: deg
			- B_12_Phi: int: Range: 0 deg to 345 deg, Unit: deg
			- B_11_Abs: float: Range: 0 to 1
			- B_12_Abs: float: Range: 0 to 1
			- B_21_Phi: int: Range: 0 deg to 345 deg, Unit: deg
			- B_22_Phi: int: Range: 0 deg to 345 deg, Unit: deg
			- B_13_Phi: int: Range: 0 deg to 345 deg, Unit: deg
			- B_14_Phi: int: Range: 0 deg to 345 deg, Unit: deg
			- B_13_Abs: float: Range: 0 to 1
			- B_14_Abs: float: Range: 0 to 1
			- B_23_Phi: int: Range: 0 deg to 345 deg, Unit: deg
			- B_24_Phi: int: Range: 0 deg to 345 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('B_11_Phi'),
			ArgStruct.scalar_int('B_12_Phi'),
			ArgStruct.scalar_float('B_11_Abs'),
			ArgStruct.scalar_float('B_12_Abs'),
			ArgStruct.scalar_int('B_21_Phi'),
			ArgStruct.scalar_int('B_22_Phi'),
			ArgStruct.scalar_int('B_13_Phi'),
			ArgStruct.scalar_int('B_14_Phi'),
			ArgStruct.scalar_float('B_13_Abs'),
			ArgStruct.scalar_float('B_14_Abs'),
			ArgStruct.scalar_int('B_23_Phi'),
			ArgStruct.scalar_int('B_24_Phi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.B_11_Phi: int = None
			self.B_12_Phi: int = None
			self.B_11_Abs: float = None
			self.B_12_Abs: float = None
			self.B_21_Phi: int = None
			self.B_22_Phi: int = None
			self.B_13_Phi: int = None
			self.B_14_Phi: int = None
			self.B_13_Abs: float = None
			self.B_14_Abs: float = None
			self.B_23_Phi: int = None
			self.B_24_Phi: int = None

	def get_matrix(self) -> MatrixStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:BEAMforming:MATRix \n
		Snippet: value: MatrixStruct = driver.configure.connection.pcc.beamforming.get_matrix() \n
		Configures the beamforming matrix coefficients for TM 7 and TM 8.
			INTRO_CMD_HELP: There are two types of parameters: \n
			- <bnmabs> defines the square of the magnitude of the coefficient nm: <bnmabs> = (bnm) 2
			- <bnmphi> defines the phase of the coefficient nm: <bnmphi> = φ(bnm) The phase can be entered in steps of 15 degrees. The setting is rounded, if necessary.
			INTRO_CMD_HELP: Depending on the size of your matrix, use the following parameters: \n
			- 1x1: <b11phi>
			- 1x2: <b11phi>, <b12phi>
			- 2x2: <b11phi>, <b12phi>, <b11abs>, <b12abs>, <b21phi>, <b22phi>
		The last six parameters are for future use and can always be omitted. \n
			:return: structure: for return value, see the help for MatrixStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:BEAMforming:MATRix?', self.__class__.MatrixStruct())

	def set_matrix(self, value: MatrixStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:BEAMforming:MATRix \n
		Snippet: driver.configure.connection.pcc.beamforming.set_matrix(value = MatrixStruct()) \n
		Configures the beamforming matrix coefficients for TM 7 and TM 8.
			INTRO_CMD_HELP: There are two types of parameters: \n
			- <bnmabs> defines the square of the magnitude of the coefficient nm: <bnmabs> = (bnm) 2
			- <bnmphi> defines the phase of the coefficient nm: <bnmphi> = φ(bnm) The phase can be entered in steps of 15 degrees. The setting is rounded, if necessary.
			INTRO_CMD_HELP: Depending on the size of your matrix, use the following parameters: \n
			- 1x1: <b11phi>
			- 1x2: <b11phi>, <b12phi>
			- 2x2: <b11phi>, <b12phi>, <b11abs>, <b12abs>, <b21phi>, <b22phi>
		The last six parameters are for future use and can always be omitted. \n
			:param value: see the help for MatrixStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:BEAMforming:MATRix', value)
