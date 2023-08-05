from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rohc:
	"""Rohc commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rohc", core, parent)

	@property
	def ulOnly(self):
		"""ulOnly commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ulOnly'):
			from .Rohc_.UlOnly import UlOnly
			self._ulOnly = UlOnly(self._core, self._base)
		return self._ulOnly

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:ENABle \n
		Snippet: value: bool = driver.configure.connection.rohc.get_enable() \n
		Enables or disables bidirectional header compression. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:ENABle \n
		Snippet: driver.configure.connection.rohc.set_enable(enable = False) \n
		Enables or disables bidirectional header compression. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:ENABle {param}')

	# noinspection PyTypeChecker
	def get_efor(self) -> enums.HeaderCompression:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:EFOR \n
		Snippet: value: enums.HeaderCompression = driver.configure.connection.rohc.get_efor() \n
		Selects for which types of dedicated bearers header compression is enabled. \n
			:return: for_py: VVB | ADB VVB: voice and video bearers ADB: all dedicated bearers
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:EFOR?')
		return Conversions.str_to_scalar_enum(response, enums.HeaderCompression)

	def set_efor(self, for_py: enums.HeaderCompression) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:EFOR \n
		Snippet: driver.configure.connection.rohc.set_efor(for_py = enums.HeaderCompression.ADB) \n
		Selects for which types of dedicated bearers header compression is enabled. \n
			:param for_py: VVB | ADB VVB: voice and video bearers ADB: all dedicated bearers
		"""
		param = Conversions.enum_scalar_to_str(for_py, enums.HeaderCompression)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:EFOR {param}')

	# noinspection PyTypeChecker
	class ProfilesStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Profile_0_X_0001: bool: OFF | ON Profile 1, for IP/UDP/RTP
			- Profile_0_X_0002: bool: OFF | ON Profile 2, for IP/UDP/...
			- Profile_0_X_0004: bool: OFF | ON Profile 4, for IP/...
			- Profile_0_X_0006: bool: OFF | ON Profile 6, for IP/TCP/..."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Profile_0_X_0001'),
			ArgStruct.scalar_bool('Profile_0_X_0002'),
			ArgStruct.scalar_bool('Profile_0_X_0004'),
			ArgStruct.scalar_bool('Profile_0_X_0006')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Profile_0_X_0001: bool = None
			self.Profile_0_X_0002: bool = None
			self.Profile_0_X_0004: bool = None
			self.Profile_0_X_0006: bool = None

	def get_profiles(self) -> ProfilesStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:PROFiles \n
		Snippet: value: ProfilesStruct = driver.configure.connection.rohc.get_profiles() \n
		Enables header compression profiles for bidirectional header compression. \n
			:return: structure: for return value, see the help for ProfilesStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:PROFiles?', self.__class__.ProfilesStruct())

	def set_profiles(self, value: ProfilesStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:ROHC:PROFiles \n
		Snippet: driver.configure.connection.rohc.set_profiles(value = ProfilesStruct()) \n
		Enables header compression profiles for bidirectional header compression. \n
			:param value: see the help for ProfilesStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:ROHC:PROFiles', value)

	def clone(self) -> 'Rohc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rohc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
