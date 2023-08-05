from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cperformance:
	"""Cperformance commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cperformance", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CPERformance:TOUT \n
		Snippet: value: float = driver.configure.cperformance.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CPERformance:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CPERformance:TOUT \n
		Snippet: driver.configure.cperformance.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CPERformance:TOUT {param}')

	def get_tlevel(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CPERformance:TLEVel \n
		Snippet: value: float = driver.configure.cperformance.get_tlevel() \n
		Target level reported to the MS during CMR performance test. \n
			:return: target_level: Range: Depending on RF connector (-130 dBm to 0 dBm for RFx COM) ; please also notice the ranges quoted in the data sheet. , Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CPERformance:TLEVel?')
		return Conversions.str_to_float(response)

	def set_tlevel(self, target_level: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CPERformance:TLEVel \n
		Snippet: driver.configure.cperformance.set_tlevel(target_level = 1.0) \n
		Target level reported to the MS during CMR performance test. \n
			:param target_level: Range: Depending on RF connector (-130 dBm to 0 dBm for RFx COM) ; please also notice the ranges quoted in the data sheet. , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(target_level)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CPERformance:TLEVel {param}')
