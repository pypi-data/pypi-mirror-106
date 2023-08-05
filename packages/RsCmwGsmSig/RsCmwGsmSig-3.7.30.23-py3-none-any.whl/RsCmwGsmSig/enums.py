from enum import Enum


# noinspection SpellCheckingInspection
class AcceptAfter(Enum):
	"""8 Members, AA1 ... IALL"""
	AA1 = 0
	AA2 = 1
	AA3 = 2
	AA4 = 3
	AA5 = 4
	AA6 = 5
	AA7 = 6
	IALL = 7


# noinspection SpellCheckingInspection
class AutoManualMode(Enum):
	"""2 Members, AUTO ... MANual"""
	AUTO = 0
	MANual = 1


# noinspection SpellCheckingInspection
class AutoMode(Enum):
	"""3 Members, AUTO ... ON"""
	AUTO = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class BandClass(Enum):
	"""21 Members, AWS ... USPC"""
	AWS = 0
	B18M = 1
	IEXT = 2
	IM2K = 3
	JTAC = 4
	KCEL = 5
	KPCS = 6
	LO7C = 7
	N45T = 8
	NA7C = 9
	NA8S = 10
	NA9C = 11
	NAPC = 12
	PA4M = 13
	PA8M = 14
	PS7C = 15
	TACS = 16
	U25B = 17
	U25F = 18
	USC = 19
	USPC = 20


# noinspection SpellCheckingInspection
class BandIndicator(Enum):
	"""2 Members, G18 ... G19"""
	G18 = 0
	G19 = 1


# noinspection SpellCheckingInspection
class BbBoard(Enum):
	"""140 Members, BBR1 ... SUW44"""
	BBR1 = 0
	BBR11 = 1
	BBR12 = 2
	BBR13 = 3
	BBR14 = 4
	BBR2 = 5
	BBR21 = 6
	BBR22 = 7
	BBR23 = 8
	BBR24 = 9
	BBR3 = 10
	BBR31 = 11
	BBR32 = 12
	BBR33 = 13
	BBR34 = 14
	BBR4 = 15
	BBR41 = 16
	BBR42 = 17
	BBR43 = 18
	BBR44 = 19
	BBT1 = 20
	BBT11 = 21
	BBT12 = 22
	BBT13 = 23
	BBT14 = 24
	BBT2 = 25
	BBT21 = 26
	BBT22 = 27
	BBT23 = 28
	BBT24 = 29
	BBT3 = 30
	BBT31 = 31
	BBT32 = 32
	BBT33 = 33
	BBT34 = 34
	BBT4 = 35
	BBT41 = 36
	BBT42 = 37
	BBT43 = 38
	BBT44 = 39
	SUA012 = 40
	SUA034 = 41
	SUA056 = 42
	SUA078 = 43
	SUA1 = 44
	SUA11 = 45
	SUA112 = 46
	SUA12 = 47
	SUA13 = 48
	SUA134 = 49
	SUA14 = 50
	SUA15 = 51
	SUA156 = 52
	SUA16 = 53
	SUA17 = 54
	SUA178 = 55
	SUA18 = 56
	SUA2 = 57
	SUA21 = 58
	SUA212 = 59
	SUA22 = 60
	SUA23 = 61
	SUA234 = 62
	SUA24 = 63
	SUA25 = 64
	SUA256 = 65
	SUA26 = 66
	SUA27 = 67
	SUA278 = 68
	SUA28 = 69
	SUA3 = 70
	SUA31 = 71
	SUA312 = 72
	SUA32 = 73
	SUA33 = 74
	SUA334 = 75
	SUA34 = 76
	SUA35 = 77
	SUA356 = 78
	SUA36 = 79
	SUA37 = 80
	SUA378 = 81
	SUA38 = 82
	SUA4 = 83
	SUA41 = 84
	SUA412 = 85
	SUA42 = 86
	SUA43 = 87
	SUA434 = 88
	SUA44 = 89
	SUA45 = 90
	SUA456 = 91
	SUA46 = 92
	SUA47 = 93
	SUA478 = 94
	SUA48 = 95
	SUA5 = 96
	SUA6 = 97
	SUA7 = 98
	SUA8 = 99
	SUU1 = 100
	SUU11 = 101
	SUU12 = 102
	SUU13 = 103
	SUU14 = 104
	SUU2 = 105
	SUU21 = 106
	SUU22 = 107
	SUU23 = 108
	SUU24 = 109
	SUU3 = 110
	SUU31 = 111
	SUU32 = 112
	SUU33 = 113
	SUU34 = 114
	SUU4 = 115
	SUU41 = 116
	SUU42 = 117
	SUU43 = 118
	SUU44 = 119
	SUW1 = 120
	SUW11 = 121
	SUW12 = 122
	SUW13 = 123
	SUW14 = 124
	SUW2 = 125
	SUW21 = 126
	SUW22 = 127
	SUW23 = 128
	SUW24 = 129
	SUW3 = 130
	SUW31 = 131
	SUW32 = 132
	SUW33 = 133
	SUW34 = 134
	SUW4 = 135
	SUW41 = 136
	SUW42 = 137
	SUW43 = 138
	SUW44 = 139


