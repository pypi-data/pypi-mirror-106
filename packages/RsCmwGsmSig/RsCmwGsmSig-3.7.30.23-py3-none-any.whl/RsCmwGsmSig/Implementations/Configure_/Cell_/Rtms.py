from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtms:
	"""Rtms commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rtms", core, parent)

	def get_cswitched(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:RTMS[:CSWitched] \n
		Snippet: value: int = driver.configure.cell.rtms.get_cswitched() \n
		Defines the time period after which a previously established but interrupted connection is dropped by the mobile station
		('Radiolink Timeout MS') . \n
			:return: time: Number of missing SACCH blocks, only multiples of 4 are allowed (rounded automatically) Range: 4 to 64
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RTMS:CSWitched?')
		return Conversions.str_to_int(response)

	def set_cswitched(self, time: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:RTMS[:CSWitched] \n
		Snippet: driver.configure.cell.rtms.set_cswitched(time = 1) \n
		Defines the time period after which a previously established but interrupted connection is dropped by the mobile station
		('Radiolink Timeout MS') . \n
			:param time: Number of missing SACCH blocks, only multiples of 4 are allowed (rounded automatically) Range: 4 to 64
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RTMS:CSWitched {param}')
