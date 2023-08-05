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

	def get(self, gsmCellNo=repcap.GsmCellNo.Nr1) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:RREPort:NCELl:GSM:CELL<nr> \n
		Snippet: value: int = driver.sense.rreport.ncell.gsm.cell.get(gsmCellNo = repcap.GsmCellNo.Nr1) \n
		Returns the RSSI value reported for a selected GSM neighbor cell as dimensionless index. \n
			:param gsmCellNo: optional repeated capability selector. Default value: Nr1
			:return: rssi: RSSI as dimensionless index Range: 0 to 63"""
		gsmCellNo_cmd_val = self._base.get_repcap_cmd_value(gsmCellNo, repcap.GsmCellNo)
		response = self._core.io.query_str(f'SENSe:GSM:SIGNaling<Instance>:RREPort:NCELl:GSM:CELL{gsmCellNo_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
