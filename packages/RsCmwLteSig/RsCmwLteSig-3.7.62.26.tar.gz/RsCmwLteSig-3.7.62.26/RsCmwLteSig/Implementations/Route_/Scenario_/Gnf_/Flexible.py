from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flexible:
	"""Flexible commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("flexible", core, parent)

	# noinspection PyTypeChecker
	class InternalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Pcc_Bb_Board: enums.BasebandBoard: No parameter help available
			- Rx_Connector: enums.RxConnector: No parameter help available
			- Rx_Converter: enums.RxConverter: No parameter help available
			- Pcc_Tx_1_Connector: enums.TxConnector: No parameter help available
			- Pcc_Tx_1_Converter: enums.TxConverter: No parameter help available
			- Pcc_Tx_2_Connector: enums.TxConnector: No parameter help available
			- Pcc_Tx_2_Converter: enums.TxConverter: No parameter help available
			- Scc_1_Bb_Board: enums.BasebandBoard: No parameter help available
			- Scc_1_Tx_1_Connector: enums.TxConnector: No parameter help available
			- Scc_1_Tx_1_Converter: enums.TxConverter: No parameter help available
			- Scc_1_Tx_2_Connector: enums.TxConnector: No parameter help available
			- Scc_1_Tx_2_Converter: enums.TxConverter: No parameter help available
			- Scc_2_Bb_Board: enums.BasebandBoard: No parameter help available
			- Scc_2_Tx_1_Connector: enums.TxConnector: No parameter help available
			- Scc_2_Tx_1_Converter: enums.TxConverter: No parameter help available
			- Scc_2_Tx_2_Connector: enums.TxConnector: No parameter help available
			- Scc_2_Tx_2_Converter: enums.TxConverter: No parameter help available
			- Scc_3_Bb_Board: enums.BasebandBoard: No parameter help available
			- Scc_3_Tx_1_Connector: enums.TxConnector: No parameter help available
			- Scc_3_Tx_1_Converter: enums.TxConverter: No parameter help available
			- Scc_3_Tx_2_Connector: enums.TxConnector: No parameter help available
			- Scc_3_Tx_2_Converter: enums.TxConverter: No parameter help available
			- Scc_4_Bb_Board: enums.BasebandBoard: No parameter help available
			- Scc_4_Tx_1_Connector: enums.TxConnector: No parameter help available
			- Scc_4_Tx_1_Converter: enums.TxConverter: No parameter help available
			- Scc_4_Tx_2_Connector: enums.TxConnector: No parameter help available
			- Scc_4_Tx_2_Converter: enums.TxConverter: No parameter help available
			- Scc_5_Bb_Board: enums.BasebandBoard: No parameter help available
			- Scc_5_Tx_1_Connector: enums.TxConnector: No parameter help available
			- Scc_5_Tx_1_Converter: enums.TxConverter: No parameter help available
			- Scc_5_Tx_2_Connector: enums.TxConnector: No parameter help available
			- Scc_5_Tx_2_Converter: enums.TxConverter: No parameter help available
			- Scc_6_Bb_Board: enums.BasebandBoard: No parameter help available
			- Scc_6_Tx_1_Connector: enums.TxConnector: No parameter help available
			- Scc_6_Tx_1_Converter: enums.TxConverter: No parameter help available
			- Scc_6_Tx_2_Connector: enums.TxConnector: No parameter help available
			- Scc_6_Tx_2_Converter: enums.TxConverter: No parameter help available
			- Pcc_Fading_Board: enums.FadingBoard: No parameter help available
			- Scc_1_Fading_Board: enums.FadingBoard: No parameter help available
			- Scc_2_Fading_Board: enums.FadingBoard: No parameter help available
			- Scc_3_Fading_Board: enums.FadingBoard: No parameter help available
			- Scc_4_Fading_Board: enums.FadingBoard: No parameter help available
			- Scc_5_Fading_Board: enums.FadingBoard: No parameter help available
			- Scc_6_Fading_Board: enums.FadingBoard: No parameter help available
			- Coprocessor: enums.BasebandBoard: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pcc_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Pcc_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Pcc_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_1_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_1_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_1_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_1_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_1_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_2_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_2_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_2_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_2_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_2_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_3_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_3_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_3_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_3_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_3_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_4_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_4_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_4_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_4_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_4_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_5_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_5_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_5_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_5_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_5_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_6_Bb_Board', enums.BasebandBoard),
			ArgStruct.scalar_enum('Scc_6_Tx_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_6_Tx_1_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Scc_6_Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Scc_6_Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Pcc_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum('Scc_1_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum('Scc_2_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum('Scc_3_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum('Scc_4_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum('Scc_5_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum('Scc_6_Fading_Board', enums.FadingBoard),
			ArgStruct.scalar_enum('Coprocessor', enums.BasebandBoard)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcc_Bb_Board: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Pcc_Tx_1_Connector: enums.TxConnector = None
			self.Pcc_Tx_1_Converter: enums.TxConverter = None
			self.Pcc_Tx_2_Connector: enums.TxConnector = None
			self.Pcc_Tx_2_Converter: enums.TxConverter = None
			self.Scc_1_Bb_Board: enums.BasebandBoard = None
			self.Scc_1_Tx_1_Connector: enums.TxConnector = None
			self.Scc_1_Tx_1_Converter: enums.TxConverter = None
			self.Scc_1_Tx_2_Connector: enums.TxConnector = None
			self.Scc_1_Tx_2_Converter: enums.TxConverter = None
			self.Scc_2_Bb_Board: enums.BasebandBoard = None
			self.Scc_2_Tx_1_Connector: enums.TxConnector = None
			self.Scc_2_Tx_1_Converter: enums.TxConverter = None
			self.Scc_2_Tx_2_Connector: enums.TxConnector = None
			self.Scc_2_Tx_2_Converter: enums.TxConverter = None
			self.Scc_3_Bb_Board: enums.BasebandBoard = None
			self.Scc_3_Tx_1_Connector: enums.TxConnector = None
			self.Scc_3_Tx_1_Converter: enums.TxConverter = None
			self.Scc_3_Tx_2_Connector: enums.TxConnector = None
			self.Scc_3_Tx_2_Converter: enums.TxConverter = None
			self.Scc_4_Bb_Board: enums.BasebandBoard = None
			self.Scc_4_Tx_1_Connector: enums.TxConnector = None
			self.Scc_4_Tx_1_Converter: enums.TxConverter = None
			self.Scc_4_Tx_2_Connector: enums.TxConnector = None
			self.Scc_4_Tx_2_Converter: enums.TxConverter = None
			self.Scc_5_Bb_Board: enums.BasebandBoard = None
			self.Scc_5_Tx_1_Connector: enums.TxConnector = None
			self.Scc_5_Tx_1_Converter: enums.TxConverter = None
			self.Scc_5_Tx_2_Connector: enums.TxConnector = None
			self.Scc_5_Tx_2_Converter: enums.TxConverter = None
			self.Scc_6_Bb_Board: enums.BasebandBoard = None
			self.Scc_6_Tx_1_Connector: enums.TxConnector = None
			self.Scc_6_Tx_1_Converter: enums.TxConverter = None
			self.Scc_6_Tx_2_Connector: enums.TxConnector = None
			self.Scc_6_Tx_2_Converter: enums.TxConverter = None
			self.Pcc_Fading_Board: enums.FadingBoard = None
			self.Scc_1_Fading_Board: enums.FadingBoard = None
			self.Scc_2_Fading_Board: enums.FadingBoard = None
			self.Scc_3_Fading_Board: enums.FadingBoard = None
			self.Scc_4_Fading_Board: enums.FadingBoard = None
			self.Scc_5_Fading_Board: enums.FadingBoard = None
			self.Scc_6_Fading_Board: enums.FadingBoard = None
			self.Coprocessor: enums.BasebandBoard = None

	# noinspection PyTypeChecker
	def get_internal(self) -> InternalStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:GNF[:FLEXible]:INTernal \n
		Snippet: value: InternalStruct = driver.route.scenario.gnf.flexible.get_internal() \n
		No command help available \n
			:return: structure: for return value, see the help for InternalStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:GNF:FLEXible:INTernal?', self.__class__.InternalStruct())

	def set_internal(self, value: InternalStruct) -> None:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario:GNF[:FLEXible]:INTernal \n
		Snippet: driver.route.scenario.gnf.flexible.set_internal(value = InternalStruct()) \n
		No command help available \n
			:param value: see the help for InternalStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario:GNF:FLEXible:INTernal', value)
