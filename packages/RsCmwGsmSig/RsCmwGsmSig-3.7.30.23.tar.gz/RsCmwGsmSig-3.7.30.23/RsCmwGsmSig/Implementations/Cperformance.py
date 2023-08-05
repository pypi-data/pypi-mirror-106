from typing import List

from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ..Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cperformance:
	"""Cperformance commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cperformance", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Cperformance_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def stop(self) -> None:
		"""SCPI: STOP:GSM:SIGNaling<instance>:CPERformance \n
		Snippet: driver.cperformance.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:GSM:SIGNaling<Instance>:CPERformance')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:GSM:SIGNaling<instance>:CPERformance \n
		Snippet: driver.cperformance.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:GSM:SIGNaling<Instance>:CPERformance')

	def abort(self) -> None:
		"""SCPI: ABORt:GSM:SIGNaling<instance>:CPERformance \n
		Snippet: driver.cperformance.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:GSM:SIGNaling<Instance>:CPERformance')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:GSM:SIGNaling<instance>:CPERformance \n
		Snippet: driver.cperformance.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:GSM:SIGNaling<Instance>:CPERformance')

	def initiate(self) -> None:
		"""SCPI: INITiate:GSM:SIGNaling<instance>:CPERformance \n
		Snippet: driver.cperformance.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:GSM:SIGNaling<Instance>:CPERformance')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:GSM:SIGNaling<instance>:CPERformance \n
		Snippet: driver.cperformance.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:GSM:SIGNaling<Instance>:CPERformance')

	def read(self) -> List[int]:
		"""SCPI: READ:GSM:SIGNaling<instance>:CPERformance \n
		Snippet: value: List[int] = driver.cperformance.read() \n
		Returns all results of the signaling CMR performance measurement. \n
		Use RsCmwGsmSig.reliability.last_value to read the updated reliability indicator. \n
			:return: result: Used codec mode number 9 values: initial value and one value per 40 ms Range: 1 to 4"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'READ:GSM:SIGNaling<Instance>:CPERformance?', suppressed)
		return response

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:GSM:SIGNaling<instance>:CPERformance \n
		Snippet: value: List[int] = driver.cperformance.fetch() \n
		Returns all results of the signaling CMR performance measurement. \n
		Use RsCmwGsmSig.reliability.last_value to read the updated reliability indicator. \n
			:return: result: Used codec mode number 9 values: initial value and one value per 40 ms Range: 1 to 4"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:GSM:SIGNaling<Instance>:CPERformance?', suppressed)
		return response

	def clone(self) -> 'Cperformance':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cperformance(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
