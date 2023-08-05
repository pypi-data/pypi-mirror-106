from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Atimeout:
	"""Atimeout commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("atimeout", core, parent)

	def get_mtc(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:ATIMeout[:MTC] \n
		Snippet: value: int or bool = driver.configure.cell.atimeout.get_mtc() \n
		Defines the maximum time period in seconds during which the phone is ringing in the case of call to mobile (mobile
		terminated call) . If the call is not answered, the R&S CMW returns to the synchronized state. \n
			:return: time: Range: 1 s to 120 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:ATIMeout:MTC?')
		return Conversions.str_to_int_or_bool(response)

	def set_mtc(self, time: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:ATIMeout[:MTC] \n
		Snippet: driver.configure.cell.atimeout.set_mtc(time = 1) \n
		Defines the maximum time period in seconds during which the phone is ringing in the case of call to mobile (mobile
		terminated call) . If the call is not answered, the R&S CMW returns to the synchronized state. \n
			:param time: Range: 1 s to 120 s, Unit: s
		"""
		param = Conversions.decimal_or_bool_value_to_str(time)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:ATIMeout:MTC {param}')

	def get_moc(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:ATIMeout:MOC \n
		Snippet: value: int or bool = driver.configure.cell.atimeout.get_moc() \n
		Defines the time period of R&S CMW alerting state. \n
			:return: time: 0: the alerting state is skipped 1 to 255: time period the R&S CMW waits before changes to 'Call Established' state Range: 0 to 255, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:ATIMeout:MOC?')
		return Conversions.str_to_int_or_bool(response)

	def set_moc(self, time: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:ATIMeout:MOC \n
		Snippet: driver.configure.cell.atimeout.set_moc(time = 1) \n
		Defines the time period of R&S CMW alerting state. \n
			:param time: 0: the alerting state is skipped 1 to 255: time period the R&S CMW waits before changes to 'Call Established' state Range: 0 to 255, Unit: s
		"""
		param = Conversions.decimal_or_bool_value_to_str(time)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:ATIMeout:MOC {param}')
