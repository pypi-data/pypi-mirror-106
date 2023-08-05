from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Thresholds:
	"""Thresholds commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("thresholds", core, parent)

	def get_high(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:GSM:THResholds:HIGH \n
		Snippet: value: int = driver.configure.ncell.gsm.thresholds.get_high() \n
		No command help available \n
			:return: high: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:NCELl:GSM:THResholds:HIGH?')
		return Conversions.str_to_int(response)

	def set_high(self, high: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:GSM:THResholds:HIGH \n
		Snippet: driver.configure.ncell.gsm.thresholds.set_high(high = 1) \n
		No command help available \n
			:param high: No help available
		"""
		param = Conversions.decimal_value_to_str(high)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:NCELl:GSM:THResholds:HIGH {param}')
