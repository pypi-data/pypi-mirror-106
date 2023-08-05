from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 8 total commands, 1 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("time", core, parent)

	@property
	def snow(self):
		"""snow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snow'):
			from .Time_.Snow import Snow
			self._snow = Snow(self._core, self._base)
		return self._snow

	# noinspection PyTypeChecker
	def get_tsource(self) -> enums.SourceTime:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:TSOurce \n
		Snippet: value: enums.SourceTime = driver.configure.cell.time.get_tsource() \n
		Selects the date and time source.
			INTRO_CMD_HELP: The time source DATE is configured via the following commands: \n
			- method RsCmwGsmSig.Configure.Cell.Time.date
			- method RsCmwGsmSig.Configure.Cell.Time.time
			- method RsCmwGsmSig.Configure.Cell.Time.daylightSavingTime
			- method RsCmwGsmSig.Configure.Cell.Time.ltzOffset \n
			:return: source_time: CMWTime | DATE CMWTime: Windows date and time DATE: 'Date / Time' specified via remote commands
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:TSOurce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceTime)

	def set_tsource(self, source_time: enums.SourceTime) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:TSOurce \n
		Snippet: driver.configure.cell.time.set_tsource(source_time = enums.SourceTime.CMWTime) \n
		Selects the date and time source.
			INTRO_CMD_HELP: The time source DATE is configured via the following commands: \n
			- method RsCmwGsmSig.Configure.Cell.Time.date
			- method RsCmwGsmSig.Configure.Cell.Time.time
			- method RsCmwGsmSig.Configure.Cell.Time.daylightSavingTime
			- method RsCmwGsmSig.Configure.Cell.Time.ltzOffset \n
			:param source_time: CMWTime | DATE CMWTime: Windows date and time DATE: 'Date / Time' specified via remote commands
		"""
		param = Conversions.enum_scalar_to_str(source_time, enums.SourceTime)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:TSOurce {param}')

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Day: int: Range: 1 to 31
			- Month: int: Range: 1 to 12
			- Year: int: Range: 2011 to 2099"""
		__meta_args_list = [
			ArgStruct.scalar_int('Day'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Year')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Day: int = None
			self.Month: int = None
			self.Year: int = None

	def get_date(self) -> DateStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:DATE \n
		Snippet: value: DateStruct = driver.configure.cell.time.get_date() \n
		Specifies the UTC date for the time source DATE (see method RsCmwGsmSig.Configure.Cell.Time.tsource) . \n
			:return: structure: for return value, see the help for DateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:DATE?', self.__class__.DateStruct())

	def set_date(self, value: DateStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:DATE \n
		Snippet: driver.configure.cell.time.set_date(value = DateStruct()) \n
		Specifies the UTC date for the time source DATE (see method RsCmwGsmSig.Configure.Cell.Time.tsource) . \n
			:param value: see the help for DateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:DATE', value)

	# noinspection PyTypeChecker
	class TimeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hour: int: Range: 0 to 23
			- Minute: int: Range: 0 to 59
			- Second: int: Range: 0 to 59"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_int('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None
			self.Second: int = None

	def get_time(self) -> TimeStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:TIME \n
		Snippet: value: TimeStruct = driver.configure.cell.time.get_time() \n
		Specifies the UTC time for the time source DATE (see method RsCmwGsmSig.Configure.Cell.Time.tsource) . \n
			:return: structure: for return value, see the help for TimeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:TIME?', self.__class__.TimeStruct())

	def set_time(self, value: TimeStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:TIME \n
		Snippet: driver.configure.cell.time.set_time(value = TimeStruct()) \n
		Specifies the UTC time for the time source DATE (see method RsCmwGsmSig.Configure.Cell.Time.tsource) . \n
			:param value: see the help for TimeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:TIME', value)

	# noinspection PyTypeChecker
	def get_daylight_saving_time(self) -> enums.DsTime:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:DSTime \n
		Snippet: value: enums.DsTime = driver.configure.cell.time.get_daylight_saving_time() \n
		Specifies a daylight saving time (DST) offset for the time source DATE (see method RsCmwGsmSig.Configure.Cell.Time.
		tsource) . \n
			:return: enable: P1H | P2H | ON | OFF P1H: +1h offset if DST is ON P2H: +2h offset if DST is ON Additional parameters OFF (ON) disables (enables) DST.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:DSTime?')
		return Conversions.str_to_scalar_enum(response, enums.DsTime)

	def set_daylight_saving_time(self, enable: enums.DsTime) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:DSTime \n
		Snippet: driver.configure.cell.time.set_daylight_saving_time(enable = enums.DsTime.OFF) \n
		Specifies a daylight saving time (DST) offset for the time source DATE (see method RsCmwGsmSig.Configure.Cell.Time.
		tsource) . \n
			:param enable: P1H | P2H | ON | OFF P1H: +1h offset if DST is ON P2H: +2h offset if DST is ON Additional parameters OFF (ON) disables (enables) DST.
		"""
		param = Conversions.enum_scalar_to_str(enable, enums.DsTime)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:DSTime {param}')

	def get_ltz_offset(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:TIME:LTZoffset \n
		Snippet: value: float = driver.configure.cell.time.get_ltz_offset() \n
		Specifies a time zone offset for the time source DATE (see method RsCmwGsmSig.Configure.Cell.Time.tsource) . \n
			:return: time_zone_offset: Range: -19.75 h to 19.75 h
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:LTZoffset?')
		return Conversions.str_to_float(response)

	def set_ltz_offset(self, time_zone_offset: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:TIME:LTZoffset \n
		Snippet: driver.configure.cell.time.set_ltz_offset(time_zone_offset = 1.0) \n
		Specifies a time zone offset for the time source DATE (see method RsCmwGsmSig.Configure.Cell.Time.tsource) . \n
			:param time_zone_offset: Range: -19.75 h to 19.75 h
		"""
		param = Conversions.decimal_value_to_str(time_zone_offset)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:LTZoffset {param}')

	def get_sattach(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SATTach \n
		Snippet: value: bool = driver.configure.cell.time.get_sattach() \n
		Enables the transfer of the date and time information to the MS at attach and location update. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SATTach?')
		return Conversions.str_to_bool(response)

	def set_sattach(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SATTach \n
		Snippet: driver.configure.cell.time.set_sattach(enable = False) \n
		Enables the transfer of the date and time information to the MS at attach and location update. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SATTach {param}')

	def get_snname(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:TIME:SNName \n
		Snippet: value: bool = driver.configure.cell.time.get_snname() \n
		If enabled, sends the full and short network name within date and time signaling to the MS. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SNName?')
		return Conversions.str_to_bool(response)

	def set_snname(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:TIME:SNName \n
		Snippet: driver.configure.cell.time.set_snname(enable = False) \n
		If enabled, sends the full and short network name within date and time signaling to the MS. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SNName {param}')

	def clone(self) -> 'Time':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Time(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
