from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 7 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_limit'):
			from .Pswitched_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:TOUT \n
		Snippet: value: float = driver.configure.ber.pswitched.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:TOUT \n
		Snippet: driver.configure.ber.pswitched.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:TOUT {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.BerPsMeasMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:MMODe \n
		Snippet: value: enums.BerPsMeasMode = driver.configure.ber.pswitched.get_mmode() \n
		Defines the measurement mode for BER PS measurements. \n
			:return: mode: BDBLer | MBEP | UBONly BDBLer: BER/DBLER MBEP: mean BEP UBONly: USF BLER only
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.BerPsMeasMode)

	def set_mmode(self, mode: enums.BerPsMeasMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:MMODe \n
		Snippet: driver.configure.ber.pswitched.set_mmode(mode = enums.BerPsMeasMode.BDBLer) \n
		Defines the measurement mode for BER PS measurements. \n
			:param mode: BDBLer | MBEP | UBONly BDBLer: BER/DBLER MBEP: mean BEP UBONly: USF BLER only
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.BerPsMeasMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:MMODe {param}')

	def get_scondition(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:SCONdition \n
		Snippet: value: int = driver.configure.ber.pswitched.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. When the measurement is stopped, it
		reaches the RDY state. \n
			:return: condition: NONE | FLIMit NONE: Continue measurement irrespective of the limit check FLIMit: Stop measurement on first limit failure
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:SCONdition?')
		return Conversions.str_to_int(response)

	def set_scondition(self, condition: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:SCONdition \n
		Snippet: driver.configure.ber.pswitched.set_scondition(condition = 1) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. When the measurement is stopped, it
		reaches the RDY state. \n
			:param condition: NONE | FLIMit NONE: Continue measurement irrespective of the limit check FLIMit: Stop measurement on first limit failure
		"""
		param = Conversions.decimal_value_to_str(condition)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:SCONdition {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:SCOunt \n
		Snippet: value: int = driver.configure.ber.pswitched.get_scount() \n
		Defines the number of RLC data blocks or radio blocks to be transmitted per measurement cycle (statistics cycle) . \n
			:return: frames: Range: 1 to 500E+3
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, frames: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:SCOunt \n
		Snippet: driver.configure.ber.pswitched.set_scount(frames = 1) \n
		Defines the number of RLC data blocks or radio blocks to be transmitted per measurement cycle (statistics cycle) . \n
			:param frames: Range: 1 to 500E+3
		"""
		param = Conversions.decimal_value_to_str(frames)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:SCOunt {param}')

	def clone(self) -> 'Pswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
