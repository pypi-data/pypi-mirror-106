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
			- Rscp_Lower: int: RSCP minimum value Range: -120 dBm to -25 dBm, Unit: dBm
			- Rscp_Upper: int: RSCP maximum value Range: -120 dBm to -25 dBm, Unit: dBm
			- Ec_No_Lower: float: Ec/No minimum value Range: -24 dB to 0 dB, Unit: dB
			- Ec_No_Upper: float: Ec/No maximum value Range: -24 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rscp_Lower'),
			ArgStruct.scalar_int('Rscp_Upper'),
			ArgStruct.scalar_float('Ec_No_Lower'),
			ArgStruct.scalar_float('Ec_No_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rscp_Lower: int = None
			self.Rscp_Upper: int = None
			self.Ec_No_Lower: float = None
			self.Ec_No_Upper: float = None

	def get(self, cellNo=repcap.CellNo.Nr1) -> GetStruct:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:RREPort:NCELl:WCDMa:CELL<nr>:RANGe \n
		Snippet: value: GetStruct = driver.sense.rreport.ncell.wcdma.cell.range.get(cellNo = repcap.CellNo.Nr1) \n
		Returns the value ranges corresponding to the dimensionless index values reported for a selected WCDMA neighbor cell. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		cellNo_cmd_val = self._base.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'SENSe:GSM:SIGNaling<Instance>:RREPort:NCELl:WCDMa:CELL{cellNo_cmd_val}:RANGe?', self.__class__.GetStruct())
