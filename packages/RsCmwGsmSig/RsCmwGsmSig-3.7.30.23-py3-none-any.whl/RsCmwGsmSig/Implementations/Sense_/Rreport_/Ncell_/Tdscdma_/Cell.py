from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Cell_.Range import Range
			self._range = Range(self._core, self._base)
		return self._range

	def get(self, cellNo=repcap.CellNo.Nr1) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:RREPort:NCELl:TDSCdma:CELL<nr> \n
		Snippet: value: int = driver.sense.rreport.ncell.tdscdma.cell.get(cellNo = repcap.CellNo.Nr1) \n
		Returns measurement report values for a selected TD-SCDMA neighbor cell. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1
			:return: rscp: RSCP as dimensionless index Range: -5 to 91"""
		cellNo_cmd_val = self._base.get_repcap_cmd_value(cellNo, repcap.CellNo)
		response = self._core.io.query_str(f'SENSe:GSM:SIGNaling<Instance>:RREPort:NCELl:TDSCdma:CELL{cellNo_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
