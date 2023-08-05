from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCategory:
	"""UeCategory commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueCategory", core, parent)

	@property
	def reported(self):
		"""reported commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reported'):
			from .UeCategory_.Reported import Reported
			self._reported = Reported(self._core, self._base)
		return self._reported

	def get_manual(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:MANual \n
		Snippet: value: int = driver.configure.connection.ueCategory.get_manual() \n
		Configures the UE category to be used by the R&S CMW if no reported value is available or usage of the reported value is
		disabled, see method RsCmwLteSig.Configure.Connection.UeCategory.Reported.set. \n
			:return: ue_cat_manual: Range: 0 to 12
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:MANual?')
		return Conversions.str_to_int(response)

	def set_manual(self, ue_cat_manual: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:MANual \n
		Snippet: driver.configure.connection.ueCategory.set_manual(ue_cat_manual = 1) \n
		Configures the UE category to be used by the R&S CMW if no reported value is available or usage of the reported value is
		disabled, see method RsCmwLteSig.Configure.Connection.UeCategory.Reported.set. \n
			:param ue_cat_manual: Range: 0 to 12
		"""
		param = Conversions.decimal_value_to_str(ue_cat_manual)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:MANual {param}')

	def get_cz_allowed(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:CZALlowed \n
		Snippet: value: bool = driver.configure.connection.ueCategory.get_cz_allowed() \n
		Specifies whether category 0 UEs are allowed to access the cell. This information is sent to the UE via broadcast in
		system information block 1. \n
			:return: allowed: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:CZALlowed?')
		return Conversions.str_to_bool(response)

	def set_cz_allowed(self, allowed: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:CZALlowed \n
		Snippet: driver.configure.connection.ueCategory.set_cz_allowed(allowed = False) \n
		Specifies whether category 0 UEs are allowed to access the cell. This information is sent to the UE via broadcast in
		system information block 1. \n
			:param allowed: OFF | ON
		"""
		param = Conversions.bool_to_str(allowed)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:CZALlowed {param}')

	def clone(self) -> 'UeCategory':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCategory(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
