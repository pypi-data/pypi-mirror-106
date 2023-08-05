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
	def get_tch(self) -> enums.OperBandGsm:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:BAND:TCH \n
		Snippet: value: enums.OperBandGsm = driver.sense.band.get_tch() \n
		Returns the current GSM band used for the traffic channel (TCH/PDCH) . After a handover, this band can differ from the
		BCCH band configured via method RsCmwGsmSig.Configure.Band.bcch. \n
			:return: band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:BAND:TCH?')
		return Conversions.str_to_scalar_enum(response, enums.OperBandGsm)
