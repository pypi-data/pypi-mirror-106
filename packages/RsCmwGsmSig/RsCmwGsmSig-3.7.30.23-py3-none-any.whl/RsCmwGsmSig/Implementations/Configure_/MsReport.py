from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsReport:
	"""MsReport commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("msReport", core, parent)

	# noinspection PyTypeChecker
	def get_wm_quantity(self) -> enums.WmQuantity:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:MSReport:WMQuantity \n
		Snippet: value: enums.WmQuantity = driver.configure.msReport.get_wm_quantity() \n
		Selects whether the MS has to determine the RSCP or the Ec/No during WCDMA neighbor cell measurements. \n
			:return: quantity: RSCP | ECNO
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:MSReport:WMQuantity?')
		return Conversions.str_to_scalar_enum(response, enums.WmQuantity)

	def set_wm_quantity(self, quantity: enums.WmQuantity) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:MSReport:WMQuantity \n
		Snippet: driver.configure.msReport.set_wm_quantity(quantity = enums.WmQuantity.ECNO) \n
		Selects whether the MS has to determine the RSCP or the Ec/No during WCDMA neighbor cell measurements. \n
			:param quantity: RSCP | ECNO
		"""
		param = Conversions.enum_scalar_to_str(quantity, enums.WmQuantity)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:MSReport:WMQuantity {param}')

	# noinspection PyTypeChecker
	def get_lm_quantity(self) -> enums.LmQuantity:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:MSReport:LMQuantity \n
		Snippet: value: enums.LmQuantity = driver.configure.msReport.get_lm_quantity() \n
		Selects whether the MS has to determine the RSRP or the RSRQ during LTE neighbor cell measurements. \n
			:return: quantity: RSRP | RSRQ
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:MSReport:LMQuantity?')
		return Conversions.str_to_scalar_enum(response, enums.LmQuantity)

	def set_lm_quantity(self, quantity: enums.LmQuantity) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:MSReport:LMQuantity \n
		Snippet: driver.configure.msReport.set_lm_quantity(quantity = enums.LmQuantity.RSRP) \n
		Selects whether the MS has to determine the RSRP or the RSRQ during LTE neighbor cell measurements. \n
			:param quantity: RSRP | RSRQ
		"""
		param = Conversions.enum_scalar_to_str(quantity, enums.LmQuantity)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:MSReport:LMQuantity {param}')
