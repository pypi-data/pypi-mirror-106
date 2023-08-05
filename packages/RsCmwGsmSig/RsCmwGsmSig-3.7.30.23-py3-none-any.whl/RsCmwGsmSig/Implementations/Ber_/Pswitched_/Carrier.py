from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability Indicator'
			- Frames: List[int]: No parameter help available
			- Frames_All: int: decimal Total number of already transmitted blocks Range: 0 to 500E+3
			- Ber: List[float]: No parameter help available
			- Berall: float: float BER result as weighted average over all timeslots Range: 0 % to 100 %, Unit: %
			- Dbler: List[float]: No parameter help available
			- Dbler_All: float: float DBLER result as weighted average over all timeslots Range: 0 % to 100 %, Unit: %
			- Usf_Bler: List[float]: No parameter help available
			- Usf_Bler_All: float: float USF BLER result as weighted average over all timeslots Range: 0 % to 100 %, Unit: %
			- False_Usf_Det: List[float]: No parameter help available
			- False_Usf_Det_All: float: No parameter help available
			- Non_Assigned_Usf: List[int]: No parameter help available
			- Non_Assign_Usfa_Ll: int: No parameter help available
			- Crc_Errors: List[float]: No parameter help available
			- Crc_Errors_All: float: float CRC error result as weighted average over all timeslots Range: 0 to 500E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Frames', DataType.IntegerList, None, False, False, 8),
			ArgStruct.scalar_int('Frames_All'),
			ArgStruct('Ber', DataType.FloatList, None, False, False, 8),
			ArgStruct.scalar_float('Berall'),
			ArgStruct('Dbler', DataType.FloatList, None, False, False, 8),
			ArgStruct.scalar_float('Dbler_All'),
			ArgStruct('Usf_Bler', DataType.FloatList, None, False, False, 8),
			ArgStruct.scalar_float('Usf_Bler_All'),
			ArgStruct('False_Usf_Det', DataType.FloatList, None, False, False, 8),
			ArgStruct.scalar_float('False_Usf_Det_All'),
			ArgStruct('Non_Assigned_Usf', DataType.IntegerList, None, False, False, 8),
			ArgStruct.scalar_int('Non_Assign_Usfa_Ll'),
			ArgStruct('Crc_Errors', DataType.FloatList, None, False, False, 8),
			ArgStruct.scalar_float('Crc_Errors_All')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Frames: List[int] = None
			self.Frames_All: int = None
			self.Ber: List[float] = None
			self.Berall: float = None
			self.Dbler: List[float] = None
			self.Dbler_All: float = None
			self.Usf_Bler: List[float] = None
			self.Usf_Bler_All: float = None
			self.False_Usf_Det: List[float] = None
			self.False_Usf_Det_All: float = None
			self.Non_Assigned_Usf: List[int] = None
			self.Non_Assign_Usfa_Ll: int = None
			self.Crc_Errors: List[float] = None
			self.Crc_Errors_All: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:SIGNaling<Instance>:BER:PSWitched:CARRier<Carrier> \n
		Snippet: value: ResultData = driver.ber.pswitched.carrier.read() \n
		Returns the results of the BER PS measurement. For details concerning the results, see 'BER PS Measurement'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:SIGNaling<Instance>:BER:PSWitched:CARRier1?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:SIGNaling<Instance>:BER:PSWitched:CARRier<Carrier> \n
		Snippet: value: ResultData = driver.ber.pswitched.carrier.fetch() \n
		Returns the results of the BER PS measurement. For details concerning the results, see 'BER PS Measurement'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:SIGNaling<Instance>:BER:PSWitched:CARRier1?', self.__class__.ResultData())
