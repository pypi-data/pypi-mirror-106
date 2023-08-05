from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	def set_action(self, ps_action: enums.PswAction) -> None:
		"""SCPI: CALL:GSM:SIGNaling<Instance>:PSWitched:ACTion \n
		Snippet: driver.call.pswitched.set_action(ps_action = enums.PswAction.CONNect) \n
		Controls the setup and release of a packet switched GSM connection. The command initiates a transition between different
		connection states; to be queried via method RsCmwGsmSig.Pswitched.State.fetch. For details, refer to 'Connection States'. \n
			:param ps_action: CONNect | DISConnect | SMS | RPContext | HANDover Connect, disconnect, send SMS, release PDP context, handover command for cell change order
		"""
		param = Conversions.enum_scalar_to_str(ps_action, enums.PswAction)
		self._core.io.write_with_opc(f'CALL:GSM:SIGNaling<Instance>:PSWitched:ACTion {param}')