# noinspection SpellCheckingInspection
class BerCsMeasMode(Enum):
	"""10 Members, AIFer ... SQUality"""
	AIFer = 0
	BBBurst = 1
	BER = 2
	BFI = 3
	FFACch = 4
	FSACch = 5
	MBEP = 6
	RFER = 7
	RUFR = 8
	SQUality = 9


# noinspection SpellCheckingInspection
class BerPsMeasMode(Enum):
	"""3 Members, BDBLer ... UBONly"""
	BDBLer = 0
	MBEP = 1
	UBONly = 2


# noinspection SpellCheckingInspection
class CallRelease(Enum):
	"""3 Members, IRELease ... NRELease"""
	IRELease = 0
	LERelease = 1
	NRELease = 2


# noinspection SpellCheckingInspection
class CmSerRejectType(Enum):
	"""7 Members, ECALl ... SMS"""
	ECALl = 0
	ECSMs = 1
	NCALl = 2
	NCECall = 3
	NCSMs = 4
	NESMs = 5
	SMS = 6


# noinspection SpellCheckingInspection
class CodingGroup(Enum):
	"""2 Members, DCMClass ... GDCoding"""
	DCMClass = 0
	GDCoding = 1


# noinspection SpellCheckingInspection
class CodingSchemeDownlink(Enum):
	"""29 Members, C1 ... MC9"""
	C1 = 0
	C2 = 1
	C3 = 2
	C4 = 3
	DA10 = 4
	DA11 = 5
	DA12 = 6
	DA5 = 7
	DA6 = 8
	DA7 = 9
	DA8 = 10
	DA9 = 11
	DB10 = 12
	DB11 = 13
	DB12 = 14
	DB5 = 15
	DB6 = 16
	DB7 = 17
	DB8 = 18
	DB9 = 19
	MC1 = 20
	MC2 = 21
	MC3 = 22
	MC4 = 23
	MC5 = 24
	MC6 = 25
	MC7 = 26
	MC8 = 27
	MC9 = 28


# noinspection SpellCheckingInspection
class CodingSchemeUplink(Enum):
	"""26 Members, C1 ... UB9"""
	C1 = 0
	C2 = 1
	C3 = 2
	C4 = 3
	MC1 = 4
	MC2 = 5
	MC3 = 6
	MC4 = 7
	MC5 = 8
	MC6 = 9
	MC7 = 10
	MC8 = 11
	MC9 = 12
	UA10 = 13
	UA11 = 14
	UA7 = 15
	UA8 = 16
	UA9 = 17
	UB10 = 18
	UB11 = 19
	UB12 = 20
	UB5 = 21
	UB6 = 22
	UB7 = 23
	UB8 = 24
	UB9 = 25


# noinspection SpellCheckingInspection
class ConnectError(Enum):
	"""7 Members, ATIMeout ... STIMeout"""
	ATIMeout = 0
	IGNored = 1
	NERRor = 2
	PTIMeout = 3
	REJected = 4
	RLTimeout = 5
	STIMeout = 6


# noinspection SpellCheckingInspection
class ConnectRequest(Enum):
	"""3 Members, ACCept ... REJect"""
	ACCept = 0
	IGNore = 1
	REJect = 2


# noinspection SpellCheckingInspection
class ControlAckBurst(Enum):
	"""2 Members, ABURsts ... NBURsts"""
	ABURsts = 0
	NBURsts = 1


# noinspection SpellCheckingInspection
class CswAction(Enum):
	"""6 Members, CONNect ... SMS"""
	CONNect = 0
	DISConnect = 1
	HANDover = 2
	OFF = 3
	ON = 4
	SMS = 5


# noinspection SpellCheckingInspection
class CswLoop(Enum):
	"""7 Members, A ... ON"""
	A = 0
	B = 1
	C = 2
	D = 3
	I = 4
	OFF = 5
	ON = 6


