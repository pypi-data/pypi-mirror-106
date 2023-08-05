from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alevel:
	"""Alevel commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("alevel", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Dldci_Crnti: int: DCI for DL with C-RNTI Range: 1 to 8
			- Uldci_Crnti: int: DCI for UL with C-RNTI Range: 1 to 8
			- Dldci_Sirnti: int: DCI for DL with SI-RNTI Range: 1 to 8"""
		__meta_args_list = [
			ArgStruct.scalar_int('Dldci_Crnti'),
			ArgStruct.scalar_int('Uldci_Crnti'),
			ArgStruct.scalar_int('Dldci_Sirnti')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dldci_Crnti: int = None
			self.Uldci_Crnti: int = None
			self.Dldci_Sirnti: int = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:PDCCh:ALEVel \n
		Snippet: value: GetStruct = driver.sense.connection.scc.pdcch.alevel.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the used PDCCH aggregation levels. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:PDCCh:ALEVel?', self.__class__.GetStruct())
