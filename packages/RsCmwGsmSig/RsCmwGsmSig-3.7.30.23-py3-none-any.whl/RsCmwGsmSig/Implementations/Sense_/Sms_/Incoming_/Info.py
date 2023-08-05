from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("info", core, parent)

	def get_dcoding(self) -> str:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:SMS:INComing:INFO:DCODing \n
		Snippet: value: str = driver.sense.sms.incoming.info.get_dcoding() \n
		Queries the short message coding. \n
			:return: message_encoding: No help available
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:SMS:INComing:INFO:DCODing?')
		return trim_str_response(response)

	def get_mtext(self) -> str:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:SMS:INComing:INFO:MTEXt \n
		Snippet: value: str = driver.sense.sms.incoming.info.get_mtext() \n
		Returns the text of the last SMS message received from the MS. Only 7-bit ASCII text is supported. \n
			:return: message_text: Message text as string
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:SMS:INComing:INFO:MTEXt?')
		return trim_str_response(response)

	def get_mlength(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:SMS:INComing:INFO:MLENgth \n
		Snippet: value: int = driver.sense.sms.incoming.info.get_mlength() \n
		Returns the length of the last SMS message received from the MS. \n
			:return: message_length: Number of characters of the message Range: 0 to 800
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:SMS:INComing:INFO:MLENgth?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	class SegmentStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Current: int: Parameter not available for the first segment Range: 2 to 12
			- Number: int: Parameter not available for the first segment Range: 2 to 12"""
		__meta_args_list = [
			ArgStruct.scalar_int('Current'),
			ArgStruct.scalar_int('Number')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Current: int = None
			self.Number: int = None

	def get_segment(self) -> SegmentStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:SMS:INComing:INFO:SEGMent \n
		Snippet: value: SegmentStruct = driver.sense.sms.incoming.info.get_segment() \n
		Queries the current and total number of segments of the concatenated SMS message. \n
			:return: structure: for return value, see the help for SegmentStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:SMS:INComing:INFO:SEGMent?', self.__class__.SegmentStruct())