# noinspection SpellCheckingInspection
class CswState(Enum):
	"""13 Members, ALER ... SYNC"""
	ALER = 0
	CEST = 1
	CONN = 2
	IHANdover = 3
	IMS = 4
	LUPD = 5
	OFF = 6
	OHANdover = 7
	ON = 8
	REL = 9
	RMESsage = 10
	SMESsage = 11
	SYNC = 12


# noinspection SpellCheckingInspection
class DigitsCount(Enum):
	"""2 Members, THRee ... TWO"""
	THRee = 0
	TWO = 1


# noinspection SpellCheckingInspection
class DownlinkCodingScheme(Enum):
	"""31 Members, C1 ... ON"""
	C1 = 0
	C2 = 1
	C3 = 2
	C4 = 3
	DA10 = 4
	DA11 = 5
	DA12 = 6
	DA5 = 7
	DA6 = 8
	DA7 = 9
	DA8 = 10
	DA9 = 11
	DB10 = 12
	DB11 = 13
	DB12 = 14
	DB5 = 15
	DB6 = 16
	DB7 = 17
	DB8 = 18
	DB9 = 19
	MC1 = 20
	MC2 = 21
	MC3 = 22
	MC4 = 23
	MC5 = 24
	MC6 = 25
	MC7 = 26
	MC8 = 27
	MC9 = 28
	OFF = 29
	ON = 30


# noinspection SpellCheckingInspection
class DsTime(Enum):
	"""4 Members, OFF ... P2H"""
	OFF = 0
	ON = 1
	P1H = 2
	P2H = 3


# noinspection SpellCheckingInspection
class EightPskPowerClass(Enum):
	"""4 Members, E1 ... U"""
	E1 = 0
	E2 = 1
	E3 = 2
	U = 3


# noinspection SpellCheckingInspection
class FadingBoard(Enum):
	"""60 Members, FAD012 ... FAD8"""
	FAD012 = 0
	FAD034 = 1
	FAD056 = 2
	FAD078 = 3
	FAD1 = 4
	FAD11 = 5
	FAD112 = 6
	FAD12 = 7
	FAD13 = 8
	FAD134 = 9
	FAD14 = 10
	FAD15 = 11
	FAD156 = 12
	FAD16 = 13
	FAD17 = 14
	FAD178 = 15
	FAD18 = 16
	FAD2 = 17
	FAD21 = 18
	FAD212 = 19
	FAD22 = 20
	FAD23 = 21
	FAD234 = 22
	FAD24 = 23
	FAD25 = 24
	FAD256 = 25
	FAD26 = 26
	FAD27 = 27
	FAD278 = 28
	FAD28 = 29
	FAD3 = 30
	FAD31 = 31
	FAD312 = 32
	FAD32 = 33
	FAD33 = 34
	FAD334 = 35
	FAD34 = 36
	FAD35 = 37
	FAD356 = 38
	FAD36 = 39
	FAD37 = 40
	FAD378 = 41
	FAD38 = 42
	FAD4 = 43
	FAD41 = 44
	FAD412 = 45
	FAD42 = 46
	FAD43 = 47
	FAD434 = 48
	FAD44 = 49
	FAD45 = 50
	FAD456 = 51
	FAD46 = 52
	FAD47 = 53
	FAD478 = 54
	FAD48 = 55
	FAD5 = 56
	FAD6 = 57
	FAD7 = 58
	FAD8 = 59


# noinspection SpellCheckingInspection
class FadingMode(Enum):
	"""2 Members, NORMal ... USER"""
	NORMal = 0
	USER = 1


# noinspection SpellCheckingInspection
class FadingStandard(Enum):
	"""30 Members, E100 ... TU60"""
	E100 = 0
	E50 = 1
	E60 = 2
	H100 = 3
	H120 = 4
	H200 = 5
	HT100 = 6
	HT120 = 7
	HT200 = 8
	R130 = 9
	R250 = 10
	R300 = 11
	R500 = 12
	T100 = 13
	T1P5 = 14
	T25 = 15
	T3 = 16
	T3P6 = 17
	T50 = 18
	T6 = 19
	T60 = 20
	TI5 = 21
	TU100 = 22
	TU1P5 = 23
	TU25 = 24
	TU3 = 25
	TU3P6 = 26
	TU50 = 27
	TU6 = 28
	TU60 = 29


# noinspection SpellCheckingInspection
class FrameTriggerMod(Enum):
	"""5 Members, EVERy ... M52"""
	EVERy = 0
	EWIDle = 1
	M104 = 2
	M26 = 3
	M52 = 4


# noinspection SpellCheckingInspection
class GeographicScope(Enum):
	"""4 Members, CIMMediate ... PLMN"""
	CIMMediate = 0
	CNORmal = 1
	LOCation = 2
	PLMN = 3


