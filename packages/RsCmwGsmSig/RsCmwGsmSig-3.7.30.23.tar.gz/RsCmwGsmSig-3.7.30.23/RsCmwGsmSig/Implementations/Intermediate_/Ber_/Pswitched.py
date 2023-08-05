from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	@property
	def mbep(self):
		"""mbep commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mbep'):
			from .Pswitched_.Mbep import Mbep
			self._mbep = Mbep(self._core, self._base)
		return self._mbep

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Frames: int: No parameter help available
			- Ber: float: No parameter help available
			- Dbler: float: No parameter help available
			- Usf_Bler: float: No parameter help available
			- False_Usf_Detect: float: No parameter help available
			- Crc_Errors: float: No parameter help available
			- Non_Assigned_Usf: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Frames'),
			ArgStruct.scalar_float('Ber'),
			ArgStruct.scalar_float('Dbler'),
			ArgStruct.scalar_float('Usf_Bler'),
			ArgStruct.scalar_float('False_Usf_Detect'),
			ArgStruct.scalar_float('Crc_Errors'),
			ArgStruct.scalar_int('Non_Assigned_Usf')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Frames: int = None
			self.Ber: float = None
			self.Dbler: float = None
			self.Usf_Bler: float = None
			self.False_Usf_Detect: float = None
			self.Crc_Errors: float = None
			self.Non_Assigned_Usf: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:PSWitched \n
		Snippet: value: FetchStruct = driver.intermediate.ber.pswitched.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:PSWitched?', self.__class__.FetchStruct())

	def clone(self) -> 'Pswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
