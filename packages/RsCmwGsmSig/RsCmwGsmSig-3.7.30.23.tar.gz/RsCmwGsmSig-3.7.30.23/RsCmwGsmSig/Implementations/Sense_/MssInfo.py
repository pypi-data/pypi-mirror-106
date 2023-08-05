from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MssInfo:
	"""MssInfo commands group definition. 32 total commands, 6 Sub-groups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mssInfo", core, parent)

	@property
	def amr(self):
		"""amr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amr'):
			from .MssInfo_.Amr import Amr
			self._amr = Amr(self._core, self._base)
		return self._amr

	@property
	def msAddress(self):
		"""msAddress commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_msAddress'):
			from .MssInfo_.MsAddress import MsAddress
			self._msAddress = MsAddress(self._core, self._base)
		return self._msAddress

	@property
	def msClass(self):
		"""msClass commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_msClass'):
			from .MssInfo_.MsClass import MsClass
			self._msClass = MsClass(self._core, self._base)
		return self._msClass

	@property
	def codec(self):
		"""codec commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_codec'):
			from .MssInfo_.Codec import Codec
			self._codec = Codec(self._core, self._base)
		return self._codec

	@property
	def vamos(self):
		"""vamos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vamos'):
			from .MssInfo_.Vamos import Vamos
			self._vamos = Vamos(self._core, self._base)
		return self._vamos

	@property
	def tcapability(self):
		"""tcapability commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_tcapability'):
			from .MssInfo_.Tcapability import Tcapability
			self._tcapability = Tcapability(self._core, self._base)
		return self._tcapability

	# noinspection PyTypeChecker
	def get_rx_power(self) -> enums.RxPower:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:MSSinfo:RXPower \n
		Snippet: value: enums.RxPower = driver.sense.mssInfo.get_rx_power() \n
		Indicates the quality of the received uplink power. \n
			:return: power: OK | UFL | OFL OK: in range UFL: underflow (underdriven) OFL: overflow (overdriven)
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:RXPower?')
		return Conversions.str_to_scalar_enum(response, enums.RxPower)

	def get_apn(self) -> List[str]:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:MSSinfo:APN \n
		Snippet: value: List[str] = driver.sense.mssInfo.get_apn() \n
		Returns all access point names used by the MS during a packet data connection. \n
			:return: apn: No help available
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:APN?')
		return Conversions.str_to_str_list(response)

	def get_imsi(self) -> str:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:IMSI \n
		Snippet: value: str = driver.sense.mssInfo.get_imsi() \n
		Returns the international mobile subscriber identity (IMSI) of the mobile under test.
			INTRO_CMD_HELP: The IMSI consists of three parts: \n
			- MCC: three-digit mobile country code
			- MNC: two- or three-digit mobile network code
			- MSIN: 10- or 9-digit mobile subscriber ID \n
			:return: imsi: 'MCC MNC MSIN' (string variable)
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:IMSI?')
		return trim_str_response(response)

	def get_imei(self) -> str:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:IMEI \n
		Snippet: value: str = driver.sense.mssInfo.get_imei() \n
		Returns the international mobile station equipment identity (IMEI) of the mobile under test.
			INTRO_CMD_HELP: The IMEI consists of four parts: \n
			- TAC: 8-digit type approval code
			- SNR: six-digit serial number
			- Spare: one-digit spare bit \n
			:return: imei: 'TAC SNR Spare' (string variable)
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:IMEI?')
		return trim_str_response(response)

	def get_dnumber(self) -> str:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:DNUMber \n
		Snippet: value: str = driver.sense.mssInfo.get_dnumber() \n
		Returns the number dialed at the mobile under test (call from MS) . \n
			:return: number: 'max. 20 digits' (string variable)
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:DNUMber?')
		return trim_str_response(response)

	def get_tty(self) -> str:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:TTY \n
		Snippet: value: str = driver.sense.mssInfo.get_tty() \n
		Queries whether the MS supports cellular text telephone modem (CTM) for teletypewriter (TTY) interface. \n
			:return: tty: 'supported' | 'not supported' 'supported': CTM supported 'not supported': CTM not supported
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:MSSinfo:TTY?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	class ScategoryStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Police: bool: OFF | ON OFF: no emergency call to police ON: emergency call to police
			- Ambulance: bool: OFF | ON
			- Fire_Brigade: bool: OFF | ON
			- Marine_Guard: bool: OFF | ON
			- Mountain_Rescue: bool: OFF | ON
			- Manual: bool: OFF | ON OFF: no emergency call set up manually ON: emergency call set up manually
			- Automatical: bool: OFF | ON OFF: no emergency call set up automatically ON: emergency call set up automatically"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Police'),
			ArgStruct.scalar_bool('Ambulance'),
			ArgStruct.scalar_bool('Fire_Brigade'),
			ArgStruct.scalar_bool('Marine_Guard'),
			ArgStruct.scalar_bool('Mountain_Rescue'),
			ArgStruct.scalar_bool('Manual'),
			ArgStruct.scalar_bool('Automatical')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Police: bool = None
			self.Ambulance: bool = None
			self.Fire_Brigade: bool = None
			self.Marine_Guard: bool = None
			self.Mountain_Rescue: bool = None
			self.Manual: bool = None
			self.Automatical: bool = None

	def get_scategory(self) -> ScategoryStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:SCATegory \n
		Snippet: value: ScategoryStruct = driver.sense.mssInfo.get_scategory() \n
		Returns the service category during emergency call. \n
			:return: structure: for return value, see the help for ScategoryStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:MSSinfo:SCATegory?', self.__class__.ScategoryStruct())

	# noinspection PyTypeChecker
	class BandsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Gsm_450: bool: No parameter help available
			- Gsm_450_Gmsk: int: No parameter help available
			- Gsm_4508_Psk: enums.EightPskPowerClass: No parameter help available
			- Gsm_480: bool: No parameter help available
			- Gsm_480_Gmsk: int: No parameter help available
			- Gsm_4808_Psk: enums.EightPskPowerClass: No parameter help available
			- Gsm_750: bool: No parameter help available
			- Gsm_750_Gmsk: int: No parameter help available
			- Gsm_7508_Psk: enums.EightPskPowerClass: No parameter help available
			- Gsm_T_810: bool: No parameter help available
			- Gsmt_810_Gmsk: int: No parameter help available
			- Gsmt_8108_Psk: enums.EightPskPowerClass: No parameter help available
			- Gsm_850: bool: No parameter help available
			- Gsm_850_Gmsk: int: No parameter help available
			- Gsm_8508_Psk: enums.EightPskPowerClass: No parameter help available
			- Gsm_900_P: bool: No parameter help available
			- Gsm_900_Pgmsk: int: No parameter help available
			- Gsm_900_P_8_Psk: enums.EightPskPowerClass: No parameter help available
			- Gsm_900_E: bool: No parameter help available
			- Gsm_900_R: bool: No parameter help available
			- Gsm_900_Rgmsk: int: No parameter help available
			- Gsm_1800: bool: No parameter help available
			- Gsm_1800_Gmsk: int: No parameter help available
			- Gsm_18008_Psk: enums.EightPskPowerClass: No parameter help available
			- Gsm_1900: bool: No parameter help available
			- Gsm_1900_Gmsk: int: No parameter help available
			- Gsm_19008_Psk: enums.EightPskPowerClass: No parameter help available
			- Umts_Fdd: bool: No parameter help available
			- Umts_Tdd_384: bool: No parameter help available
			- Umts_Tdd_128: bool: No parameter help available
			- Cdma_2000: bool: OFF | ON Support of CDMA2000 technology"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Gsm_450'),
			ArgStruct.scalar_int('Gsm_450_Gmsk'),
			ArgStruct.scalar_enum('Gsm_4508_Psk', enums.EightPskPowerClass),
			ArgStruct.scalar_bool('Gsm_480'),
			ArgStruct.scalar_int('Gsm_480_Gmsk'),
			ArgStruct.scalar_enum('Gsm_4808_Psk', enums.EightPskPowerClass),
			ArgStruct.scalar_bool('Gsm_750'),
			ArgStruct.scalar_int('Gsm_750_Gmsk'),
			ArgStruct.scalar_enum('Gsm_7508_Psk', enums.EightPskPowerClass),
			ArgStruct.scalar_bool('Gsm_T_810'),
			ArgStruct.scalar_int('Gsmt_810_Gmsk'),
			ArgStruct.scalar_enum('Gsmt_8108_Psk', enums.EightPskPowerClass),
			ArgStruct.scalar_bool('Gsm_850'),
			ArgStruct.scalar_int('Gsm_850_Gmsk'),
			ArgStruct.scalar_enum('Gsm_8508_Psk', enums.EightPskPowerClass),
			ArgStruct.scalar_bool('Gsm_900_P'),
			ArgStruct.scalar_int('Gsm_900_Pgmsk'),
			ArgStruct.scalar_enum('Gsm_900_P_8_Psk', enums.EightPskPowerClass),
			ArgStruct.scalar_bool('Gsm_900_E'),
			ArgStruct.scalar_bool('Gsm_900_R'),
			ArgStruct.scalar_int('Gsm_900_Rgmsk'),
			ArgStruct.scalar_bool('Gsm_1800'),
			ArgStruct.scalar_int('Gsm_1800_Gmsk'),
			ArgStruct.scalar_enum('Gsm_18008_Psk', enums.EightPskPowerClass),
			ArgStruct.scalar_bool('Gsm_1900'),
			ArgStruct.scalar_int('Gsm_1900_Gmsk'),
			ArgStruct.scalar_enum('Gsm_19008_Psk', enums.EightPskPowerClass),
			ArgStruct.scalar_bool('Umts_Fdd'),
			ArgStruct.scalar_bool('Umts_Tdd_384'),
			ArgStruct.scalar_bool('Umts_Tdd_128'),
			ArgStruct.scalar_bool('Cdma_2000')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Gsm_450: bool = None
			self.Gsm_450_Gmsk: int = None
			self.Gsm_4508_Psk: enums.EightPskPowerClass = None
			self.Gsm_480: bool = None
			self.Gsm_480_Gmsk: int = None
			self.Gsm_4808_Psk: enums.EightPskPowerClass = None
			self.Gsm_750: bool = None
			self.Gsm_750_Gmsk: int = None
			self.Gsm_7508_Psk: enums.EightPskPowerClass = None
			self.Gsm_T_810: bool = None
			self.Gsmt_810_Gmsk: int = None
			self.Gsmt_8108_Psk: enums.EightPskPowerClass = None
			self.Gsm_850: bool = None
			self.Gsm_850_Gmsk: int = None
			self.Gsm_8508_Psk: enums.EightPskPowerClass = None
			self.Gsm_900_P: bool = None
			self.Gsm_900_Pgmsk: int = None
			self.Gsm_900_P_8_Psk: enums.EightPskPowerClass = None
			self.Gsm_900_E: bool = None
			self.Gsm_900_R: bool = None
			self.Gsm_900_Rgmsk: int = None
			self.Gsm_1800: bool = None
			self.Gsm_1800_Gmsk: int = None
			self.Gsm_18008_Psk: enums.EightPskPowerClass = None
			self.Gsm_1900: bool = None
			self.Gsm_1900_Gmsk: int = None
			self.Gsm_19008_Psk: enums.EightPskPowerClass = None
			self.Umts_Fdd: bool = None
			self.Umts_Tdd_384: bool = None
			self.Umts_Tdd_128: bool = None
			self.Cdma_2000: bool = None

	def get_bands(self) -> BandsStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:BANDs \n
		Snippet: value: BandsStruct = driver.sense.mssInfo.get_bands() \n
		Returns the supported GSM band(s) , support indicators for UMTS and CDMA2000 and the power class. \n
			:return: structure: for return value, see the help for BandsStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:MSSinfo:BANDs?', self.__class__.BandsStruct())

	# noinspection PyTypeChecker
	class EdAllocationStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Gprs: bool: OFF | ON Support of extended dynamic allocation in GPRS mode
			- Egprs: bool: OFF | ON Support of extended dynamic allocation in EGPRS mode"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Gprs'),
			ArgStruct.scalar_bool('Egprs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Gprs: bool = None
			self.Egprs: bool = None

	def get_ed_allocation(self) -> EdAllocationStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:MSSinfo:EDALlocation \n
		Snippet: value: EdAllocationStruct = driver.sense.mssInfo.get_ed_allocation() \n
		Returns support indicators for extended dynamic allocation. \n
			:return: structure: for return value, see the help for EdAllocationStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:MSSinfo:EDALlocation?', self.__class__.EdAllocationStruct())

	def clone(self) -> 'MssInfo':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MssInfo(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
