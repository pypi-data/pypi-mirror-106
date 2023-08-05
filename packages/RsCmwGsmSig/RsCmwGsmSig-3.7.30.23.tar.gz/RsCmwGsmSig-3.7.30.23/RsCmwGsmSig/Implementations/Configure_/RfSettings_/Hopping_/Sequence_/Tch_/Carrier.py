from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Carrier, default value after init: Carrier.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_carrier_get', 'repcap_carrier_set', repcap.Carrier.Nr1)

	def repcap_carrier_set(self, enum_value: repcap.Carrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Carrier.Default
		Default value after init: Carrier.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_carrier_get(self) -> repcap.Carrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, number: List[int or bool], carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:HOPPing:SEQuence:TCH[:CARRier<Carrier>] \n
		Snippet: driver.configure.rfSettings.hopping.sequence.tch.carrier.set(number = [1, True, 2, False, 3], carrier = repcap.Carrier.Default) \n
		Defines the hopping list. Each entry equals a channel number. You can specify the 64 entries in any order. The list is
		sorted automatically from lowest channel number to highest channel number followed by eventual OFF entries. The range of
		values depends on the selected band. For an overview, see 'GSM Bands and Channels' \n
			:param number: ON | OFF Comma-separated list of 64 list entries (channel numbers) Range: 1 to 124, 940 to 1023 Additional parameters: OFF | ON (disables | enables the list entry using the previous/default value)
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		param = Conversions.list_to_csv_str(number)
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:HOPPing:SEQuence:TCH:CARRier{carrier_cmd_val} {param}')

	def get(self, carrier=repcap.Carrier.Default) -> List[int or bool]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:HOPPing:SEQuence:TCH[:CARRier<Carrier>] \n
		Snippet: value: List[int or bool] = driver.configure.rfSettings.hopping.sequence.tch.carrier.get(carrier = repcap.Carrier.Default) \n
		Defines the hopping list. Each entry equals a channel number. You can specify the 64 entries in any order. The list is
		sorted automatically from lowest channel number to highest channel number followed by eventual OFF entries. The range of
		values depends on the selected band. For an overview, see 'GSM Bands and Channels' \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: number: ON | OFF Comma-separated list of 64 list entries (channel numbers) Range: 1 to 124, 940 to 1023 Additional parameters: OFF | ON (disables | enables the list entry using the previous/default value)"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:HOPPing:SEQuence:TCH:CARRier{carrier_cmd_val}?')
		return Conversions.str_to_int_or_bool_list(response)

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
