from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	def get_ber(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:BER \n
		Snippet: value: float = driver.configure.ber.cswitched.limit.get_ber() \n
		Specifies an upper limit for the BER results of the BER CS measurement in burst by burst mode. If you set the limit via
		this command, a coupling to the class II bits limit is removed. The coupling can only be enabled via the GUI. \n
			:return: limit: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:BER?')
		return Conversions.str_to_float(response)

	def set_ber(self, limit: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:BER \n
		Snippet: driver.configure.ber.cswitched.limit.set_ber(limit = 1.0) \n
		Specifies an upper limit for the BER results of the BER CS measurement in burst by burst mode. If you set the limit via
		this command, a coupling to the class II bits limit is removed. The coupling can only be enabled via the GUI. \n
			:param limit: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(limit)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:BER {param}')

	def get_cii_bits(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:CIIBits \n
		Snippet: value: float = driver.configure.ber.cswitched.limit.get_cii_bits() \n
		Specifies upper limits for the BER and RBER class II bit results of the BER CS measurement. A limit for the burst by
		burst mode can be set separately, see method RsCmwGsmSig.Configure.Ber.Cswitched.Limit.ber. \n
			:return: class_2_bits: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:CIIBits?')
		return Conversions.str_to_float(response)

	def set_cii_bits(self, class_2_bits: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:CIIBits \n
		Snippet: driver.configure.ber.cswitched.limit.set_cii_bits(class_2_bits = 1.0) \n
		Specifies upper limits for the BER and RBER class II bit results of the BER CS measurement. A limit for the burst by
		burst mode can be set separately, see method RsCmwGsmSig.Configure.Ber.Cswitched.Limit.ber. \n
			:param class_2_bits: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(class_2_bits)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:CIIBits {param}')

	def get_cib_bits(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:CIBBits \n
		Snippet: value: float = driver.configure.ber.cswitched.limit.get_cib_bits() \n
		Specifies upper limits for the BER and RBER class Ib bit results of the BER CS measurement. \n
			:return: class_ib_bits: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:CIBBits?')
		return Conversions.str_to_float(response)

	def set_cib_bits(self, class_ib_bits: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:CIBBits \n
		Snippet: driver.configure.ber.cswitched.limit.set_cib_bits(class_ib_bits = 1.0) \n
		Specifies upper limits for the BER and RBER class Ib bit results of the BER CS measurement. \n
			:param class_ib_bits: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(class_ib_bits)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:CIBBits {param}')

	def get_fer(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FER \n
		Snippet: value: float = driver.configure.ber.cswitched.limit.get_fer() \n
		Specifies an upper limit for the FER results of the BER CS measurement in mode 'RBER/FER' and 'AMR Inband FER'. \n
			:return: fer: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FER?')
		return Conversions.str_to_float(response)

	def set_fer(self, fer: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FER \n
		Snippet: driver.configure.ber.cswitched.limit.set_fer(fer = 1.0) \n
		Specifies an upper limit for the FER results of the BER CS measurement in mode 'RBER/FER' and 'AMR Inband FER'. \n
			:param fer: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(fer)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FER {param}')

	def get_ffacch(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FFACch \n
		Snippet: value: float = driver.configure.ber.cswitched.limit.get_ffacch() \n
		Specifies an upper limit for the frame error rate (FER) results of the BER CS measurement in the measurement modes FER
		FACCH and FER SACCH. \n
			:return: fer_facch: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FFACch?')
		return Conversions.str_to_float(response)

	def set_ffacch(self, fer_facch: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FFACch \n
		Snippet: driver.configure.ber.cswitched.limit.set_ffacch(fer_facch = 1.0) \n
		Specifies an upper limit for the frame error rate (FER) results of the BER CS measurement in the measurement modes FER
		FACCH and FER SACCH. \n
			:param fer_facch: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(fer_facch)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FFACch {param}')

	def get_fsacch(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FSACch \n
		Snippet: value: float = driver.configure.ber.cswitched.limit.get_fsacch() \n
		Specifies an upper limit for the frame error rate (FER) results of the BER CS measurement in the measurement modes FER
		FACCH and FER SACCH. \n
			:return: fer_sacch: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FSACch?')
		return Conversions.str_to_float(response)

	def set_fsacch(self, fer_sacch: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FSACch \n
		Snippet: driver.configure.ber.cswitched.limit.set_fsacch(fer_sacch = 1.0) \n
		Specifies an upper limit for the frame error rate (FER) results of the BER CS measurement in the measurement modes FER
		FACCH and FER SACCH. \n
			:param fer_sacch: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(fer_sacch)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BER:CSWitched:LIMit:FSACch {param}')
