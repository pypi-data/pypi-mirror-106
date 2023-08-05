from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eutra:
	"""Eutra commands group definition. 6 total commands, 3 Sub-groups, 1 group commands
	Repeated Capability: EutraBand, default value after init: EutraBand.Band1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eutra", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_eutraBand_get', 'repcap_eutraBand_set', repcap.EutraBand.Band1)

	def repcap_eutraBand_set(self, enum_value: repcap.EutraBand) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to EutraBand.Default
		Default value after init: EutraBand.Band1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_eutraBand_get(self) -> repcap.EutraBand:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def bclass(self):
		"""bclass commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bclass'):
			from .Eutra_.Bclass import Bclass
			self._bclass = Bclass(self._core, self._base)
		return self._bclass

	@property
	def mcapability(self):
		"""mcapability commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcapability'):
			from .Eutra_.Mcapability import Mcapability
			self._mcapability = Mcapability(self._core, self._base)
		return self._mcapability

	@property
	def scproc(self):
		"""scproc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scproc'):
			from .Eutra_.Scproc import Scproc
			self._scproc = Scproc(self._core, self._base)
		return self._scproc

	# noinspection PyTypeChecker
	def get(self, ueReport=repcap.UeReport.V1020, eutraBand=repcap.EutraBand.Default) -> List[enums.OperatingBandC]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:BCOMbination:V<Number>:EUTRa<BandNr> \n
		Snippet: value: List[enums.OperatingBandC] = driver.sense.ueCapability.rf.bcombination.v.eutra.get(ueReport = repcap.UeReport.V1020, eutraBand = repcap.EutraBand.Default) \n
		Returns the operating band combinations supported for carrier aggregation. \n
			:param ueReport: optional repeated capability selector. Default value: V1020
			:param eutraBand: optional repeated capability selector. Default value: Band1 (settable in the interface 'Eutra')
			:return: band: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB250 | OB252 | OB255 Comma-separated list of bands, one band per band combination (combination 0 to n)"""
		ueReport_cmd_val = self._base.get_repcap_cmd_value(ueReport, repcap.UeReport)
		eutraBand_cmd_val = self._base.get_repcap_cmd_value(eutraBand, repcap.EutraBand)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:RF:BCOMbination:V{ueReport_cmd_val}:EUTRa{eutraBand_cmd_val}?')
		return Conversions.str_to_list_enum(response, enums.OperatingBandC)

	def clone(self) -> 'Eutra':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eutra(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
