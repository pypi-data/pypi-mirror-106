from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oall:
	"""Oall commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("oall", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Bler: float: BLER as weighted average over all timeslots Range: 0 % to 100 %, Unit: %
			- Rlc_Blocks: int: Total number of RLC data blocks received by the MS Range: 0 to 10E+7
			- Rlc_Data_Rate: float: Total data rate in all timeslots Range: 0 kbit/s to 130 kbit/s times the no. of slots, Unit: kbit/s
			- Throughput: float: Overall long-term throughput Range: 0 kbit/s to 130 kbit/s times the no. of slots, Unit: kbit/s
			- Throughput_Slot: float: Long-term throughput per slot Range: 0 kbit/s to 130 kbit/s, Unit: kbit/s
			- Corrupted_Blocks: int: Number of corrupted data blocks transmitted in DL Range: 0 to 10E+7
			- False_Ack_Blocks: int: Number of corrupted data blocks reported by the MS as fault free Range: 0 to 10E+7"""
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

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:SIGNaling<Instance>:BLER:OALL \n
		Snippet: value: ResultData = driver.bler.oall.fetch() \n
		Returns the overall results of the BLER measurement. For details, see 'BLER Measurement'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:SIGNaling<Instance>:BLER:OALL?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:SIGNaling<Instance>:BLER:OALL \n
		Snippet: value: ResultData = driver.bler.oall.read() \n
		Returns the overall results of the BLER measurement. For details, see 'BLER Measurement'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:SIGNaling<Instance>:BLER:OALL?', self.__class__.ResultData())
