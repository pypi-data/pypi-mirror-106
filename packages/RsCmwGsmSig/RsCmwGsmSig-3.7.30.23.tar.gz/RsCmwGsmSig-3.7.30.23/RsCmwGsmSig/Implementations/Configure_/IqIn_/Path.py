from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Path, default value after init: Path.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("path", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_path_get', 'repcap_path_set', repcap.Path.Nr1)

	def repcap_path_set(self, enum_value: repcap.Path) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Path.Default
		Default value after init: Path.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_path_get(self) -> repcap.Path:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class PathStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Pep: float: Peak envelope power of the incoming baseband signal Range: -60 dBFS to 0 dBFS, Unit: dBFS
			- Level: float: Average level of the incoming baseband signal (without noise) Range: depends on crest factor and level of outgoing baseband signal , Unit: dBFS"""
		__meta_args_list = [
			ArgStruct.scalar_float('Pep'),
			ArgStruct.scalar_float('Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pep: float = None
			self.Level: float = None

	def set(self, structure: PathStruct, path=repcap.Path.Default) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:IQIN:PATH<n> \n
		Snippet: driver.configure.iqIn.path.set(value = [PROPERTY_STRUCT_NAME](), path = repcap.Path.Default) \n
		Specifies properties of the baseband signal at the I/Q input. \n
			:param structure: for set value, see the help for PathStruct structure arguments.
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')"""
		path_cmd_val = self._base.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write_struct(f'CONFigure:GSM:SIGNaling<Instance>:IQIN:PATH{path_cmd_val}', structure)

	def get(self, path=repcap.Path.Default) -> PathStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:IQIN:PATH<n> \n
		Snippet: value: PathStruct = driver.configure.iqIn.path.get(path = repcap.Path.Default) \n
		Specifies properties of the baseband signal at the I/Q input. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: structure: for return value, see the help for PathStruct structure arguments."""
		path_cmd_val = self._base.get_repcap_cmd_value(path, repcap.Path)
		return self._core.io.query_struct(f'CONFigure:GSM:SIGNaling<Instance>:IQIN:PATH{path_cmd_val}?', self.__class__.PathStruct())

	def clone(self) -> 'Path':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Path(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
