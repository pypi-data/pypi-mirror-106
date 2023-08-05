from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dshift:
	"""Dshift commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dshift", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Dshift_.Mode import Mode
			self._mode = Mode(self._core, self._base)
		return self._mode

	def set(self, frequency: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:DSHift \n
		Snippet: driver.configure.fading.scc.fadingSimulator.dshift.set(frequency = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the maximum Doppler frequency for the fading simulator. A setting is only allowed in USER mode (see
		CONFigure:LTE:SIGN<i>:FSIMulator:DSHift:MODE) . \n
			:param frequency: Range: 1 Hz to 2000 Hz, Unit: Hz
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		param = Conversions.decimal_value_to_str(frequency)
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:DSHift {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:DSHift \n
		Snippet: value: float = driver.configure.fading.scc.fadingSimulator.dshift.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the maximum Doppler frequency for the fading simulator. A setting is only allowed in USER mode (see
		CONFigure:LTE:SIGN<i>:FSIMulator:DSHift:MODE) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: frequency: Range: 1 Hz to 2000 Hz, Unit: Hz"""
		secondaryCompCarrier_cmd_val = self._base.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:DSHift?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Dshift':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dshift(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
