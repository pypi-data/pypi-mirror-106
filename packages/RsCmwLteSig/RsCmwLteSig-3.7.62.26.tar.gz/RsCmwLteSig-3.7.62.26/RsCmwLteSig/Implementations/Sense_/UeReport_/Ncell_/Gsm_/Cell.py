from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Cell_.Range import Range
			self._range = Range(self._core, self._base)
		return self._range

	def get(self, cellNo=repcap.CellNo.Default) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:NCELl:GSM:CELL<nr> \n
		Snippet: value: int = driver.sense.ueReport.ncell.gsm.cell.get(cellNo = repcap.CellNo.Default) \n
		Returns the RSSI value reported as dimensionless index for the GSM neighbor cell number <no>. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: rssi: Range: 0 to 63"""
		cellNo_cmd_val = self._base.get_repcap_cmd_value(cellNo, repcap.CellNo)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UEReport:NCELl:GSM:CELL{cellNo_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
