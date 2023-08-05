from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Restart:
	"""Restart commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("restart", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Restart_.Mode import Mode
			self._mode = Mode(self._core, self._base)
		return self._mode

	def set(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:RESTart \n
		Snippet: driver.configure.fading.scc.fadingSimulator.restart.set(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Restarts the fading process in MANual mode (see also CONFigure:...:FSIMulator:RESTart:MODE) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:RESTart')

	def set_with_opc(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:RESTart \n
		Snippet: driver.configure.fading.scc.fadingSimulator.restart.set_with_opc(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Restarts the fading process in MANual mode (see also CONFigure:...:FSIMulator:RESTart:MODE) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:RESTart')

	def clone(self) -> 'Restart':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Restart(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
