from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("info", core, parent)

	# noinspection PyTypeChecker
	class SegmentStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Current: int: Parameter invalid for the first segment Range: 2 to 6
			- Number: int: Parameter invalid for the first segment Range: 2 to 6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Current'),
			ArgStruct.scalar_int('Number')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Current: int = None
			self.Number: int = None

	def get_segment(self) -> SegmentStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:SMS:OUTGoing:INFO:SEGMent \n
		Snippet: value: SegmentStruct = driver.sense.sms.outgoing.info.get_segment() \n
		Displays the currently processed SMS segment and the total number of segments. \n
			:return: structure: for return value, see the help for SegmentStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:SMS:OUTGoing:INFO:SEGMent?', self.__class__.SegmentStruct())

	# noinspection PyTypeChecker
	def get_lmsent(self) -> enums.LastMessageSent:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:SMS:OUTGoing:INFO:LMSent \n
		Snippet: value: enums.LastMessageSent = driver.sense.sms.outgoing.info.get_lmsent() \n
		Queries the status of the last sent message. \n
			:return: last_message_sent: SUCCessful | FAILed
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:SMS:OUTGoing:INFO:LMSent?')
		return Conversions.str_to_scalar_enum(response, enums.LastMessageSent)
