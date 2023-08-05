from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handover:
	"""Handover commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handover", core, parent)

	def start(self) -> None:
		"""SCPI: CALL:GSM:SIGNaling<Instance>:HANDover:STARt \n
		Snippet: driver.call.handover.start() \n
		Initiates a handover to a network selected via method RsCmwGsmSig.Prepare.Handover.target. \n
		"""
		self._core.io.write(f'CALL:GSM:SIGNaling<Instance>:HANDover:STARt')

	def start_with_opc(self) -> None:
		"""SCPI: CALL:GSM:SIGNaling<Instance>:HANDover:STARt \n
		Snippet: driver.call.handover.start_with_opc() \n
		Initiates a handover to a network selected via method RsCmwGsmSig.Prepare.Handover.target. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CALL:GSM:SIGNaling<Instance>:HANDover:STARt')
