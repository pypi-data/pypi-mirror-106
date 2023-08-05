from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channel", core, parent)

	@property
	def tch(self):
		"""tch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tch'):
			from .Channel_.Tch import Tch
			self._tch = Tch(self._core, self._base)
		return self._tch

	def get_bcch(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:CHANnel:BCCH \n
		Snippet: value: int = driver.configure.rfSettings.channel.get_bcch() \n
		Sets the GSM channel number for the broadcast control channel (BCCH) . The range of values depends on the selected band
		(method RsCmwGsmSig.Configure.Band.bcch) ; for an overview see 'GSM Bands and Channels'. The values below are for GSM 900. \n
			:return: channel: decimal Range: 0 to 124, 940 to 1023
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:CHANnel:BCCH?')
		return Conversions.str_to_int(response)

	def set_bcch(self, channel: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:CHANnel:BCCH \n
		Snippet: driver.configure.rfSettings.channel.set_bcch(channel = 1) \n
		Sets the GSM channel number for the broadcast control channel (BCCH) . The range of values depends on the selected band
		(method RsCmwGsmSig.Configure.Band.bcch) ; for an overview see 'GSM Bands and Channels'. The values below are for GSM 900. \n
			:param channel: decimal Range: 0 to 124, 940 to 1023
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:CHANnel:BCCH {param}')

	def clone(self) -> 'Channel':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Channel(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
