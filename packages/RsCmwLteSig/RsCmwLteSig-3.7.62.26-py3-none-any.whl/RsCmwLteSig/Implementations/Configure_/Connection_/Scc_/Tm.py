from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tm:
	"""Tm commands group definition. 15 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tm", core, parent)

	@property
	def chMatrix(self):
		"""chMatrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chMatrix'):
			from .Tm_.ChMatrix import ChMatrix
			self._chMatrix = ChMatrix(self._core, self._base)
		return self._chMatrix

	@property
	def cmatrix(self):
		"""cmatrix commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmatrix'):
			from .Tm_.Cmatrix import Cmatrix
			self._cmatrix = Cmatrix(self._core, self._base)
		return self._cmatrix

	@property
	def zp(self):
		"""zp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_zp'):
			from .Tm_.Zp import Zp
			self._zp = Zp(self._core, self._base)
		return self._zp

	@property
	def csirs(self):
		"""csirs commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Tm_.Csirs import Csirs
			self._csirs = Csirs(self._core, self._base)
		return self._csirs

	@property
	def pmatrix(self):
		"""pmatrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmatrix'):
			from .Tm_.Pmatrix import Pmatrix
			self._pmatrix = Pmatrix(self._core, self._base)
		return self._pmatrix

	@property
	def codewords(self):
		"""codewords commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_codewords'):
			from .Tm_.Codewords import Codewords
			self._codewords = Codewords(self._core, self._base)
		return self._codewords

	@property
	def ntxAntennas(self):
		"""ntxAntennas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntxAntennas'):
			from .Tm_.NtxAntennas import NtxAntennas
			self._ntxAntennas = NtxAntennas(self._core, self._base)
		return self._ntxAntennas

	def clone(self) -> 'Tm':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tm(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
