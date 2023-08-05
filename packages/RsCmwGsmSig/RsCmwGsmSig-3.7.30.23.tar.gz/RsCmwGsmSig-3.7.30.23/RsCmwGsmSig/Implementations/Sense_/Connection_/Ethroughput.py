from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ethroughput:
	"""Ethroughput commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ethroughput", core, parent)

	def get_uplink(self) -> float:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:CONNection:ETHRoughput:UL \n
		Snippet: value: float = driver.sense.connection.ethroughput.get_uplink() \n
		Queries the maximum possible RLC throughput in the uplink, resulting from the uplink PS slot configuration. \n
			:return: throughput: Range: 0 bit/s to 100E+3 bit/s, Unit: bit/s
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:CONNection:ETHRoughput:UL?')
		return Conversions.str_to_float(response)

	def get_downlink(self) -> float:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:CONNection:ETHRoughput:DL \n
		Snippet: value: float = driver.sense.connection.ethroughput.get_downlink() \n
		Queries the maximum possible RLC throughput in the downlink, resulting from the downlink PS slot configuration. \n
			:return: throughput: Range: 0 bit/s to 1E+6 bit/s, Unit: bit/s
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:CONNection:ETHRoughput:DL?')
		return Conversions.str_to_float(response)
