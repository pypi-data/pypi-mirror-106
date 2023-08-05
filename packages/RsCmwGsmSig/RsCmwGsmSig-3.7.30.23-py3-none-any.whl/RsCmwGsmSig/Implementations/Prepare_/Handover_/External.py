from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("external", core, parent)

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.HandoverDestination:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:DESTination \n
		Snippet: value: enums.HandoverDestination = driver.prepare.handover.external.get_destination() \n
		Selects the target radio access technology for handover to another instrument. \n
			:return: destination: LTE | GSM | WCDMa | TDSCdma
		"""
		response = self._core.io.query_str('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.HandoverDestination)

	def set_destination(self, destination: enums.HandoverDestination) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:DESTination \n
		Snippet: driver.prepare.handover.external.set_destination(destination = enums.HandoverDestination.CDMA) \n
		Selects the target radio access technology for handover to another instrument. \n
			:param destination: LTE | GSM | WCDMa | TDSCdma
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.HandoverDestination)
		self._core.io.write(f'PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:DESTination {param}')

	# noinspection PyTypeChecker
	class LteStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperBandLte: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB15 | OB16 | OB17 | OB18 | OB19 | OB20 | OB21 | OB22 | OB23 | OB24 | OB25 | OB26 | OB27 | OB28 | OB29 | OB30 | OB31 | OB32 | OB33 | OB34 | OB35 | OB36 | OB37 | OB38 | OB39 | OB40 | OB41 | OB42 | OB43 | OB44 | OB45 | OB46 | OB48 | OB49 | OB50 | OB51 | OB52 | OB65 | OB66 | OB67 | OB68 | OB69 | OB70 | OB71 | OB72 | OB73 | OB74 | OB75 | OB76 | OB85 | OB250 | OB252 | OB255 Operating bands 1 to 46, 48 to 52, 65 to 76, 85, 250, 252, 255
			- Dl_Channel: int: Downlink channel number Range: The allowed range depends on the LTE band, see table below."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperBandLte),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperBandLte = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_lte(self) -> LteStruct:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:LTE \n
		Snippet: value: LteStruct = driver.prepare.handover.external.get_lte() \n
		Configures the destination parameters for handover to an LTE destination at another instrument. \n
			:return: structure: for return value, see the help for LteStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:LTE?', self.__class__.LteStruct())

	def set_lte(self, value: LteStruct) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:LTE \n
		Snippet: driver.prepare.handover.external.set_lte(value = LteStruct()) \n
		Configures the destination parameters for handover to an LTE destination at another instrument. \n
			:param value: see the help for LteStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:LTE', value)

	# noinspection PyTypeChecker
	class GsmStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperBandGsm: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
			- Dl_Channel: int: Channel number used for the broadcast control channel (BCCH) Range: 0 to 1023, depending on GSM band
			- Band_Indicator: enums.BandIndicator: G18 | G19 Band indicator for distinction of GSM 1800 and GSM 1900 bands. The two bands partially use the same channel numbers for different frequencies."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperBandGsm),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum('Band_Indicator', enums.BandIndicator)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperBandGsm = None
			self.Dl_Channel: int = None
			self.Band_Indicator: enums.BandIndicator = None

	# noinspection PyTypeChecker
	def get_gsm(self) -> GsmStruct:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:GSM \n
		Snippet: value: GsmStruct = driver.prepare.handover.external.get_gsm() \n
		Configures the destination parameters for handover to a GSM destination at another instrument. For channel number ranges
		depending on operating bands see 'GSM Bands and Channels'. \n
			:return: structure: for return value, see the help for GsmStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:GSM?', self.__class__.GsmStruct())

	def set_gsm(self, value: GsmStruct) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:GSM \n
		Snippet: driver.prepare.handover.external.set_gsm(value = GsmStruct()) \n
		Configures the destination parameters for handover to a GSM destination at another instrument. For channel number ranges
		depending on operating bands see 'GSM Bands and Channels'. \n
			:param value: see the help for GsmStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:GSM', value)

	# noinspection PyTypeChecker
	class CdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band_Class: enums.BandClass: No parameter help available
			- Dl_Channel: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Class', enums.BandClass),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Class: enums.BandClass = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_cdma(self) -> CdmaStruct:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:CDMA \n
		Snippet: value: CdmaStruct = driver.prepare.handover.external.get_cdma() \n
		No command help available \n
			:return: structure: for return value, see the help for CdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:CDMA?', self.__class__.CdmaStruct())

	def set_cdma(self, value: CdmaStruct) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:CDMA \n
		Snippet: driver.prepare.handover.external.set_cdma(value = CdmaStruct()) \n
		No command help available \n
			:param value: see the help for CdmaStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:CDMA', value)

	# noinspection PyTypeChecker
	class EvdoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band_Class: enums.BandClass: No parameter help available
			- Dl_Channel: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Class', enums.BandClass),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Class: enums.BandClass = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_evdo(self) -> EvdoStruct:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:EVDO \n
		Snippet: value: EvdoStruct = driver.prepare.handover.external.get_evdo() \n
		No command help available \n
			:return: structure: for return value, see the help for EvdoStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:EVDO?', self.__class__.EvdoStruct())

	def set_evdo(self, value: EvdoStruct) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:EVDO \n
		Snippet: driver.prepare.handover.external.set_evdo(value = EvdoStruct()) \n
		No command help available \n
			:param value: see the help for EvdoStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:EVDO', value)

	# noinspection PyTypeChecker
	class WcdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperBandWcdma: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB19 | OB20 | OB21 | OBS1 | OBS2 | OBS3 | OBL1 | OB22 | OB25 | OB26 OB1, ..., OB14: operating band I to XIV OB19, ..., OB22: operating band XIX to XXII OB25: operating band XXV OB26: operating band XXVI OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L
			- Dl_Channel: int: Downlink channel number Range: 412 to 11000, depending on operating band, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperBandWcdma),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperBandWcdma = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_wcdma(self) -> WcdmaStruct:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:WCDMa \n
		Snippet: value: WcdmaStruct = driver.prepare.handover.external.get_wcdma() \n
		Configures the destination parameters for handover to a WCDMA destination at another instrument. \n
			:return: structure: for return value, see the help for WcdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:WCDMa?', self.__class__.WcdmaStruct())

	def set_wcdma(self, value: WcdmaStruct) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:WCDMa \n
		Snippet: driver.prepare.handover.external.set_wcdma(value = WcdmaStruct()) \n
		Configures the destination parameters for handover to a WCDMA destination at another instrument. \n
			:param value: see the help for WcdmaStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:WCDMa', value)

	# noinspection PyTypeChecker
	class TdscdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperBandTdsCdma: OB1 | OB2 | OB3 OB1: Band 1 (F) , 1880 MHz to 1920 MHz OB2: Band 2 (A) , 2010 MHz to 2025 MHz OB3: Band 3 (E) , 2300 MHz to 2400 MHz
			- Dl_Channel: int: Downlink channel number Range: The allowed range depends on the frequency band, see table below."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperBandTdsCdma),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperBandTdsCdma = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_tdscdma(self) -> TdscdmaStruct:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:TDSCdma \n
		Snippet: value: TdscdmaStruct = driver.prepare.handover.external.get_tdscdma() \n
		Configures the destination parameters for handover to a TD-SCDMA destination at another instrument. \n
			:return: structure: for return value, see the help for TdscdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:TDSCdma?', self.__class__.TdscdmaStruct())

	def set_tdscdma(self, value: TdscdmaStruct) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:EXTernal:TDSCdma \n
		Snippet: driver.prepare.handover.external.set_tdscdma(value = TdscdmaStruct()) \n
		Configures the destination parameters for handover to a TD-SCDMA destination at another instrument. \n
			:param value: see the help for TdscdmaStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:GSM:SIGNaling<Instance>:HANDover:EXTernal:TDSCdma', value)
