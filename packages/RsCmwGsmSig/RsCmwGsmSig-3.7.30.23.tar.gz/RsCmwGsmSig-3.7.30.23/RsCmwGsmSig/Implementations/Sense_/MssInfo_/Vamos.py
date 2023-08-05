from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vamos:
	"""Vamos commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("vamos", core, parent)

	def get_level(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:MSSinfo:VAMos:LEVel \n
		Snippet: value: int = driver.sense.mssInfo.vamos.get_level() \n
		Indicates the VAMOS support of the MS and the VAMOS level supported. \n
			:return: level: 0: VAMOS not supported 1: VAMOS I supported 2: VAMOS II supported 3: VAMOS III supported Range: 0 to 3
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:VAMos:LEVel?')
		return Conversions.str_to_int(response)
