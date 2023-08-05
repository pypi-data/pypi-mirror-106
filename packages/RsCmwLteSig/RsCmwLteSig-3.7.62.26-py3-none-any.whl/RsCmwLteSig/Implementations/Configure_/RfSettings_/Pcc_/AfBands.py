from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AfBands:
	"""AfBands commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("afBands", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: List[bool]: OFF | ON Enables/disables the entry.
			- Bands: List[enums.OperatingBandC]: OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB250 | OB252 | OB255"""
		__meta_args_list = [
			ArgStruct('Enable', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Bands', DataType.EnumList, enums.OperatingBandC, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: List[bool] = None
			self.Bands: List[enums.OperatingBandC] = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:AFBands:ALL \n
		Snippet: value: AllStruct = driver.configure.rfSettings.pcc.afBands.get_all() \n
		Configures additional frequency bands supported by the cell ('multiBandInfoList') . There are eight entries.
		You can enable/disable each entry and assign a band to each entry. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:AFBands:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:AFBands:ALL \n
		Snippet: driver.configure.rfSettings.pcc.afBands.set_all(value = AllStruct()) \n
		Configures additional frequency bands supported by the cell ('multiBandInfoList') . There are eight entries.
		You can enable/disable each entry and assign a band to each entry. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:AFBands:ALL', value)
