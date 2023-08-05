from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Thresholds:
	"""Thresholds commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("thresholds", core, parent)

	# noinspection PyTypeChecker
	class LowStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Valid: bool: OFF | ON OFF: use individual thresholds defined by separate commands ON: use common threshold defined by this command
			- Low: int: Range: 0 to 31"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Valid'),
			ArgStruct.scalar_int('Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Valid: bool = None
			self.Low: int = None

	def get_low(self) -> LowStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:ALL:THResholds:LOW \n
		Snippet: value: LowStruct = driver.configure.ncell.all.thresholds.get_low() \n
		Configures a common reselection threshold value 'threshX-Low' applicable to all technologies. Alternatively to a common
		threshold you can also use individual thresholds. They are defined per technology via the commands
		CONFigure:LTE:SIGN<i>:NCELl:<Technology>:THResholds:LOW. The parameter <Valid> selects whether common or individual
		thresholds are used. \n
			:return: structure: for return value, see the help for LowStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:NCELl:ALL:THResholds:LOW?', self.__class__.LowStruct())

	def set_low(self, value: LowStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:ALL:THResholds:LOW \n
		Snippet: driver.configure.ncell.all.thresholds.set_low(value = LowStruct()) \n
		Configures a common reselection threshold value 'threshX-Low' applicable to all technologies. Alternatively to a common
		threshold you can also use individual thresholds. They are defined per technology via the commands
		CONFigure:LTE:SIGN<i>:NCELl:<Technology>:THResholds:LOW. The parameter <Valid> selects whether common or individual
		thresholds are used. \n
			:param value: see the help for LowStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:NCELl:ALL:THResholds:LOW', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Valid: bool: No parameter help available
			- High: int: No parameter help available
			- Low: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Valid'),
			ArgStruct.scalar_int('High'),
			ArgStruct.scalar_int('Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Valid: bool = None
			self.High: int = None
			self.Low: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:ALL:THResholds \n
		Snippet: value: ValueStruct = driver.configure.ncell.all.thresholds.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:NCELl:ALL:THResholds?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:ALL:THResholds \n
		Snippet: driver.configure.ncell.all.thresholds.set_value(value = ValueStruct()) \n
		No command help available \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:NCELl:ALL:THResholds', value)
