from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InterFreqNgaps:
	"""InterFreqNgaps commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("interFreqNgaps", core, parent)

	@property
	def v(self):
		"""v commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_v'):
			from .InterFreqNgaps_.V import V
			self._v = V(self._core, self._base)
		return self._v

	def get(self, index: enums.OperatingBandC = None) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:IFNGaps \n
		Snippet: value: List[bool] = driver.sense.ueCapability.meas.interFreqNgaps.get(index = enums.OperatingBandC.OB1) \n
		Returns a list of values indicating the need for downlink measurement gaps when operating on a specific E-UTRA band and
		measuring on (another) specific E-UTRA band. The full list contains 256 times 256 values. The 256 values/repetitions
		correspond to the LTE bands. The list is ordered as follows: {measured band: user-defined, 1, 2, ..., 255}used band:
		user-defined, {measured band: user-defined, 1, 2, ..., 255}used band: 1, ..., {measured band: user-defined, 1, 2, ...
		, 255}used band: 255 Via the optional parameter <Index>, you can alternatively query the list for one measured band:
		{used band: user-defined, 1, 2, ..., 255}measured band <Index> \n
			:param index: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB250 | OB252 | OB255 Selects the measured E-UTRA band, for which the list is returned.
			:return: value: OFF | ON Without Index: 256 x 256 = 65536 values With Index: 256 values"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Enum, True))
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:IFNGaps? {param}'.rstrip())
		return Conversions.str_to_bool_list(response)

	def clone(self) -> 'InterFreqNgaps':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InterFreqNgaps(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
