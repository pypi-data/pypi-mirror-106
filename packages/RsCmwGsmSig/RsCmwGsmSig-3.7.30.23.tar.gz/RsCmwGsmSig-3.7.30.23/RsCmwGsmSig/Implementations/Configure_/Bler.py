from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bler:
	"""Bler commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bler", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BLER:TOUT \n
		Snippet: value: float = driver.configure.bler.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BLER:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BLER:TOUT \n
		Snippet: driver.configure.bler.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BLER:TOUT {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BLER:SCOunt \n
		Snippet: value: int = driver.configure.bler.get_scount() \n
		Defines the number of RLC data blocks to be transmitted per measurement cycle (statistics cycle) . \n
			:return: rlc_block_count: Range: 1 to 10E+6
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BLER:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, rlc_block_count: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BLER:SCOunt \n
		Snippet: driver.configure.bler.set_scount(rlc_block_count = 1) \n
		Defines the number of RLC data blocks to be transmitted per measurement cycle (statistics cycle) . \n
			:param rlc_block_count: Range: 1 to 10E+6
		"""
		param = Conversions.decimal_value_to_str(rlc_block_count)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BLER:SCOunt {param}')
