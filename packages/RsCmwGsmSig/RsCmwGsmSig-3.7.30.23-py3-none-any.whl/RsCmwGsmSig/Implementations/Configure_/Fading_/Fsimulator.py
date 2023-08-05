from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fsimulator:
	"""Fsimulator commands group definition. 11 total commands, 4 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fsimulator", core, parent)

	@property
	def globale(self):
		"""globale commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_globale'):
			from .Fsimulator_.Globale import Globale
			self._globale = Globale(self._core, self._base)
		return self._globale

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_restart'):
			from .Fsimulator_.Restart import Restart
			self._restart = Restart(self._core, self._base)
		return self._restart

	@property
	def iloss(self):
		"""iloss commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_iloss'):
			from .Fsimulator_.Iloss import Iloss
			self._iloss = Iloss(self._core, self._base)
		return self._iloss

	@property
	def dshift(self):
		"""dshift commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dshift'):
			from .Fsimulator_.Dshift import Dshift
			self._dshift = Dshift(self._core, self._base)
		return self._dshift

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ENABle \n
		Snippet: value: bool = driver.configure.fading.fsimulator.get_enable() \n
		Enables or disables the fading simulator. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ENABle \n
		Snippet: driver.configure.fading.fsimulator.set_enable(enable = False) \n
		Enables or disables the fading simulator. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ENABle {param}')

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.FadingStandard:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:STANdard \n
		Snippet: value: enums.FadingStandard = driver.configure.fading.fsimulator.get_standard() \n
		Selects one of the multipath propagation condition profiles defined in annex C.3 of 3GPP TS 45.005. \n
			:return: standard: TI5 | T1P5 | T3 | T3P6 | T6 | T50 | T60 | T100 | H100 | H120 | H200 | R130 | R250 | R300 | R500 | E50 | E60 | E100 | T25 | TU1P5 | TU3 | TU25 | TU50 | HT100 The letter indicates the type of the model as follows: TI: TI (2 path) T: TUx (6 path) H: HTx (6 path) R: RAx (6 path) E: EQx (6 path) TU: TUx (12 path) HT: HTx (12 path) The number indicates the speed of the mobile in km/h. Example: HT100 means 100 km/h, T1P5 means 1.5 km/h.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.FadingStandard)

	def set_standard(self, standard: enums.FadingStandard) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:STANdard \n
		Snippet: driver.configure.fading.fsimulator.set_standard(standard = enums.FadingStandard.E100) \n
		Selects one of the multipath propagation condition profiles defined in annex C.3 of 3GPP TS 45.005. \n
			:param standard: TI5 | T1P5 | T3 | T3P6 | T6 | T50 | T60 | T100 | H100 | H120 | H200 | R130 | R250 | R300 | R500 | E50 | E60 | E100 | T25 | TU1P5 | TU3 | TU25 | TU50 | HT100 The letter indicates the type of the model as follows: TI: TI (2 path) T: TUx (6 path) H: HTx (6 path) R: RAx (6 path) E: EQx (6 path) TU: TUx (12 path) HT: HTx (12 path) The number indicates the speed of the mobile in km/h. Example: HT100 means 100 km/h, T1P5 means 1.5 km/h.
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.FadingStandard)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:STANdard {param}')

	def clone(self) -> 'Fsimulator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fsimulator(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
