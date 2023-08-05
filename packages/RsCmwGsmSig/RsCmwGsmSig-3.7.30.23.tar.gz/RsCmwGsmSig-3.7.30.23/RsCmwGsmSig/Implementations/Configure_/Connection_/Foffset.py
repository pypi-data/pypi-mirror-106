from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("foffset", core, parent)

	def get_uplink(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:FOFFset[:UL] \n
		Snippet: value: int = driver.configure.connection.foffset.get_uplink() \n
		Sets the positive or negative offset to the center frequency of the uplink/downlink traffic channel. \n
			:return: offset: Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:FOFFset:UL?')
		return Conversions.str_to_int(response)

	def set_uplink(self, offset: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:FOFFset[:UL] \n
		Snippet: driver.configure.connection.foffset.set_uplink(offset = 1) \n
		Sets the positive or negative offset to the center frequency of the uplink/downlink traffic channel. \n
			:param offset: Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:FOFFset:UL {param}')

	def get_downlink(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:FOFFset:DL \n
		Snippet: value: int = driver.configure.connection.foffset.get_downlink() \n
		Sets the positive or negative offset to the center frequency of the uplink/downlink traffic channel. \n
			:return: offset: Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:FOFFset:DL?')
		return Conversions.str_to_int(response)

	def set_downlink(self, offset: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:FOFFset:DL \n
		Snippet: driver.configure.connection.foffset.set_downlink(offset = 1) \n
		Sets the positive or negative offset to the center frequency of the uplink/downlink traffic channel. \n
			:param offset: Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:FOFFset:DL {param}')
