from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enhanced:
	"""Enhanced commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enhanced", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability Indicator' Zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Number_Of_Results: int: decimal Total number of segments to be displayed Range: 0 to 10
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see Reliability parameter.
			- Mean_Bep_Gmsk: List[int]: No parameter help available
			- Cv_Bep_Gmsk: List[int]: decimal Coefficient of variation of BEP (GMSK) as dimensionless index Range: 0 to 7
			- Mean_Bep_8_Psk: List[int]: No parameter help available
			- Cv_Bep_8_Psk: List[int]: decimal Coefficient of variation of BEP (8PSK) as dimensionless index Range: 0 to 7
			- Mean_Bep_Qpsk: List[int]: No parameter help available
			- Cv_Bep_Qpsk: List[int]: decimal Coefficient of variation of BEP (QPSK) as dimensionless index Range: 0 to 7
			- Mean_Bep_16_Qam: List[int]: No parameter help available
			- Cv_Bep_16_Qam: List[int]: No parameter help available
			- Mean_Bep_32_Qam: List[int]: No parameter help available
			- Cv_Bep_32_Qam: List[int]: No parameter help available
			- Mbep_16_Qam_Hsr: List[int]: No parameter help available
			- Cbep_16_Qam_Hsr: List[int]: No parameter help available
			- Mbep_32_Qam_Hsr: List[int]: No parameter help available
			- Cbep_32_Qam_Hsr: List[int]: No parameter help available
			- Tdma_Frame_Nr: List[int]: No parameter help available
			- Ber: List[float]: float Overall BER result from the start of the measurement Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Number_Of_Results'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mean_Bep_Gmsk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cv_Bep_Gmsk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mean_Bep_8_Psk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cv_Bep_8_Psk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mean_Bep_Qpsk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cv_Bep_Qpsk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mean_Bep_16_Qam', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cv_Bep_16_Qam', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mean_Bep_32_Qam', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cv_Bep_32_Qam', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mbep_16_Qam_Hsr', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cbep_16_Qam_Hsr', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mbep_32_Qam_Hsr', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cbep_32_Qam_Hsr', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tdma_Frame_Nr', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Ber', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Number_Of_Results: int = None
			self.Seg_Reliability: List[int] = None
			self.Mean_Bep_Gmsk: List[int] = None
			self.Cv_Bep_Gmsk: List[int] = None
			self.Mean_Bep_8_Psk: List[int] = None
			self.Cv_Bep_8_Psk: List[int] = None
			self.Mean_Bep_Qpsk: List[int] = None
			self.Cv_Bep_Qpsk: List[int] = None
			self.Mean_Bep_16_Qam: List[int] = None
			self.Cv_Bep_16_Qam: List[int] = None
			self.Mean_Bep_32_Qam: List[int] = None
			self.Cv_Bep_32_Qam: List[int] = None
			self.Mbep_16_Qam_Hsr: List[int] = None
			self.Cbep_16_Qam_Hsr: List[int] = None
			self.Mbep_32_Qam_Hsr: List[int] = None
			self.Cbep_32_Qam_Hsr: List[int] = None
			self.Tdma_Frame_Nr: List[int] = None
			self.Ber: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:PSWitched:MBEP:ENHanced \n
		Snippet: value: FetchStruct = driver.intermediate.ber.pswitched.mbep.enhanced.fetch() \n
		Returns the intermediate results of the BER PS measurement for enhanced mean BEP measurement (TBF level EGPRS2-A) in
		'Mean BEP' mode. Results return as follows: <Reliability>, <NoOfResults>, {<SegReliability>, <MeanBEP_GMSK>,
		<CV_BEP_GMSK>, <MeanBEP_8PSK>, <CV_BEP_8PSK>, <MeanBEP_QPSK>, <CV_BEP_QPSK>, <MeanBEP_16QAM>, <CV_BEP_16QAM>,
		<MeanBEP_32QAM>, <CV_BEP_32QAM>, <MBEP_16QAM_HSR>, <CBEP_16QAM_HSR>, <MBEP_32QAM_HSR>, <CBEP_32QAM_HSR>, <TDMA_FrameNr>,
		<BER>}segment 1, {...}seg. 2, ..., {...}<NoOfResults> For the details of measure modes and results, see 'BER PS
		Measurement'. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:PSWitched:MBEP:ENHanced?', self.__class__.FetchStruct())
