from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enable", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Enable_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	def get_uplink(self) -> List[bool]:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:ENABle:UL \n
		Snippet: value: List[bool] = driver.prepare.handover.pswitched.enable.get_uplink() \n
		Specifies the uplink timeslots the mobile has to use in a packet switched connection in the destination GSM band.
		Timeslot 0 cannot be enabled (always OFF) . \n
			:return: enable: OFF | ON List of 8 values for timeslot 0 to 7
		"""
		response = self._core.io.query_str_with_opc('PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:ENABle:UL?')
		return Conversions.str_to_bool_list(response)

	def set_uplink(self, enable: List[bool]) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:ENABle:UL \n
		Snippet: driver.prepare.handover.pswitched.enable.set_uplink(enable = [True, False, True]) \n
		Specifies the uplink timeslots the mobile has to use in a packet switched connection in the destination GSM band.
		Timeslot 0 cannot be enabled (always OFF) . \n
			:param enable: OFF | ON List of 8 values for timeslot 0 to 7
		"""
		param = Conversions.list_to_csv_str(enable)
		self._core.io.write_with_opc(f'PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:ENABle:UL {param}')

	def clone(self) -> 'Enable':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Enable(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
