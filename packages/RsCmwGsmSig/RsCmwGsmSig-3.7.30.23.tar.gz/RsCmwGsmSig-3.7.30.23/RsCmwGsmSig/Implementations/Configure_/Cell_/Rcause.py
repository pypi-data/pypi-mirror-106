from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rcause:
	"""Rcause commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rcause", core, parent)

	# noinspection PyTypeChecker
	def get_location(self) -> enums.RejectionCause1:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:LOCation \n
		Snippet: value: enums.RejectionCause1 = driver.configure.cell.rcause.get_location() \n
		Enables or disables the rejection of location area update requests and selects the rejection cause to be transmitted. \n
			:return: cause_number: C2 | C3 | C6 | C11 | C12 | C13 | C15 | C96 | C99 | C100 | C111 | C4 | C5 | C17 | C20 | C21 | C22 | C23 | C25 | C32 | C33 | C34 | C38 | C48 | C95 | C97 | C98 | C101 | ON | OFF C2: IMSI unknown in HLR C3: Illegal mobile subscriber C4: IMSI unknown in VLR C5: IMEI not accepted C6: Illegal mobile equipment C11: PLMN not allowed C12: Location area not allowed C13: Roaming not allowed in location area C15: No suitable cells in location area C17: Network failure C20: MAC failure C21: Synch failure C22: Congestion C23: GSM authentication unacceptable C25: Not authorized for this CSG C32: Service option not supported C33: Requested service option not subscribed C34: Service option temporarily out of order C38: Call cannot be identified C48: Retry upon entry into a new cell C95: Semantically incorrect message C96: Invalid mandatory information C97: Message type non-existent or not implemented C98: Message type not compatible with protocol state C99: Information element non-existent or not implemented C100: Conditional information element error C101: Message not compatible with protocol state C111: Protocol error, unspecified Additional parameters OFF (ON) disables (enables) the rejection of requests.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:LOCation?')
		return Conversions.str_to_scalar_enum(response, enums.RejectionCause1)

	def set_location(self, cause_number: enums.RejectionCause1) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:LOCation \n
		Snippet: driver.configure.cell.rcause.set_location(cause_number = enums.RejectionCause1.C100) \n
		Enables or disables the rejection of location area update requests and selects the rejection cause to be transmitted. \n
			:param cause_number: C2 | C3 | C6 | C11 | C12 | C13 | C15 | C96 | C99 | C100 | C111 | C4 | C5 | C17 | C20 | C21 | C22 | C23 | C25 | C32 | C33 | C34 | C38 | C48 | C95 | C97 | C98 | C101 | ON | OFF C2: IMSI unknown in HLR C3: Illegal mobile subscriber C4: IMSI unknown in VLR C5: IMEI not accepted C6: Illegal mobile equipment C11: PLMN not allowed C12: Location area not allowed C13: Roaming not allowed in location area C15: No suitable cells in location area C17: Network failure C20: MAC failure C21: Synch failure C22: Congestion C23: GSM authentication unacceptable C25: Not authorized for this CSG C32: Service option not supported C33: Requested service option not subscribed C34: Service option temporarily out of order C38: Call cannot be identified C48: Retry upon entry into a new cell C95: Semantically incorrect message C96: Invalid mandatory information C97: Message type non-existent or not implemented C98: Message type not compatible with protocol state C99: Information element non-existent or not implemented C100: Conditional information element error C101: Message not compatible with protocol state C111: Protocol error, unspecified Additional parameters OFF (ON) disables (enables) the rejection of requests.
		"""
		param = Conversions.enum_scalar_to_str(cause_number, enums.RejectionCause1)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:LOCation {param}')

	# noinspection PyTypeChecker
	def get_attach(self) -> enums.RejectionCause2:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:ATTach \n
		Snippet: value: enums.RejectionCause2 = driver.configure.cell.rcause.get_attach() \n
		Enables or disables the rejection of attach requests and selects the rejection cause to be transmitted. \n
			:return: cause_number: C2 | C3 | C4 | C5 | C6 | C11 | C12 | C13 | C15 | C17 | C20 | C21 | C22 | C23 | C32 | C33 | C34 | C38 | C95 | C96 | C97 | C98 | C99 | C100 | C101 | C111 | C7 | C8 | C9 | C14 | C16 | C10 | C25 | C28 | C40 | C48 | ON | OFF C2: IMSI unknown in HLR C3: Illegal mobile subscriber C4: IMSI unknown in VLR C5: IMEI not accepted C6: Illegal mobile equipment C7: GPRS services not allowed C8: GPRS services and non-GPRS services not allowed C9: MS identity cannot be derived by the network C10: Implicitly detached C11: PLMN not allowed C12: Location area not allowed C13: Roaming not allowed in location area C14: GPRS services not allowed in this PLMN C15: No suitable cells in location area C16: MSC temporarily not reachable C17: Network failure C20: MAC failure C21: Synch failure C22: Congestion C23: GSM authentication unacceptable C25: Not authorized for this CSG C28: SMS provided via GPRS in this routing area C32: Service option unsupported C33: Service option not subscribed C34: Service option temporarily out of order C38: Call not identified C40: No PDP context activated C48: Retry upon entry into a new cell C95: Semantically incorrect message C96: Invalid mandatory information C97: Message type non-existent or not implemented C98: Message type not compatible with protocol state C99: Information element non-existent or not implemented C100: Conditional information element error C101: Message not compatible with protocol state C111: Protocol error, unspecified Additional parameters OFF (ON) disables (enables) the rejection of requests.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:ATTach?')
		return Conversions.str_to_scalar_enum(response, enums.RejectionCause2)

	def set_attach(self, cause_number: enums.RejectionCause2) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:ATTach \n
		Snippet: driver.configure.cell.rcause.set_attach(cause_number = enums.RejectionCause2.C10) \n
		Enables or disables the rejection of attach requests and selects the rejection cause to be transmitted. \n
			:param cause_number: C2 | C3 | C4 | C5 | C6 | C11 | C12 | C13 | C15 | C17 | C20 | C21 | C22 | C23 | C32 | C33 | C34 | C38 | C95 | C96 | C97 | C98 | C99 | C100 | C101 | C111 | C7 | C8 | C9 | C14 | C16 | C10 | C25 | C28 | C40 | C48 | ON | OFF C2: IMSI unknown in HLR C3: Illegal mobile subscriber C4: IMSI unknown in VLR C5: IMEI not accepted C6: Illegal mobile equipment C7: GPRS services not allowed C8: GPRS services and non-GPRS services not allowed C9: MS identity cannot be derived by the network C10: Implicitly detached C11: PLMN not allowed C12: Location area not allowed C13: Roaming not allowed in location area C14: GPRS services not allowed in this PLMN C15: No suitable cells in location area C16: MSC temporarily not reachable C17: Network failure C20: MAC failure C21: Synch failure C22: Congestion C23: GSM authentication unacceptable C25: Not authorized for this CSG C28: SMS provided via GPRS in this routing area C32: Service option unsupported C33: Service option not subscribed C34: Service option temporarily out of order C38: Call not identified C40: No PDP context activated C48: Retry upon entry into a new cell C95: Semantically incorrect message C96: Invalid mandatory information C97: Message type non-existent or not implemented C98: Message type not compatible with protocol state C99: Information element non-existent or not implemented C100: Conditional information element error C101: Message not compatible with protocol state C111: Protocol error, unspecified Additional parameters OFF (ON) disables (enables) the rejection of requests.
		"""
		param = Conversions.enum_scalar_to_str(cause_number, enums.RejectionCause2)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:ATTach {param}')

	# noinspection PyTypeChecker
	def get_ra_update(self) -> enums.RejectionCause2:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:RAUPdate \n
		Snippet: value: enums.RejectionCause2 = driver.configure.cell.rcause.get_ra_update() \n
		Enables or disables the rejection of routing area update requests and selects the rejection cause to be transmitted. \n
			:return: cause_number: C2 | C3 | C4 | C5 | C6 | C11 | C12 | C13 | C15 | C17 | C20 | C21 | C22 | C23 | C32 | C33 | C34 | C38 | C95 | C96 | C97 | C98 | C99 | C100 | C101 | C111 | C7 | C8 | C9 | C14 | C16 | C10 | C25 | C28 | C40 | C48 | ON | OFF C2: IMSI unknown in HLR C3: Illegal mobile subscriber C4: IMSI unknown in VLR C5: IMEI not accepted C6: Illegal mobile equipment C7: GPRS services not allowed C8: GPRS services and non-GPRS services not allowed C9: MS identity cannot be derived by the network C10: Implicitly detached C11: PLMN not allowed C12: Location area not allowed C13: Roaming not allowed in location area C14: GPRS services not allowed in this PLMN C15: No suitable cells in location area C16: MSC temporarily not reachable C17: Network failure C20: MAC failure C21: Synch failure C22: Congestion C23: GSM authentication unacceptable C25: Not authorized for this CSG C28: SMS provided via GPRS in this routing area C32: Service option not supported C33: Requested service option not subscribed C34: Service option temporarily out of order C38: Call cannot be identified C40: No PDP context activated C48: Retry upon entry into a new cell C95: Semantically incorrect message C96: Invalid mandatory information C97: Message type non-existent or not implemented C98: Message type not compatible with protocol state C99: Information element non-existent or not implemented C100: Conditional information element error C101: Message not compatible with protocol state C111: Protocol error, unspecified Additional parameters OFF (ON) disables (enables) the rejection of requests.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:RAUPdate?')
		return Conversions.str_to_scalar_enum(response, enums.RejectionCause2)

	def set_ra_update(self, cause_number: enums.RejectionCause2) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:RAUPdate \n
		Snippet: driver.configure.cell.rcause.set_ra_update(cause_number = enums.RejectionCause2.C10) \n
		Enables or disables the rejection of routing area update requests and selects the rejection cause to be transmitted. \n
			:param cause_number: C2 | C3 | C4 | C5 | C6 | C11 | C12 | C13 | C15 | C17 | C20 | C21 | C22 | C23 | C32 | C33 | C34 | C38 | C95 | C96 | C97 | C98 | C99 | C100 | C101 | C111 | C7 | C8 | C9 | C14 | C16 | C10 | C25 | C28 | C40 | C48 | ON | OFF C2: IMSI unknown in HLR C3: Illegal mobile subscriber C4: IMSI unknown in VLR C5: IMEI not accepted C6: Illegal mobile equipment C7: GPRS services not allowed C8: GPRS services and non-GPRS services not allowed C9: MS identity cannot be derived by the network C10: Implicitly detached C11: PLMN not allowed C12: Location area not allowed C13: Roaming not allowed in location area C14: GPRS services not allowed in this PLMN C15: No suitable cells in location area C16: MSC temporarily not reachable C17: Network failure C20: MAC failure C21: Synch failure C22: Congestion C23: GSM authentication unacceptable C25: Not authorized for this CSG C28: SMS provided via GPRS in this routing area C32: Service option not supported C33: Requested service option not subscribed C34: Service option temporarily out of order C38: Call cannot be identified C40: No PDP context activated C48: Retry upon entry into a new cell C95: Semantically incorrect message C96: Invalid mandatory information C97: Message type non-existent or not implemented C98: Message type not compatible with protocol state C99: Information element non-existent or not implemented C100: Conditional information element error C101: Message not compatible with protocol state C111: Protocol error, unspecified Additional parameters OFF (ON) disables (enables) the rejection of requests.
		"""
		param = Conversions.enum_scalar_to_str(cause_number, enums.RejectionCause2)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:RAUPdate {param}')

	# noinspection PyTypeChecker
	def get_cs_request(self) -> enums.RejectionCause1:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:CSRequest \n
		Snippet: value: enums.RejectionCause1 = driver.configure.cell.rcause.get_cs_request() \n
		Enables or disables the rejection of CM service requests and selects the rejection cause to be transmitted. The setting
		is relevant only for the specified service types, see method RsCmwGsmSig.Configure.Cell.Rcause.csType \n
			:return: cause_number: C2 | C3 | C6 | C11 | C12 | C13 | C15 | C96 | C99 | C100 | C111 | C4 | C5 | C17 | C20 | C21 | C22 | C23 | C25 | C32 | C33 | C34 | C38 | C48 | C95 | C97 | C98 | C101 | ON | OFF C2: IMSI unknown in HLR C3: Illegal mobile subscriber C4: IMSI unknown in VLR C5: IMEI not accepted C6: Illegal mobile equipment C11: PLMN not allowed C12: Location area not allowed C13: Roaming not allowed in location area C15: No suitable cells in location area C17: Network failure C20: MAC failure C21: Synch failure C22: Congestion C23: GSM authentication unacceptable C25: Not authorized for this CSG C32: Service option not supported C33: Requested service option not subscribed C34: Service option temporarily out of order C38: Call cannot be identified C48: Retry upon entry into a new cell C95: Semantically incorrect message C96: Invalid mandatory information C97: Message type non-existent or not implemented C98: Message type not compatible with protocol state C99: Information element non-existent or not implemented C100: Conditional information element error C101: Message not compatible with protocol state C111: Protocol error, unspecified Additional parameters: OFF | ON (disables | enables the rejection of requests)
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:CSRequest?')
		return Conversions.str_to_scalar_enum(response, enums.RejectionCause1)

	def set_cs_request(self, cause_number: enums.RejectionCause1) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:CSRequest \n
		Snippet: driver.configure.cell.rcause.set_cs_request(cause_number = enums.RejectionCause1.C100) \n
		Enables or disables the rejection of CM service requests and selects the rejection cause to be transmitted. The setting
		is relevant only for the specified service types, see method RsCmwGsmSig.Configure.Cell.Rcause.csType \n
			:param cause_number: C2 | C3 | C6 | C11 | C12 | C13 | C15 | C96 | C99 | C100 | C111 | C4 | C5 | C17 | C20 | C21 | C22 | C23 | C25 | C32 | C33 | C34 | C38 | C48 | C95 | C97 | C98 | C101 | ON | OFF C2: IMSI unknown in HLR C3: Illegal mobile subscriber C4: IMSI unknown in VLR C5: IMEI not accepted C6: Illegal mobile equipment C11: PLMN not allowed C12: Location area not allowed C13: Roaming not allowed in location area C15: No suitable cells in location area C17: Network failure C20: MAC failure C21: Synch failure C22: Congestion C23: GSM authentication unacceptable C25: Not authorized for this CSG C32: Service option not supported C33: Requested service option not subscribed C34: Service option temporarily out of order C38: Call cannot be identified C48: Retry upon entry into a new cell C95: Semantically incorrect message C96: Invalid mandatory information C97: Message type non-existent or not implemented C98: Message type not compatible with protocol state C99: Information element non-existent or not implemented C100: Conditional information element error C101: Message not compatible with protocol state C111: Protocol error, unspecified Additional parameters: OFF | ON (disables | enables the rejection of requests)
		"""
		param = Conversions.enum_scalar_to_str(cause_number, enums.RejectionCause1)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:CSRequest {param}')

	# noinspection PyTypeChecker
	def get_cs_type(self) -> enums.CmSerRejectType:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:CSTYpe \n
		Snippet: value: enums.CmSerRejectType = driver.configure.cell.rcause.get_cs_type() \n
		Specifies, to which type of CM service a request reject applies. Refer to method RsCmwGsmSig.Configure.Cell.Rcause.
		csRequest \n
			:return: cm_ser_reject_type: NESMs | NCECall | NCSMs | ECSMs | NCALl | ECALl | SMS NESMs: Normal call + emergency call + SMS NCECall: Normal call + emergency call NCSMs: Normal call + SMS ECSMs: Emergency call + SMS NCALl: Normal call ECALl: Emergency call SMS: SMS
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:CSTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.CmSerRejectType)

	def set_cs_type(self, cm_ser_reject_type: enums.CmSerRejectType) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RCAuse:CSTYpe \n
		Snippet: driver.configure.cell.rcause.set_cs_type(cm_ser_reject_type = enums.CmSerRejectType.ECALl) \n
		Specifies, to which type of CM service a request reject applies. Refer to method RsCmwGsmSig.Configure.Cell.Rcause.
		csRequest \n
			:param cm_ser_reject_type: NESMs | NCECall | NCSMs | ECSMs | NCALl | ECALl | SMS NESMs: Normal call + emergency call + SMS NCECall: Normal call + emergency call NCSMs: Normal call + SMS ECSMs: Emergency call + SMS NCALl: Normal call ECALl: Emergency call SMS: SMS
		"""
		param = Conversions.enum_scalar_to_str(cm_ser_reject_type, enums.CmSerRejectType)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RCAuse:CSTYpe {param}')
