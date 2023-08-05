from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 69 total commands, 13 Sub-groups, 25 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def reSelection(self):
		"""reSelection commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_reSelection'):
			from .Cell_.ReSelection import ReSelection
			self._reSelection = ReSelection(self._core, self._base)
		return self._reSelection

	@property
	def imsi(self):
		"""imsi commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_imsi'):
			from .Cell_.Imsi import Imsi
			self._imsi = Imsi(self._core, self._base)
		return self._imsi

	@property
	def ncc(self):
		"""ncc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ncc'):
			from .Cell_.Ncc import Ncc
			self._ncc = Ncc(self._core, self._base)
		return self._ncc

	@property
	def cswitched(self):
		"""cswitched commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cswitched'):
			from .Cell_.Cswitched import Cswitched
			self._cswitched = Cswitched(self._core, self._base)
		return self._cswitched

	@property
	def pswitched(self):
		"""pswitched commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_pswitched'):
			from .Cell_.Pswitched import Pswitched
			self._pswitched = Pswitched(self._core, self._base)
		return self._pswitched

	@property
	def security(self):
		"""security commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_security'):
			from .Cell_.Security import Security
			self._security = Security(self._core, self._base)
		return self._security

	@property
	def rcause(self):
		"""rcause commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_rcause'):
			from .Cell_.Rcause import Rcause
			self._rcause = Rcause(self._core, self._base)
		return self._rcause

	@property
	def mnc(self):
		"""mnc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mnc'):
			from .Cell_.Mnc import Mnc
			self._mnc = Mnc(self._core, self._base)
		return self._mnc

	@property
	def rtms(self):
		"""rtms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtms'):
			from .Cell_.Rtms import Rtms
			self._rtms = Rtms(self._core, self._base)
		return self._rtms

	@property
	def rtbs(self):
		"""rtbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtbs'):
			from .Cell_.Rtbs import Rtbs
			self._rtbs = Rtbs(self._core, self._base)
		return self._rtbs

	@property
	def atimeout(self):
		"""atimeout commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_atimeout'):
			from .Cell_.Atimeout import Atimeout
			self._atimeout = Atimeout(self._core, self._base)
		return self._atimeout

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_time'):
			from .Cell_.Time import Time
			self._time = Time(self._core, self._base)
		return self._time

	@property
	def sync(self):
		"""sync commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sync'):
			from .Cell_.Sync import Sync
			self._sync = Sync(self._core, self._base)
		return self._sync

	def get_psdomain(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:PSDomain \n
		Snippet: value: bool = driver.configure.cell.get_psdomain() \n
		Enables or disables the support of packet switched connections by the emulated cell. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PSDomain?')
		return Conversions.str_to_bool(response)

	def set_psdomain(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:PSDomain \n
		Snippet: driver.configure.cell.set_psdomain(enable = False) \n
		Enables or disables the support of packet switched connections by the emulated cell. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PSDomain {param}')

	# noinspection PyTypeChecker
	def get_nsupport(self) -> enums.NetworkSupport:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:NSUPport \n
		Snippet: value: enums.NetworkSupport = driver.configure.cell.get_nsupport() \n
		Selects the support of GPRS or EGPRS in packet domain. \n
			:return: network_support: GPRS | EGPRs
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:NSUPport?')
		return Conversions.str_to_scalar_enum(response, enums.NetworkSupport)

	def set_nsupport(self, network_support: enums.NetworkSupport) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:NSUPport \n
		Snippet: driver.configure.cell.set_nsupport(network_support = enums.NetworkSupport.EGPRs) \n
		Selects the support of GPRS or EGPRS in packet domain. \n
			:param network_support: GPRS | EGPRs
		"""
		param = Conversions.enum_scalar_to_str(network_support, enums.NetworkSupport)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:NSUPport {param}')

	def get_eciot(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:ECIot \n
		Snippet: value: bool = driver.configure.cell.get_eciot() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:ECIot?')
		return Conversions.str_to_bool(response)

	def set_eciot(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:ECIot \n
		Snippet: driver.configure.cell.set_eciot(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:ECIot {param}')

	def get_dt_mode(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:DTMode \n
		Snippet: value: bool = driver.configure.cell.get_dt_mode() \n
		Enables or disables dual transfer mode. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:DTMode?')
		return Conversions.str_to_bool(response)

	def set_dt_mode(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:DTMode \n
		Snippet: driver.configure.cell.set_dt_mode(enable = False) \n
		Enables or disables dual transfer mode. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:DTMode {param}')

	def get_bs_ag_blks_res(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:BSAGblksres \n
		Snippet: value: int = driver.configure.cell.get_bs_ag_blks_res() \n
		Defines the number of access grant channel (AGCH) data blocks reserved for the AGCH access. \n
			:return: blocks: Range: 0 to 2
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:BSAGblksres?')
		return Conversions.str_to_int(response)

	def set_bs_ag_blks_res(self, blocks: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:BSAGblksres \n
		Snippet: driver.configure.cell.set_bs_ag_blks_res(blocks = 1) \n
		Defines the number of access grant channel (AGCH) data blocks reserved for the AGCH access. \n
			:param blocks: Range: 0 to 2
		"""
		param = Conversions.decimal_value_to_str(blocks)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:BSAGblksres {param}')

	def get_bs_pa_mfrms(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:BSPamfrms \n
		Snippet: value: int = driver.configure.cell.get_bs_pa_mfrms() \n
		Defines the interval between two paging requests of the R&S CMW in multiframes (basic service paging blocks available per
		multiframes) . \n
			:return: frames: Range: 2 to 9
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:BSPamfrms?')
		return Conversions.str_to_int(response)

	def set_bs_pa_mfrms(self, frames: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:BSPamfrms \n
		Snippet: driver.configure.cell.set_bs_pa_mfrms(frames = 1) \n
		Defines the interval between two paging requests of the R&S CMW in multiframes (basic service paging blocks available per
		multiframes) . \n
			:param frames: Range: 2 to 9
		"""
		param = Conversions.decimal_value_to_str(frames)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:BSPamfrms {param}')

	# noinspection PyTypeChecker
	def get_bindicator(self) -> enums.BandIndicator:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:BINDicator \n
		Snippet: value: enums.BandIndicator = driver.configure.cell.get_bindicator() \n
		Indicates the band GSM1800 or GSM1900 that the MS under test can use. \n
			:return: band: G18 | G19 GSM1800 | GSM1900
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:BINDicator?')
		return Conversions.str_to_scalar_enum(response, enums.BandIndicator)

	def set_bindicator(self, band: enums.BandIndicator) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:BINDicator \n
		Snippet: driver.configure.cell.set_bindicator(band = enums.BandIndicator.G18) \n
		Indicates the band GSM1800 or GSM1900 that the MS under test can use. \n
			:param band: G18 | G19 GSM1800 | GSM1900
		"""
		param = Conversions.enum_scalar_to_str(band, enums.BandIndicator)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:BINDicator {param}')

	# noinspection PyTypeChecker
	def get_pmode(self) -> enums.PageMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PMODe \n
		Snippet: value: enums.PageMode = driver.configure.cell.get_pmode() \n
		Selects paging mode. \n
			:return: page_mode: NPAGing | PREorganize NPAGing: normal paging PREorganize: paging reorganization
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.PageMode)

	def set_pmode(self, page_mode: enums.PageMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PMODe \n
		Snippet: driver.configure.cell.set_pmode(page_mode = enums.PageMode.NPAGing) \n
		Selects paging mode. \n
			:param page_mode: NPAGing | PREorganize NPAGing: normal paging PREorganize: paging reorganization
		"""
		param = Conversions.enum_scalar_to_str(page_mode, enums.PageMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PMODe {param}')

	def get_mretrans(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:MRETrans \n
		Snippet: value: int = driver.configure.cell.get_mretrans() \n
		Maximum no. of the DL retransmissions. \n
			:return: max_retrans: Range: 1, 2, 4, 7
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:MRETrans?')
		return Conversions.str_to_int(response)

	def set_mretrans(self, max_retrans: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:MRETrans \n
		Snippet: driver.configure.cell.set_mretrans(max_retrans = 1) \n
		Maximum no. of the DL retransmissions. \n
			:param max_retrans: Range: 1, 2, 4, 7
		"""
		param = Conversions.decimal_value_to_str(max_retrans)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:MRETrans {param}')

	def get_ip_reduction(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IPReduction \n
		Snippet: value: int or bool = driver.configure.cell.get_ip_reduction() \n
		Specifies the MS transmit level reduction for the RACH at the very beginning of the connection before the standard power
		control algorithm starts. \n
			:return: value: 0: 10 dB 1: 10 dB, for emergency calls no power reduction Range: 0 to 1 ON (OFF) commands the MS to apply (not apply) the initial power reduction.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:IPReduction?')
		return Conversions.str_to_int_or_bool(response)

	def set_ip_reduction(self, value: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IPReduction \n
		Snippet: driver.configure.cell.set_ip_reduction(value = 1) \n
		Specifies the MS transmit level reduction for the RACH at the very beginning of the connection before the standard power
		control algorithm starts. \n
			:param value: 0: 10 dB 1: 10 dB, for emergency calls no power reduction Range: 0 to 1 ON (OFF) commands the MS to apply (not apply) the initial power reduction.
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:IPReduction {param}')

	def get_cbarring(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CBARring \n
		Snippet: value: bool = driver.configure.cell.get_cbarring() \n
		Enables/disables the MS to camp to the R&S CMW cell. \n
			:return: enable: OFF | ON OFF: the MS is allowed to camp to the cell ON: the MS is not allowed to camp to the cell
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:CBARring?')
		return Conversions.str_to_bool(response)

	def set_cbarring(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CBARring \n
		Snippet: driver.configure.cell.set_cbarring(enable = False) \n
		Enables/disables the MS to camp to the R&S CMW cell. \n
			:param enable: OFF | ON OFF: the MS is allowed to camp to the cell ON: the MS is not allowed to camp to the cell
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:CBARring {param}')

	# noinspection PyTypeChecker
	def get_pm_identity(self) -> enums.Paging:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PMIDentity \n
		Snippet: value: enums.Paging = driver.configure.cell.get_pm_identity() \n
		Selects the MS identity used by paging. \n
			:return: paging: IMSI | TMSI
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PMIDentity?')
		return Conversions.str_to_scalar_enum(response, enums.Paging)

	def set_pm_identity(self, paging: enums.Paging) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PMIDentity \n
		Snippet: driver.configure.cell.set_pm_identity(paging = enums.Paging.IMSI) \n
		Selects the MS identity used by paging. \n
			:param paging: IMSI | TMSI
		"""
		param = Conversions.enum_scalar_to_str(paging, enums.Paging)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PMIDentity {param}')

	def get_cdescription(self) -> List[int or bool]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CDEScription \n
		Snippet: value: List[int or bool] = driver.configure.cell.get_cdescription() \n
		Specifies the allowed DL traffic channels within the simulated GSM cell. \n
			:return: number: ON | OFF 64 entries: one or several channel numbers in parallel, ON (OFF) switches on (off) a channel. Range: 0 Ch to 1023 Ch
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:CDEScription?')
		return Conversions.str_to_int_or_bool_list(response)

	def set_cdescription(self, number: List[int or bool]) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CDEScription \n
		Snippet: driver.configure.cell.set_cdescription(number = [1, True, 2, False, 3]) \n
		Specifies the allowed DL traffic channels within the simulated GSM cell. \n
			:param number: ON | OFF 64 entries: one or several channel numbers in parallel, ON (OFF) switches on (off) a channel. Range: 0 Ch to 1023 Ch
		"""
		param = Conversions.list_to_csv_str(number)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:CDEScription {param}')

	def get_ec_sending(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:ECSending \n
		Snippet: value: bool = driver.configure.cell.get_ec_sending() \n
		Activates/deactivates early classmark sending as defined in 3GPP TS 44.018. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:ECSending?')
		return Conversions.str_to_bool(response)

	def set_ec_sending(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:ECSending \n
		Snippet: driver.configure.cell.set_ec_sending(enable = False) \n
		Activates/deactivates early classmark sending as defined in 3GPP TS 44.018. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:ECSending {param}')

	# noinspection PyTypeChecker
	def get_lupdate(self) -> enums.LocationUpdate:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:LUPDate \n
		Snippet: value: enums.LocationUpdate = driver.configure.cell.get_lupdate() \n
		Defines in which instances the MS performs a location update. \n
			:return: loc_update: ALWays | AUTO ALWays: location update each time the mobile is switched on AUTO: location update only if necessary
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:LUPDate?')
		return Conversions.str_to_scalar_enum(response, enums.LocationUpdate)

	def set_lupdate(self, loc_update: enums.LocationUpdate) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:LUPDate \n
		Snippet: driver.configure.cell.set_lupdate(loc_update = enums.LocationUpdate.ALWays) \n
		Defines in which instances the MS performs a location update. \n
			:param loc_update: ALWays | AUTO ALWays: location update each time the mobile is switched on AUTO: location update only if necessary
		"""
		param = Conversions.enum_scalar_to_str(loc_update, enums.LocationUpdate)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:LUPDate {param}')

	def get_dtx(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:DTX \n
		Snippet: value: bool = driver.configure.cell.get_dtx() \n
		Specifies whether the mobile station supports operating mode discontinuous transmission (DTX) . \n
			:return: mode: OFF | ON Enable | disable DTX mode
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:DTX?')
		return Conversions.str_to_bool(response)

	def set_dtx(self, mode: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:DTX \n
		Snippet: driver.configure.cell.set_dtx(mode = False) \n
		Specifies whether the mobile station supports operating mode discontinuous transmission (DTX) . \n
			:param mode: OFF | ON Enable | disable DTX mode
		"""
		param = Conversions.bool_to_str(mode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:DTX {param}')

	def get_identity(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IDENtity \n
		Snippet: value: int = driver.configure.cell.get_identity() \n
		Defines the cell identity of the simulated cell. \n
			:return: identity: Range: 0 to 216 - 1 (65535)
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:IDENtity?')
		return Conversions.str_to_int(response)

	def set_identity(self, identity: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IDENtity \n
		Snippet: driver.configure.cell.set_identity(identity = 1) \n
		Defines the cell identity of the simulated cell. \n
			:param identity: Range: 0 to 216 - 1 (65535)
		"""
		param = Conversions.decimal_value_to_str(identity)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:IDENtity {param}')

	def get_mcc(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:MCC \n
		Snippet: value: int = driver.configure.cell.get_mcc() \n
		Defines the mobile country code of the simulated network. \n
			:return: mcc: Range: 0 to 999
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:MCC?')
		return Conversions.str_to_int(response)

	def set_mcc(self, mcc: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:MCC \n
		Snippet: driver.configure.cell.set_mcc(mcc = 1) \n
		Defines the mobile country code of the simulated network. \n
			:param mcc: Range: 0 to 999
		"""
		param = Conversions.decimal_value_to_str(mcc)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:MCC {param}')

	def get_lac(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:LAC \n
		Snippet: value: int = driver.configure.cell.get_lac() \n
		Defines the location area code of the simulated base station. \n
			:return: lac: Range: 1 to 65533
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:LAC?')
		return Conversions.str_to_int(response)

	def set_lac(self, lac: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:LAC \n
		Snippet: driver.configure.cell.set_lac(lac = 1) \n
		Defines the location area code of the simulated base station. \n
			:param lac: Range: 1 to 65533
		"""
		param = Conversions.decimal_value_to_str(lac)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:LAC {param}')

	def get_rac(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:RAC \n
		Snippet: value: int = driver.configure.cell.get_rac() \n
		Defines the routing area code of the simulated base station. \n
			:return: rac: Range: 0 to 255
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RAC?')
		return Conversions.str_to_int(response)

	def set_rac(self, rac: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:RAC \n
		Snippet: driver.configure.cell.set_rac(rac = 1) \n
		Defines the routing area code of the simulated base station. \n
			:param rac: Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(rac)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RAC {param}')

	def get_bcc(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:BCC \n
		Snippet: value: int = driver.configure.cell.get_bcc() \n
		Defines the base transceiver station color code of the simulated base station. \n
			:return: bcc: Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:BCC?')
		return Conversions.str_to_int(response)

	def set_bcc(self, bcc: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:BCC \n
		Snippet: driver.configure.cell.set_bcc(bcc = 1) \n
		Defines the base transceiver station color code of the simulated base station. \n
			:param bcc: Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(bcc)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:BCC {param}')

	def get_imei_request(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IMEirequest \n
		Snippet: value: bool = driver.configure.cell.get_imei_request() \n
		Enables or disables request of the IMEI during location update. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:IMEirequest?')
		return Conversions.str_to_bool(response)

	def set_imei_request(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:IMEirequest \n
		Snippet: driver.configure.cell.set_imei_request(enable = False) \n
		Enables or disables request of the IMEI during location update. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:IMEirequest {param}')

	def get_crequest(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CREQuest \n
		Snippet: value: bool = driver.configure.cell.get_crequest() \n
		Activates/deactivates the classmark 3 information element as specified in 3GPP TS 24.008, section 10.5.1.7. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:CREQuest?')
		return Conversions.str_to_bool(response)

	def set_crequest(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:CREQuest \n
		Snippet: driver.configure.cell.set_crequest(enable = False) \n
		Activates/deactivates the classmark 3 information element as specified in 3GPP TS 24.008, section 10.5.1.7. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:CREQuest {param}')

	def get_pra_update(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PRAupdate \n
		Snippet: value: int or bool = driver.configure.cell.get_pra_update() \n
		Defines the value of the timer T3312 of the periodic routing area updating procedure. \n
			:return: value: Range: 0 to 31, Unit: deci-hour (6 minutes)
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PRAupdate?')
		return Conversions.str_to_int_or_bool(response)

	def set_pra_update(self, value: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PRAupdate \n
		Snippet: driver.configure.cell.set_pra_update(value = 1) \n
		Defines the value of the timer T3312 of the periodic routing area updating procedure. \n
			:param value: Range: 0 to 31, Unit: deci-hour (6 minutes)
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PRAupdate {param}')

	def get_pl_update(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PLUPdate \n
		Snippet: value: int or bool = driver.configure.cell.get_pl_update() \n
		Defines the value of the timer T3212 of the periodic location updating procedure. \n
			:return: value: Range: 0 to 255, Unit: deci-hour (6 minutes)
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:PLUPdate?')
		return Conversions.str_to_int_or_bool(response)

	def set_pl_update(self, value: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:PLUPdate \n
		Snippet: driver.configure.cell.set_pl_update(value = 1) \n
		Defines the value of the timer T3212 of the periodic location updating procedure. \n
			:param value: Range: 0 to 255, Unit: deci-hour (6 minutes)
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:PLUPdate {param}')

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
