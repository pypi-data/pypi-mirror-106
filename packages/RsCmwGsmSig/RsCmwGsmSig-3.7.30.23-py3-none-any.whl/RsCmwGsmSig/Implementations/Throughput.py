from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 23 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Throughput_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Throughput_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def stop(self) -> None:
		"""SCPI: STOP:GSM:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:GSM:SIGNaling<Instance>:THRoughput')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:GSM:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:GSM:SIGNaling<Instance>:THRoughput')

	def abort(self) -> None:
		"""SCPI: ABORt:GSM:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:GSM:SIGNaling<Instance>:THRoughput')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:GSM:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:GSM:SIGNaling<Instance>:THRoughput')

	def initiate(self) -> None:
		"""SCPI: INITiate:GSM:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:GSM:SIGNaling<Instance>:THRoughput')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:GSM:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:GSM:SIGNaling<Instance>:THRoughput')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability Indicator'
			- Curr_Dl_Pdu: float: float Current, average, maximum and minimum DL PDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Avg_Dl_Pdu: float: float Current, average, maximum and minimum DL PDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Max_Dl_Pdu: float: float Current, average, maximum and minimum DL PDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Min_Dl_Pdu: float: float Current, average, maximum and minimum DL PDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Curr_Dl_Sdu: float: float Current, average, maximum and minimum DL SDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Avg_Dl_Sdu: float: float Current, average, maximum and minimum DL SDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Max_Dl_Sdu: float: float Current, average, maximum and minimum DL SDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Min_Dl_Sdu: float: float Current, average, maximum and minimum DL SDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Blocks_Dl_Pdu: int: decimal Number of transmitted RLC PDUs Range: 0 to 1E+6
			- Curr_Ul_Pdu: float: float Current, average, maximum and minimum UL PDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Avg_Ul_Pdu: float: float Current, average, maximum and minimum UL PDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Max_Ul_Pdu: float: float Current, average, maximum and minimum UL PDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Min_Ul_Pdu: float: float Current, average, maximum and minimum UL PDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Curr_Ul_Sdu: float: float Current, average, maximum and minimum UL SDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Avg_Ul_Sdu: float: float Current, average, maximum and minimum UL SDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Max_Ul_Sdu: float: float Current, average, maximum and minimum UL SDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Min_Ul_Sdu: float: float Current, average, maximum and minimum UL SDU results Range: 0 bit/s to 100E+6 bit/s , Unit: bit/s
			- Blocks_Ul_Pdu: float: float Range: 0 to 1E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Curr_Dl_Pdu'),
			ArgStruct.scalar_float('Avg_Dl_Pdu'),
			ArgStruct.scalar_float('Max_Dl_Pdu'),
			ArgStruct.scalar_float('Min_Dl_Pdu'),
			ArgStruct.scalar_float('Curr_Dl_Sdu'),
			ArgStruct.scalar_float('Avg_Dl_Sdu'),
			ArgStruct.scalar_float('Max_Dl_Sdu'),
			ArgStruct.scalar_float('Min_Dl_Sdu'),
			ArgStruct.scalar_int('Blocks_Dl_Pdu'),
			ArgStruct.scalar_float('Curr_Ul_Pdu'),
			ArgStruct.scalar_float('Avg_Ul_Pdu'),
			ArgStruct.scalar_float('Max_Ul_Pdu'),
			ArgStruct.scalar_float('Min_Ul_Pdu'),
			ArgStruct.scalar_float('Curr_Ul_Sdu'),
			ArgStruct.scalar_float('Avg_Ul_Sdu'),
			ArgStruct.scalar_float('Max_Ul_Sdu'),
			ArgStruct.scalar_float('Min_Ul_Sdu'),
			ArgStruct.scalar_float('Blocks_Ul_Pdu')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Curr_Dl_Pdu: float = None
			self.Avg_Dl_Pdu: float = None
			self.Max_Dl_Pdu: float = None
			self.Min_Dl_Pdu: float = None
			self.Curr_Dl_Sdu: float = None
			self.Avg_Dl_Sdu: float = None
			self.Max_Dl_Sdu: float = None
			self.Min_Dl_Sdu: float = None
			self.Blocks_Dl_Pdu: int = None
			self.Curr_Ul_Pdu: float = None
			self.Avg_Ul_Pdu: float = None
			self.Max_Ul_Pdu: float = None
			self.Min_Ul_Pdu: float = None
			self.Curr_Ul_Sdu: float = None
			self.Avg_Ul_Sdu: float = None
			self.Max_Ul_Sdu: float = None
			self.Min_Ul_Sdu: float = None
			self.Blocks_Ul_Pdu: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:SIGNaling<instance>:THRoughput \n
		Snippet: value: ResultData = driver.throughput.fetch() \n
		Returns all single value throughput results. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:SIGNaling<Instance>:THRoughput?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:SIGNaling<instance>:THRoughput \n
		Snippet: value: ResultData = driver.throughput.read() \n
		Returns all single value throughput results. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:SIGNaling<Instance>:THRoughput?', self.__class__.ResultData())

	def clone(self) -> 'Throughput':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Throughput(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
