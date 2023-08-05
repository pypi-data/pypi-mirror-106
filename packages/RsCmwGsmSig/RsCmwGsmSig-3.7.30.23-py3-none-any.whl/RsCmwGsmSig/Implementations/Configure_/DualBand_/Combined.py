from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Combined:
	"""Combined commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("combined", core, parent)

	# noinspection PyTypeChecker
	class CsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperBandGsm: G085 | G09 | G18 | G19 Handover destination band/network used for TCH/PDCH: GSM 850, GSM 900, GSM 1800, GSM 1900
			- Channel: int: TCH/PDCH channel in the destination GSM band The range of values depends on the selected band ; for an overview see 'GSM Bands and Channels'. The values below are for GSM 900. Range: 512 to 885
			- Level: float: Absolute TCH/PDCH level in the destination GSM band Range: Depends on RF connector (-130 dBm to 0 dBm for RFx COM) ; please also notice the ranges quoted in the data sheet. , Unit: dBm
			- Pcl: int: PCL of the MS in the destination GSM band Range: 0 to 31
			- Timeslot: int: Timeslot for the circuit switched connection the destination GSM band Range: 1 to 7"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperBandGsm),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_int('Pcl'),
			ArgStruct.scalar_int('Timeslot')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperBandGsm = None
			self.Channel: int = None
			self.Level: float = None
			self.Pcl: int = None
			self.Timeslot: int = None

	# noinspection PyTypeChecker
	def get_cs(self) -> CsStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:DUALband:COMBined:CS \n
		Snippet: value: CsStruct = driver.configure.dualBand.combined.get_cs() \n
		Selects parameters of a handover destination and initiates a dual band GSM handover. This command executes handover even
		if the handover dialog is opened. \n
			:return: structure: for return value, see the help for CsStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:DUALband:COMBined:CS?', self.__class__.CsStruct())

	def set_cs(self, value: CsStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:DUALband:COMBined:CS \n
		Snippet: driver.configure.dualBand.combined.set_cs(value = CsStruct()) \n
		Selects parameters of a handover destination and initiates a dual band GSM handover. This command executes handover even
		if the handover dialog is opened. \n
			:param value: see the help for CsStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:DUALband:COMBined:CS', value)
