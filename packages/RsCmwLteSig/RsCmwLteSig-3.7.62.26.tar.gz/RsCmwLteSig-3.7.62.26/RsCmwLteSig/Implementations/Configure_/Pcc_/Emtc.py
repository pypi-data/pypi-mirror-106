from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emtc:
	"""Emtc commands group definition. 33 total commands, 6 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("emtc", core, parent)

	@property
	def mpdcch(self):
		"""mpdcch commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_mpdcch'):
			from .Emtc_.Mpdcch import Mpdcch
			self._mpdcch = Mpdcch(self._core, self._base)
		return self._mpdcch

	@property
	def pdsch(self):
		"""pdsch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Emtc_.Pdsch import Pdsch
			self._pdsch = Pdsch(self._core, self._base)
		return self._pdsch

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Emtc_.Pucch import Pucch
			self._pucch = Pucch(self._core, self._base)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Emtc_.Pusch import Pusch
			self._pusch = Pusch(self._core, self._base)
		return self._pusch

	@property
	def ce(self):
		"""ce commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ce'):
			from .Emtc_.Ce import Ce
			self._ce = Ce(self._core, self._base)
		return self._ce

	@property
	def hopping(self):
		"""hopping commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hopping'):
			from .Emtc_.Hopping import Hopping
			self._hopping = Hopping(self._core, self._base)
		return self._hopping

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:ENABle \n
		Snippet: value: bool = driver.configure.pcc.emtc.get_enable() \n
		Enables or disables eMTC. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:ENABle \n
		Snippet: driver.configure.pcc.emtc.set_enable(enable = False) \n
		Enables or disables eMTC. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:ENABle {param}')

	def get_mb(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MB<number> \n
		Snippet: value: bool = driver.configure.pcc.emtc.get_mb() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MB5?')
		return Conversions.str_to_bool(response)

	def set_mb(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MB<number> \n
		Snippet: driver.configure.pcc.emtc.set_mb(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MB5 {param}')

	def clone(self) -> 'Emtc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emtc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
