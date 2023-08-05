from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmax:
	"""Pmax commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pmax", core, parent)

	def get_bcch(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:PMAX:BCCH \n
		Snippet: value: int = driver.configure.rfSettings.pmax.get_bcch() \n
		Defines the maximum transmitter output level of the MS in any uplink (UL) timeslots. The level PMax is signaled to the MS
		under test as a power control level (PCL) value. \n
			:return: pcl: Range: 0 to 31
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RFSettings:PMAX:BCCH?')
		return Conversions.str_to_int(response)

	def set_bcch(self, pcl: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:PMAX:BCCH \n
		Snippet: driver.configure.rfSettings.pmax.set_bcch(pcl = 1) \n
		Defines the maximum transmitter output level of the MS in any uplink (UL) timeslots. The level PMax is signaled to the MS
		under test as a power control level (PCL) value. \n
			:param pcl: Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(pcl)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RFSettings:PMAX:BCCH {param}')
