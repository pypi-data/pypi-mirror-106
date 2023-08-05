from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcluster:
	"""Mcluster commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mcluster", core, parent)

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Cluster: str: Bitmap, enabling or disabling the individual RBGs 1 means RBG is allocated, 0 means RBG is not allocated The number of bits depends on the cell bandwidth and equals the total number of RBGs. The bitmap starts with RBG 0 (most significant bit) and continues with increasing RBG index / frequency. Example for BW 1.4 MHz: #B101010 means that the RBGs 0, 2 and 4 are allocated
			- Table: enums.MultiClusterDlTable: DETermined | UDEFined DETermined: Automatic CQI-MCS mapping table UDEFined: User-defined mapping table"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Cluster'),
			ArgStruct.scalar_enum('Table', enums.MultiClusterDlTable)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cluster: str = None
			self.Table: enums.MultiClusterDlTable = None

	def get_downlink(self) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FCRI:MCLuster:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.pcc.fcri.mcluster.get_downlink() \n
		Configures the downlink for the scheduling type 'Follow WB CQI-RI', with multi-cluster allocation. The allowed input
		ranges have dependencies and are described in the background information, see 'CQI Channels' and especially Table 'RBG
		parameters'. \n
			:return: structure: for return value, see the help for DownlinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FCRI:MCLuster:DL?', self.__class__.DownlinkStruct())

	def set_downlink(self, value: DownlinkStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FCRI:MCLuster:DL \n
		Snippet: driver.configure.connection.pcc.fcri.mcluster.set_downlink(value = DownlinkStruct()) \n
		Configures the downlink for the scheduling type 'Follow WB CQI-RI', with multi-cluster allocation. The allowed input
		ranges have dependencies and are described in the background information, see 'CQI Channels' and especially Table 'RBG
		parameters'. \n
			:param value: see the help for DownlinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FCRI:MCLuster:DL', value)
