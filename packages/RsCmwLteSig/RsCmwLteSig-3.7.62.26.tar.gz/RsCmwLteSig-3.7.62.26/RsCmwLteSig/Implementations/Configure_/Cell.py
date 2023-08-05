from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 88 total commands, 15 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Cell_.Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._base)
		return self._bandwidth

	@property
	def pcc(self):
		"""pcc commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_pcc'):
			from .Cell_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	@property
	def scc(self):
		"""scc commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Cell_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdd'):
			from .Cell_.Tdd import Tdd
			self._tdd = Tdd(self._core, self._base)
		return self._tdd

	@property
	def prach(self):
		"""prach commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_prach'):
			from .Cell_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	@property
	def rar(self):
		"""rar commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rar'):
			from .Cell_.Rar import Rar
			self._rar = Rar(self._core, self._base)
		return self._rar

	@property
	def mnc(self):
		"""mnc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mnc'):
			from .Cell_.Mnc import Mnc
			self._mnc = Mnc(self._core, self._base)
		return self._mnc

	@property
	def security(self):
		"""security commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_security'):
			from .Cell_.Security import Security
			self._security = Security(self._core, self._base)
		return self._security

	@property
	def ueIdentity(self):
		"""ueIdentity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueIdentity'):
			from .Cell_.UeIdentity import UeIdentity
			self._ueIdentity = UeIdentity(self._core, self._base)
		return self._ueIdentity

	@property
	def timeout(self):
		"""timeout commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_timeout'):
			from .Cell_.Timeout import Timeout
			self._timeout = Timeout(self._core, self._base)
		return self._timeout

	@property
	def reSelection(self):
		"""reSelection commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_reSelection'):
			from .Cell_.ReSelection import ReSelection
			self._reSelection = ReSelection(self._core, self._base)
		return self._reSelection

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_time'):
			from .Cell_.Time import Time
			self._time = Time(self._core, self._base)
		return self._time

	@property
	def nas(self):
		"""nas commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_nas'):
			from .Cell_.Nas import Nas
			self._nas = Nas(self._core, self._base)
		return self._nas

	@property
	def acause(self):
		"""acause commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acause'):
			from .Cell_.Acause import Acause
			self._acause = Acause(self._core, self._base)
		return self._acause

	@property
	def rcause(self):
		"""rcause commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rcause'):
			from .Cell_.Rcause import Rcause
			self._rcause = Rcause(self._core, self._base)
		return self._rcause

	# noinspection PyTypeChecker
	def get_cprefix(self) -> enums.CyclicPrefix:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:CPRefix \n
		Snippet: value: enums.CyclicPrefix = driver.configure.cell.get_cprefix() \n
		Defines whether a normal or extended cyclic prefix (CP) is used. \n
			:return: cyclic_prefix: NORMal | EXTended
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:CPRefix?')
		return Conversions.str_to_scalar_enum(response, enums.CyclicPrefix)

	def set_cprefix(self, cyclic_prefix: enums.CyclicPrefix) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:CPRefix \n
		Snippet: driver.configure.cell.set_cprefix(cyclic_prefix = enums.CyclicPrefix.EXTended) \n
		Defines whether a normal or extended cyclic prefix (CP) is used. \n
			:param cyclic_prefix: NORMal | EXTended
		"""
		param = Conversions.enum_scalar_to_str(cyclic_prefix, enums.CyclicPrefix)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:CPRefix {param}')

	def get_mcc(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:MCC \n
		Snippet: value: int = driver.configure.cell.get_mcc() \n
		Specifies the three-digit mobile country code (MCC) . You can omit leading zeros. \n
			:return: mcc: Range: 0 to 999
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:MCC?')
		return Conversions.str_to_int(response)

	def set_mcc(self, mcc: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:MCC \n
		Snippet: driver.configure.cell.set_mcc(mcc = 1) \n
		Specifies the three-digit mobile country code (MCC) . You can omit leading zeros. \n
			:param mcc: Range: 0 to 999
		"""
		param = Conversions.decimal_value_to_str(mcc)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:MCC {param}')

	def get_tac(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TAC \n
		Snippet: value: int = driver.configure.cell.get_tac() \n
		Specifies the tracking area code. \n
			:return: tac: Range: 0 to 65535
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:TAC?')
		return Conversions.str_to_int(response)

	def set_tac(self, tac: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TAC \n
		Snippet: driver.configure.cell.set_tac(tac = 1) \n
		Specifies the tracking area code. \n
			:param tac: Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(tac)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TAC {param}')

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
