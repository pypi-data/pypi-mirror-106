from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DldCarrier:
	"""DldCarrier commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dldCarrier", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DLDCarrier:ENABle \n
		Snippet: value: bool = driver.configure.connection.pswitched.dldCarrier.get_enable() \n
		Enables or disables the downlink dual carrier mode. In this mode, the R&S CMW uses two radio frequency channels to assign
		resources to the mobile station; see 3GPP TS 44.060. Some settings can be configured individually per carrier.
		The related commands distinguish the two carriers via the mnemonics CARRier1 and CARRier2. See e.g.
		CONFigure:GSM:SIGN<i>:RFSettings:CHANnel. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DLDCarrier:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DLDCarrier:ENABle \n
		Snippet: driver.configure.connection.pswitched.dldCarrier.set_enable(enable = False) \n
		Enables or disables the downlink dual carrier mode. In this mode, the R&S CMW uses two radio frequency channels to assign
		resources to the mobile station; see 3GPP TS 44.060. Some settings can be configured individually per carrier.
		The related commands distinguish the two carriers via the mnemonics CARRier1 and CARRier2. See e.g.
		CONFigure:GSM:SIGN<i>:RFSettings:CHANnel. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DLDCarrier:ENABle {param}')
