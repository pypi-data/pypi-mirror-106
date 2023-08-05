from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtext:
	"""Mtext commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mtext", core, parent)

	def set(self) -> None:
		"""SCPI: CLEan:LTE:SIGNaling<instance>:SMS:INComing:INFO:MTEXt \n
		Snippet: driver.clean.sms.incoming.info.mtext.set() \n
		Resets all parameters related to a received SMS message. The 'message read' flag is set to true. \n
		"""
		self._core.io.write(f'CLEan:LTE:SIGNaling<Instance>:SMS:INComing:INFO:MTEXt')

	def set_with_opc(self) -> None:
		"""SCPI: CLEan:LTE:SIGNaling<instance>:SMS:INComing:INFO:MTEXt \n
		Snippet: driver.clean.sms.incoming.info.mtext.set_with_opc() \n
		Resets all parameters related to a received SMS message. The 'message read' flag is set to true. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CLEan:LTE:SIGNaling<Instance>:SMS:INComing:INFO:MTEXt')
