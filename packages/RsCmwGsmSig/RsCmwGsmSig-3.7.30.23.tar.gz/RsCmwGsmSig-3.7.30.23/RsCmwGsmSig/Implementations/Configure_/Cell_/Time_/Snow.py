from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Snow:
	"""Snow commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("snow", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SNOW \n
		Snippet: driver.configure.cell.time.snow.set() \n
		Triggers the transfer of the date and time information to the MS. \n
		"""
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SNOW')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SNOW \n
		Snippet: driver.configure.cell.time.snow.set_with_opc() \n
		Triggers the transfer of the date and time information to the MS. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwGsmSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:GSM:SIGNaling<Instance>:CELL:TIME:SNOW')
