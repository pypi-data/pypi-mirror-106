from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	def get_carrier(self) -> List[int]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:UDCYcle:DL:CARRier<Carrier> \n
		Snippet: value: List[int] = driver.configure.connection.pswitched.sconfig.udCycle.downlink.get_carrier() \n
		No command help available \n
			:return: assigned: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:UDCYcle:DL:CARRier1?')
		return response

	def set_carrier(self, assigned: List[int]) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:UDCYcle:DL:CARRier<Carrier> \n
		Snippet: driver.configure.connection.pswitched.sconfig.udCycle.downlink.set_carrier(assigned = [1, 2, 3]) \n
		No command help available \n
			:param assigned: No help available
		"""
		param = Conversions.list_to_csv_str(assigned)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:UDCYcle:DL:CARRier1 {param}')

	def get_value(self) -> List[int]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:UDCYcle:DL \n
		Snippet: value: List[int] = driver.configure.connection.pswitched.sconfig.udCycle.downlink.get_value() \n
		Percentage of downlink GPRS radio blocks containing the USF assigned to the MS. In sum, eight values are specified (slot
		0 to slot 7) . \n
			:return: assigned: Range: 0 | 1 | 25 | 50 | 75| 100 , Unit: %
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:UDCYcle:DL?')
		return response

	def set_value(self, assigned: List[int]) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:UDCYcle:DL \n
		Snippet: driver.configure.connection.pswitched.sconfig.udCycle.downlink.set_value(assigned = [1, 2, 3]) \n
		Percentage of downlink GPRS radio blocks containing the USF assigned to the MS. In sum, eight values are specified (slot
		0 to slot 7) . \n
			:param assigned: Range: 0 | 1 | 25 | 50 | 75| 100 , Unit: %
		"""
		param = Conversions.list_to_csv_str(assigned)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:UDCYcle:DL {param}')