# noinspection SpellCheckingInspection
class HandoverDestination(Enum):
	"""6 Members, CDMA ... WCDMa"""
	CDMA = 0
	EVDO = 1
	GSM = 2
	LTE = 3
	TDSCdma = 4
	WCDMa = 5


# noinspection SpellCheckingInspection
class HandoverMode(Enum):
	"""4 Members, CCORder ... REDirection"""
	CCORder = 0
	DUALband = 1
	HANDover = 2
	REDirection = 3


# noinspection SpellCheckingInspection
class HandoverState(Enum):
	"""2 Members, DUALband ... OFF"""
	DUALband = 0
	OFF = 1


# noinspection SpellCheckingInspection
class InsertLossMode(Enum):
	"""3 Members, LACP ... USER"""
	LACP = 0
	NORMal = 1
	USER = 2


# noinspection SpellCheckingInspection
class IpAddrIndex(Enum):
	"""3 Members, IP1 ... IP3"""
	IP1 = 0
	IP2 = 1
	IP3 = 2


# noinspection SpellCheckingInspection
class LastMessageSent(Enum):
	"""4 Members, FAILed ... SUCCessful"""
	FAILed = 0
	OFF = 1
	ON = 2
	SUCCessful = 3


# noinspection SpellCheckingInspection
class LmQuantity(Enum):
	"""2 Members, RSRP ... RSRQ"""
	RSRP = 0
	RSRQ = 1


# noinspection SpellCheckingInspection
class LocationUpdate(Enum):
	"""2 Members, ALWays ... AUTO"""
	ALWays = 0
	AUTO = 1


# noinspection SpellCheckingInspection
class LogCategory(Enum):
	"""4 Members, CONTinue ... WARNing"""
	CONTinue = 0
	ERRor = 1
	INFO = 2
	WARNing = 3


# noinspection SpellCheckingInspection
class MainState(Enum):
	"""3 Members, OFF ... RFHandover"""
	OFF = 0
	ON = 1
	RFHandover = 2


# noinspection SpellCheckingInspection
class MessageClass(Enum):
	"""5 Members, CL0 ... NONE"""
	CL0 = 0
	CL1 = 1
	CL2 = 2
	CL3 = 3
	NONE = 4


# noinspection SpellCheckingInspection
class MsgIdSeverity(Enum):
	"""5 Members, AAMBer ... UDEFined"""
	AAMBer = 0
	AEXTreme = 1
	APResidentia = 2
	ASEVere = 3
	UDEFined = 4


# noinspection SpellCheckingInspection
class NbCodec(Enum):
	"""10 Members, C0475 ... ON"""
	C0475 = 0
	C0515 = 1
	C0590 = 2
	C0670 = 3
	C0740 = 4
	C0795 = 5
	C1020 = 6
	C1220 = 7
	OFF = 8
	ON = 9


# noinspection SpellCheckingInspection
class NetworkSupport(Enum):
	"""2 Members, EGPRs ... GPRS"""
	EGPRs = 0
	GPRS = 1


# noinspection SpellCheckingInspection
class NominalPowerMode(Enum):
	"""3 Members, AUToranging ... ULPC"""
	AUToranging = 0
	MANual = 1
	ULPC = 2


# noinspection SpellCheckingInspection
class OperBandGsm(Enum):
	"""6 Members, G04 ... GT081"""
	G04 = 0
	G085 = 1
	G09 = 2
	G18 = 3
	G19 = 4
	GT081 = 5


# noinspection SpellCheckingInspection
class OperBandLte(Enum):
	"""67 Members, OB1 ... OB9"""
	OB1 = 0
	OB10 = 1
	OB11 = 2
	OB12 = 3
	OB13 = 4
	OB14 = 5
	OB15 = 6
	OB16 = 7
	OB17 = 8
	OB18 = 9
	OB19 = 10
	OB2 = 11
	OB20 = 12
	OB21 = 13
	OB22 = 14
	OB23 = 15
	OB24 = 16
	OB25 = 17
	OB250 = 18
	OB252 = 19
	OB255 = 20
	OB26 = 21
	OB27 = 22
	OB28 = 23
	OB29 = 24
	OB3 = 25
	OB30 = 26
	OB31 = 27
	OB32 = 28
	OB33 = 29
	OB34 = 30
	OB35 = 31
	OB36 = 32
	OB37 = 33
	OB38 = 34
	OB39 = 35
	OB4 = 36
	OB40 = 37
	OB41 = 38
	OB42 = 39
	OB43 = 40
	OB44 = 41
	OB45 = 42
	OB46 = 43
	OB48 = 44
	OB49 = 45
	OB5 = 46
	OB50 = 47
	OB51 = 48
	OB52 = 49
	OB6 = 50
	OB65 = 51
	OB66 = 52
	OB67 = 53
	OB68 = 54
	OB69 = 55
	OB7 = 56
	OB70 = 57
	OB71 = 58
	OB72 = 59
	OB73 = 60
	OB74 = 61
	OB75 = 62
	OB76 = 63
	OB8 = 64
	OB85 = 65
	OB9 = 66


