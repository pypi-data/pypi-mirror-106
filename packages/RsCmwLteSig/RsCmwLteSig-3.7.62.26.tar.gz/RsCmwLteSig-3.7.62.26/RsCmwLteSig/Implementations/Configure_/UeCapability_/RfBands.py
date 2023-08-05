from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfBands:
	"""RfBands commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfBands", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: List[bool]: OFF | ON Disables or enables the entry
			- Band: List[enums.OperatingBandC]: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB250 | OB252 | OB255 Assigns a band to the entry"""
		__meta_args_list = [
			ArgStruct('Enable', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Band', DataType.EnumList, enums.OperatingBandC, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: List[bool] = None
			self.Band: List[enums.OperatingBandC] = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RFBands:ALL \n
		Snippet: value: AllStruct = driver.configure.ueCapability.rfBands.get_all() \n
		Configures the list of operating bands for the information element 'requestedFrequencyBands' of the 'ueCapabilityEnquiry'
		message. The command has 32 parameters, for 16 entries with two parameters each: {<Enable>, <Band>}entry 1, {<Enable>,
		<Band>}entry 2, ..., {<Enable>, <Band>}entry 16 \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:UECapability:RFBands:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RFBands:ALL \n
		Snippet: driver.configure.ueCapability.rfBands.set_all(value = AllStruct()) \n
		Configures the list of operating bands for the information element 'requestedFrequencyBands' of the 'ueCapabilityEnquiry'
		message. The command has 32 parameters, for 16 entries with two parameters each: {<Enable>, <Band>}entry 1, {<Enable>,
		<Band>}entry 2, ..., {<Enable>, <Band>}entry 16 \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:UECapability:RFBands:ALL', value)
