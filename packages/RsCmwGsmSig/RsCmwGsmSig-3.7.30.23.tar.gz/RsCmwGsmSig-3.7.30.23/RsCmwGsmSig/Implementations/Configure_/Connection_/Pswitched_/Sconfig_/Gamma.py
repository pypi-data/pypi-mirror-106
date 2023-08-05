from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gamma:
	"""Gamma commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gamma", core, parent)

	def get_uplink(self) -> List[int]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:GAMMa:UL \n
		Snippet: value: List[int] = driver.configure.connection.pswitched.sconfig.gamma.get_uplink() \n
		Specifies the power control parameter ΓCH per UL timeslot. \n
			:return: gamma: List of 8 gamma values for slot 0 to 7 Range: 0 to 31
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:GAMMa:UL?')
		return response

	def set_uplink(self, gamma: List[int]) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:GAMMa:UL \n
		Snippet: driver.configure.connection.pswitched.sconfig.gamma.set_uplink(gamma = [1, 2, 3]) \n
		Specifies the power control parameter ΓCH per UL timeslot. \n
			:param gamma: List of 8 gamma values for slot 0 to 7 Range: 0 to 31
		"""
		param = Conversions.list_to_csv_str(gamma)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:GAMMa:UL {param}')
