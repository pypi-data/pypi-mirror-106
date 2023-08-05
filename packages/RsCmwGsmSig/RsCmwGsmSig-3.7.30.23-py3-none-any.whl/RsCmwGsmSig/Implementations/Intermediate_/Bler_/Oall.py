from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oall:
	"""Oall commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("oall", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bler: float: No parameter help available
			- Rlc_Blocks: int: No parameter help available
			- Rlc_Data_Rate: float: No parameter help available
			- Throughput: float: No parameter help available
			- Throughput_Slot: float: No parameter help available
			- Corrupted_Blocks: int: No parameter help available
			- False_Ack_Blocks: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_int('Rlc_Blocks'),
			ArgStruct.scalar_float('Rlc_Data_Rate'),
			ArgStruct.scalar_float('Throughput'),
			ArgStruct.scalar_float('Throughput_Slot'),
			ArgStruct.scalar_int('Corrupted_Blocks'),
			ArgStruct.scalar_int('False_Ack_Blocks')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bler: float = None
			self.Rlc_Blocks: int = None
			self.Rlc_Data_Rate: float = None
			self.Throughput: float = None
			self.Throughput_Slot: float = None
			self.Corrupted_Blocks: int = None
			self.False_Ack_Blocks: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:INTermediate:GSM:SIGNaling<Instance>:BLER:OALL \n
		Snippet: value: FetchStruct = driver.intermediate.bler.oall.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:INTermediate:GSM:SIGNaling<Instance>:BLER:OALL?', self.__class__.FetchStruct())
