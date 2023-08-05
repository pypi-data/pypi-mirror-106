from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Imsi:
	"""Imsi commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("imsi", core, parent)

	def get_filter_py(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IMSI:FILTer \n
		Snippet: value: bool = driver.configure.cell.imsi.get_filter_py() \n
		If enabled, the R&S CMW allows only the default IMSI to execute location update and attach. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:IMSI:FILTer?')
		return Conversions.str_to_bool(response)

	def set_filter_py(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IMSI:FILTer \n
		Snippet: driver.configure.cell.imsi.set_filter_py(enable = False) \n
		If enabled, the R&S CMW allows only the default IMSI to execute location update and attach. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:IMSI:FILTer {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Mcc: int: Range: 0 to 999
			- Mnc: int: Range: 01 to 99 (2-digit MNC) or 001 to 999 (3-digit MNC)
			- Msin: int: Range: 0 to 9999999999 (2-digit MNC) or 0 to 999999999 (3-digit MNC)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Mcc'),
			ArgStruct.scalar_int('Mnc'),
			ArgStruct.scalar_int('Msin')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mcc: int = None
			self.Mnc: int = None
			self.Msin: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IMSI \n
		Snippet: value: ValueStruct = driver.configure.cell.imsi.get_value() \n
		Defines the default IMSI which is used to set up the connection if the mobile does not initiate a location update.
		See also method RsCmwGsmSig.Configure.Cell.lupdate. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:IMSI?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IMSI \n
		Snippet: driver.configure.cell.imsi.set_value(value = ValueStruct()) \n
		Defines the default IMSI which is used to set up the connection if the mobile does not initiate a location update.
		See also method RsCmwGsmSig.Configure.Cell.lupdate. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:CELL:IMSI', value)
