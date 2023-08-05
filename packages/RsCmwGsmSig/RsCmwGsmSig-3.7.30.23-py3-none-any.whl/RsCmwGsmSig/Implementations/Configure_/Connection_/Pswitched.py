from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 25 total commands, 4 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	@property
	def sconfig(self):
		"""sconfig commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_sconfig'):
			from .Pswitched_.Sconfig import Sconfig
			self._sconfig = Sconfig(self._core, self._base)
		return self._sconfig

	@property
	def dpControl(self):
		"""dpControl commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_dpControl'):
			from .Pswitched_.DpControl import DpControl
			self._dpControl = DpControl(self._core, self._base)
		return self._dpControl

	@property
	def cscheme(self):
		"""cscheme commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cscheme'):
			from .Pswitched_.Cscheme import Cscheme
			self._cscheme = Cscheme(self._core, self._base)
		return self._cscheme

	@property
	def dldCarrier(self):
		"""dldCarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dldCarrier'):
			from .Pswitched_.DldCarrier import DldCarrier
			self._dldCarrier = DldCarrier(self._core, self._base)
		return self._dldCarrier

	# noinspection PyTypeChecker
	def get_service(self) -> enums.PswitchedService:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SERVice \n
		Snippet: value: enums.PswitchedService = driver.configure.connection.pswitched.get_service() \n
		Selects a service mode for the PS connection. \n
			:return: service: TMA | TMB | BLER | SRB TMA: test mode A TMB: test mode B BLER: BLER mode SRB: EGPRS switched radio block loopback mode
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SERVice?')
		return Conversions.str_to_scalar_enum(response, enums.PswitchedService)

	def set_service(self, service: enums.PswitchedService) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SERVice \n
		Snippet: driver.configure.connection.pswitched.set_service(service = enums.PswitchedService.BLER) \n
		Selects a service mode for the PS connection. \n
			:param service: TMA | TMB | BLER | SRB TMA: test mode A TMB: test mode B BLER: BLER mode SRB: EGPRS switched radio block loopback mode
		"""
		param = Conversions.enum_scalar_to_str(service, enums.PswitchedService)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SERVice {param}')

	# noinspection PyTypeChecker
	def get_dsource(self) -> enums.SwitchedSourceMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DSOurce \n
		Snippet: value: enums.SwitchedSourceMode = driver.configure.connection.pswitched.get_dsource() \n
		Selects the data which the R&S CMW transmits on its DL traffic channel for PS connections. \n
			:return: mode: PR9 | PR11 | PR15 | PR16 PR9: PRBS 2E9-1 PR11: PRBS 2E11-1 PR15: PRBS 2E15-1 PR16: PRBS 2E16-1
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DSOurce?')
		return Conversions.str_to_scalar_enum(response, enums.SwitchedSourceMode)

	def set_dsource(self, mode: enums.SwitchedSourceMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DSOurce \n
		Snippet: driver.configure.connection.pswitched.set_dsource(mode = enums.SwitchedSourceMode.ALL0) \n
		Selects the data which the R&S CMW transmits on its DL traffic channel for PS connections. \n
			:param mode: PR9 | PR11 | PR15 | PR16 PR9: PRBS 2E9-1 PR11: PRBS 2E11-1 PR15: PRBS 2E15-1 PR16: PRBS 2E16-1
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SwitchedSourceMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:DSOurce {param}')

	# noinspection PyTypeChecker
	def get_tlevel(self) -> enums.TbfLevel:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:TLEVel \n
		Snippet: value: enums.TbfLevel = driver.configure.connection.pswitched.get_tlevel() \n
		Selects the set of modulation and coding schemes to be used. \n
			:return: tbf_level: GPRS | EGPRs | EG2A GPRS CS-1 to CS-4 EGPRs MCS-1 to MCS-9 EG2A DL: MCS-1 to MCS-4, MCS-7, MCS-8, DAS-5 to DAS-12 UL: MCS-1 to MCS-6, UAS-7 to UAS-11
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:TLEVel?')
		return Conversions.str_to_scalar_enum(response, enums.TbfLevel)

	def set_tlevel(self, tbf_level: enums.TbfLevel) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:TLEVel \n
		Snippet: driver.configure.connection.pswitched.set_tlevel(tbf_level = enums.TbfLevel.EG2A) \n
		Selects the set of modulation and coding schemes to be used. \n
			:param tbf_level: GPRS | EGPRs | EG2A GPRS CS-1 to CS-4 EGPRs MCS-1 to MCS-9 EG2A DL: MCS-1 to MCS-4, MCS-7, MCS-8, DAS-5 to DAS-12 UL: MCS-1 to MCS-6, UAS-7 to UAS-11
		"""
		param = Conversions.enum_scalar_to_str(tbf_level, enums.TbfLevel)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:TLEVel {param}')

	# noinspection PyTypeChecker
	def get_ed_allocation(self) -> enums.AutoMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:EDALlocation \n
		Snippet: value: enums.AutoMode = driver.configure.connection.pswitched.get_ed_allocation() \n
		Enables or disables the optional medium access mode 'extended dynamic allocation'. \n
			:return: mode: OFF | ON | AUTO OFF: disabled ON: enabled AUTO: enabled if supported by the mobile, otherwise disabled
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:EDALlocation?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)

	def set_ed_allocation(self, mode: enums.AutoMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:EDALlocation \n
		Snippet: driver.configure.connection.pswitched.set_ed_allocation(mode = enums.AutoMode.AUTO) \n
		Enables or disables the optional medium access mode 'extended dynamic allocation'. \n
			:param mode: OFF | ON | AUTO OFF: disabled ON: enabled AUTO: enabled if supported by the mobile, otherwise disabled
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:EDALlocation {param}')

	def get_nopdus(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:NOPDus \n
		Snippet: value: int = driver.configure.connection.pswitched.get_nopdus() \n
		Number of PDUs that the MS is to transmit in the uplink during GPRS test mode A. If supported by the mobile, a value of 0
		can be used to request an 'infinite' test that is not terminated by the mobile after a certain number of PDUs. \n
			:return: number: Range: 0 to 4095
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:NOPDus?')
		return Conversions.str_to_int(response)

	def set_nopdus(self, number: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:NOPDus \n
		Snippet: driver.configure.connection.pswitched.set_nopdus(number = 1) \n
		Number of PDUs that the MS is to transmit in the uplink during GPRS test mode A. If supported by the mobile, a value of 0
		can be used to request an 'infinite' test that is not terminated by the mobile after a certain number of PDUs. \n
			:param number: Range: 0 to 4095
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:NOPDus {param}')

	def get_soffset(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SOFFset \n
		Snippet: value: int = driver.configure.connection.pswitched.get_soffset() \n
		Timeslot that is to be taken as the first DL timeslot when the MS is in multi-slot operation (downlink timeslot offset
		parameter in the GPRS_TEST_MODE_CMD) . \n
			:return: offset: Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SOFFset?')
		return Conversions.str_to_int(response)

	def set_soffset(self, offset: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SOFFset \n
		Snippet: driver.configure.connection.pswitched.set_soffset(offset = 1) \n
		Timeslot that is to be taken as the first DL timeslot when the MS is in multi-slot operation (downlink timeslot offset
		parameter in the GPRS_TEST_MODE_CMD) . \n
			:param offset: Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SOFFset {param}')

	# noinspection PyTypeChecker
	def get_ca_type(self) -> enums.ControlAckBurst:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:CATYpe \n
		Snippet: value: enums.ControlAckBurst = driver.configure.connection.pswitched.get_ca_type() \n
		Selects the burst type to be used by a mobile for sending a PACKET CONTROL ACKNOWLEDGEMENT. \n
			:return: mode: NBURsts | ABURsts NBURsts: normal bursts ABURsts: access bursts
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:CATYpe?')
		return Conversions.str_to_scalar_enum(response, enums.ControlAckBurst)

	def set_ca_type(self, mode: enums.ControlAckBurst) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:CATYpe \n
		Snippet: driver.configure.connection.pswitched.set_ca_type(mode = enums.ControlAckBurst.ABURsts) \n
		Selects the burst type to be used by a mobile for sending a PACKET CONTROL ACKNOWLEDGEMENT. \n
			:param mode: NBURsts | ABURsts NBURsts: normal bursts ABURsts: access bursts
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ControlAckBurst)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:CATYpe {param}')

	def get_bperiod(self) -> int or bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:BPERiod<Nr> \n
		Snippet: value: int or bool = driver.configure.connection.pswitched.get_bperiod() \n
		Configures the BEP_PERIOD2 defined in 3GPP TS 45.008 that the MS uses for the mean BEP and the CV BEP calculation. \n
			:return: value: Range: 0 to 15 ON (OFF) commands the MS to apply (not apply) the BEP period 2.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:BPERiod2?')
		return Conversions.str_to_int_or_bool(response)

	def set_bperiod(self, value: int or bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:BPERiod<Nr> \n
		Snippet: driver.configure.connection.pswitched.set_bperiod(value = 1) \n
		Configures the BEP_PERIOD2 defined in 3GPP TS 45.008 that the MS uses for the mean BEP and the CV BEP calculation. \n
			:param value: Range: 0 to 15 ON (OFF) commands the MS to apply (not apply) the BEP period 2.
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:BPERiod2 {param}')

	def get_bdc_rate(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:BDCRate \n
		Snippet: value: int = driver.configure.connection.pswitched.get_bdc_rate() \n
		Specifies volume of corrupted data the R&S CMW generates. \n
			:return: rate: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:BDCRate?')
		return Conversions.str_to_int(response)

	def set_bdc_rate(self, rate: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:BDCRate \n
		Snippet: driver.configure.connection.pswitched.set_bdc_rate(rate = 1) \n
		Specifies volume of corrupted data the R&S CMW generates. \n
			:param rate: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(rate)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:BDCRate {param}')

	def get_asrd_blocks(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:ASRDblocks \n
		Snippet: value: bool = driver.configure.connection.pswitched.get_asrd_blocks() \n
		Enables the filler dummy data blocks. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:ASRDblocks?')
		return Conversions.str_to_bool(response)

	def set_asrd_blocks(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:ASRDblocks \n
		Snippet: driver.configure.connection.pswitched.set_asrd_blocks(enable = False) \n
		Enables the filler dummy data blocks. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:ASRDblocks {param}')

	def get_iredundancy(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:IREDundancy \n
		Snippet: value: bool = driver.configure.connection.pswitched.get_iredundancy() \n
		Enables or disables the incremental redundancy RLC mode for the downlink. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:IREDundancy?')
		return Conversions.str_to_bool(response)

	def set_iredundancy(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:IREDundancy \n
		Snippet: driver.configure.connection.pswitched.set_iredundancy(enable = False) \n
		Enables or disables the incremental redundancy RLC mode for the downlink. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:IREDundancy {param}')

	def clone(self) -> 'Pswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