# noinspection SpellCheckingInspection
class OperBandTdsCdma(Enum):
	"""3 Members, OB1 ... OB3"""
	OB1 = 0
	OB2 = 1
	OB3 = 2


# noinspection SpellCheckingInspection
class OperBandWcdma(Enum):
	"""24 Members, OB1 ... OBS3"""
	OB1 = 0
	OB10 = 1
	OB11 = 2
	OB12 = 3
	OB13 = 4
	OB14 = 5
	OB19 = 6
	OB2 = 7
	OB20 = 8
	OB21 = 9
	OB22 = 10
	OB25 = 11
	OB26 = 12
	OB3 = 13
	OB4 = 14
	OB5 = 15
	OB6 = 16
	OB7 = 17
	OB8 = 18
	OB9 = 19
	OBL1 = 20
	OBS1 = 21
	OBS2 = 22
	OBS3 = 23


# noinspection SpellCheckingInspection
class PageMode(Enum):
	"""2 Members, NPAGing ... PREorganize"""
	NPAGing = 0
	PREorganize = 1


# noinspection SpellCheckingInspection
class Paging(Enum):
	"""2 Members, IMSI ... TMSI"""
	IMSI = 0
	TMSI = 1


# noinspection SpellCheckingInspection
class PcmChannel(Enum):
	"""2 Members, BCCH ... PDCH"""
	BCCH = 0
	PDCH = 1


# noinspection SpellCheckingInspection
class PowerReductionField(Enum):
	"""4 Members, DB0 ... NUSable"""
	DB0 = 0
	DB3 = 1
	DB7 = 2
	NUSable = 3


# noinspection SpellCheckingInspection
class PowerReductionMode(Enum):
	"""2 Members, PMA ... PMB"""
	PMA = 0
	PMB = 1


# noinspection SpellCheckingInspection
class Priority(Enum):
	"""3 Members, BACKground ... NORMal"""
	BACKground = 0
	HIGH = 1
	NORMal = 2


# noinspection SpellCheckingInspection
class Profile(Enum):
	"""5 Members, OFF ... TUSer"""
	OFF = 0
	ON = 1
	SUSer = 2
	TUDTx = 3
	TUSer = 4


# noinspection SpellCheckingInspection
class PswAction(Enum):
	"""7 Members, CONNect ... SMS"""
	CONNect = 0
	DISConnect = 1
	HANDover = 2
	OFF = 3
	ON = 4
	RPContext = 5
	SMS = 6


# noinspection SpellCheckingInspection
class PswitchedService(Enum):
	"""4 Members, BLER ... TMB"""
	BLER = 0
	SRB = 1
	TMA = 2
	TMB = 3


# noinspection SpellCheckingInspection
class PswPowerReduction(Enum):
	"""16 Members, DB0 ... DB8"""
	DB0 = 0
	DB10 = 1
	DB12 = 2
	DB14 = 3
	DB16 = 4
	DB18 = 5
	DB2 = 6
	DB20 = 7
	DB22 = 8
	DB24 = 9
	DB26 = 10
	DB28 = 11
	DB30 = 12
	DB4 = 13
	DB6 = 14
	DB8 = 15


# noinspection SpellCheckingInspection
class PswState(Enum):
	"""12 Members, AIPR ... TBF"""
	AIPR = 0
	ATT = 1
	CTIP = 2
	DIPR = 3
	OFF = 4
	ON = 5
	PAIP = 6
	PDIP = 7
	PDP = 8
	RAUP = 9
	REL = 10
	TBF = 11


# noinspection SpellCheckingInspection
class ReactionMode(Enum):
	"""2 Members, ACCept ... REJect"""
	ACCept = 0
	REJect = 1


# noinspection SpellCheckingInspection
class RejectionCause1(Enum):
	"""30 Members, C100 ... ON"""
	C100 = 0
	C101 = 1
	C11 = 2
	C111 = 3
	C12 = 4
	C13 = 5
	C15 = 6
	C17 = 7
	C2 = 8
	C20 = 9
	C21 = 10
	C22 = 11
	C23 = 12
	C25 = 13
	C3 = 14
	C32 = 15
	C33 = 16
	C34 = 17
	C38 = 18
	C4 = 19
	C48 = 20
	C5 = 21
	C6 = 22
	C95 = 23
	C96 = 24
	C97 = 25
	C98 = 26
	C99 = 27
	OFF = 28
	ON = 29


