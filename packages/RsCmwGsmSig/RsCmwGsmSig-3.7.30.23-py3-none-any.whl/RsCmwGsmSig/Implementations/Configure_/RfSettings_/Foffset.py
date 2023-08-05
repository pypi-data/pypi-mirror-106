from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("foffset", core, parent)

	def get_downlink(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:FOFFset:DL \n
		Snippet: value: int = driver.configure.rfSettings.foffset.get_downlink() \n
		Specifies a positive or negative frequency offset to be added to the downlink center frequency of the configured channel,
		see CONFigure:GSM:SIGN<i>:RFSettings:CHANnel. \n
			:return: offset: Range: -100000 Hz to 100000 Hz , Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:FOFFset:DL?')
		return Conversions.str_to_int(response)

	def set_downlink(self, offset: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:FOFFset:DL \n
		Snippet: driver.configure.rfSettings.foffset.set_downlink(offset = 1) \n
		Specifies a positive or negative frequency offset to be added to the downlink center frequency of the configured channel,
		see CONFigure:GSM:SIGN<i>:RFSettings:CHANnel. \n
			:param offset: Range: -100000 Hz to 100000 Hz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:FOFFset:DL {param}')

	def get_uplink(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:FOFFset:UL \n
		Snippet: value: int = driver.configure.rfSettings.foffset.get_uplink() \n
		Specifies a positive or negative frequency offset to be added to the uplink center frequency of the configured channel,
		see CONFigure:GSM:SIGN<i>:RFSettings:CHANnel. \n
			:return: offset: Range: -100000 Hz to 100000 Hz , Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:FOFFset:UL?')
		return Conversions.str_to_int(response)

	def set_uplink(self, offset: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:FOFFset:UL \n
		Snippet: driver.configure.rfSettings.foffset.set_uplink(offset = 1) \n
		Specifies a positive or negative frequency offset to be added to the uplink center frequency of the configured channel,
		see CONFigure:GSM:SIGN<i>:RFSettings:CHANnel. \n
			:param offset: Range: -100000 Hz to 100000 Hz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:FOFFset:UL {param}')
