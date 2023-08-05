from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 23 total commands, 9 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	@property
	def eattenuation(self):
		"""eattenuation commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_eattenuation'):
			from .RfSettings_.Eattenuation import Eattenuation
			self._eattenuation = Eattenuation(self._core, self._base)
		return self._eattenuation

	@property
	def channel(self):
		"""channel commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .RfSettings_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def level(self):
		"""level commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .RfSettings_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def pmax(self):
		"""pmax commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmax'):
			from .RfSettings_.Pmax import Pmax
			self._pmax = Pmax(self._core, self._base)
		return self._pmax

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_foffset'):
			from .RfSettings_.Foffset import Foffset
			self._foffset = Foffset(self._core, self._base)
		return self._foffset

	@property
	def pcl(self):
		"""pcl commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcl'):
			from .RfSettings_.Pcl import Pcl
			self._pcl = Pcl(self._core, self._base)
		return self._pcl

	@property
	def chcCombined(self):
		"""chcCombined commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_chcCombined'):
			from .RfSettings_.ChcCombined import ChcCombined
			self._chcCombined = ChcCombined(self._core, self._base)
		return self._chcCombined

	@property
	def edc(self):
		"""edc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_edc'):
			from .RfSettings_.Edc import Edc
			self._edc = Edc(self._core, self._base)
		return self._edc

	@property
	def hopping(self):
		"""hopping commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_hopping'):
			from .RfSettings_.Hopping import Hopping
			self._hopping = Hopping(self._core, self._base)
		return self._hopping

	def get_ml_offset(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:MLOFfset \n
		Snippet: value: int = driver.configure.rfSettings.get_ml_offset() \n
		Sets the input level offset of the mixer in the analyzer path. \n
			:return: mix_lev_offset: Range: -10 dB to 10 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:MLOFfset?')
		return Conversions.str_to_int(response)

	def set_ml_offset(self, mix_lev_offset: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:MLOFfset \n
		Snippet: driver.configure.rfSettings.set_ml_offset(mix_lev_offset = 1) \n
		Sets the input level offset of the mixer in the analyzer path. \n
			:param mix_lev_offset: Range: -10 dB to 10 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(mix_lev_offset)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:MLOFfset {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the UL signal in manual mode or queries the result if the expected nominal power is
		calculated automatically according to the UL power control. To configure the expected nominal power mode, see method
		RsCmwGsmSig.Configure.RfSettings.enpMode. \n
			:return: expected_power: In manual mode the range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, expected_power: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:RFSettings:ENPower \n
		Snippet: driver.configure.rfSettings.set_envelope_power(expected_power = 1.0) \n
		Sets the expected nominal power of the UL signal in manual mode or queries the result if the expected nominal power is
		calculated automatically according to the UL power control. To configure the expected nominal power mode, see method
		RsCmwGsmSig.Configure.RfSettings.enpMode. \n
			:param expected_power: In manual mode the range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(expected_power)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:ENPower {param}')

	# noinspection PyTypeChecker
	def get_enp_mode(self) -> enums.NominalPowerMode:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:RFSettings:ENPMode \n
		Snippet: value: enums.NominalPowerMode = driver.configure.rfSettings.get_enp_mode() \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- method RsCmwGsmSig.Configure.RfSettings.envelopePower
			- method RsCmwGsmSig.Configure.RfSettings.umargin \n
			:return: mode: MANual | ULPC MANual: The expected nominal power and margin are specified manually. ULPC: The expected nominal power is calculated according to the UL power control settings. For the margin, 7 dB are applied.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:ENPMode?')
		return Conversions.str_to_scalar_enum(response, enums.NominalPowerMode)

	def set_enp_mode(self, mode: enums.NominalPowerMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:RFSettings:ENPMode \n
		Snippet: driver.configure.rfSettings.set_enp_mode(mode = enums.NominalPowerMode.AUToranging) \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- method RsCmwGsmSig.Configure.RfSettings.envelopePower
			- method RsCmwGsmSig.Configure.RfSettings.umargin \n
			:param mode: MANual | ULPC MANual: The expected nominal power and margin are specified manually. ULPC: The expected nominal power is calculated according to the UL power control settings. For the margin, 7 dB are applied.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NominalPowerMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:ENPMode {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.get_umargin() \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode.
		If the expected nominal power is calculated automatically according to the UL power control settings, a fix margin of 6
		dB is used instead. The reference level minus the external input attenuation must be within the power range of the
		selected input connector; refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- method RsCmwGsmSig.Configure.RfSettings.enpMode
			- method RsCmwGsmSig.Configure.RfSettings.envelopePower
			- method RsCmwGsmSig.Configure.RfSettings.Eattenuation.inputPy \n
			:return: margin: Range: 0 dB to (55 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, margin: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.rfSettings.set_umargin(margin = 1.0) \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode.
		If the expected nominal power is calculated automatically according to the UL power control settings, a fix margin of 6
		dB is used instead. The reference level minus the external input attenuation must be within the power range of the
		selected input connector; refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- method RsCmwGsmSig.Configure.RfSettings.enpMode
			- method RsCmwGsmSig.Configure.RfSettings.envelopePower
			- method RsCmwGsmSig.Configure.RfSettings.Eattenuation.inputPy \n
			:param margin: Range: 0 dB to (55 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(margin)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:UMARgin {param}')

	def clone(self) -> 'RfSettings':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettings(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
