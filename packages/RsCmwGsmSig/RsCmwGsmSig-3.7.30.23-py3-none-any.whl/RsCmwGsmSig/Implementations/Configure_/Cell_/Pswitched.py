from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 9 total commands, 0 Sub-groups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	# noinspection PyTypeChecker
	def get_pdp_context(self) -> enums.ReactionMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:PDPContext \n
		Snippet: value: enums.ReactionMode = driver.configure.cell.pswitched.get_pdp_context() \n
		Defines how the R&S CMW reacts to an ACTIVATE PDP CONTEXT REQUEST sent by the MS. \n
			:return: mode: REJect | ACCept
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:PDPContext?')
		return Conversions.str_to_scalar_enum(response, enums.ReactionMode)

	def set_pdp_context(self, mode: enums.ReactionMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:PDPContext \n
		Snippet: driver.configure.cell.pswitched.set_pdp_context(mode = enums.ReactionMode.ACCept) \n
		Defines how the R&S CMW reacts to an ACTIVATE PDP CONTEXT REQUEST sent by the MS. \n
			:param mode: REJect | ACCept
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ReactionMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:PDPContext {param}')

	def get_tavgtw(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:TAVGtw \n
		Snippet: value: int = driver.configure.cell.pswitched.get_tavgtw() \n
		Specifies the signal level filter period for power control. The same value is used for TAVG_T and TAVG_W. \n
			:return: value: Range: 0 to 25
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:TAVGtw?')
		return Conversions.str_to_int(response)

	def set_tavgtw(self, value: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:TAVGtw \n
		Snippet: driver.configure.cell.pswitched.set_tavgtw(value = 1) \n
		Specifies the signal level filter period for power control. The same value is used for TAVG_T and TAVG_W. \n
			:param value: Range: 0 to 25
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:TAVGtw {param}')

	def get_bperiod(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:BPERiod \n
		Snippet: value: int = driver.configure.cell.pswitched.get_bperiod() \n
		Specifies the BEP_PERIOD defined in 3GPP TS 45.008. \n
			:return: value: Range: 0 to 10
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:BPERiod?')
		return Conversions.str_to_int(response)

	def set_bperiod(self, value: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:BPERiod \n
		Snippet: driver.configure.cell.pswitched.set_bperiod(value = 1) \n
		Specifies the BEP_PERIOD defined in 3GPP TS 45.008. \n
			:param value: Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:BPERiod {param}')

	# noinspection PyTypeChecker
	def get_pcm_channel(self) -> enums.PcmChannel:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:PCMChannel \n
		Snippet: value: enums.PcmChannel = driver.configure.cell.pswitched.get_pcm_channel() \n
		Selects the channel type that the mobile uses to determine the received signal strength and quality. \n
			:return: channel: BCCH | PDCH
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:PCMChannel?')
		return Conversions.str_to_scalar_enum(response, enums.PcmChannel)

	def set_pcm_channel(self, channel: enums.PcmChannel) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:PCMChannel \n
		Snippet: driver.configure.cell.pswitched.set_pcm_channel(channel = enums.PcmChannel.BCCH) \n
		Selects the channel type that the mobile uses to determine the received signal strength and quality. \n
			:param channel: BCCH | PDCH
		"""
		param = Conversions.enum_scalar_to_str(channel, enums.PcmChannel)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:PCMChannel {param}')

	# noinspection PyTypeChecker
	class CrequestStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Connect_Request: enums.ConnectRequest: ACCept | REJect | IGNore ACCept: accept connection REJect: reject connection IGNore: ignore first attempt, AcceptAfter parameter defines further handling
			- Accept_After: enums.AcceptAfter: AA1 | AA2 | AA3 | AA4 | AA5 | AA6 | AA7 | IALL AA1 to AA7: accept after burst 1 to 7 IALL: ignore all"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Connect_Request', enums.ConnectRequest),
			ArgStruct.scalar_enum('Accept_After', enums.AcceptAfter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Connect_Request: enums.ConnectRequest = None
			self.Accept_After: enums.AcceptAfter = None

	# noinspection PyTypeChecker
	def get_crequest(self) -> CrequestStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:CREQuest \n
		Snippet: value: CrequestStruct = driver.configure.cell.pswitched.get_crequest() \n
		Specifies the handling of the MS originating CS/PS connection request. \n
			:return: structure: for return value, see the help for CrequestStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:CREQuest?', self.__class__.CrequestStruct())

	def set_crequest(self, value: CrequestStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:CREQuest \n
		Snippet: driver.configure.cell.pswitched.set_crequest(value = CrequestStruct()) \n
		Specifies the handling of the MS originating CS/PS connection request. \n
			:param value: see the help for CrequestStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:CREQuest', value)

	def get_neutbf(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:NEUTbf \n
		Snippet: value: bool = driver.configure.cell.pswitched.get_neutbf() \n
		Indicates whether the network supports the extended uplink TBF mode. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:NEUTbf?')
		return Conversions.str_to_bool(response)

	def set_neutbf(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:NEUTbf \n
		Snippet: driver.configure.cell.pswitched.set_neutbf(enable = False) \n
		Indicates whether the network supports the extended uplink TBF mode. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:NEUTbf {param}')

	def get_euno_data(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:EUNodata \n
		Snippet: value: bool = driver.configure.cell.pswitched.get_euno_data() \n
		Enables / disables MS operation in an EXT_UTBF_NODATA mode, where the MS cannot transmit a dummy block to a network. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:EUNodata?')
		return Conversions.str_to_bool(response)

	def set_euno_data(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:EUNodata \n
		Snippet: driver.configure.cell.pswitched.set_euno_data(enable = False) \n
		Enables / disables MS operation in an EXT_UTBF_NODATA mode, where the MS cannot transmit a dummy block to a network. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:EUNodata {param}')

	def get_iar_timer(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:IARTimer \n
		Snippet: value: int or bool = driver.configure.cell.pswitched.get_iar_timer() \n
		Sets the immediate assignment reject timers for CS (T3122) / PS (T3142) . \n
			:return: value: Range: 0 s to 255 s , Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:IARTimer?')
		return Conversions.str_to_int_or_bool(response)

	def set_iar_timer(self, value: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:IARTimer \n
		Snippet: driver.configure.cell.pswitched.set_iar_timer(value = 1) \n
		Sets the immediate assignment reject timers for CS (T3122) / PS (T3142) . \n
			:param value: Range: 0 s to 255 s , Unit: s
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:IARTimer {param}')

	def get_tr_timer(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:TRTimer \n
		Snippet: value: int = driver.configure.cell.pswitched.get_tr_timer() \n
		Defines the TBF release timer for PS. \n
			:return: value: For mapping of values and timer durations in ms, see the table below. Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:TRTimer?')
		return Conversions.str_to_int(response)

	def set_tr_timer(self, value: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:TRTimer \n
		Snippet: driver.configure.cell.pswitched.set_tr_timer(value = 1) \n
		Defines the TBF release timer for PS. \n
			:param value: For mapping of values and timer durations in ms, see the table below. Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSWitched:TRTimer {param}')
