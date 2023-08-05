from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("range", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Lower: float: Range: -3.6 to -0.6
			- Upper: float: Range: -3.6 to -0.6"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: float = None
			self.Upper: float = None

	def get(self, nsrQAM=repcap.NsrQAM.Default) -> GetStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:NSRQam<ModOrder>:MBEP:RANGe \n
		Snippet: value: GetStruct = driver.sense.rreport.nsrqam.mbep.range.get(nsrQAM = repcap.NsrQAM.Default) \n
		Returns the bit error probability (BEP) range, corresponding to the mean BEP index reported by the MS for a 16-QAM or
		32-QAM modulated DL signal with normal symbol rate (NSR) . \n
			:param nsrQAM: optional repeated capability selector. Default value: QAM16 (settable in the interface 'Nsrqam')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		nsrQAM_cmd_val = self._base.get_repcap_cmd_value(nsrQAM, repcap.NsrQAM)
		return self._core.io.query_struct(f'SENSe:GSM:SIGNaling<Instance>:RREPort:NSRQam{nsrQAM_cmd_val}:MBEP:RANGe?', self.__class__.GetStruct())
