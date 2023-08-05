from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FadingSimulator:
	"""FadingSimulator commands group definition. 18 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fadingSimulator", core, parent)

	@property
	def globale(self):
		"""globale commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_globale'):
			from .FadingSimulator_.Globale import Globale
			self._globale = Globale(self._core, self._base)
		return self._globale

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .FadingSimulator_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def bypass(self):
		"""bypass commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bypass'):
			from .FadingSimulator_.Bypass import Bypass
			self._bypass = Bypass(self._core, self._base)
		return self._bypass

	@property
	def standard(self):
		"""standard commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_standard'):
			from .FadingSimulator_.Standard import Standard
			self._standard = Standard(self._core, self._base)
		return self._standard

	@property
	def restart(self):
		"""restart commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_restart'):
			from .FadingSimulator_.Restart import Restart
			self._restart = Restart(self._core, self._base)
		return self._restart

	@property
	def profile(self):
		"""profile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_profile'):
			from .FadingSimulator_.Profile import Profile
			self._profile = Profile(self._core, self._base)
		return self._profile

	@property
	def iloss(self):
		"""iloss commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iloss'):
			from .FadingSimulator_.Iloss import Iloss
			self._iloss = Iloss(self._core, self._base)
		return self._iloss

	@property
	def dshift(self):
		"""dshift commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dshift'):
			from .FadingSimulator_.Dshift import Dshift
			self._dshift = Dshift(self._core, self._base)
		return self._dshift

	@property
	def matrix(self):
		"""matrix commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_matrix'):
			from .FadingSimulator_.Matrix import Matrix
			self._matrix = Matrix(self._core, self._base)
		return self._matrix

	@property
	def hmat(self):
		"""hmat commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_hmat'):
			from .FadingSimulator_.Hmat import Hmat
			self._hmat = Hmat(self._core, self._base)
		return self._hmat

	def clone(self) -> 'FadingSimulator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FadingSimulator(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
