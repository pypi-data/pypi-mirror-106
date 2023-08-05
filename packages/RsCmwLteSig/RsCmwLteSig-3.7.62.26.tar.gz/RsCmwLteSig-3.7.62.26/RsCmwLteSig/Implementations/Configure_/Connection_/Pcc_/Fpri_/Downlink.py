from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	def get_stti(self) -> List[bool]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPRI:DL:STTI \n
		Snippet: value: List[bool] = driver.configure.connection.pcc.fpri.downlink.get_stti() \n
		Configures which subframes are scheduled for the DL of the scheduling type 'Follow WB PMI-RI'. For most subframes, the
		setting is fixed, depending on the duplex mode and the UL-DL configuration. For these subframes, your setting is ignored. \n
			:return: scheduled: OFF | ON Comma-separated list of 10 values, for subframe 0 to 9
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPRI:DL:STTI?')
		return Conversions.str_to_bool_list(response)

	def set_stti(self, scheduled: List[bool]) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPRI:DL:STTI \n
		Snippet: driver.configure.connection.pcc.fpri.downlink.set_stti(scheduled = [True, False, True]) \n
		Configures which subframes are scheduled for the DL of the scheduling type 'Follow WB PMI-RI'. For most subframes, the
		setting is fixed, depending on the duplex mode and the UL-DL configuration. For these subframes, your setting is ignored. \n
			:param scheduled: OFF | ON Comma-separated list of 10 values, for subframe 0 to 9
		"""
		param = Conversions.list_to_csv_str(scheduled)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPRI:DL:STTI {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number_Rb: int: Number of allocated resource blocks
			- Start_Rb: int: Position of first resource block
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 Modulation type QPSK | 16-QAM | 64-QAM | 256-QAM
			- Trans_Block_Size_Idx: int: Transport block size index"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int('Trans_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPRI:DL \n
		Snippet: value: ValueStruct = driver.configure.connection.pcc.fpri.downlink.get_value() \n
		Configures the downlink for the scheduling type 'Follow WB PMI-RI', with contiguous allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI Channels'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPRI:DL?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPRI:DL \n
		Snippet: driver.configure.connection.pcc.fpri.downlink.set_value(value = ValueStruct()) \n
		Configures the downlink for the scheduling type 'Follow WB PMI-RI', with contiguous allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI Channels'. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPRI:DL', value)
