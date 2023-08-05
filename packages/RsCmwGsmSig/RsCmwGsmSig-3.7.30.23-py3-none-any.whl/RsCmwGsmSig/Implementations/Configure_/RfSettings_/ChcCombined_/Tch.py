from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tch:
	"""Tch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tch", core, parent)

	# noinspection PyTypeChecker
	class CswitchedStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Channel: int: Range: 0 to 124, 940 to 1023
			- Timeslot: int: Range: 1 to 7
			- Pcl: int: Range: 0 to 31"""
		__meta_args_list = [
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_int('Timeslot'),
			ArgStruct.scalar_int('Pcl')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Channel: int = None
			self.Timeslot: int = None
			self.Pcl: int = None

	def get_cswitched(self) -> CswitchedStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:CHCCombined:TCH:CSWitched \n
		Snippet: value: CswitchedStruct = driver.configure.rfSettings.chcCombined.tch.get_cswitched() \n
		Sets/changes the GSM channel number, timeslot, and PCL. All parameters can be changed during a connection.
			INTRO_CMD_HELP: This command combines the following three commands: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:CHANnel for carrier 1
			- method RsCmwGsmSig.Configure.Connection.Cswitched.tslot
			- method RsCmwGsmSig.Configure.RfSettings.Pcl.Tch.cswitched
		The range of channel numbers depends on the selected band, for an overview see 'GSM Bands and Channels'. \n
			:return: structure: for return value, see the help for CswitchedStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:RFSettings:CHCCombined:TCH:CSWitched?', self.__class__.CswitchedStruct())

	def set_cswitched(self, value: CswitchedStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RFSettings:CHCCombined:TCH:CSWitched \n
		Snippet: driver.configure.rfSettings.chcCombined.tch.set_cswitched(value = CswitchedStruct()) \n
		Sets/changes the GSM channel number, timeslot, and PCL. All parameters can be changed during a connection.
			INTRO_CMD_HELP: This command combines the following three commands: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:CHANnel for carrier 1
			- method RsCmwGsmSig.Configure.Connection.Cswitched.tslot
			- method RsCmwGsmSig.Configure.RfSettings.Pcl.Tch.cswitched
		The range of channel numbers depends on the selected band, for an overview see 'GSM Bands and Channels'. \n
			:param value: see the help for CswitchedStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:RFSettings:CHCCombined:TCH:CSWitched', value)
