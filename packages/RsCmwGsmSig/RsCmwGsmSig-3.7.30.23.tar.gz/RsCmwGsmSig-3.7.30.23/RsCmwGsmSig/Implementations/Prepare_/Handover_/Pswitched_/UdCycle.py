from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdCycle:
	"""UdCycle commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("udCycle", core, parent)

	def get_downlink(self) -> List[int]:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:UDCYcle:DL \n
		Snippet: value: List[int] = driver.prepare.handover.pswitched.udCycle.get_downlink() \n
		Percentage of downlink GPRS radio blocks containing the USF to be assigned to the MS in the handover destination. In sum,
		eight values are specified (slot 0 to slot 7) . \n
			:return: assigned: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_bin_or_ascii_int_list_with_opc('PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:UDCYcle:DL?')
		return response

	def set_downlink(self, assigned: List[int]) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:UDCYcle:DL \n
		Snippet: driver.prepare.handover.pswitched.udCycle.set_downlink(assigned = [1, 2, 3]) \n
		Percentage of downlink GPRS radio blocks containing the USF to be assigned to the MS in the handover destination. In sum,
		eight values are specified (slot 0 to slot 7) . \n
			:param assigned: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.list_to_csv_str(assigned)
		self._core.io.write_with_opc(f'PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:UDCYcle:DL {param}')
