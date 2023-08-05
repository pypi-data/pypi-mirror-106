from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iloss:
	"""Iloss commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iloss", core, parent)

	@property
	def loss(self):
		"""loss commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_loss'):
			from .Iloss_.Loss import Loss
			self._loss = Loss(self._core, self._base)
		return self._loss

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.InsertLossMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:MODE \n
		Snippet: value: enums.InsertLossMode = driver.configure.fading.fsimulator.iloss.get_mode() \n
		Sets the insertion loss mode. \n
			:return: insert_loss_mode: NORMal | USER NORMal: the insertion loss is determined by the fading profile USER: the insertion loss can be adjusted manually
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.InsertLossMode)

	def set_mode(self, insert_loss_mode: enums.InsertLossMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:MODE \n
		Snippet: driver.configure.fading.fsimulator.iloss.set_mode(insert_loss_mode = enums.InsertLossMode.LACP) \n
		Sets the insertion loss mode. \n
			:param insert_loss_mode: NORMal | USER NORMal: the insertion loss is determined by the fading profile USER: the insertion loss can be adjusted manually
		"""
		param = Conversions.enum_scalar_to_str(insert_loss_mode, enums.InsertLossMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:MODE {param}')

	def get_csamples(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:FADing:FSIMulator:ILOSs:CSAMples \n
		Snippet: value: float = driver.configure.fading.fsimulator.iloss.get_csamples() \n
		Displays the percentage of clipped samples. \n
			:return: clipped_samples: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:CSAMples?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Iloss':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iloss(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
