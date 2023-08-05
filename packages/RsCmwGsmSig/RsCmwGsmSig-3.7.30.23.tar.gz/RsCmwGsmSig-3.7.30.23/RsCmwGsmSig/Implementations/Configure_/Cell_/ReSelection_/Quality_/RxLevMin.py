from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxLevMin:
	"""RxLevMin commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rxLevMin", core, parent)

	def get_eutran(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RESelection:QUALity:RXLevmin:EUTRan \n
		Snippet: value: int = driver.configure.cell.reSelection.quality.rxLevMin.get_eutran() \n
		Defines the minimum RX level at a UE antenna required for access to the LTE cell. This parameter is transmitted via BCCH. \n
			:return: qrxlevmin: Range: -140 dBm to -78 dBm
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:QUALity:RXLevmin:EUTRan?')
		return Conversions.str_to_int(response)

	def set_eutran(self, qrxlevmin: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RESelection:QUALity:RXLevmin:EUTRan \n
		Snippet: driver.configure.cell.reSelection.quality.rxLevMin.set_eutran(qrxlevmin = 1) \n
		Defines the minimum RX level at a UE antenna required for access to the LTE cell. This parameter is transmitted via BCCH. \n
			:param qrxlevmin: Range: -140 dBm to -78 dBm
		"""
		param = Conversions.decimal_value_to_str(qrxlevmin)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:QUALity:RXLevmin:EUTRan {param}')

	def get_utran(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RESelection:QUALity:RXLevmin:UTRan \n
		Snippet: value: int = driver.configure.cell.reSelection.quality.rxLevMin.get_utran() \n
		Defines the minimum RX level at a UE antenna required for access to the UMTS cell. This parameter is transmitted via BCCH. \n
			:return: qrxlevmin: Range: -119 dBm to -57 dBm
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:QUALity:RXLevmin:UTRan?')
		return Conversions.str_to_int(response)

	def set_utran(self, qrxlevmin: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RESelection:QUALity:RXLevmin:UTRan \n
		Snippet: driver.configure.cell.reSelection.quality.rxLevMin.set_utran(qrxlevmin = 1) \n
		Defines the minimum RX level at a UE antenna required for access to the UMTS cell. This parameter is transmitted via BCCH. \n
			:param qrxlevmin: Range: -119 dBm to -57 dBm
		"""
		param = Conversions.decimal_value_to_str(qrxlevmin)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:QUALity:RXLevmin:UTRan {param}')

	def get_access(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RESelection:QUALity:RXLevmin:ACCess \n
		Snippet: value: int = driver.configure.cell.reSelection.quality.rxLevMin.get_access() \n
		Defines the minimum RX level at an MS antenna required for access to the GSM cell. This parameter is transmitted via BCCH. \n
			:return: qrxlevmin: Range: -111 dBm to -48 dBm
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:QUALity:RXLevmin:ACCess?')
		return Conversions.str_to_int(response)

	def set_access(self, qrxlevmin: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RESelection:QUALity:RXLevmin:ACCess \n
		Snippet: driver.configure.cell.reSelection.quality.rxLevMin.set_access(qrxlevmin = 1) \n
		Defines the minimum RX level at an MS antenna required for access to the GSM cell. This parameter is transmitted via BCCH. \n
			:param qrxlevmin: Range: -111 dBm to -48 dBm
		"""
		param = Conversions.decimal_value_to_str(qrxlevmin)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:QUALity:RXLevmin:ACCess {param}')
