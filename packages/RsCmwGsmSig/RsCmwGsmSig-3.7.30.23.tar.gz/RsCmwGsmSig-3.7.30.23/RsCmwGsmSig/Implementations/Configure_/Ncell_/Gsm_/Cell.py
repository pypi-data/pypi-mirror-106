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
	Repeated Capability: GsmCellNo, default value after init: GsmCellNo.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_gsmCellNo_get', 'repcap_gsmCellNo_set', repcap.GsmCellNo.Nr1)

	def repcap_gsmCellNo_set(self, enum_value: repcap.GsmCellNo) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GsmCellNo.Default
		Default value after init: GsmCellNo.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_gsmCellNo_get(self) -> repcap.GsmCellNo:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the entry
			- Band: enums.OperBandGsm: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
			- Channel: int: Channel number used for the broadcast control channel (BCCH) , see 'GSM Bands and Channels' Range: depends on operating band
			- Measurement: bool: Optional setting parameter. OFF | ON Enables or disables the MS neighbor cell measurement
			- Bsic: int: Optional setting parameter. Base station identity code Range: 0 to 63"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.OperBandGsm),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_bool('Measurement'),
			ArgStruct.scalar_int('Bsic')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.OperBandGsm = None
			self.Channel: int = None
			self.Measurement: bool = None
			self.Bsic: int = None

	def set(self, structure: CellStruct, gsmCellNo=repcap.GsmCellNo.Default) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:GSM:CELL<n> \n
		Snippet: driver.configure.ncell.gsm.cell.set(value = [PROPERTY_STRUCT_NAME](), gsmCellNo = repcap.GsmCellNo.Default) \n
		Configures an entry of the neighbor cell list for GSM. For channel number ranges depending on operating bands see Table
		'GSM operating bands and frequencies'. \n
			:param structure: for set value, see the help for CellStruct structure arguments.
			:param gsmCellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')"""
		gsmCellNo_cmd_val = self._base.get_repcap_cmd_value(gsmCellNo, repcap.GsmCellNo)
		self._core.io.write_struct(f'CONFigure:GSM:SIGNaling<Instance>:NCELl:GSM:CELL{gsmCellNo_cmd_val}', structure)

	def get(self, gsmCellNo=repcap.GsmCellNo.Default) -> CellStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:GSM:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.gsm.cell.get(gsmCellNo = repcap.GsmCellNo.Default) \n
		Configures an entry of the neighbor cell list for GSM. For channel number ranges depending on operating bands see Table
		'GSM operating bands and frequencies'. \n
			:param gsmCellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		gsmCellNo_cmd_val = self._base.get_repcap_cmd_value(gsmCellNo, repcap.GsmCellNo)
		return self._core.io.query_struct(f'CONFigure:GSM:SIGNaling<Instance>:NCELl:GSM:CELL{gsmCellNo_cmd_val}?', self.__class__.CellStruct())

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
