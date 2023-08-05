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
	def fetch(self) -> enums.PswState:
		"""SCPI: FETCh:GSM:SIGNaling<Instance>:PSWitched:STATe \n
		Snippet: value: enums.PswState = driver.pswitched.state.fetch() \n
		Returns the PS connection state. Use method RsCmwGsmSig.Call.Pswitched.action to initiate a transition between different
		connection states. The PS state changes to ON when the signaling generator is started (see method RsCmwGsmSig.Source.Cell.
		State.value) . To make sure that a GSM cell signal is available, query the cell state. It must be ON, ADJ (see method
		RsCmwGsmSig.Source.Cell.State.all) . \n
			:return: ps_state: OFF | ON | ATT | TBF | PDP | AIPR | RAUP | PAIP | CTIP | REL | PDIP | DIPR For a description of the states, refer to 'Connection States'. The values indicate the following states: ATT = attached TBF = TBF established PDP = PDP context activated AIPR = attaching (attach in progress) RAUP = routing area update PAIP = PDP context activation (PDP context activation in progress) CTIP = connecting (connecting TBF in progress) REL = releasing PDIP = PDP context deactivation (PDP context deactivation in progress) DIPR = detaching (detach in progress)"""
		response = self._core.io.query_str(f'FETCh:GSM:SIGNaling<Instance>:PSWitched:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.PswState)
