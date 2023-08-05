from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dtx:
	"""Dtx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dtx", core, parent)

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Enable / disable DL DTX
			- No_Data_Frames: float: Relative level in the DL DTX frames, where no SID frames and no SACCH frames are sent Range: -40 dB to 0 dB, Unit: dB
			- Sid_Frames_2_Part: float: Relative level of the second part of SID frames. This level is required for test case 3GPP 51.010-1, TC 21.1.4.2, step 64. Range: -40 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('No_Data_Frames'),
			ArgStruct.scalar_float('Sid_Frames_2_Part')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.No_Data_Frames: float = None
			self.Sid_Frames_2_Part: float = None

	def get_downlink(self) -> DownlinkStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:DTX:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.cswitched.dtx.get_downlink() \n
		Configures the discontinuous transmission of the R&S CMW. Level values are relative to the set TCH/PDCH level, see 'DL
		Reference Level'. \n
			:return: structure: for return value, see the help for DownlinkStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:DTX:DL?', self.__class__.DownlinkStruct())

	def set_downlink(self, value: DownlinkStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:DTX:DL \n
		Snippet: driver.configure.connection.cswitched.dtx.set_downlink(value = DownlinkStruct()) \n
		Configures the discontinuous transmission of the R&S CMW. Level values are relative to the set TCH/PDCH level, see 'DL
		Reference Level'. \n
			:param value: see the help for DownlinkStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:DTX:DL', value)
