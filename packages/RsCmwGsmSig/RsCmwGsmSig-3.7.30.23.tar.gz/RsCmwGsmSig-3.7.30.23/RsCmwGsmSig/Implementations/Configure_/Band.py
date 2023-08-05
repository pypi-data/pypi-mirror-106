from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Band:
	"""Band commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("band", core, parent)

	# noinspection PyTypeChecker
	def get_bcch(self) -> enums.OperBandGsm:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BAND:BCCH \n
		Snippet: value: enums.OperBandGsm = driver.configure.band.get_bcch() \n
		Selects the GSM band used for the BCCH and initially also for the TCH. The TCH band can be changed via a handover.
		To check the current TCH band, see method RsCmwGsmSig.Sense.Band.tch. \n
			:return: band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900 bands
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:BAND:BCCH?')
		return Conversions.str_to_scalar_enum(response, enums.OperBandGsm)

	def set_bcch(self, band: enums.OperBandGsm) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:BAND:BCCH \n
		Snippet: driver.configure.band.set_bcch(band = enums.OperBandGsm.G04) \n
		Selects the GSM band used for the BCCH and initially also for the TCH. The TCH band can be changed via a handover.
		To check the current TCH band, see method RsCmwGsmSig.Sense.Band.tch. \n
			:param band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900 bands
		"""
		param = Conversions.enum_scalar_to_str(band, enums.OperBandGsm)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:BAND:BCCH {param}')
