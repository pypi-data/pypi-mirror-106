from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 2 total commands, 0 Sub-groups, 2 group commands
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

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability Indicator'
			- Bler: List[float]: No parameter help available
			- Bler_All: float: float BLER result as weighted average over all timeslots Range: 0 % to 100 %, Unit: %
			- Rlc_Blocks: List[int]: No parameter help available
			- Rlc_Blocks_All: int: No parameter help available
			- Rlc_Data_Rate: List[float]: No parameter help available
			- Rlc_Data_Rate_All: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Bler', DataType.FloatList, None, False, False, 8),
			ArgStruct.scalar_float('Bler_All'),
			ArgStruct('Rlc_Blocks', DataType.IntegerList, None, False, False, 8),
			ArgStruct.scalar_int('Rlc_Blocks_All'),
			ArgStruct('Rlc_Data_Rate', DataType.FloatList, None, False, False, 8),
			ArgStruct.scalar_float('Rlc_Data_Rate_All')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bler: List[float] = None
			self.Bler_All: float = None
			self.Rlc_Blocks: List[int] = None
			self.Rlc_Blocks_All: int = None
			self.Rlc_Data_Rate: List[float] = None
			self.Rlc_Data_Rate_All: float = None

	def fetch(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: FETCh:GSM:SIGNaling<Instance>:BLER:CARRier<Carrier> \n
		Snippet: value: ResultData = driver.bler.carrier.fetch(carrier = repcap.Carrier.Default) \n
		Returns the results of the BLER measurement for the individual timeslots. For details, see 'BLER Measurement'. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'FETCh:GSM:SIGNaling<Instance>:BLER:CARRier{carrier_cmd_val}?', self.__class__.ResultData())

	def read(self, carrier=repcap.Carrier.Default) -> ResultData:
		"""SCPI: READ:GSM:SIGNaling<Instance>:BLER:CARRier<Carrier> \n
		Snippet: value: ResultData = driver.bler.carrier.read(carrier = repcap.Carrier.Default) \n
		Returns the results of the BLER measurement for the individual timeslots. For details, see 'BLER Measurement'. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'READ:GSM:SIGNaling<Instance>:BLER:CARRier{carrier_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
