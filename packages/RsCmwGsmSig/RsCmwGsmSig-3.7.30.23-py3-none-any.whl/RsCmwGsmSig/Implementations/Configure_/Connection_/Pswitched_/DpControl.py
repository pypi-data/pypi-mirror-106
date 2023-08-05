from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpControl:
	"""DpControl commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpControl", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:ENABle \n
		Snippet: value: bool = driver.configure.connection.pswitched.dpControl.get_enable() \n
		Enables/disables downlink power control. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:ENABle \n
		Snippet: driver.configure.connection.pswitched.dpControl.set_enable(enable = False) \n
		Enables/disables downlink power control. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:ENABle {param}')

	# noinspection PyTypeChecker
	def get_p(self) -> enums.PswPowerReduction:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:P \n
		Snippet: value: enums.PswPowerReduction = driver.configure.connection.pswitched.dpControl.get_p() \n
		Defines a power reduction relative to BCCH. \n
			:return: p_0: DB0 | DB2 | DB4 | DB6 | DB8 | DB10 | DB12 | DB14 | DB16 | DB18 | DB20 | DB22 | DB24 | DB26 | DB28 | DB30 0 dB to 30 dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:P?')
		return Conversions.str_to_scalar_enum(response, enums.PswPowerReduction)

	def set_p(self, p_0: enums.PswPowerReduction) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:P \n
		Snippet: driver.configure.connection.pswitched.dpControl.set_p(p_0 = enums.PswPowerReduction.DB0) \n
		Defines a power reduction relative to BCCH. \n
			:param p_0: DB0 | DB2 | DB4 | DB6 | DB8 | DB10 | DB12 | DB14 | DB16 | DB18 | DB20 | DB22 | DB24 | DB26 | DB28 | DB30 0 dB to 30 dB
		"""
		param = Conversions.enum_scalar_to_str(p_0, enums.PswPowerReduction)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:P {param}')

	# noinspection PyTypeChecker
	def get_pmode(self) -> enums.PowerReductionMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:PMODe \n
		Snippet: value: enums.PowerReductionMode = driver.configure.connection.pswitched.dpControl.get_pmode() \n
		Defines the power reduction mode of the downlink power control. \n
			:return: pr_mode: PMA | PMB PMA: power reduction mode A PMB: power reduction mode B
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.PowerReductionMode)

	def set_pmode(self, pr_mode: enums.PowerReductionMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:PMODe \n
		Snippet: driver.configure.connection.pswitched.dpControl.set_pmode(pr_mode = enums.PowerReductionMode.PMA) \n
		Defines the power reduction mode of the downlink power control. \n
			:param pr_mode: PMA | PMB PMA: power reduction mode A PMB: power reduction mode B
		"""
		param = Conversions.enum_scalar_to_str(pr_mode, enums.PowerReductionMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:PMODe {param}')

	# noinspection PyTypeChecker
	def get_pfield(self) -> enums.PowerReductionField:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:PFIeld \n
		Snippet: value: enums.PowerReductionField = driver.configure.connection.pswitched.dpControl.get_pfield() \n
		Indicates the power level reduction of the current RLC block. \n
			:return: pr_field: DB0 | DB3 | DB7 | NUSable DB0: 0 dB to 3 dB (excluded) less than BCCH level - P0 DB3: 3 dB to 7dB (excluded) less than BCCH level - P0 DB7: 7 dB to 10 dB less than BCCH level - P0 NUSable: not usable - MS has to ignore PR field
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:PFIeld?')
		return Conversions.str_to_scalar_enum(response, enums.PowerReductionField)

	def set_pfield(self, pr_field: enums.PowerReductionField) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:PFIeld \n
		Snippet: driver.configure.connection.pswitched.dpControl.set_pfield(pr_field = enums.PowerReductionField.DB0) \n
		Indicates the power level reduction of the current RLC block. \n
			:param pr_field: DB0 | DB3 | DB7 | NUSable DB0: 0 dB to 3 dB (excluded) less than BCCH level - P0 DB3: 3 dB to 7dB (excluded) less than BCCH level - P0 DB7: 7 dB to 10 dB less than BCCH level - P0 NUSable: not usable - MS has to ignore PR field
		"""
		param = Conversions.enum_scalar_to_str(pr_field, enums.PowerReductionField)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DPControl:PFIeld {param}')
