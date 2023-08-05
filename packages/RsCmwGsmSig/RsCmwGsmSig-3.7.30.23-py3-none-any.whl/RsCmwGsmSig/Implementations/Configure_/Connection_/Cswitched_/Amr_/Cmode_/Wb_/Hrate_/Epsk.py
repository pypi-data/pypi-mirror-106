from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Epsk:
	"""Epsk commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("epsk", core, parent)

	def get_downlink(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:CMODe:WB:HRATe:EPSK:DL \n
		Snippet: value: int or bool = driver.configure.connection.cswitched.amr.cmode.wb.hrate.epsk.get_downlink() \n
		Select the codec modes to be used by the R&S CMW (downlink) and the MS (uplink) for the half-rate wideband AMR codec
		(8PSK modulation) . Only active codec modes can be selected. For configuration and activation/deactivation of the codec
		modes, see method RsCmwGsmSig.Configure.Connection.Cswitched.Amr.Rset.Wb.Hrate.epsk. \n
			:return: codec_mode: integer | ON | OFF Range: 1 to 3 (if all codec modes are active, otherwise less) Additional parameters OFF (ON) disables (enables) codec mode.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:CMODe:WB:HRATe:EPSK:DL?')
		return Conversions.str_to_int_or_bool(response)

	def set_downlink(self, codec_mode: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:CMODe:WB:HRATe:EPSK:DL \n
		Snippet: driver.configure.connection.cswitched.amr.cmode.wb.hrate.epsk.set_downlink(codec_mode = 1) \n
		Select the codec modes to be used by the R&S CMW (downlink) and the MS (uplink) for the half-rate wideband AMR codec
		(8PSK modulation) . Only active codec modes can be selected. For configuration and activation/deactivation of the codec
		modes, see method RsCmwGsmSig.Configure.Connection.Cswitched.Amr.Rset.Wb.Hrate.epsk. \n
			:param codec_mode: integer | ON | OFF Range: 1 to 3 (if all codec modes are active, otherwise less) Additional parameters OFF (ON) disables (enables) codec mode.
		"""
		param = Conversions.decimal_or_bool_value_to_str(codec_mode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:CMODe:WB:HRATe:EPSK:DL {param}')

	def get_uplink(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:CMODe:WB:HRATe:EPSK:UL \n
		Snippet: value: int or bool = driver.configure.connection.cswitched.amr.cmode.wb.hrate.epsk.get_uplink() \n
		Select the codec modes to be used by the R&S CMW (downlink) and the MS (uplink) for the half-rate wideband AMR codec
		(8PSK modulation) . Only active codec modes can be selected. For configuration and activation/deactivation of the codec
		modes, see method RsCmwGsmSig.Configure.Connection.Cswitched.Amr.Rset.Wb.Hrate.epsk. \n
			:return: codec_mode: integer | ON | OFF Range: 1 to 3 (if all codec modes are active, otherwise less) Additional parameters OFF (ON) disables (enables) codec mode.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:CMODe:WB:HRATe:EPSK:UL?')
		return Conversions.str_to_int_or_bool(response)

	def set_uplink(self, codec_mode: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:CMODe:WB:HRATe:EPSK:UL \n
		Snippet: driver.configure.connection.cswitched.amr.cmode.wb.hrate.epsk.set_uplink(codec_mode = 1) \n
		Select the codec modes to be used by the R&S CMW (downlink) and the MS (uplink) for the half-rate wideband AMR codec
		(8PSK modulation) . Only active codec modes can be selected. For configuration and activation/deactivation of the codec
		modes, see method RsCmwGsmSig.Configure.Connection.Cswitched.Amr.Rset.Wb.Hrate.epsk. \n
			:param codec_mode: integer | ON | OFF Range: 1 to 3 (if all codec modes are active, otherwise less) Additional parameters OFF (ON) disables (enables) codec mode.
		"""
		param = Conversions.decimal_or_bool_value_to_str(codec_mode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:CMODe:WB:HRATe:EPSK:UL {param}')
