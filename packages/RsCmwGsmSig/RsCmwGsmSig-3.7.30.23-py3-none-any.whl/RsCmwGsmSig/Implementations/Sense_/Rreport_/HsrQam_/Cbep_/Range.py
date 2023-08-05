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
			- Lower: float: Range: 0 to 1.75
			- Upper: float: Range: 0.25 to 2"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: float = None
			self.Upper: float = None

	def get(self, hsrQAM=repcap.HsrQAM.Default) -> GetStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:HSRQam<ModOrder>:CBEP:RANGe \n
		Snippet: value: GetStruct = driver.sense.rreport.hsrQam.cbep.range.get(hsrQAM = repcap.HsrQAM.Default) \n
		Returns the CV BEP range, corresponding to the 'CV BEP' index reported by the MS for a 16-QAM or 32-QAM modulated DL
		signal with higher symbol rate (HSR) . \n
			:param hsrQAM: optional repeated capability selector. Default value: QAM16 (settable in the interface 'HsrQam')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		hsrQAM_cmd_val = self._base.get_repcap_cmd_value(hsrQAM, repcap.HsrQAM)
		return self._core.io.query_struct(f'SENSe:GSM:SIGNaling<Instance>:RREPort:HSRQam{hsrQAM_cmd_val}:CBEP:RANGe?', self.__class__.GetStruct())
