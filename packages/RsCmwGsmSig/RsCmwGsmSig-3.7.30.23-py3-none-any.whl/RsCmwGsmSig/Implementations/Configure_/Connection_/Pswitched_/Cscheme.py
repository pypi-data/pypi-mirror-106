from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cscheme:
	"""Cscheme commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cscheme", core, parent)

	# noinspection PyTypeChecker
	def get_uplink(self) -> enums.CodingSchemeUplink:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:CSCHeme:UL \n
		Snippet: value: enums.CodingSchemeUplink = driver.configure.connection.pswitched.cscheme.get_uplink() \n
		Selects the coding scheme for uplink packet data channels. The selected value must be compatible to the configured set of
		modulation and coding schemes, see method RsCmwGsmSig.Configure.Connection.Pswitched.tlevel. \n
			:return: cscheme: C1 | C2 | C3 | C4 | MC1 | MC2 | MC3 | MC4 | MC5 | MC6 | MC7 | MC8 | MC9 | UA7 | UA8 | UA9 | UA10 | UA11 C1 to C4: CS-1 to CS-4 MC1 to MC9: MCS-1 to MCS-9 UA7 to UA11: UAS-7 to UAS-11
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:CSCHeme:UL?')
		return Conversions.str_to_scalar_enum(response, enums.CodingSchemeUplink)

	def set_uplink(self, cscheme: enums.CodingSchemeUplink) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:CSCHeme:UL \n
		Snippet: driver.configure.connection.pswitched.cscheme.set_uplink(cscheme = enums.CodingSchemeUplink.C1) \n
		Selects the coding scheme for uplink packet data channels. The selected value must be compatible to the configured set of
		modulation and coding schemes, see method RsCmwGsmSig.Configure.Connection.Pswitched.tlevel. \n
			:param cscheme: C1 | C2 | C3 | C4 | MC1 | MC2 | MC3 | MC4 | MC5 | MC6 | MC7 | MC8 | MC9 | UA7 | UA8 | UA9 | UA10 | UA11 C1 to C4: CS-1 to CS-4 MC1 to MC9: MCS-1 to MCS-9 UA7 to UA11: UAS-7 to UAS-11
		"""
		param = Conversions.enum_scalar_to_str(cscheme, enums.CodingSchemeUplink)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:CSCHeme:UL {param}')
