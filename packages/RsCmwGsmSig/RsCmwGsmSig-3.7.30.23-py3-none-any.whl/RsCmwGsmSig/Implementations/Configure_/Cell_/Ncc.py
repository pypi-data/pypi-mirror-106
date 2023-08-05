from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ncc:
	"""Ncc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ncc", core, parent)

	def get_permitted(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:NCC:PERMitted \n
		Snippet: value: int = driver.configure.cell.ncc.get_permitted() \n
		Specifies the neighbor cell by its network color code (NCC) that the MS is allowed to measure. \n
			:return: ncc_permitted: Range: 0 to 255
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:NCC:PERMitted?')
		return Conversions.str_to_int(response)

	def set_permitted(self, ncc_permitted: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:NCC:PERMitted \n
		Snippet: driver.configure.cell.ncc.set_permitted(ncc_permitted = 1) \n
		Specifies the neighbor cell by its network color code (NCC) that the MS is allowed to measure. \n
			:param ncc_permitted: Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(ncc_permitted)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:NCC:PERMitted {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:NCC \n
		Snippet: value: int = driver.configure.cell.ncc.get_value() \n
		Defines the network color code of the simulated radio network. \n
			:return: ncc: Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:NCC?')
		return Conversions.str_to_int(response)

	def set_value(self, ncc: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:NCC \n
		Snippet: driver.configure.cell.ncc.set_value(ncc = 1) \n
		Defines the network color code of the simulated radio network. \n
			:param ncc: Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(ncc)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:NCC {param}')
