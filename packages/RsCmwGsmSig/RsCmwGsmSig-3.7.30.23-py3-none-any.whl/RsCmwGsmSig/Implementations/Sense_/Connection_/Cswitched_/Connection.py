from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connection", core, parent)

	def get_attempt(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:CONNection:CSWitched:CONNection:ATTempt \n
		Snippet: value: int = driver.sense.connection.cswitched.connection.get_attempt() \n
		Queries the counters of connection attempt / reject. \n
			:return: counter: Range: 0 to 2^32
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:CONNection:CSWitched:CONNection:ATTempt?')
		return Conversions.str_to_int(response)

	def get_reject(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:CONNection:CSWitched:CONNection:REJect \n
		Snippet: value: int = driver.sense.connection.cswitched.connection.get_reject() \n
		Queries the counters of connection attempt / reject. \n
			:return: counter: Range: 0 to 2^32
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:CONNection:CSWitched:CONNection:REJect?')
		return Conversions.str_to_int(response)
