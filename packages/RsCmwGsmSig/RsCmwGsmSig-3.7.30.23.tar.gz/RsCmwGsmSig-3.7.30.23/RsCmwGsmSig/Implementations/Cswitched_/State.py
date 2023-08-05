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
	def fetch(self) -> enums.CswState:
		"""SCPI: FETCh:GSM:SIGNaling<Instance>:CSWitched:STATe \n
		Snippet: value: enums.CswState = driver.cswitched.state.fetch() \n
		Returns the CS connection state. Use method RsCmwGsmSig.Call.Cswitched.action to initiate a transition between different
		connection states. The CS state changes to ON when the signaling generator is started (see method RsCmwGsmSig.Source.Cell.
		State.value) . To make sure that a GSM cell signal is available, query the cell state. It must be ON, ADJ (see method
		RsCmwGsmSig.Source.Cell.State.all) . \n
			:return: cs_state: OFF | ON | SYNC | ALER | CEST | LUPD | CONN | REL | IMS | SMESsage | RMESsage | IHANdover | OHANdover For a description of the states, refer to 'Connection States'. The values indicate the following states: SYNC = synchronized ALER = alerting CEST = call established LUPD = location update CONN = connecting REL = releasing IMS = IMSI detach SMESsage = sending message RMESsage = receiving message IHANdover = incoming handover in progress OHANdover = outgoing handover in progress"""
		response = self._core.io.query_str(f'FETCh:GSM:SIGNaling<Instance>:CSWitched:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.CswState)
