from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 9 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Pswitched_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def carrier(self):
		"""carrier commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_carrier'):
			from .Pswitched_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	def initiate(self) -> None:
		"""SCPI: INITiate:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: driver.ber.pswitched.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:GSM:SIGNaling<Instance>:BER:PSWitched')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: driver.ber.pswitched.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:GSM:SIGNaling<Instance>:BER:PSWitched')

	def stop(self) -> None:
		"""SCPI: STOP:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: driver.ber.pswitched.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:GSM:SIGNaling<Instance>:BER:PSWitched')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: driver.ber.pswitched.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:GSM:SIGNaling<Instance>:BER:PSWitched')

	def abort(self) -> None:
		"""SCPI: ABORt:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: driver.ber.pswitched.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:GSM:SIGNaling<Instance>:BER:PSWitched')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: driver.ber.pswitched.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:GSM:SIGNaling<Instance>:BER:PSWitched')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Frames: int: Number of already transmitted blocks Range: 0 to 500E+3
			- Ber: float: BER Range: 0 % to 100 %, Unit: %
			- Dbler: float: DBLER Range: 0 % to 100 %, Unit: %
			- Usf_Bler: float: USF BLER Range: 0 % to 100 %, Unit: %
			- False_Usf_Detect: float: False USF BLER Range: 0 % to 100 %, Unit: %
			- Crc_Errors: float: CRC errors Range: 0 to 500E+3
			- Non_Assigned_Usf: int: Number of USFs in data blocks not assigned to the MS Range: 0 to 500E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Frames'),
			ArgStruct.scalar_float('Ber'),
			ArgStruct.scalar_float('Dbler'),
			ArgStruct.scalar_float('Usf_Bler'),
			ArgStruct.scalar_float('False_Usf_Detect'),
			ArgStruct.scalar_float('Crc_Errors'),
			ArgStruct.scalar_int('Non_Assigned_Usf')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Frames: int = None
			self.Ber: float = None
			self.Dbler: float = None
			self.Usf_Bler: float = None
			self.False_Usf_Detect: float = None
			self.Crc_Errors: float = None
			self.Non_Assigned_Usf: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: value: ResultData = driver.ber.pswitched.read() \n
		Returns the results of the BER PS measurement over all carriers. For the details of the results, see 'BER PS Measurement'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:SIGNaling<Instance>:BER:PSWitched?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: value: ResultData = driver.ber.pswitched.fetch() \n
		Returns the results of the BER PS measurement over all carriers. For the details of the results, see 'BER PS Measurement'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:SIGNaling<Instance>:BER:PSWitched?', self.__class__.ResultData())

	def clone(self) -> 'Pswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
