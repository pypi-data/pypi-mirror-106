from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emtc:
	"""Emtc commands group definition. 8 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("emtc", core, parent)

	@property
	def nbPosition(self):
		"""nbPosition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_nbPosition'):
			from .Emtc_.NbPosition import NbPosition
			self._nbPosition = NbPosition(self._core, self._base)
		return self._nbPosition

	@property
	def b(self):
		"""b commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_b'):
			from .Emtc_.B import B
			self._b = B(self._core, self._base)
		return self._b

	@property
	def a(self):
		"""a commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_a'):
			from .Emtc_.A import A
			self._a = A(self._core, self._base)
		return self._a

	# noinspection PyTypeChecker
	def get_sf_pattern(self) -> enums.SubFramePattern:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:SFPattern \n
		Snippet: value: enums.SubFramePattern = driver.configure.connection.pcc.udChannels.emtc.get_sf_pattern() \n
		No command help available \n
			:return: pattern: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:SFPattern?')
		return Conversions.str_to_scalar_enum(response, enums.SubFramePattern)

	def set_sf_pattern(self, pattern: enums.SubFramePattern) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:SFPattern \n
		Snippet: driver.configure.connection.pcc.udChannels.emtc.set_sf_pattern(pattern = enums.SubFramePattern.HAB10) \n
		No command help available \n
			:param pattern: No help available
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.SubFramePattern)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:SFPattern {param}')

	def clone(self) -> 'Emtc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emtc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
