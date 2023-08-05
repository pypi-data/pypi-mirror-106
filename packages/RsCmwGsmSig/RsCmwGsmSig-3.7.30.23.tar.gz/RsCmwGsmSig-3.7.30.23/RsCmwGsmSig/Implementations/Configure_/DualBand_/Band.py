from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Band:
	"""Band commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("band", core, parent)

	# noinspection PyTypeChecker
	def get_tch(self) -> enums.OperBandGsm:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:DUALband:BAND:TCH \n
		Snippet: value: enums.OperBandGsm = driver.configure.dualBand.band.get_tch() \n
		Selects a handover destination band/network used for TCH/PDCH and initiates a dual band GSM handover.
		This command executes handover even if the handover dialog is opened. \n
			:return: band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:DUALband:BAND:TCH?')
		return Conversions.str_to_scalar_enum(response, enums.OperBandGsm)

	def set_tch(self, band: enums.OperBandGsm) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:DUALband:BAND:TCH \n
		Snippet: driver.configure.dualBand.band.set_tch(band = enums.OperBandGsm.G04) \n
		Selects a handover destination band/network used for TCH/PDCH and initiates a dual band GSM handover.
		This command executes handover even if the handover dialog is opened. \n
			:param band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
		"""
		param = Conversions.enum_scalar_to_str(band, enums.OperBandGsm)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:DUALband:BAND:TCH {param}')
