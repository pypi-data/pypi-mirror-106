from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Thresholds:
	"""Thresholds commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("thresholds", core, parent)

	def get_low(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:CDMA:THResholds:LOW \n
		Snippet: value: int = driver.configure.ncell.cdma.thresholds.get_low() \n
		Configures the reselection threshold value 'threshX-Low' for CDMA2000 neighbor cells. \n
			:return: low: Range: 0 to 63
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:NCELl:CDMA:THResholds:LOW?')
		return Conversions.str_to_int(response)

	def set_low(self, low: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:CDMA:THResholds:LOW \n
		Snippet: driver.configure.ncell.cdma.thresholds.set_low(low = 1) \n
		Configures the reselection threshold value 'threshX-Low' for CDMA2000 neighbor cells. \n
			:param low: Range: 0 to 63
		"""
		param = Conversions.decimal_value_to_str(low)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:CDMA:THResholds:LOW {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- High: int: No parameter help available
			- Low: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('High'),
			ArgStruct.scalar_int('Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.High: int = None
			self.Low: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:CDMA:THResholds \n
		Snippet: value: ValueStruct = driver.configure.ncell.cdma.thresholds.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:NCELl:CDMA:THResholds?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:CDMA:THResholds \n
		Snippet: driver.configure.ncell.cdma.thresholds.set_value(value = ValueStruct()) \n
		No command help available \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:NCELl:CDMA:THResholds', value)
