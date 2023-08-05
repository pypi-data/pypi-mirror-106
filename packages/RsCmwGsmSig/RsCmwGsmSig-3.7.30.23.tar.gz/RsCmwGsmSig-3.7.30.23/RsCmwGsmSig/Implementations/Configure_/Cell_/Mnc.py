from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mnc:
	"""Mnc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mnc", core, parent)

	# noinspection PyTypeChecker
	def get_digits(self) -> enums.DigitsCount:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:MNC:DIGits \n
		Snippet: value: enums.DigitsCount = driver.configure.cell.mnc.get_digits() \n
		Defines the number of digits of the mobile network code (MNC) . \n
			:return: no_digits: TWO | THRee Two- or three-digit MNC
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:MNC:DIGits?')
		return Conversions.str_to_scalar_enum(response, enums.DigitsCount)

	def set_digits(self, no_digits: enums.DigitsCount) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:MNC:DIGits \n
		Snippet: driver.configure.cell.mnc.set_digits(no_digits = enums.DigitsCount.THRee) \n
		Defines the number of digits of the mobile network code (MNC) . \n
			:param no_digits: TWO | THRee Two- or three-digit MNC
		"""
		param = Conversions.enum_scalar_to_str(no_digits, enums.DigitsCount)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:MNC:DIGits {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:MNC \n
		Snippet: value: int = driver.configure.cell.mnc.get_value() \n
		Defines the mobile network code of the simulated radio network. \n
			:return: mnc: Range: 0 to 99 / 999 (two- or three-digit MNC)
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:MNC?')
		return Conversions.str_to_int(response)

	def set_value(self, mnc: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:MNC \n
		Snippet: driver.configure.cell.mnc.set_value(mnc = 1) \n
		Defines the mobile network code of the simulated radio network. \n
			:param mnc: Range: 0 to 99 / 999 (two- or three-digit MNC)
		"""
		param = Conversions.decimal_value_to_str(mnc)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:MNC {param}')
