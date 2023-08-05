from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frate:
	"""Frate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frate", core, parent)

	def get_gmsk(self) -> List[float or bool]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:THReshold:NB:FRATe:GMSK \n
		Snippet: value: List[float or bool] = driver.configure.connection.cswitched.amr.threshold.nb.frate.get_gmsk() \n
		Selects the upper and lower limits for the codec mode swapping. The threshold sequence is following: lower 4, upper 3,
		lower 3, upper 2, lower 2, and upper 1 threshold. Value OFF disables threshold. \n
			:return: threshold: ON | OFF 0 dB to 31.5 dB: limit of codec mode Additional parameters OFF (ON) disables (enables) the limit. Range: OFF, 0 dB to 31.5 dB , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:THReshold:NB:FRATe:GMSK?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_gmsk(self, threshold: List[float or bool]) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:THReshold:NB:FRATe:GMSK \n
		Snippet: driver.configure.connection.cswitched.amr.threshold.nb.frate.set_gmsk(threshold = [1.1, True, 2.2, False, 3.3]) \n
		Selects the upper and lower limits for the codec mode swapping. The threshold sequence is following: lower 4, upper 3,
		lower 3, upper 2, lower 2, and upper 1 threshold. Value OFF disables threshold. \n
			:param threshold: ON | OFF 0 dB to 31.5 dB: limit of codec mode Additional parameters OFF (ON) disables (enables) the limit. Range: OFF, 0 dB to 31.5 dB , Unit: dB
		"""
		param = Conversions.list_to_csv_str(threshold)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:THReshold:NB:FRATe:GMSK {param}')