# noinspection SpellCheckingInspection
class RejectionCause2(Enum):
	"""38 Members, C10 ... ON"""
	C10 = 0
	C100 = 1
	C101 = 2
	C11 = 3
	C111 = 4
	C12 = 5
	C13 = 6
	C14 = 7
	C15 = 8
	C16 = 9
	C17 = 10
	C2 = 11
	C20 = 12
	C21 = 13
	C22 = 14
	C23 = 15
	C25 = 16
	C28 = 17
	C3 = 18
	C32 = 19
	C33 = 20
	C34 = 21
	C38 = 22
	C4 = 23
	C40 = 24
	C48 = 25
	C5 = 26
	C6 = 27
	C7 = 28
	C8 = 29
	C9 = 30
	C95 = 31
	C96 = 32
	C97 = 33
	C98 = 34
	C99 = 35
	OFF = 36
	ON = 37


# noinspection SpellCheckingInspection
class Repeat(Enum):
	"""2 Members, CONTinuous ... SINGleshot"""
	CONTinuous = 0
	SINGleshot = 1


# noinspection SpellCheckingInspection
class ResourceState(Enum):
	"""8 Members, ACTive ... RUN"""
	ACTive = 0
	ADJusted = 1
	INValid = 2
	OFF = 3
	PENDing = 4
	QUEued = 5
	RDY = 6
	RUN = 7


# noinspection SpellCheckingInspection
class RestartMode(Enum):
	"""3 Members, AUTO ... TRIGger"""
	AUTO = 0
	MANual = 1
	TRIGger = 2


# noinspection SpellCheckingInspection
class RxConnector(Enum):
	"""154 Members, I11I ... RH8"""
	I11I = 0
	I13I = 1
	I15I = 2
	I17I = 3
	I21I = 4
	I23I = 5
	I25I = 6
	I27I = 7
	I31I = 8
	I33I = 9
	I35I = 10
	I37I = 11
	I41I = 12
	I43I = 13
	I45I = 14
	I47I = 15
	IF1 = 16
	IF2 = 17
	IF3 = 18
	IQ1I = 19
	IQ3I = 20
	IQ5I = 21
	IQ7I = 22
	R11 = 23
	R11C = 24
	R12 = 25
	R12C = 26
	R12I = 27
	R13 = 28
	R13C = 29
	R14 = 30
	R14C = 31
	R14I = 32
	R15 = 33
	R16 = 34
	R17 = 35
	R18 = 36
	R21 = 37
	R21C = 38
	R22 = 39
	R22C = 40
	R22I = 41
	R23 = 42
	R23C = 43
	R24 = 44
	R24C = 45
	R24I = 46
	R25 = 47
	R26 = 48
	R27 = 49
	R28 = 50
	R31 = 51
	R31C = 52
	R32 = 53
	R32C = 54
	R32I = 55
	R33 = 56
	R33C = 57
	R34 = 58
	R34C = 59
	R34I = 60
	R35 = 61
	R36 = 62
	R37 = 63
	R38 = 64
	R41 = 65
	R41C = 66
	R42 = 67
	R42C = 68
	R42I = 69
	R43 = 70
	R43C = 71
	R44 = 72
	R44C = 73
	R44I = 74
	R45 = 75
	R46 = 76
	R47 = 77
	R48 = 78
	RA1 = 79
	RA2 = 80
	RA3 = 81
	RA4 = 82
	RA5 = 83
	RA6 = 84
	RA7 = 85
	RA8 = 86
	RB1 = 87
	RB2 = 88
	RB3 = 89
	RB4 = 90
	RB5 = 91
	RB6 = 92
	RB7 = 93
	RB8 = 94
	RC1 = 95
	RC2 = 96
	RC3 = 97
	RC4 = 98
	RC5 = 99
	RC6 = 100
	RC7 = 101
	RC8 = 102
	RD1 = 103
	RD2 = 104
	RD3 = 105
	RD4 = 106
	RD5 = 107
	RD6 = 108
	RD7 = 109
	RD8 = 110
	RE1 = 111
	RE2 = 112
	RE3 = 113
	RE4 = 114
	RE5 = 115
	RE6 = 116
	RE7 = 117
	RE8 = 118
	RF1 = 119
	RF1C = 120
	RF2 = 121
	RF2C = 122
	RF2I = 123
	RF3 = 124
	RF3C = 125
	RF4 = 126
	RF4C = 127
	RF4I = 128
	RF5 = 129
	RF5C = 130
	RF6 = 131
	RF6C = 132
	RF7 = 133
	RF8 = 134
	RFAC = 135
	RFBC = 136
	RFBI = 137
	RG1 = 138
	RG2 = 139
	RG3 = 140
	RG4 = 141
	RG5 = 142
	RG6 = 143
	RG7 = 144
	RG8 = 145
	RH1 = 146
	RH2 = 147
	RH3 = 148
	RH4 = 149
	RH5 = 150
	RH6 = 151
	RH7 = 152
	RH8 = 153


