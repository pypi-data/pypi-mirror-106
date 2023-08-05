from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ce:
	"""Ce commands group definition. 9 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ce", core, parent)

	@property
	def level(self):
		"""level commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Ce_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.CoverageEnhMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:MODE \n
		Snippet: value: enums.CoverageEnhMode = driver.configure.pcc.emtc.ce.get_mode() \n
		Selects the coverage enhancement mode. \n
			:return: mode: A | B
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CoverageEnhMode)

	def set_mode(self, mode: enums.CoverageEnhMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:MODE \n
		Snippet: driver.configure.pcc.emtc.ce.set_mode(mode = enums.CoverageEnhMode.A) \n
		Selects the coverage enhancement mode. \n
			:param mode: A | B
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CoverageEnhMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:MODE {param}')

	# noinspection PyTypeChecker
	def get_ilevel(self) -> enums.IdleLevel:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:ILEVel \n
		Snippet: value: enums.IdleLevel = driver.configure.pcc.emtc.ce.get_ilevel() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:ILEVel?')
		return Conversions.str_to_scalar_enum(response, enums.IdleLevel)

	def set_ilevel(self, level: enums.IdleLevel) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:ILEVel \n
		Snippet: driver.configure.pcc.emtc.ce.set_ilevel(level = enums.IdleLevel.LEV0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.enum_scalar_to_str(level, enums.IdleLevel)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:ILEVel {param}')

	def clone(self) -> 'Ce':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ce(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
