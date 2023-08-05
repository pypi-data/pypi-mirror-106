from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bcch:
	"""Bcch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bcch", core, parent)

	def get_output(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:EATTenuation:BCCH:OUTPut \n
		Snippet: value: float = driver.configure.rfSettings.eattenuation.bcch.get_output() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF output connector for the
		BCCH path. This command is only relevant for scenario 'BCCH and TCH/PDCH'. The allowed value range can be calculated as
		follows: Range = [-130 - (BCCH DL 'Level') to -(BCCH DL 'Level') ] \n
			:return: ext_rf_out_att: Range: see above , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:EATTenuation:BCCH:OUTPut?')
		return Conversions.str_to_float(response)

	def set_output(self, ext_rf_out_att: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:EATTenuation:BCCH:OUTPut \n
		Snippet: driver.configure.rfSettings.eattenuation.bcch.set_output(ext_rf_out_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF output connector for the
		BCCH path. This command is only relevant for scenario 'BCCH and TCH/PDCH'. The allowed value range can be calculated as
		follows: Range = [-130 - (BCCH DL 'Level') to -(BCCH DL 'Level') ] \n
			:param ext_rf_out_att: Range: see above , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(ext_rf_out_att)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:EATTenuation:BCCH:OUTPut {param}')
