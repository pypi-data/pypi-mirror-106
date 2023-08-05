from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcapability:
	"""Tcapability commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tcapability", core, parent)

	def get_ss_channels(self) -> bool:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:MSSinfo:TCAPability:SSCHannels \n
		Snippet: value: bool = driver.sense.mssInfo.tcapability.get_ss_channels() \n
		Indicates tightened link level performance support of the MS. The related commands distinguish the supported channels via
		the last mnemonics:
			INTRO_CMD_HELP: The IMEI consists of four parts: \n
			- ETWO: support for EGPRS2
			- GEGP: support for GPRS and EGPRS
			- SSCH: support for speech and signaling channels \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:TCAPability:SSCHannels?')
		return Conversions.str_to_bool(response)

	def get_gegprs(self) -> bool:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:MSSinfo:TCAPability:GEGPrs \n
		Snippet: value: bool = driver.sense.mssInfo.tcapability.get_gegprs() \n
		Indicates tightened link level performance support of the MS. The related commands distinguish the supported channels via
		the last mnemonics:
			INTRO_CMD_HELP: The IMEI consists of four parts: \n
			- ETWO: support for EGPRS2
			- GEGP: support for GPRS and EGPRS
			- SSCH: support for speech and signaling channels \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:TCAPability:GEGPrs?')
		return Conversions.str_to_bool(response)

	def get_etwo(self) -> bool:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:MSSinfo:TCAPability:ETWO \n
		Snippet: value: bool = driver.sense.mssInfo.tcapability.get_etwo() \n
		Indicates tightened link level performance support of the MS. The related commands distinguish the supported channels via
		the last mnemonics:
			INTRO_CMD_HELP: The IMEI consists of four parts: \n
			- ETWO: support for EGPRS2
			- GEGP: support for GPRS and EGPRS
			- SSCH: support for speech and signaling channels \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:TCAPability:ETWO?')
		return Conversions.str_to_bool(response)
