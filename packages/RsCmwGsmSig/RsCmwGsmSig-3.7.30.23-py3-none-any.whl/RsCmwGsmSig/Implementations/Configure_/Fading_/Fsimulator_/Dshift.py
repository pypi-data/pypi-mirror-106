from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dshift:
	"""Dshift commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dshift", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FadingMode:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:FADing:FSIMulator:DSHift:MODE \n
		Snippet: value: enums.FadingMode = driver.configure.fading.fsimulator.dshift.get_mode() \n
		Sets the Doppler shift mode. \n
			:return: mode: NORMal | USER NORMal: the maximum Doppler frequency is determined by the fading profile USER: the maximum Doppler frequency can be adjusted manually
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:DSHift:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadingMode)

	def set_mode(self, mode: enums.FadingMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:FADing:FSIMulator:DSHift:MODE \n
		Snippet: driver.configure.fading.fsimulator.dshift.set_mode(mode = enums.FadingMode.NORMal) \n
		Sets the Doppler shift mode. \n
			:param mode: NORMal | USER NORMal: the maximum Doppler frequency is determined by the fading profile USER: the maximum Doppler frequency can be adjusted manually
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FadingMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:DSHift:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:FADing:FSIMulator:DSHift \n
		Snippet: value: float = driver.configure.fading.fsimulator.dshift.get_value() \n
		Displays the maximum Doppler frequency for the fading simulator. A setting is only allowed in USER mode (see method
		RsCmwGsmSig.Configure.Fading.Fsimulator.Dshift.mode) . \n
			:return: frequency: Range: 1 Hz to 2000 Hz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:DSHift?')
		return Conversions.str_to_float(response)

	def set_value(self, frequency: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:FADing:FSIMulator:DSHift \n
		Snippet: driver.configure.fading.fsimulator.dshift.set_value(frequency = 1.0) \n
		Displays the maximum Doppler frequency for the fading simulator. A setting is only allowed in USER mode (see method
		RsCmwGsmSig.Configure.Fading.Fsimulator.Dshift.mode) . \n
			:param frequency: Range: 1 Hz to 2000 Hz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:DSHift {param}')
