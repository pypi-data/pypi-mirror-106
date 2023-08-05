from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Security:
	"""Security commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("security", core, parent)

	def get_authenticate(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:SECurity:AUTHenticat \n
		Snippet: value: bool = driver.configure.cell.security.get_authenticate() \n
		Enables or disables authentication, to be performed during location update or attach. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:SECurity:AUTHenticat?')
		return Conversions.str_to_bool(response)

	def set_authenticate(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:SECurity:AUTHenticat \n
		Snippet: driver.configure.cell.security.set_authenticate(enable = False) \n
		Enables or disables authentication, to be performed during location update or attach. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:SECurity:AUTHenticat {param}')

	def get_skey(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:SECurity:SKEY \n
		Snippet: value: float = driver.configure.cell.security.get_skey() \n
		Defines the secret key Ki as 32-digit hexadecimal number. Leading zeros can be omitted. \n
			:return: secret_key: Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:SECurity:SKEY?')
		return Conversions.str_to_float(response)

	def set_skey(self, secret_key: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:SECurity:SKEY \n
		Snippet: driver.configure.cell.security.set_skey(secret_key = 1.0) \n
		Defines the secret key Ki as 32-digit hexadecimal number. Leading zeros can be omitted. \n
			:param secret_key: Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.decimal_value_to_str(secret_key)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:SECurity:SKEY {param}')

	# noinspection PyTypeChecker
	def get_sim_card(self) -> enums.SimCardType:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:SECurity:SIMCard \n
		Snippet: value: enums.SimCardType = driver.configure.cell.security.get_sim_card() \n
		Selects the type of the used SIM card. \n
			:return: sim_card_type: C3G | C2G C3G: 3G USIM C2G: 2G SIM
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:SECurity:SIMCard?')
		return Conversions.str_to_scalar_enum(response, enums.SimCardType)

	def set_sim_card(self, sim_card_type: enums.SimCardType) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:SECurity:SIMCard \n
		Snippet: driver.configure.cell.security.set_sim_card(sim_card_type = enums.SimCardType.C2G) \n
		Selects the type of the used SIM card. \n
			:param sim_card_type: C3G | C2G C3G: 3G USIM C2G: 2G SIM
		"""
		param = Conversions.enum_scalar_to_str(sim_card_type, enums.SimCardType)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:SECurity:SIMCard {param}')
