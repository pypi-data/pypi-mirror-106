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
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:TDSCdma:THResholds:HIGH \n
		Snippet: value: int = driver.configure.ncell.tdscdma.thresholds.get_high() \n
		Configures the high reselection threshold value for TD-SCDMA neighbor cells. \n
			:return: high: Range: 0 to 31, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:NCELl:TDSCdma:THResholds:HIGH?')
		return Conversions.str_to_int(response)

	def set_high(self, high: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:TDSCdma:THResholds:HIGH \n
		Snippet: driver.configure.ncell.tdscdma.thresholds.set_high(high = 1) \n
		Configures the high reselection threshold value for TD-SCDMA neighbor cells. \n
			:param high: Range: 0 to 31, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(high)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:NCELl:TDSCdma:THResholds:HIGH {param}')
