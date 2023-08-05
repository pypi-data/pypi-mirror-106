from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	@property
	def mbep(self):
		"""mbep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mbep'):
			from .Cswitched_.Mbep import Mbep
			self._mbep = Mbep(self._core, self._base)
		return self._mbep

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Frames: int: No parameter help available
			- Ber: float: No parameter help available
			- Crc_Errors: int: No parameter help available
			- Class_Ii: float: No parameter help available
			- Class_Ib: float: No parameter help available
			- Fer: float: No parameter help available
			- L_2_Frames_Rep: float: No parameter help available
			- Error_Events: float: No parameter help available
			- Number_Sid_Frames: int: No parameter help available
			- Sid_Frame_Err_Rate: float: No parameter help available
			- False_Bfi_Rate: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Frames'),
			ArgStruct.scalar_float('Ber'),
			ArgStruct.scalar_int('Crc_Errors'),
			ArgStruct.scalar_float('Class_Ii'),
			ArgStruct.scalar_float('Class_Ib'),
			ArgStruct.scalar_float('Fer'),
			ArgStruct.scalar_float('L_2_Frames_Rep'),
			ArgStruct.scalar_float('Error_Events'),
			ArgStruct.scalar_int('Number_Sid_Frames'),
			ArgStruct.scalar_float('Sid_Frame_Err_Rate'),
			ArgStruct.scalar_float('False_Bfi_Rate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frames: int = None
			self.Ber: float = None
			self.Crc_Errors: int = None
			self.Class_Ii: float = None
			self.Class_Ib: float = None
			self.Fer: float = None
			self.L_2_Frames_Rep: float = None
			self.Error_Events: float = None
			self.Number_Sid_Frames: int = None
			self.Sid_Frame_Err_Rate: float = None
			self.False_Bfi_Rate: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:CSWitched \n
		Snippet: value: FetchStruct = driver.intermediate.ber.cswitched.fetch() \n
		No command help available \n
		Use RsCmwGsmSig.reliability.last_value to read the updated reliability indicator. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:CSWitched?', self.__class__.FetchStruct())

	def clone(self) -> 'Cswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
