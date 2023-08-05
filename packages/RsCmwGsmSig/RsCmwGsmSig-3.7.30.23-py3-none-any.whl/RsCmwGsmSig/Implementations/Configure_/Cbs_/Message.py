from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Message:
	"""Message commands group definition. 8 total commands, 0 Sub-groups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("message", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:ENABle \n
		Snippet: value: bool = driver.configure.cbs.message.get_enable() \n
		Enables the particular CB message. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:ENABle \n
		Snippet: driver.configure.cbs.message.set_enable(enable = False) \n
		Enables the particular CB message. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:ENABle {param}')

	def get_id(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:ID \n
		Snippet: value: int = driver.configure.cbs.message.get_id() \n
		Identifies source/type of a CB message. Edit this parameter for user-defined settings. Also, hexadecimal values are
		displayed for information. \n
			:return: idn: Range: 0 to 65.535E+3
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:ID?')
		return Conversions.str_to_int(response)

	def set_id(self, idn: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:ID \n
		Snippet: driver.configure.cbs.message.set_id(idn = 1) \n
		Identifies source/type of a CB message. Edit this parameter for user-defined settings. Also, hexadecimal values are
		displayed for information. \n
			:param idn: Range: 0 to 65.535E+3
		"""
		param = Conversions.decimal_value_to_str(idn)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:ID {param}')

	# noinspection PyTypeChecker
	def get_id_type(self) -> enums.MsgIdSeverity:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:IDTYpe \n
		Snippet: value: enums.MsgIdSeverity = driver.configure.cbs.message.get_id_type() \n
		Specifies the severity of the message ID. \n
			:return: type_py: UDEFined | APResidentia | AEXTreme | ASEVere | AAMBer UDEFined: user defined APResidentia: presidential level alerts (IDs 4370 and 4383) AEXTreme: extreme alerts (IDs 4371 to 4372 and 4384 to 4385) ASEVere: severe alerts (IDs 4373 to 4378 and 4386 to 4391) AAMBer: amber alerts (IDs 4379 and 4392)
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:IDTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.MsgIdSeverity)

	def set_id_type(self, type_py: enums.MsgIdSeverity) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:IDTYpe \n
		Snippet: driver.configure.cbs.message.set_id_type(type_py = enums.MsgIdSeverity.AAMBer) \n
		Specifies the severity of the message ID. \n
			:param type_py: UDEFined | APResidentia | AEXTreme | ASEVere | AAMBer UDEFined: user defined APResidentia: presidential level alerts (IDs 4370 and 4383) AEXTreme: extreme alerts (IDs 4371 to 4372 and 4384 to 4385) ASEVere: severe alerts (IDs 4373 to 4378 and 4386 to 4391) AAMBer: amber alerts (IDs 4379 and 4392)
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.MsgIdSeverity)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:IDTYpe {param}')

	# noinspection PyTypeChecker
	class SerialStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Geo_Scope: enums.GeographicScope: CIMMediate | PLMN | LOCation | CNORmal The geographical area over which the message code is unique. CIMMediate: cell-wide, immediate display PLMN: PLMN-wide, normal display LOCation: location area-wide, normal display CNORmal: cell-wide, normal display
			- Message_Code: int: CB message identification Range: 0 to 1023
			- Auto_Incr: bool: OFF | ON OFF: no increase of UpdateNumber upon a CB message change ON: increase UpdateNumber automatically upon a CB message change
			- Update_Number: int: Indication of a content change of the same CB message Range: 0 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Geo_Scope', enums.GeographicScope),
			ArgStruct.scalar_int('Message_Code'),
			ArgStruct.scalar_bool('Auto_Incr'),
			ArgStruct.scalar_int('Update_Number')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Geo_Scope: enums.GeographicScope = None
			self.Message_Code: int = None
			self.Auto_Incr: bool = None
			self.Update_Number: int = None

	# noinspection PyTypeChecker
	def get_serial(self) -> SerialStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:SERial \n
		Snippet: value: SerialStruct = driver.configure.cbs.message.get_serial() \n
		Specifies the unique CB message identification. \n
			:return: structure: for return value, see the help for SerialStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:SERial?', self.__class__.SerialStruct())

	def set_serial(self, value: SerialStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:SERial \n
		Snippet: driver.configure.cbs.message.set_serial(value = SerialStruct()) \n
		Specifies the unique CB message identification. \n
			:param value: see the help for SerialStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:SERial', value)

	def get_dc_scheme(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:DCSCheme \n
		Snippet: value: int = driver.configure.cbs.message.get_dc_scheme() \n
		Specifies language using the GSM 7-bit default alphabet. \n
			:return: data_code_scheme: 0: coding group 0000, language 0001 (English) 1: coding group 0001, language 0000 (GSM 7-bit default alphabet; message preceded by language indication) Range: 0 to 1
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:DCSCheme?')
		return Conversions.str_to_int(response)

	def set_dc_scheme(self, data_code_scheme: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:DCSCheme \n
		Snippet: driver.configure.cbs.message.set_dc_scheme(data_code_scheme = 1) \n
		Specifies language using the GSM 7-bit default alphabet. \n
			:param data_code_scheme: 0: coding group 0000, language 0001 (English) 1: coding group 0001, language 0000 (GSM 7-bit default alphabet; message preceded by language indication) Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(data_code_scheme)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:DCSCheme {param}')

	# noinspection PyTypeChecker
	def get_category(self) -> enums.Priority:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:CATegory \n
		Snippet: value: enums.Priority = driver.configure.cbs.message.get_category() \n
		No command help available \n
			:return: category: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:CATegory?')
		return Conversions.str_to_scalar_enum(response, enums.Priority)

	def set_category(self, category: enums.Priority) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:CATegory \n
		Snippet: driver.configure.cbs.message.set_category(category = enums.Priority.BACKground) \n
		No command help available \n
			:param category: No help available
		"""
		param = Conversions.enum_scalar_to_str(category, enums.Priority)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:CATegory {param}')

	def get_data(self) -> str:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:DATA \n
		Snippet: value: str = driver.configure.cbs.message.get_data() \n
		Defines the CB message text. \n
			:return: data: Up to 160 characters
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:DATA?')
		return trim_str_response(response)

	def set_data(self, data: str) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:DATA \n
		Snippet: driver.configure.cbs.message.set_data(data = '1') \n
		Defines the CB message text. \n
			:param data: Up to 160 characters
		"""
		param = Conversions.value_to_quoted_str(data)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:DATA {param}')

	def get_period(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:PERiod \n
		Snippet: value: int = driver.configure.cbs.message.get_period() \n
		No command help available \n
			:return: interval: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:PERiod?')
		return Conversions.str_to_int(response)

	def set_period(self, interval: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:MESSage:PERiod \n
		Snippet: driver.configure.cbs.message.set_period(interval = 1) \n
		No command help available \n
			:param interval: No help available
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CBS:MESSage:PERiod {param}')
