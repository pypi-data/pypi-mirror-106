from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

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
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CSWitched:CREQuest \n
		Snippet: value: CrequestStruct = driver.configure.cell.cswitched.get_crequest() \n
		Specifies the handling of the MS originating CS/PS connection request. \n
			:return: structure: for return value, see the help for CrequestStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:CSWitched:CREQuest?', self.__class__.CrequestStruct())

	def set_crequest(self, value: CrequestStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CSWitched:CREQuest \n
		Snippet: driver.configure.cell.cswitched.set_crequest(value = CrequestStruct()) \n
		Specifies the handling of the MS originating CS/PS connection request. \n
			:param value: see the help for CrequestStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:CSWitched:CREQuest', value)

	def get_iar_timer(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CSWitched:IARTimer \n
		Snippet: value: int or bool = driver.configure.cell.cswitched.get_iar_timer() \n
		Sets the immediate assignment reject timers for CS (T3122) / PS (T3142) . \n
			:return: value: Range: 0 s to 255 s , Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:CSWitched:IARTimer?')
		return Conversions.str_to_int_or_bool(response)

	def set_iar_timer(self, value: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CSWitched:IARTimer \n
		Snippet: driver.configure.cell.cswitched.set_iar_timer(value = 1) \n
		Sets the immediate assignment reject timers for CS (T3122) / PS (T3142) . \n
			:param value: Range: 0 s to 255 s , Unit: s
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:CSWitched:IARTimer {param}')
