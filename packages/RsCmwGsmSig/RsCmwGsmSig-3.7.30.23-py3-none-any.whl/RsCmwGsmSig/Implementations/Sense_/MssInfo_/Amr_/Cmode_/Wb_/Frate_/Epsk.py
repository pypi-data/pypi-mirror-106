from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Epsk:
	"""Epsk commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("epsk", core, parent)

	def get_downlink(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:AMR:CMODe:WB:FRATe:EPSK:DL \n
		Snippet: value: int = driver.sense.mssInfo.amr.cmode.wb.frate.epsk.get_downlink() \n
		Query the DL AMR codec mode requested by the MS (DL) and the actual UL codec mode used by the MS (UL) . Separate commands
		are available for the half-rate (HRATe) and full-rate (FRATe) narrowband (NB) and wideband (WB) AMR codecs, for GMSK and
		8PSK modulation. For the modes used in downlink and requested for uplink,
		refer to the CONFigure:GSM:SIGN<i>:CONNection:CSWitched:AMR:CMODe:... commands. \n
			:return: codec_mode: Range: 1 to 4 (1 to 3 for WB:FRATe:GMSK and WB:HRATe:EPSK)
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:AMR:CMODe:WB:FRATe:EPSK:DL?')
		return Conversions.str_to_int(response)

	def get_uplink(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:AMR:CMODe:WB:FRATe:EPSK:UL \n
		Snippet: value: int = driver.sense.mssInfo.amr.cmode.wb.frate.epsk.get_uplink() \n
		Query the DL AMR codec mode requested by the MS (DL) and the actual UL codec mode used by the MS (UL) . Separate commands
		are available for the half-rate (HRATe) and full-rate (FRATe) narrowband (NB) and wideband (WB) AMR codecs, for GMSK and
		8PSK modulation. For the modes used in downlink and requested for uplink,
		refer to the CONFigure:GSM:SIGN<i>:CONNection:CSWitched:AMR:CMODe:... commands. \n
			:return: codec_mode: Range: 1 to 4 (1 to 3 for WB:FRATe:GMSK and WB:HRATe:EPSK)
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:AMR:CMODe:WB:FRATe:EPSK:UL?')
		return Conversions.str_to_int(response)
