from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsClass:
	"""MsClass commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("msClass", core, parent)

	def get_gprs(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:MSCLass:GPRS \n
		Snippet: value: int = driver.sense.mssInfo.msClass.get_gprs() \n
		Returns the multislot class of the mobile station in GPRS mode. \n
			:return: gprs: Range: 1 to 45
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:MSCLass:GPRS?')
		return Conversions.str_to_int(response)

	def get_egprs(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:MSCLass:EGPRs \n
		Snippet: value: int = driver.sense.mssInfo.msClass.get_egprs() \n
		Returns the multislot class of the mobile station in EGPRS mode. \n
			:return: egprs: Range: 1 to 45
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:MSCLass:EGPRs?')
		return Conversions.str_to_int(response)

	def get_dgprs(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:MSCLass:DGPRs \n
		Snippet: value: int = driver.sense.mssInfo.msClass.get_dgprs() \n
		Returns the multislot class of the mobile station in GPRS DTM mode. \n
			:return: dtm_gprs: Range: 1 to 45
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:MSCLass:DGPRs?')
		return Conversions.str_to_int(response)

	def get_degprs(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:MSCLass:DEGPrs \n
		Snippet: value: int = driver.sense.mssInfo.msClass.get_degprs() \n
		Returns the multislot class of the mobile station in EGPRS DTM mode. \n
			:return: dtm_egprs: Range: 1 to 45
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:MSCLass:DEGPrs?')
		return Conversions.str_to_int(response)
