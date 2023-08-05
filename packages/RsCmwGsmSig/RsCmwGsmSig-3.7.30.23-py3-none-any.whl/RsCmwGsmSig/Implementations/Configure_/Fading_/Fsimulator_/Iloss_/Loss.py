from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Loss:
	"""Loss commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("loss", core, parent)

	def get_user(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:FADing:FSIMulator:ILOSs:LOSS[:USER] \n
		Snippet: value: float = driver.configure.fading.fsimulator.iloss.loss.get_user() \n
		Sets the insertion loss for the fading simulator. A setting is only allowed in USER mode (see method RsCmwGsmSig.
		Configure.Fading.Fsimulator.Iloss.mode) . \n
			:return: insertion_loss: Range: 0 dB to 18 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:LOSS:USER?')
		return Conversions.str_to_float(response)

	def set_user(self, insertion_loss: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:FADing:FSIMulator:ILOSs:LOSS[:USER] \n
		Snippet: driver.configure.fading.fsimulator.iloss.loss.set_user(insertion_loss = 1.0) \n
		Sets the insertion loss for the fading simulator. A setting is only allowed in USER mode (see method RsCmwGsmSig.
		Configure.Fading.Fsimulator.Iloss.mode) . \n
			:param insertion_loss: Range: 0 dB to 18 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(insertion_loss)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:LOSS:USER {param}')

	def get_normal(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:FADing:FSIMulator:ILOSs:LOSS:NORMal \n
		Snippet: value: float = driver.configure.fading.fsimulator.iloss.loss.get_normal() \n
		Queries the insertion loss for the fading simulator. The command is only relevant in NORMal mode (see method RsCmwGsmSig.
		Configure.Fading.Fsimulator.Iloss.mode) . \n
			:return: insertion_loss: Range: 0 dB to 18 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:FADing:FSIMulator:ILOSs:LOSS:NORMal?')
		return Conversions.str_to_float(response)
