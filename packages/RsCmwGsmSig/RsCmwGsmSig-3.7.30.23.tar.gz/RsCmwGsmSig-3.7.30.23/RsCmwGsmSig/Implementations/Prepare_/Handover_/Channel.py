from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channel", core, parent)

	def get_tch(self) -> int:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:CHANnel:TCH \n
		Snippet: value: int = driver.prepare.handover.channel.get_tch() \n
		Selects the TCH/PDCH channel in the destination GSM band. The range of values depends on the selected band (method
		RsCmwGsmSig.Prepare.Handover.target) ; for an overview see 'GSM Bands and Channels'. The values below are for GSM 900. \n
			:return: channel: Range: 512 to 885
		"""
		response = self._core.io.query_str('PREPare:GSM:SIGNaling<Instance>:HANDover:CHANnel:TCH?')
		return Conversions.str_to_int(response)

	def set_tch(self, channel: int) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:CHANnel:TCH \n
		Snippet: driver.prepare.handover.channel.set_tch(channel = 1) \n
		Selects the TCH/PDCH channel in the destination GSM band. The range of values depends on the selected band (method
		RsCmwGsmSig.Prepare.Handover.target) ; for an overview see 'GSM Bands and Channels'. The values below are for GSM 900. \n
			:param channel: Range: 512 to 885
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'PREPare:GSM:SIGNaling<Instance>:HANDover:CHANnel:TCH {param}')
