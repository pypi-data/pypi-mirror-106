from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbep:
	"""Mbep commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mbep", core, parent)

	@property
	def enhanced(self):
		"""enhanced commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enhanced'):
			from .Mbep_.Enhanced import Enhanced
			self._enhanced = Enhanced(self._core, self._base)
		return self._enhanced

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator' Zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Number_Of_Results: int: Total number of segments to be displayed Range: 0 to 10
			- Seg_Reliability: List[int]: Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see Reliability parameter.
			- Mean_Bep_Gmsk: List[int]: Mean BEP (GMSK) as dimensionless index Range: 0 to 31
			- Cv_Bep_Gmsk: List[int]: Coefficient of variation of BEP (GMSK) as dimensionless index Range: 0 to 7
			- Mean_Bep_8_Psk: List[int]: Mean BEP (8PSK) as dimensionless index Range: 0 to 31
			- Cv_Bep_8_Psk: List[int]: Coefficient of variation of BEP (8PSK) as dimensionless index Range: 0 to 7
			- Tdma_Frame_Nr: List[int]: Current TDMA frame number Range: 0 to 2715647
			- Ber: List[float]: Overall BER result from the start of the measurement Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Number_Of_Results'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mean_Bep_Gmsk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cv_Bep_Gmsk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mean_Bep_8_Psk', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Cv_Bep_8_Psk', DataType.IntegerList, None, False, True, 1),
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
			self.Tdma_Frame_Nr: List[int] = None
			self.Ber: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:PSWitched:MBEP \n
		Snippet: value: FetchStruct = driver.intermediate.ber.pswitched.mbep.fetch() \n
		Returns the intermediate results of the BER PS measurement for mean BEP measurement (TBF level EGPRS) in 'Mean BEP' mode.
		Results return as follows: <Reliability>, <NumberOfResults>, {<SegReliability>, <MeanBEP_GMSK>, <CV_BEP_GMSK>,
		<MeanBEP_8PSK>, <CV_BEP_8PSK>, <TDMA_FrameNr>, <BER>}segment 1, {...}seg. 2, ..., {...}<NumberOfResults> For the details
		of measure modes and results, see 'BER PS Measurement'. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:INTermediate:GSM:SIGNaling<Instance>:BER:PSWitched:MBEP?', self.__class__.FetchStruct())

	def clone(self) -> 'Mbep':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mbep(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
