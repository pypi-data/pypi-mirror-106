from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	def get_epower(self) -> float:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RFSettings:EPOWer \n
		Snippet: value: float = driver.sense.rfSettings.get_epower() \n
		No command help available \n
			:return: power: No help available
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RFSettings:EPOWer?')
		return Conversions.str_to_float(response)

	def get_efrequency(self) -> float:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RFSettings:EFRequency \n
		Snippet: value: float = driver.sense.rfSettings.get_efrequency() \n
		No command help available \n
			:return: frequency: No help available
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RFSettings:EFRequency?')
		return Conversions.str_to_float(response)
