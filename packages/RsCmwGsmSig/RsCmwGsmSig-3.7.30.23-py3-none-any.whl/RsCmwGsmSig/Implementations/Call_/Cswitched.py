from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	def set_action(self, cs_action: enums.CswAction) -> None:
		"""SCPI: CALL:GSM:SIGNaling<Instance>:CSWitched:ACTion \n
		Snippet: driver.call.cswitched.set_action(cs_action = enums.CswAction.CONNect) \n
		Controls the setup and release of a circuit switched GSM connection or sends a short message to the MS. To query the
		current CS connection state, see method RsCmwGsmSig.Cswitched.State.fetch. For background information concerning the
		state model, see 'Connection States'. \n
			:param cs_action: CONNect | DISConnect | SMS | HANDover
		"""
		param = Conversions.enum_scalar_to_str(cs_action, enums.CswAction)
		self._core.io.write_with_opc(f'CALL:GSM:SIGNaling<Instance>:CSWitched:ACTion {param}')
