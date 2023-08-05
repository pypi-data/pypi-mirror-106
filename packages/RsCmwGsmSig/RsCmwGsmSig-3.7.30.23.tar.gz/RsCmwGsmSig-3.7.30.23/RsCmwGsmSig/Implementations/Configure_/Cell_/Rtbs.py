from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtbs:
	"""Rtbs commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rtbs", core, parent)

	def get_cswitched(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:RTBS[:CSWitched] \n
		Snippet: value: int = driver.configure.cell.rtbs.get_cswitched() \n
		Defines the time period after which an existing, but interrupted connection is aborted by the R&S CMW ('Radiolink Timeout
		BS') . \n
			:return: time: Number of missing SACCH blocks Range: 4 to 64
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RTBS:CSWitched?')
		return Conversions.str_to_int(response)

	def set_cswitched(self, time: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:RTBS[:CSWitched] \n
		Snippet: driver.configure.cell.rtbs.set_cswitched(time = 1) \n
		Defines the time period after which an existing, but interrupted connection is aborted by the R&S CMW ('Radiolink Timeout
		BS') . \n
			:param time: Number of missing SACCH blocks Range: 4 to 64
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RTBS:CSWitched {param}')
