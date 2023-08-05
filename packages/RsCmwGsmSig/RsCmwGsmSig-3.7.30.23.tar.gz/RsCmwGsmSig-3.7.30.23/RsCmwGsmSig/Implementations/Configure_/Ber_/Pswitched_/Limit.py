from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	def get_cii_bits(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:CIIBits \n
		Snippet: value: float = driver.configure.ber.pswitched.limit.get_cii_bits() \n
		Specifies upper limits for the BER class II bit results of the BER PS measurement. \n
			:return: class_2_bits: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:CIIBits?')
		return Conversions.str_to_float(response)

	def set_cii_bits(self, class_2_bits: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:CIIBits \n
		Snippet: driver.configure.ber.pswitched.limit.set_cii_bits(class_2_bits = 1.0) \n
		Specifies upper limits for the BER class II bit results of the BER PS measurement. \n
			:param class_2_bits: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(class_2_bits)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:CIIBits {param}')

	def get_dbler(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:DBLer \n
		Snippet: value: float = driver.configure.ber.pswitched.limit.get_dbler() \n
		Specifies upper limits for the DBLER results of the BER PS measurement. \n
			:return: dbler: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:DBLer?')
		return Conversions.str_to_float(response)

	def set_dbler(self, dbler: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:DBLer \n
		Snippet: driver.configure.ber.pswitched.limit.set_dbler(dbler = 1.0) \n
		Specifies upper limits for the DBLER results of the BER PS measurement. \n
			:param dbler: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(dbler)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:DBLer {param}')

	def get_usf_bler(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:USFBler \n
		Snippet: value: float = driver.configure.ber.pswitched.limit.get_usf_bler() \n
		Specifies upper limits for the USF BLER results of the BER PS measurement. \n
			:return: usf_bler: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:USFBler?')
		return Conversions.str_to_float(response)

	def set_usf_bler(self, usf_bler: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:USFBler \n
		Snippet: driver.configure.ber.pswitched.limit.set_usf_bler(usf_bler = 1.0) \n
		Specifies upper limits for the USF BLER results of the BER PS measurement. \n
			:param usf_bler: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(usf_bler)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:PSWitched:LIMit:USFBler {param}')
