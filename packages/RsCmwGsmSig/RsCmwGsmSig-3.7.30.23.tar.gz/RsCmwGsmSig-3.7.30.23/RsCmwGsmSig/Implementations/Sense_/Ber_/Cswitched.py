from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	def get_rt_delay(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:BER:CSWitched:RTDelay \n
		Snippet: value: int = driver.sense.ber.cswitched.get_rt_delay() \n
		Queries duration in bursts the loopback signal needs from a transmission to detection by the R&S CMW. \n
			:return: bursts: Range: 0 to 24
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:BER:CSWitched:RTDelay?')
		return Conversions.str_to_int(response)
