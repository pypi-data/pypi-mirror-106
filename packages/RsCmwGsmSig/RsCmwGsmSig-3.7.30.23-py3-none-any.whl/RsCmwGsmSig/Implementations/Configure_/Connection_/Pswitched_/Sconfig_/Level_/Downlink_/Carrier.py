from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


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

	def set(self, level: List[float or bool], carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:LEVel:DL:CARRier<Carrier> \n
		Snippet: driver.configure.connection.pswitched.sconfig.level.downlink.carrier.set(level = [1.1, True, 2.2, False, 3.3], carrier = repcap.Carrier.Default) \n
		Defines the DL signal level in all timeslots relative to the reference level (see CONFigure:GSM:SIGN<i>:RFSettings:LEVel.
		The DL timeslot level can also be set to off level (no signal transmission) . \n
			:param level: ON | OFF List of 8 signal levels for slot 0 to 7 Range: -40 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables DL signal transmission)
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		param = Conversions.list_to_csv_str(level)
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:LEVel:DL:CARRier{carrier_cmd_val} {param}')

	def get(self, carrier=repcap.Carrier.Default) -> List[float or bool]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:LEVel:DL:CARRier<Carrier> \n
		Snippet: value: List[float or bool] = driver.configure.connection.pswitched.sconfig.level.downlink.carrier.get(carrier = repcap.Carrier.Default) \n
		Defines the DL signal level in all timeslots relative to the reference level (see CONFigure:GSM:SIGN<i>:RFSettings:LEVel.
		The DL timeslot level can also be set to off level (no signal transmission) . \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: level: ON | OFF List of 8 signal levels for slot 0 to 7 Range: -40 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables DL signal transmission)"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:LEVel:DL:CARRier{carrier_cmd_val}?')
		return Conversions.str_to_float_or_bool_list(response)

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
