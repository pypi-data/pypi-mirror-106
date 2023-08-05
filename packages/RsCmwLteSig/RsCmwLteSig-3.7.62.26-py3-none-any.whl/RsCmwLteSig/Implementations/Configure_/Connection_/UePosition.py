from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UePosition:
	"""UePosition commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uePosition", core, parent)

	def reset(self) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UEPosition:RESet \n
		Snippet: driver.configure.connection.uePosition.reset() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UEPosition:RESet')

	def reset_with_opc(self) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UEPosition:RESet \n
		Snippet: driver.configure.connection.uePosition.reset_with_opc() \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UEPosition:RESet')
