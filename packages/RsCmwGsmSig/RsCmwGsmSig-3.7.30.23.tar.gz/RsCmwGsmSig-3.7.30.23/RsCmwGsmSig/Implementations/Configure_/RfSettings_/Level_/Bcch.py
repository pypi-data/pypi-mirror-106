from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bcch:
	"""Bcch commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bcch", core, parent)

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Bcch_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	def get_value(self) -> float:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:LEVel:BCCH \n
		Snippet: value: float = driver.configure.rfSettings.level.bcch.get_value() \n
		Defines the absolute level of the broadcast control channel (BCCH) .
			INTRO_CMD_HELP: The BCCH level depends on the selected scenario. \n
			- Setting the BCCH level is only allowed for scenario 'BCCH and TCH/PDCH'. The allowed range can be calculated as follows: Range (Level) = Range (Output Power) - External Attenuation - Insertion Loss + (Baseband Level + 15 dB) Range (Output Power) = -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet. Please notice the ranges of output power quoted in the data sheet. Insertion Loss is only relevant for internal fading, (Baseband Level + 15 dB) only for external fading.
			- For other scenarios, the BCCH level equals the TCH/PDCH 'DL Reference Level' with the lower level limit of -95 dBm. \n
			:return: level: Range: see above , Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:LEVel:BCCH?')
		return Conversions.str_to_float(response)

	def set_value(self, level: float) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:LEVel:BCCH \n
		Snippet: driver.configure.rfSettings.level.bcch.set_value(level = 1.0) \n
		Defines the absolute level of the broadcast control channel (BCCH) .
			INTRO_CMD_HELP: The BCCH level depends on the selected scenario. \n
			- Setting the BCCH level is only allowed for scenario 'BCCH and TCH/PDCH'. The allowed range can be calculated as follows: Range (Level) = Range (Output Power) - External Attenuation - Insertion Loss + (Baseband Level + 15 dB) Range (Output Power) = -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet. Please notice the ranges of output power quoted in the data sheet. Insertion Loss is only relevant for internal fading, (Baseband Level + 15 dB) only for external fading.
			- For other scenarios, the BCCH level equals the TCH/PDCH 'DL Reference Level' with the lower level limit of -95 dBm. \n
			:param level: Range: see above , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:LEVel:BCCH {param}')

	def clone(self) -> 'Bcch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bcch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
