from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Col:
	"""Col commands group definition. 2 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: HMatrixColumn, default value after init: HMatrixColumn.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("col", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_hMatrixColumn_get', 'repcap_hMatrixColumn_set', repcap.HMatrixColumn.Nr1)

	def repcap_hMatrixColumn_set(self, enum_value: repcap.HMatrixColumn) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to HMatrixColumn.Default
		Default value after init: HMatrixColumn.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_hMatrixColumn_get(self) -> repcap.HMatrixColumn:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def imag(self):
		"""imag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imag'):
			from .Col_.Imag import Imag
			self._imag = Imag(self._core, self._base)
		return self._imag

	@property
	def real(self):
		"""real commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_real'):
			from .Col_.Real import Real
			self._real = Real(self._core, self._base)
		return self._real

	def clone(self) -> 'Col':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Col(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
