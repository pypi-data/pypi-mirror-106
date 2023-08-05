from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import enums
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 6 total commands, 5 Sub-groups, 1 group commands
	Repeated Capability: SecondaryCompCarrier, default value after init: SecondaryCompCarrier.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_secondaryCompCarrier_get', 'repcap_secondaryCompCarrier_set', repcap.SecondaryCompCarrier.CC1)

	def repcap_secondaryCompCarrier_set(self, enum_value: repcap.SecondaryCompCarrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCompCarrier.Default
		Default value after init: SecondaryCompCarrier.CC1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_secondaryCompCarrier_get(self) -> repcap.SecondaryCompCarrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def uul(self):
		"""uul commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uul'):
			from .Scc_.Uul import Uul
			self._uul = Uul(self._core, self._base)
		return self._uul

	@property
	def dmode(self):
		"""dmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmode'):
			from .Scc_.Dmode import Dmode
			self._dmode = Dmode(self._core, self._base)
		return self._dmode

	@property
	def band(self):
		"""band commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_band'):
			from .Scc_.Band import Band
			self._band = Band(self._core, self._base)
		return self._band

	@property
	def fstructure(self):
		"""fstructure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fstructure'):
			from .Scc_.Fstructure import Fstructure
			self._fstructure = Fstructure(self._core, self._base)
		return self._fstructure

	@property
	def caggregation(self):
		"""caggregation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caggregation'):
			from .Scc_.Caggregation import Caggregation
			self._caggregation = Caggregation(self._core, self._base)
		return self._caggregation

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.AutoManualModeExt:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC:AMODe \n
		Snippet: value: enums.AutoManualModeExt = driver.configure.scc.get_amode() \n
		Selects the SCC activation mode. For manual triggering of a state transition, see method RsCmwLteSig.Call.Scc.Action.set. \n
			:return: mode: AUTO | MANual | SEMiauto AUTO All SCCs are activated automatically at RRC connection establishment, so that the state 'MAC Activated' is reached. MANual Each state transition step must be initiated separately for each SCC. So several actions are required to reach the state 'MAC Activated'. SEMiauto The activation must be initiated manually for each SCC. As a result, all state transitions required to reach the state 'MAC Activated' are performed.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SCC:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualModeExt)

	def set_amode(self, mode: enums.AutoManualModeExt) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC:AMODe \n
		Snippet: driver.configure.scc.set_amode(mode = enums.AutoManualModeExt.AUTO) \n
		Selects the SCC activation mode. For manual triggering of a state transition, see method RsCmwLteSig.Call.Scc.Action.set. \n
			:param mode: AUTO | MANual | SEMiauto AUTO All SCCs are activated automatically at RRC connection establishment, so that the state 'MAC Activated' is reached. MANual Each state transition step must be initiated separately for each SCC. So several actions are required to reach the state 'MAC Activated'. SEMiauto The activation must be initiated manually for each SCC. As a result, all state transitions required to reach the state 'MAC Activated' are performed.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualModeExt)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SCC:AMODe {param}')

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
