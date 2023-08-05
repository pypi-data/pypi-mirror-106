from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Elog:
	"""Elog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("elog", core, parent)

	def set(self) -> None:
		"""SCPI: CLEan:GSM:SIGNaling<Instance>:ELOG \n
		Snippet: driver.clean.elog.set() \n
		Clears the event log. \n
		"""
		self._core.io.write(f'CLEan:GSM:SIGNaling<Instance>:ELOG')

	def set_with_opc(self) -> None:
		"""SCPI: CLEan:GSM:SIGNaling<Instance>:ELOG \n
		Snippet: driver.clean.elog.set_with_opc() \n
		Clears the event log. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CLEan:GSM:SIGNaling<Instance>:ELOG')
