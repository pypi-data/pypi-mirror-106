from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 41 total commands, 3 Sub-groups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	@property
	def dtx(self):
		"""dtx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtx'):
			from .Cswitched_.Dtx import Dtx
			self._dtx = Dtx(self._core, self._base)
		return self._dtx

	@property
	def amr(self):
		"""amr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_amr'):
			from .Cswitched_.Amr import Amr
			self._amr = Amr(self._core, self._base)
		return self._amr

	@property
	def vamos(self):
		"""vamos commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_vamos'):
			from .Cswitched_.Vamos import Vamos
			self._vamos = Vamos(self._core, self._base)
		return self._vamos

	def get_tslot(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TSLot \n
		Snippet: value: int = driver.configure.connection.cswitched.get_tslot() \n
		Selects a traffic channel timeslot for the circuit switched connection. \n
			:return: slot: Range: 1 to 7
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TSLot?')
		return Conversions.str_to_int(response)

	def set_tslot(self, slot: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TSLot \n
		Snippet: driver.configure.connection.cswitched.set_tslot(slot = 1) \n
		Selects a traffic channel timeslot for the circuit switched connection. \n
			:param slot: Range: 1 to 7
		"""
		param = Conversions.decimal_value_to_str(slot)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TSLot {param}')

	# noinspection PyTypeChecker
	def get_tmode(self) -> enums.SpeechChannelCodingMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TMODe \n
		Snippet: value: enums.SpeechChannelCodingMode = driver.configure.connection.cswitched.get_tmode() \n
		Selects the speech channel coding for circuit switched connections. \n
			:return: mode: FV1 | FV2 | HV1 | ANFG | ANHG | ANH8 | AWFG | AWF8 | AWH8 FV1: full-rate version 1 speech codec FV2: full-rate version 2 speech codec HV1: half-rate version 1 speech codec ANFG: AMR narrowband full-rate GMSK codec ANHG: AMR narrowband half-rate GMSK codec ANH8: AMR narrowband half-rate 8PSK codec AWFG: AMR wideband full-rate GMSK codec AWF8: AMR wideband full-rate 8PSK codec AWH8: AMR wideband half-rate 8PSK codec
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TMODe?')
		return Conversions.str_to_scalar_enum(response, enums.SpeechChannelCodingMode)

	def set_tmode(self, mode: enums.SpeechChannelCodingMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TMODe \n
		Snippet: driver.configure.connection.cswitched.set_tmode(mode = enums.SpeechChannelCodingMode.ANFG) \n
		Selects the speech channel coding for circuit switched connections. \n
			:param mode: FV1 | FV2 | HV1 | ANFG | ANHG | ANH8 | AWFG | AWF8 | AWH8 FV1: full-rate version 1 speech codec FV2: full-rate version 2 speech codec HV1: half-rate version 1 speech codec ANFG: AMR narrowband full-rate GMSK codec ANHG: AMR narrowband half-rate GMSK codec ANH8: AMR narrowband half-rate 8PSK codec AWFG: AMR wideband full-rate GMSK codec AWF8: AMR wideband full-rate 8PSK codec AWH8: AMR wideband half-rate 8PSK codec
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SpeechChannelCodingMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TMODe {param}')

	def get_hrsub_channel(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:HRSubchannel \n
		Snippet: value: int = driver.configure.connection.cswitched.get_hrsub_channel() \n
		Selects the subchannel to be used for half-rate coding. \n
			:return: channel: Range: 0 to 1
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:HRSubchannel?')
		return Conversions.str_to_int(response)

	def set_hrsub_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:HRSubchannel \n
		Snippet: driver.configure.connection.cswitched.set_hrsub_channel(channel = 1) \n
		Selects the subchannel to be used for half-rate coding. \n
			:param channel: Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:HRSubchannel {param}')

	# noinspection PyTypeChecker
	def get_dsource(self) -> enums.SwitchedSourceMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:DSOurce \n
		Snippet: value: enums.SwitchedSourceMode = driver.configure.connection.cswitched.get_dsource() \n
		Selects how the R&S CMW transmits data on its CS DL traffic channel. ECHO is incompatible with an enabled test loop (see
		method RsCmwGsmSig.Configure.Connection.Cswitched.loop) . \n
			:return: mode: ECHO | PR9 | PR11 | PR15 | PR16 | SP1 ECHO: loop-back of UL speech data after a fixed delay PR9: PRBS 2E9-1 PR11: PRBS 2E11-1 PR15: PRBS 2E15-1 PR16: PRBS 2E16-1 SP1: speech connection with codec board
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:DSOurce?')
		return Conversions.str_to_scalar_enum(response, enums.SwitchedSourceMode)

	def set_dsource(self, mode: enums.SwitchedSourceMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:DSOurce \n
		Snippet: driver.configure.connection.cswitched.set_dsource(mode = enums.SwitchedSourceMode.ALL0) \n
		Selects how the R&S CMW transmits data on its CS DL traffic channel. ECHO is incompatible with an enabled test loop (see
		method RsCmwGsmSig.Configure.Connection.Cswitched.loop) . \n
			:param mode: ECHO | PR9 | PR11 | PR15 | PR16 | SP1 ECHO: loop-back of UL speech data after a fixed delay PR9: PRBS 2E9-1 PR11: PRBS 2E11-1 PR15: PRBS 2E15-1 PR16: PRBS 2E16-1 SP1: speech connection with codec board
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SwitchedSourceMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:DSOurce {param}')

	# noinspection PyTypeChecker
	def get_crelease(self) -> enums.CallRelease:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:CRELease \n
		Snippet: value: enums.CallRelease = driver.configure.connection.cswitched.get_crelease() \n
		Specifies the signaling volume during the call release. \n
			:return: call_release: NRELease | IRELease | LERelease NRELease: normal release IRELease: immediate release LERelease: local end release
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:CRELease?')
		return Conversions.str_to_scalar_enum(response, enums.CallRelease)

	def set_crelease(self, call_release: enums.CallRelease) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:CRELease \n
		Snippet: driver.configure.connection.cswitched.set_crelease(call_release = enums.CallRelease.IRELease) \n
		Specifies the signaling volume during the call release. \n
			:param call_release: NRELease | IRELease | LERelease NRELease: normal release IRELease: immediate release LERelease: local end release
		"""
		param = Conversions.enum_scalar_to_str(call_release, enums.CallRelease)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:CRELease {param}')

	def get_edelay(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:EDELay \n
		Snippet: value: int = driver.configure.connection.cswitched.get_edelay() \n
		Defines the time that the R&S CMW waits before it loops back the received data in Echo mode. \n
			:return: echo_delay: Range: 0 s to 10 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:EDELay?')
		return Conversions.str_to_int(response)

	def set_edelay(self, echo_delay: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:EDELay \n
		Snippet: driver.configure.connection.cswitched.set_edelay(echo_delay = 1) \n
		Defines the time that the R&S CMW waits before it loops back the received data in Echo mode. \n
			:param echo_delay: Range: 0 s to 10 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(echo_delay)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:EDELay {param}')

	# noinspection PyTypeChecker
	def get_loop(self) -> enums.CswLoop:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:LOOP \n
		Snippet: value: enums.CswLoop = driver.configure.connection.cswitched.get_loop() \n
		Selects a test loop type and activates/deactivates the test loop (i.e. whether the MS is commanded to establish the test
		loop) . \n
			:return: loop: C | A | B | D | I | ON | OFF A: TCH loop including signaling of erased frames B: TCH loop without signaling of erased frames C: TCH burst-by-burst loop D: TCH loop including signaling of erased frames and unreliable frames I: TCH loop for inband signaling Additional parameters: OFF | ON (disables | enables the loop)
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:LOOP?')
		return Conversions.str_to_scalar_enum(response, enums.CswLoop)

	def set_loop(self, loop: enums.CswLoop) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:LOOP \n
		Snippet: driver.configure.connection.cswitched.set_loop(loop = enums.CswLoop.A) \n
		Selects a test loop type and activates/deactivates the test loop (i.e. whether the MS is commanded to establish the test
		loop) . \n
			:param loop: C | A | B | D | I | ON | OFF A: TCH loop including signaling of erased frames B: TCH loop without signaling of erased frames C: TCH burst-by-burst loop D: TCH loop including signaling of erased frames and unreliable frames I: TCH loop for inband signaling Additional parameters: OFF | ON (disables | enables the loop)
		"""
		param = Conversions.enum_scalar_to_str(loop, enums.CswLoop)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:LOOP {param}')

	def get_lreclose(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:LREClose \n
		Snippet: value: bool = driver.configure.connection.cswitched.get_lreclose() \n
		Enables or disables automatic re-establishing a test loop after TCH reconfiguration. Re-establishing the test loop is
		required for MS that opens an established test loop when a TCH reconfiguration is performed. \n
			:return: reclose_loop: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:LREClose?')
		return Conversions.str_to_bool(response)

	def set_lreclose(self, reclose_loop: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:LREClose \n
		Snippet: driver.configure.connection.cswitched.set_lreclose(reclose_loop = False) \n
		Enables or disables automatic re-establishing a test loop after TCH reconfiguration. Re-establishing the test loop is
		required for MS that opens an established test loop when a TCH reconfiguration is performed. \n
			:param reclose_loop: OFF | ON
		"""
		param = Conversions.bool_to_str(reclose_loop)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:LREClose {param}')

	def get_cid(self) -> str:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:CID \n
		Snippet: value: str = driver.configure.connection.cswitched.get_cid() \n
		Defines a 1 to 20-digit ID number for SMS and circuit switched calls, to be displayed at the mobile under test. Values
		are entered as number digits according to Table 'Number digits according to table 10.5.118 / 3GPP TS 24.008'. \n
			:return: idn: Range: '0' to 'cccccccccccccccccccc' (string)
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:CID?')
		return trim_str_response(response)

	def set_cid(self, idn: str) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:CID \n
		Snippet: driver.configure.connection.cswitched.set_cid(idn = '1') \n
		Defines a 1 to 20-digit ID number for SMS and circuit switched calls, to be displayed at the mobile under test. Values
		are entered as number digits according to Table 'Number digits according to table 10.5.118 / 3GPP TS 24.008'. \n
			:param idn: Range: '0' to 'cccccccccccccccccccc' (string)
		"""
		param = Conversions.value_to_quoted_str(idn)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:CID {param}')

	# noinspection PyTypeChecker
	def get_tch_assign(self) -> enums.TchAssignment:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TCHassign \n
		Snippet: value: enums.TchAssignment = driver.configure.connection.cswitched.get_tch_assign() \n
		Specifies when is the traffic channel assigned during connection setup. \n
			:return: tch_assignment: VEARly | EARLy | LATE | ON | OFF VEARly: The TCH is assigned very early. Signaling is done via the fast associated control channel (FACCH) . EARLy: The TCH is assigned early, which means that alerting takes place on the TCH. For call setup to the traffic channel, signaling is done via the standalone dedicated control channel (SDCCH) . LATE: The traffic channel is assigned late, which means after alerting. For call setup to the traffic channel and alerting, signaling is done via the SDCCH. OFF (ON) disables (enables) the TCH assignment.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TCHassign?')
		return Conversions.str_to_scalar_enum(response, enums.TchAssignment)

	def set_tch_assign(self, tch_assignment: enums.TchAssignment) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TCHassign \n
		Snippet: driver.configure.connection.cswitched.set_tch_assign(tch_assignment = enums.TchAssignment.EARLy) \n
		Specifies when is the traffic channel assigned during connection setup. \n
			:param tch_assignment: VEARly | EARLy | LATE | ON | OFF VEARly: The TCH is assigned very early. Signaling is done via the fast associated control channel (FACCH) . EARLy: The TCH is assigned early, which means that alerting takes place on the TCH. For call setup to the traffic channel, signaling is done via the standalone dedicated control channel (SDCCH) . LATE: The traffic channel is assigned late, which means after alerting. For call setup to the traffic channel and alerting, signaling is done via the SDCCH. OFF (ON) disables (enables) the TCH assignment.
		"""
		param = Conversions.enum_scalar_to_str(tch_assignment, enums.TchAssignment)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:TCHassign {param}')

	def get_rfacch(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:RFACch \n
		Snippet: value: bool = driver.configure.connection.cswitched.get_rfacch() \n
		Enables/disables repeated FACCH and repeated SACCH transmission in the DL GSM signal. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:RFACch?')
		return Conversions.str_to_bool(response)

	def set_rfacch(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:RFACch \n
		Snippet: driver.configure.connection.cswitched.set_rfacch(enable = False) \n
		Enables/disables repeated FACCH and repeated SACCH transmission in the DL GSM signal. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:RFACch {param}')

	def get_rsacch(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:RSACch \n
		Snippet: value: bool = driver.configure.connection.cswitched.get_rsacch() \n
		Enables/disables repeated FACCH and repeated SACCH transmission in the DL GSM signal. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:RSACch?')
		return Conversions.str_to_bool(response)

	def set_rsacch(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:RSACch \n
		Snippet: driver.configure.connection.cswitched.set_rsacch(enable = False) \n
		Enables/disables repeated FACCH and repeated SACCH transmission in the DL GSM signal. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:RSACch {param}')

	def clone(self) -> 'Cswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
