from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Cswitched_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def initiate(self) -> None:
		"""SCPI: INITiate:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: driver.ber.cswitched.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:GSM:SIGNaling<Instance>:BER:CSWitched')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: driver.ber.cswitched.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:GSM:SIGNaling<Instance>:BER:CSWitched')

	def stop(self) -> None:
		"""SCPI: STOP:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: driver.ber.cswitched.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:GSM:SIGNaling<Instance>:BER:CSWitched')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: driver.ber.cswitched.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:GSM:SIGNaling<Instance>:BER:CSWitched')

	def abort(self) -> None:
		"""SCPI: ABORt:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: driver.ber.cswitched.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:GSM:SIGNaling<Instance>:BER:CSWitched')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: driver.ber.cswitched.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:GSM:SIGNaling<Instance>:BER:CSWitched')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Frames: int: Number of already transmitted bursts, blocks or frames Range: 0 to 500E+3
			- Ber: float: BER result (modes: burst-by-burst, mean BEP, signal quality) Range: 0 % to 100 %, Unit: %
			- Crc_Errors: int: Number of failed CRC checks (modes: BER, RBER/FER, RBER/UFR, BFI) Range: 0 to 500E+3
			- Class_Ii: float: BER result for class II bits (BER mode) RBER result for class II bits (modes: RBER/FER, RBER/UFR) Range: 0 % to 100 %, Unit: %
			- Class_Ib: float: BER result for class Ib bits (BER mode) RBER result for class Ib bits (modes: RBER/FER, RBER/UFR) Range: 0 % to 100 %, Unit: %
			- Fer: float: FER result (modes: RBER/FER, FER FACCH, FER SACCH, AMR inband FER) UFR result (RBER/UFR mode) Range: 0 % to 100 %, Unit: %
			- L_2_Frames_Rep: float: Number of repeated L2 frames (FER FACCH mode) Range: 0 to 500E+3
			- Error_Events: float: Number of error events (FER SACCH mode) Range: 0 to 500E+3
			- Number_Sid_Frames: int: Number of already transmitted silence insertion descriptor (SID) frames (BFI mode) Range: 0 to 500E+3
			- Sid_Frame_Err_Rate: float: SID frame error rate (BFI mode) Range: 0 % to 100 %, Unit: %
			- False_Bfi_Rate: float: False BFI rate (BFI mode) Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Frames'),
			ArgStruct.scalar_float('Ber'),
			ArgStruct.scalar_int('Crc_Errors'),
			ArgStruct.scalar_float('Class_Ii'),
			ArgStruct.scalar_float('Class_Ib'),
			ArgStruct.scalar_float('Fer'),
			ArgStruct.scalar_float('L_2_Frames_Rep'),
			ArgStruct.scalar_float('Error_Events'),
			ArgStruct.scalar_int('Number_Sid_Frames'),
			ArgStruct.scalar_float('Sid_Frame_Err_Rate'),
			ArgStruct.scalar_float('False_Bfi_Rate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frames: int = None
			self.Ber: float = None
			self.Crc_Errors: int = None
			self.Class_Ii: float = None
			self.Class_Ib: float = None
			self.Fer: float = None
			self.L_2_Frames_Rep: float = None
			self.Error_Events: float = None
			self.Number_Sid_Frames: int = None
			self.Sid_Frame_Err_Rate: float = None
			self.False_Bfi_Rate: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: value: ResultData = driver.ber.cswitched.read() \n
		Returns the results of the BER CS measurement. As indicated in the parameter descriptions below, each measure mode
		provides valid results for a subset of the parameters only. For the other parameters NCAP is returned.
		For details concerning measure modes and results, see 'BER CS Measurement'. \n
		Use RsCmwGsmSig.reliability.last_value to read the updated reliability indicator. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:SIGNaling<Instance>:BER:CSWitched?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: value: ResultData = driver.ber.cswitched.fetch() \n
		Returns the results of the BER CS measurement. As indicated in the parameter descriptions below, each measure mode
		provides valid results for a subset of the parameters only. For the other parameters NCAP is returned.
		For details concerning measure modes and results, see 'BER CS Measurement'. \n
		Use RsCmwGsmSig.reliability.last_value to read the updated reliability indicator. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:SIGNaling<Instance>:BER:CSWitched?', self.__class__.ResultData())

	def clone(self) -> 'Cswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