# noinspection SpellCheckingInspection
class RxConverter(Enum):
	"""40 Members, IRX1 ... RX44"""
	IRX1 = 0
	IRX11 = 1
	IRX12 = 2
	IRX13 = 3
	IRX14 = 4
	IRX2 = 5
	IRX21 = 6
	IRX22 = 7
	IRX23 = 8
	IRX24 = 9
	IRX3 = 10
	IRX31 = 11
	IRX32 = 12
	IRX33 = 13
	IRX34 = 14
	IRX4 = 15
	IRX41 = 16
	IRX42 = 17
	IRX43 = 18
	IRX44 = 19
	RX1 = 20
	RX11 = 21
	RX12 = 22
	RX13 = 23
	RX14 = 24
	RX2 = 25
	RX21 = 26
	RX22 = 27
	RX23 = 28
	RX24 = 29
	RX3 = 30
	RX31 = 31
	RX32 = 32
	RX33 = 33
	RX34 = 34
	RX4 = 35
	RX41 = 36
	RX42 = 37
	RX43 = 38
	RX44 = 39


# noinspection SpellCheckingInspection
class RxPower(Enum):
	"""6 Members, INV ... UFL"""
	INV = 0
	NAV = 1
	NCAP = 2
	OFL = 3
	OK = 4
	UFL = 5


# noinspection SpellCheckingInspection
class SampleRate(Enum):
	"""8 Members, M1 ... M9"""
	M1 = 0
	M100 = 1
	M15 = 2
	M19 = 3
	M3 = 4
	M30 = 5
	M7 = 6
	M9 = 7


# noinspection SpellCheckingInspection
class Scenario(Enum):
	"""6 Members, BATC ... SCFDiversity"""
	BATC = 0
	IORI = 1
	NAV = 2
	SCEL = 3
	SCF = 4
	SCFDiversity = 5


# noinspection SpellCheckingInspection
class SignalingMode(Enum):
	"""2 Members, LTRR ... RATScch"""
	LTRR = 0
	RATScch = 1


# noinspection SpellCheckingInspection
class SimCardType(Enum):
	"""2 Members, C2G ... C3G"""
	C2G = 0
	C3G = 1


# noinspection SpellCheckingInspection
class SmsDataCoding(Enum):
	"""2 Members, BIT7 ... BIT8"""
	BIT7 = 0
	BIT8 = 1


# noinspection SpellCheckingInspection
class SmsDomain(Enum):
	"""3 Members, AUTO ... PS"""
	AUTO = 0
	CS = 1
	PS = 2


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class SourceTime(Enum):
	"""2 Members, CMWTime ... DATE"""
	CMWTime = 0
	DATE = 1


# noinspection SpellCheckingInspection
class SpeechChannelCodingMode(Enum):
	"""9 Members, ANFG ... HV1"""
	ANFG = 0
	ANH8 = 1
	ANHG = 2
	AWF8 = 3
	AWFG = 4
	AWH8 = 5
	FV1 = 6
	FV2 = 7
	HV1 = 8


# noinspection SpellCheckingInspection
class SwitchedSourceMode(Enum):
	"""11 Members, ALL0 ... UPATtern"""
	ALL0 = 0
	ALL1 = 1
	ALTernating = 2
	ECHO = 3
	PR11 = 4
	PR15 = 5
	PR16 = 6
	PR9 = 7
	SP1 = 8
	SP2 = 9
	UPATtern = 10


# noinspection SpellCheckingInspection
class SyncState(Enum):
	"""7 Members, ADINtermed ... RFHandover"""
	ADINtermed = 0
	ADJusted = 1
	INValid = 2
	OFF = 3
	ON = 4
	PENDing = 5
	RFHandover = 6


# noinspection SpellCheckingInspection
class SyncZone(Enum):
	"""2 Members, NONE ... Z1"""
	NONE = 0
	Z1 = 1


