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

	def set(self, enable: List[bool], carrier=repcap.Carrier.Default) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:ENABle:DL:CARRier<Carrier> \n
		Snippet: driver.prepare.handover.pswitched.enable.downlink.carrier.set(enable = [True, False, True], carrier = repcap.Carrier.Default) \n
		Specifies the downlink timeslots the mobile has to use in a packet switched connection in the destination GSM band.
		Timeslot 0 cannot be enabled (always OFF) . \n
			:param enable: OFF | ON List of 8 values for timeslot 0 to 7
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		param = Conversions.list_to_csv_str(enable)
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write_with_opc(f'PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:ENABle:DL:CARRier{carrier_cmd_val} {param}')

	def get(self, carrier=repcap.Carrier.Default) -> List[bool]:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:ENABle:DL:CARRier<Carrier> \n
		Snippet: value: List[bool] = driver.prepare.handover.pswitched.enable.downlink.carrier.get(carrier = repcap.Carrier.Default) \n
		Specifies the downlink timeslots the mobile has to use in a packet switched connection in the destination GSM band.
		Timeslot 0 cannot be enabled (always OFF) . \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: enable: OFF | ON List of 8 values for timeslot 0 to 7"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str_with_opc(f'PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:ENABle:DL:CARRier{carrier_cmd_val}?')
		return Conversions.str_to_bool_list(response)

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
