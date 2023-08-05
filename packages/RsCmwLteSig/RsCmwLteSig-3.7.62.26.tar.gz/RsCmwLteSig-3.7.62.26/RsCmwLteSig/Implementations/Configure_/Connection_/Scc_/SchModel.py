from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SchModel:
	"""SchModel commands group definition. 5 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("schModel", core, parent)

	@property
	def enable(self):
		"""enable commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .SchModel_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def mselection(self):
		"""mselection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mselection'):
			from .SchModel_.Mselection import Mselection
			self._mselection = Mselection(self._core, self._base)
		return self._mselection

	@property
	def mimo(self):
		"""mimo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mimo'):
			from .SchModel_.Mimo import Mimo
			self._mimo = Mimo(self._core, self._base)
		return self._mimo

	# noinspection PyTypeChecker
	class SchModelStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- H_11_Abs: float: Square of magnitude of h11 Range: 0 to 1
			- H_11_Phi: int: Phase of h11 Range: 0 deg to 345 deg, Unit: deg
			- H_12_Phi: int: Phase of h12 Range: 0 deg to 345 deg, Unit: deg
			- H_21_Abs: float: Square of magnitude of h21 Range: 0 to 1
			- H_21_Phi: int: Phase of h21 Range: 0 deg to 345 deg, Unit: deg
			- H_22_Phi: int: Phase of h22 Range: 0 deg to 345 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_float('H_11_Abs'),
			ArgStruct.scalar_int('H_11_Phi'),
			ArgStruct.scalar_int('H_12_Phi'),
			ArgStruct.scalar_float('H_21_Abs'),
			ArgStruct.scalar_int('H_21_Phi'),
			ArgStruct.scalar_int('H_22_Phi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.H_11_Abs: float = None
			self.H_11_Phi: int = None
			self.H_12_Phi: int = None
			self.H_21_Abs: float = None
			self.H_21_Phi: int = None
			self.H_22_Phi: int = None

	def set(self, structure: SchModelStruct, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:SCHModel \n
		Snippet: driver.configure.connection.scc.schModel.set(value = [PROPERTY_STRUCT_NAME](), secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the channel coefficients, characterizing the radio channel for MIMO 2x2. \n
			:param structure: for set value, see the help for SchModelStruct structure arguments.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:SCHModel', structure)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> SchModelStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:SCHModel \n
		Snippet: value: SchModelStruct = driver.configure.connection.scc.schModel.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the channel coefficients, characterizing the radio channel for MIMO 2x2. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for SchModelStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:SCHModel?', self.__class__.SchModelStruct())

	def clone(self) -> 'SchModel':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SchModel(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
