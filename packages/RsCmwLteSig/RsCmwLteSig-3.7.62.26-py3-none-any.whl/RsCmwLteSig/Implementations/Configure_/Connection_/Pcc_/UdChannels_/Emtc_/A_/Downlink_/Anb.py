from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Anb:
	"""Anb commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Anb, default value after init: Anb.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("anb", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_anb_get', 'repcap_anb_set', repcap.Anb.Nr1)

	def repcap_anb_set(self, enum_value: repcap.Anb) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Anb.Default
		Default value after init: Anb.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_anb_get(self) -> repcap.Anb:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, additional_nb: bool, anb=repcap.Anb.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:A:DL:ANB<Number> \n
		Snippet: driver.configure.connection.pcc.udChannels.emtc.a.downlink.anb.set(additional_nb = False, anb = repcap.Anb.Default) \n
		No command help available \n
			:param additional_nb: No help available
			:param anb: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Anb')"""
		param = Conversions.bool_to_str(additional_nb)
		anb_cmd_val = self._base.get_repcap_cmd_value(anb, repcap.Anb)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:A:DL:ANB{anb_cmd_val} {param}')

	def get(self, anb=repcap.Anb.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:A:DL:ANB<Number> \n
		Snippet: value: bool = driver.configure.connection.pcc.udChannels.emtc.a.downlink.anb.get(anb = repcap.Anb.Default) \n
		No command help available \n
			:param anb: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Anb')
			:return: additional_nb: No help available"""
		anb_cmd_val = self._base.get_repcap_cmd_value(anb, repcap.Anb)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:A:DL:ANB{anb_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Anb':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Anb(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
