from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("range", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Rssi_Lower: int: RSSI minimum value Range: -110 dBm to -48 dBm, Unit: dBm
			- Rssi_Upper: int: RSSI maximum value Range: -110 dBm to -48 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rssi_Lower'),
			ArgStruct.scalar_int('Rssi_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rssi_Lower: int = None
			self.Rssi_Upper: int = None

	def get(self, gsmCellNo=repcap.GsmCellNo.Nr1) -> GetStruct:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:RREPort:NCELl:GSM:CELL<nr>:RANGe \n
		Snippet: value: GetStruct = driver.sense.rreport.ncell.gsm.cell.range.get(gsmCellNo = repcap.GsmCellNo.Nr1) \n
		Returns the value range corresponding to the dimensionless RSSI index value reported for a selected GSM neighbor cell. \n
			:param gsmCellNo: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		gsmCellNo_cmd_val = self._base.get_repcap_cmd_value(gsmCellNo, repcap.GsmCellNo)
		return self._core.io.query_struct(f'SENSe:GSM:SIGNaling<Instance>:RREPort:NCELl:GSM:CELL{gsmCellNo_cmd_val}:RANGe?', self.__class__.GetStruct())
