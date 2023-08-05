from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 11 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_limit'):
			from .Cswitched_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:TOUT \n
		Snippet: value: float = driver.configure.ber.cswitched.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:TOUT \n
		Snippet: driver.configure.ber.cswitched.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:TOUT {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.BerCsMeasMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:MMODe \n
		Snippet: value: enums.BerCsMeasMode = driver.configure.ber.cswitched.get_mmode() \n
		Selects the measurement mode of the BER CS measurement. For a detailed description of the modes, see 'BER CS Measurement'. \n
			:return: mode: BBBurst | BER | RFER | FFACch | FSACch | RUFR | AIFer | MBEP | SQUality | BFI BBBurst: 'Burst by Burst' mode BER: 'BER' mode RFER: 'RBER/FER' mode FFACch: 'FER FACCH' mode FSACch: 'FER SACCH' mode RUFR: 'RBER/UFR' mode AIFer: 'AMR Inband FER' mode MBEP: 'Mean BEP' mode SQUality: 'Signal Quality' mode BFI: 'Bad Frame Indication' mode
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.BerCsMeasMode)

	def set_mmode(self, mode: enums.BerCsMeasMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:MMODe \n
		Snippet: driver.configure.ber.cswitched.set_mmode(mode = enums.BerCsMeasMode.AIFer) \n
		Selects the measurement mode of the BER CS measurement. For a detailed description of the modes, see 'BER CS Measurement'. \n
			:param mode: BBBurst | BER | RFER | FFACch | FSACch | RUFR | AIFer | MBEP | SQUality | BFI BBBurst: 'Burst by Burst' mode BER: 'BER' mode RFER: 'RBER/FER' mode FFACch: 'FER FACCH' mode FSACch: 'FER SACCH' mode RUFR: 'RBER/UFR' mode AIFer: 'AMR Inband FER' mode MBEP: 'Mean BEP' mode SQUality: 'Signal Quality' mode BFI: 'Bad Frame Indication' mode
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.BerCsMeasMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:MMODe {param}')

	def get_scondition(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:SCONdition \n
		Snippet: value: int = driver.configure.ber.cswitched.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. When the measurement is stopped, it
		reaches the RDY state. \n
			:return: condition: NONE | FLIMit NONE: Continue measurement irrespective of the limit check FLIMit: Stop measurement on first limit failure
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:SCONdition?')
		return Conversions.str_to_int(response)

	def set_scondition(self, condition: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:SCONdition \n
		Snippet: driver.configure.ber.cswitched.set_scondition(condition = 1) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. When the measurement is stopped, it
		reaches the RDY state. \n
			:param condition: NONE | FLIMit NONE: Continue measurement irrespective of the limit check FLIMit: Stop measurement on first limit failure
		"""
		param = Conversions.decimal_value_to_str(condition)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:SCONdition {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:SCOunt \n
		Snippet: value: int = driver.configure.ber.cswitched.get_scount() \n
		Defines the number of bursts or speech frames to be transmitted per measurement cycle (statistics cycle) . \n
			:return: frames: Range: 1 to 500E+3
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, frames: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:SCOunt \n
		Snippet: driver.configure.ber.cswitched.set_scount(frames = 1) \n
		Defines the number of bursts or speech frames to be transmitted per measurement cycle (statistics cycle) . \n
			:param frames: Range: 1 to 500E+3
		"""
		param = Conversions.decimal_value_to_str(frames)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:SCOunt {param}')

	# noinspection PyTypeChecker
	class RtDelayStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Mode: enums.AutoManualMode: AUTO | MANual AUTO: number of bursts set automatically MAN: number of bursts specified manually
			- Bursts: int: Round-trip delay Range: 0 to 24, Unit: burst"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mode', enums.AutoManualMode),
			ArgStruct.scalar_int('Bursts')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mode: enums.AutoManualMode = None
			self.Bursts: int = None

	# noinspection PyTypeChecker
	def get_rt_delay(self) -> RtDelayStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:RTDelay \n
		Snippet: value: RtDelayStruct = driver.configure.ber.cswitched.get_rt_delay() \n
		Specifies the number of bursts used as the round-trip delay. \n
			:return: structure: for return value, see the help for RtDelayStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:RTDelay?', self.__class__.RtDelayStruct())

	def set_rt_delay(self, value: RtDelayStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:RTDelay \n
		Snippet: driver.configure.ber.cswitched.set_rt_delay(value = RtDelayStruct()) \n
		Specifies the number of bursts used as the round-trip delay. \n
			:param value: see the help for RtDelayStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:RTDelay', value)

	def clone(self) -> 'Cswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