# noinspection SpellCheckingInspection
class TbfLevel(Enum):
	"""4 Members, EG2A ... GPRS"""
	EG2A = 0
	EG2B = 1
	EGPRs = 2
	GPRS = 3


# noinspection SpellCheckingInspection
class TchAssignment(Enum):
	"""5 Members, EARLy ... VEARly"""
	EARLy = 0
	LATE = 1
	OFF = 2
	ON = 3
	VEARly = 4


# noinspection SpellCheckingInspection
class TxConnector(Enum):
	"""77 Members, I12O ... RH18"""
	I12O = 0
	I14O = 1
	I16O = 2
	I18O = 3
	I22O = 4
	I24O = 5
	I26O = 6
	I28O = 7
	I32O = 8
	I34O = 9
	I36O = 10
	I38O = 11
	I42O = 12
	I44O = 13
	I46O = 14
	I48O = 15
	IF1 = 16
	IF2 = 17
	IF3 = 18
	IQ2O = 19
	IQ4O = 20
	IQ6O = 21
	IQ8O = 22
	R118 = 23
	R1183 = 24
	R1184 = 25
	R11C = 26
	R11O = 27
	R11O3 = 28
	R11O4 = 29
	R12C = 30
	R13C = 31
	R13O = 32
	R14C = 33
	R214 = 34
	R218 = 35
	R21C = 36
	R21O = 37
	R22C = 38
	R23C = 39
	R23O = 40
	R24C = 41
	R258 = 42
	R318 = 43
	R31C = 44
	R31O = 45
	R32C = 46
	R33C = 47
	R33O = 48
	R34C = 49
	R418 = 50
	R41C = 51
	R41O = 52
	R42C = 53
	R43C = 54
	R43O = 55
	R44C = 56
	RA18 = 57
	RB14 = 58
	RB18 = 59
	RC18 = 60
	RD18 = 61
	RE18 = 62
	RF18 = 63
	RF1C = 64
	RF1O = 65
	RF2C = 66
	RF3C = 67
	RF3O = 68
	RF4C = 69
	RF5C = 70
	RF6C = 71
	RFAC = 72
	RFAO = 73
	RFBC = 74
	RG18 = 75
	RH18 = 76


# noinspection SpellCheckingInspection
class TxConverter(Enum):
	"""40 Members, ITX1 ... TX44"""
	ITX1 = 0
	ITX11 = 1
	ITX12 = 2
	ITX13 = 3
	ITX14 = 4
	ITX2 = 5
	ITX21 = 6
	ITX22 = 7
	ITX23 = 8
	ITX24 = 9
	ITX3 = 10
	ITX31 = 11
	ITX32 = 12
	ITX33 = 13
	ITX34 = 14
	ITX4 = 15
	ITX41 = 16
	ITX42 = 17
	ITX43 = 18
	ITX44 = 19
	TX1 = 20
	TX11 = 21
	TX12 = 22
	TX13 = 23
	TX14 = 24
	TX2 = 25
	TX21 = 26
	TX22 = 27
	TX23 = 28
	TX24 = 29
	TX3 = 30
	TX31 = 31
	TX32 = 32
	TX33 = 33
	TX34 = 34
	TX4 = 35
	TX41 = 36
	TX42 = 37
	TX43 = 38
	TX44 = 39


# noinspection SpellCheckingInspection
class UplinkCodingScheme(Enum):
	"""28 Members, C1 ... UB9"""
	C1 = 0
	C2 = 1
	C3 = 2
	C4 = 3
	MC1 = 4
	MC2 = 5
	MC3 = 6
	MC4 = 7
	MC5 = 8
	MC6 = 9
	MC7 = 10
	MC8 = 11
	MC9 = 12
	OFF = 13
	ON = 14
	UA10 = 15
	UA11 = 16
	UA7 = 17
	UA8 = 18
	UA9 = 19
	UB10 = 20
	UB11 = 21
	UB12 = 22
	UB5 = 23
	UB6 = 24
	UB7 = 25
	UB8 = 26
	UB9 = 27


# noinspection SpellCheckingInspection
class VamosMode(Enum):
	"""3 Members, AUTO ... VAM2"""
	AUTO = 0
	VAM1 = 1
	VAM2 = 2


# noinspection SpellCheckingInspection
class WbCodec(Enum):
	"""7 Members, C0660 ... ON"""
	C0660 = 0
	C0885 = 1
	C1265 = 2
	C1585 = 3
	C2385 = 4
	OFF = 5
	ON = 6


# noinspection SpellCheckingInspection
class WmQuantity(Enum):
	"""2 Members, ECNO ... RSCP"""
	ECNO = 0
	RSCP = 1
