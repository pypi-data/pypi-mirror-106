from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EeLog:
	"""EeLog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eeLog", core, parent)

	def set(self) -> None:
		"""SCPI: CLEan:LTE:SIGNaling<instance>:EELog \n
		Snippet: driver.clean.eeLog.set() \n
		No command help available \n
		"""
		self._core.io.write(f'CLEan:LTE:SIGNaling<Instance>:EELog')

	def set_with_opc(self) -> None:
		"""SCPI: CLEan:LTE:SIGNaling<instance>:EELog \n
		Snippet: driver.clean.eeLog.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CLEan:LTE:SIGNaling<Instance>:EELog')
