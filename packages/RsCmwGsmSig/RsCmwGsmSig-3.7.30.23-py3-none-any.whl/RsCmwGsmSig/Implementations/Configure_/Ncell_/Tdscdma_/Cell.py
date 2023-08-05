from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: CellNo, default value after init: CellNo.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_cellNo_get', 'repcap_cellNo_set', repcap.CellNo.Nr1)

	def repcap_cellNo_set(self, enum_value: repcap.CellNo) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CellNo.Default
		Default value after init: CellNo.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_cellNo_get(self) -> repcap.CellNo:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the entry
			- Band: enums.OperBandTdsCdma: OB1 | OB2 | OB3 OB1: Band 1 (F) , 1880.8 MHz to 1919.2 MHz OB2: Band 2 (A) , 2010.8 MHz to 2024.2 MHz OB3: Band 3 (E) , 2300.8 MHz to 2399.2 MHz
			- Channel: int: Range: depends on operating band, see table below
			- Cell_Parameter_Id: str: Scrambling code Range: #H0 to #H7F
			- Measurement: bool: Optional setting parameter. OFF | ON Enables or disables the MS neighbor cell measurement"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.OperBandTdsCdma),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_raw_str('Cell_Parameter_Id'),
			ArgStruct.scalar_bool('Measurement')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.OperBandTdsCdma = None
			self.Channel: int = None
			self.Cell_Parameter_Id: str = None
			self.Measurement: bool = None

	def set(self, structure: CellStruct, cellNo=repcap.CellNo.Default) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:TDSCdma:CELL<n> \n
		Snippet: driver.configure.ncell.tdscdma.cell.set(value = [PROPERTY_STRUCT_NAME](), cellNo = repcap.CellNo.Default) \n
		Configures an entry of the neighbor cell list for TD-SCDMA. \n
			:param structure: for set value, see the help for CellStruct structure arguments.
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')"""
		cellNo_cmd_val = self._base.get_repcap_cmd_value(cellNo, repcap.CellNo)
		self._core.io.write_struct(f'CONFigure:GSM:SIGNaling<Instance>:NCELl:TDSCdma:CELL{cellNo_cmd_val}', structure)

	def get(self, cellNo=repcap.CellNo.Default) -> CellStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:TDSCdma:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.tdscdma.cell.get(cellNo = repcap.CellNo.Default) \n
		Configures an entry of the neighbor cell list for TD-SCDMA. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cellNo_cmd_val = self._base.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'CONFigure:GSM:SIGNaling<Instance>:NCELl:TDSCdma:CELL{cellNo_cmd_val}?', self.__class__.CellStruct())

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
