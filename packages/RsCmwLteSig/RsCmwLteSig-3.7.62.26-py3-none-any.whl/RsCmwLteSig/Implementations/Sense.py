from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 319 total commands, 13 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sense", core, parent)

	@property
	def iqOut(self):
		"""iqOut commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOut'):
			from .Sense_.IqOut import IqOut
			self._iqOut = IqOut(self._core, self._base)
		return self._iqOut

	@property
	def fading(self):
		"""fading commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Sense_.Fading import Fading
			self._fading = Fading(self._core, self._base)
		return self._fading

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Sense_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Sense_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	@property
	def connection(self):
		"""connection commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Sense_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	@property
	def cqiReporting(self):
		"""cqiReporting commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqiReporting'):
			from .Sense_.CqiReporting import CqiReporting
			self._cqiReporting = CqiReporting(self._core, self._base)
		return self._cqiReporting

	@property
	def ueReport(self):
		"""ueReport commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueReport'):
			from .Sense_.UeReport import UeReport
			self._ueReport = UeReport(self._core, self._base)
		return self._ueReport

	@property
	def uesInfo(self):
		"""uesInfo commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_uesInfo'):
			from .Sense_.UesInfo import UesInfo
			self._uesInfo = UesInfo(self._core, self._base)
		return self._uesInfo

	@property
	def ueCapability(self):
		"""ueCapability commands group. 19 Sub-classes, 9 commands."""
		if not hasattr(self, '_ueCapability'):
			from .Sense_.UeCapability import UeCapability
			self._ueCapability = UeCapability(self._core, self._base)
		return self._ueCapability

	@property
	def sms(self):
		"""sms commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Sense_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def eeLog(self):
		"""eeLog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eeLog'):
			from .Sense_.EeLog import EeLog
			self._eeLog = EeLog(self._core, self._base)
		return self._eeLog

	@property
	def elog(self):
		"""elog commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_elog'):
			from .Sense_.Elog import Elog
			self._elog = Elog(self._core, self._base)
		return self._elog

	@property
	def sib(self):
		"""sib commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sib'):
			from .Sense_.Sib import Sib
			self._sib = Sib(self._core, self._base)
		return self._sib

	# noinspection PyTypeChecker
	def get_rrc_state(self) -> enums.RrcState:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:RRCState \n
		Snippet: value: enums.RrcState = driver.sense.get_rrc_state() \n
		Queries whether an RRC connection is established (connected) or not (idle) . \n
			:return: state: IDLE | CONNected
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:RRCState?')
		return Conversions.str_to_scalar_enum(response, enums.RrcState)

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
