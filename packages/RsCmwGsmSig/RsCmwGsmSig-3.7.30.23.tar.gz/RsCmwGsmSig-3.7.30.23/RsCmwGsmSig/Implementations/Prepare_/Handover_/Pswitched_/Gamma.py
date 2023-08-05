from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gamma:
	"""Gamma commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gamma", core, parent)

	def get_uplink(self) -> List[int]:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:GAMMa:UL \n
		Snippet: value: List[int] = driver.prepare.handover.pswitched.gamma.get_uplink() \n
		Specifies the power control parameter ΓCH per UL timeslot in the destination GSM band. \n
			:return: gamma: Range: 0 to 31
		"""
		response = self._core.io.query_bin_or_ascii_int_list_with_opc('PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:GAMMa:UL?')
		return response

	def set_uplink(self, gamma: List[int]) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:GAMMa:UL \n
		Snippet: driver.prepare.handover.pswitched.gamma.set_uplink(gamma = [1, 2, 3]) \n
		Specifies the power control parameter ΓCH per UL timeslot in the destination GSM band. \n
			:param gamma: Range: 0 to 31
		"""
		param = Conversions.list_to_csv_str(gamma)
		self._core.io.write_with_opc(f'PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:GAMMa:UL {param}')
