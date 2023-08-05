from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.HandoverState:
		"""SCPI: FETCh:GSM:SIGNaling<Instance>:HANDover:STATe \n
		Snippet: value: enums.HandoverState = driver.handover.state.fetch() \n
		Returns whether the BCCH and the TCH are in different GSM bands. Initially both channels use the same band, but the band
		used by the TCH can be changed via a dual-band handover. A disconnect resets the parameter. \n
			:return: handover_state: OFF | DUALband OFF: BCCH channel and TCH channel are in the same GSM band - either because no handover at all has been performed or the last handover target was the original band DUALband: Dual-band handover to another GSM band has been performed successfully; BCCH and TCH are in different GSM bands"""
		response = self._core.io.query_str(f'FETCh:GSM:SIGNaling<Instance>:HANDover:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.HandoverState)
