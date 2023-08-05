from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdSequence:
	"""UdSequence commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("udSequence", core, parent)

	def get_length(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:UDSequence:LENGth \n
		Snippet: value: int = driver.configure.connection.harq.downlink.udSequence.get_length() \n
		Specifies the length of the user-defined redundancy version sequence. \n
			:return: length: Range: 1 to 4
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:UDSequence:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, length: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:UDSequence:LENGth \n
		Snippet: driver.configure.connection.harq.downlink.udSequence.set_length(length = 1) \n
		Specifies the length of the user-defined redundancy version sequence. \n
			:param length: Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:UDSequence:LENGth {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Value_1: int: In this software version fixed set to 0 Range: 0
			- Value_2: int: Range: 0 to 3
			- Value_3: int: Range: 0 to 3
			- Value_4: int: Range: 0 to 3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Value_1'),
			ArgStruct.scalar_int('Value_2'),
			ArgStruct.scalar_int('Value_3'),
			ArgStruct.scalar_int('Value_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Value_1: int = None
			self.Value_2: int = None
			self.Value_3: int = None
			self.Value_4: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:UDSequence \n
		Snippet: value: ValueStruct = driver.configure.connection.harq.downlink.udSequence.get_value() \n
		Specifies the user-defined redundancy version sequence. Only the first n values are used, according to the specified
		length, see method RsCmwLteSig.Configure.Connection.Harq.Downlink.UdSequence.length. You can either set the first value
		only (relevant for initial transmissions) or all four values. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:UDSequence?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:UDSequence \n
		Snippet: driver.configure.connection.harq.downlink.udSequence.set_value(value = ValueStruct()) \n
		Specifies the user-defined redundancy version sequence. Only the first n values are used, according to the specified
		length, see method RsCmwLteSig.Configure.Connection.Harq.Downlink.UdSequence.length. You can either set the first value
		only (relevant for initial transmissions) or all four values. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:UDSequence', value)
