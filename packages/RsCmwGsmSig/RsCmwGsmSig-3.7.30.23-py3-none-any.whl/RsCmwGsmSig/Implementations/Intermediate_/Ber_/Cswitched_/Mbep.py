from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbep:
	"""Mbep commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mbep", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator' Zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Number_Of_Results: int: Total number of segments to be displayed Range: 0 to 10
			- Seg_Reliability: List[int]: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see Reliability parameter.
			- Rx_Quality_Full: List[int]: RX quality full as dimensionless index measured over the full set of TDMA frames Range: 0 to 7
			- Rx_Quality_Sub: List[int]: RX quality sub as dimensionless index measured in a subset of 4 SACCH frames Range: 0 to 7
			- Mean_Bep: List[int]: Mean BEP as dimensionless index Range: 0 to 31
			- Cv_Bep: List[int]: Coefficient of variation of BEP as dimensionless index Range: 0 to 7
			- Number_Of_Blocks: List[int]: Number of already correctly decoded blocks Range: 0 to 24
			- Tdma_Frame_Nr: List[int]: Current TDMA frame number Range: 0 to 2715647
			- Ber: List[float]: BER result (for mean BEP and signal quality mode) Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Number_Of_Results'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Rx_Quality_Full', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Rx_Quality_Sub', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mean_Bep', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cv_Bep', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Number_Of_Blocks', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tdma_Frame_Nr', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Ber', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Number_Of_Results: int = None
			self.Seg_Reliability: List[int] = None
			self.Rx_Quality_Full: List[int] = None
			self.Rx_Quality_Sub: List[int] = None
			self.Mean_Bep: List[int] = None
			self.Cv_Bep: List[int] = None
			self.Number_Of_Blocks: List[int] = None
			self.Tdma_Frame_Nr: List[int] = None
			self.Ber: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:CSWitched:MBEP \n
		Snippet: value: FetchStruct = driver.intermediate.ber.cswitched.mbep.fetch() \n
		Returns the intermediate results of the BER CS measurement in mean BEP and signal quality mode. As indicated in the
		parameter descriptions below, each measure mode provides valid results for a subset of the parameters only. For the other
		parameters INV is returned. Results return as follows: <Reliability>, <NumberOfResults>, {<SegReliability>,
		<RXQualityFull>, <RXQualitySub>, <MeanBEP>, <CV_BEP>, <NumberOfBlocks>, <TDMA_FrameNr>, <BER>}segment 1, {...}seg. 2, ...,
		{...}<NumberOfResults> For the details of measure modes and results, see 'BER CS Measurement'. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:CSWitched:MBEP?', self.__class__.FetchStruct())
