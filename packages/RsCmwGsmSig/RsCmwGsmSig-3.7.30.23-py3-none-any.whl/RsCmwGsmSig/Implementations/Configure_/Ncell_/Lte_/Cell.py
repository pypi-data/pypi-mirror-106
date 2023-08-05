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
			- Band: enums.OperBandLte: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB15 | OB16 | OB17 | OB18 | OB19 | OB20 | OB21 | OB22 | OB23 | OB24 | OB25 | OB26 | OB27 | OB28 | OB29 | OB30 | OB31 | OB32 | OB33 | OB34 | OB35 | OB36 | OB37 | OB38 | OB39 | OB40 | OB41 | OB42 | OB43 | OB44 | OB45 | OB46 | OB48 | OB49 | OB50 | OB51 | OB52 | OB65 | OB66 | OB67 | OB68 | OB69 | OB70 | OB71 | OB72 | OB73 | OB74 | OB75 | OB76 | OB85 | OB250 | OB252 | OB255 Operating bands 1 to 46, 48 to 52, 65 to 76, 85, 250, 252, 255
			- Channel: int: Downlink channel number Range: Depending on operating band, see tables below
			- Cell_Id: int: Physical cell ID (scrambling code) Range: 0 to 503
			- Measurement: bool: Optional setting parameter. OFF | ON Enables or disables the MS neighbor cell measurement"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.OperBandLte),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_int('Cell_Id'),
			ArgStruct.scalar_bool('Measurement')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.OperBandLte = None
			self.Channel: int = None
			self.Cell_Id: int = None
			self.Measurement: bool = None

	def set(self, structure: CellStruct, cellNo=repcap.CellNo.Default) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:LTE:CELL<n> \n
		Snippet: driver.configure.ncell.lte.cell.set(value = [PROPERTY_STRUCT_NAME](), cellNo = repcap.CellNo.Default) \n
		Configures an entry of the neighbor cell list for LTE. \n
			:param structure: for set value, see the help for CellStruct structure arguments.
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')"""
		cellNo_cmd_val = self._base.get_repcap_cmd_value(cellNo, repcap.CellNo)
		self._core.io.write_struct(f'CONFigure:GSM:SIGNaling<Instance>:NCELl:LTE:CELL{cellNo_cmd_val}', structure)

	def get(self, cellNo=repcap.CellNo.Default) -> CellStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:LTE:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.lte.cell.get(cellNo = repcap.CellNo.Default) \n
		Configures an entry of the neighbor cell list for LTE. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cellNo_cmd_val = self._base.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'CONFigure:GSM:SIGNaling<Instance>:NCELl:LTE:CELL{cellNo_cmd_val}?', self.__class__.CellStruct())

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
