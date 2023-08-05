from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tch:
	"""Tch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tch", core, parent)

	def get_cswitched(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:PCL:TCH:CSWitched \n
		Snippet: value: int = driver.configure.rfSettings.pcl.tch.get_cswitched() \n
		Defines the MS transmitter output level in the TCH timeslot that the MS uses for circuit switched connections. The level
		is signaled to the MS under test as a power control level (PCL) value. \n
			:return: pcl: Range: 0 to 31
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:PCL:TCH:CSWitched?')
		return Conversions.str_to_int(response)

	def set_cswitched(self, pcl: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:PCL:TCH:CSWitched \n
		Snippet: driver.configure.rfSettings.pcl.tch.set_cswitched(pcl = 1) \n
		Defines the MS transmitter output level in the TCH timeslot that the MS uses for circuit switched connections. The level
		is signaled to the MS under test as a power control level (PCL) value. \n
			:param pcl: Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(pcl)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:PCL:TCH:CSWitched {param}')
