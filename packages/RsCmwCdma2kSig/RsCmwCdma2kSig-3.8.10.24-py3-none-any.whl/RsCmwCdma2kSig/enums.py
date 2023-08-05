from enum import Enum


# noinspection SpellCheckingInspection
class AcceptState(Enum):
	"""2 Members, ACCept ... REJect"""
	ACCept = 0
	REJect = 1


# noinspection SpellCheckingInspection
class AccessProbeMode(Enum):
	"""2 Members, ACK ... IGN"""
	ACK = 0
	IGN = 1


# noinspection SpellCheckingInspection
class AckState(Enum):
	"""2 Members, ACK ... NACK"""
	ACK = 0
	NACK = 1


# noinspection SpellCheckingInspection
class ApplyTimeAt(Enum):
	"""3 Members, EVER ... SUSO"""
	EVER = 0
	NEXT = 1
	SUSO = 2


# noinspection SpellCheckingInspection
class AvgEncodingRate(Enum):
	"""8 Members, R48K ... R93K"""
	R48K = 0
	R58K = 1
	R62K = 2
	R66K = 3
	R70K = 4
	R75K = 5
	R85K = 6
	R93K = 7


# noinspection SpellCheckingInspection
class BandClass(Enum):
	"""23 Members, AWS ... USPC"""
	AWS = 0
	B18M = 1
	IEXT = 2
	IM2K = 3
	JTAC = 4
	KCEL = 5
	KPCS = 6
	LBANd = 7
	LO7C = 8
	N45T = 9
	NA7C = 10
	NA8S = 11
	NA9C = 12
	NAPC = 13
	PA4M = 14
	PA8M = 15
	PS7C = 16
	SBANd = 17
	TACS = 18
	U25B = 19
	U25F = 20
	USC = 21
	USPC = 22


# noinspection SpellCheckingInspection
class CallerIdPresentation(Enum):
	"""3 Members, NNAV ... PRES"""
	NNAV = 0
	PAL = 1
	PRES = 2


# noinspection SpellCheckingInspection
class CsAction(Enum):
	"""6 Members, BROadcast ... UNRegister"""
	BROadcast = 0
	CONNect = 1
	DISConnect = 2
	HANDoff = 3
	SMS = 4
	UNRegister = 5


# noinspection SpellCheckingInspection
class CsState(Enum):
	"""9 Members, ALERting ... SENDing"""
	ALERting = 0
	BROadcast = 1
	CONNected = 2
	IDLE = 3
	OFF = 4
	ON = 5
	PAGing = 6
	REGistered = 7
	SENDing = 8


# noinspection SpellCheckingInspection
class DeliveryStatus(Enum):
	"""5 Members, ACKTimeout ... SUCCess"""
	ACKTimeout = 0
	BADData = 1
	CSTate = 2
	PENDing = 3
	SUCCess = 4


# noinspection SpellCheckingInspection
class DeviceType(Enum):
	"""3 Members, FULL ... NO"""
	FULL = 0
	LIMited = 1
	NO = 2


# noinspection SpellCheckingInspection
class DirectionHorizontal(Enum):
	"""2 Members, EAST ... WEST"""
	EAST = 0
	WEST = 1


# noinspection SpellCheckingInspection
class DirectionVertical(Enum):
	"""2 Members, NORTh ... SOUTh"""
	NORTh = 0
	SOUTh = 1


# noinspection SpellCheckingInspection
class DisplayTab(Enum):
	"""5 Members, FERFch ... SPEech"""
	FERFch = 0
	FERSch0 = 1
	POWer = 2
	RLP = 3
	SPEech = 4


# noinspection SpellCheckingInspection
class ExpectedPowerMode(Enum):
	"""4 Members, MANual ... OLRule"""
	MANual = 0
	MAX = 1
	MIN = 2
	OLRule = 3


# noinspection SpellCheckingInspection
class FadingSimRestartMode(Enum):
	"""3 Members, AUTO ... TRIGger"""
	AUTO = 0
	MANual = 1
	TRIGger = 2


# noinspection SpellCheckingInspection
class FadingSimStandard(Enum):
	"""6 Members, P1 ... P6"""
	P1 = 0
	P2 = 1
	P3 = 2
	P4 = 3
	P5 = 4
	P6 = 5


# noinspection SpellCheckingInspection
class ForwardCoding(Enum):
	"""2 Members, CONV ... TURB"""
	CONV = 0
	TURB = 1


# noinspection SpellCheckingInspection
class ForwardDataRate(Enum):
	"""10 Members, R115k ... R9K"""
	R115k = 0
	R14K = 1
	R153k = 2
	R19K = 3
	R230k = 4
	R28K = 5
	R38K = 6
	R57K = 7
	R76K = 8
	R9K = 9


# noinspection SpellCheckingInspection
class ForwardFrameType(Enum):
	"""2 Members, R1 ... R2"""
	R1 = 0
	R2 = 1


# noinspection SpellCheckingInspection
class FrameRate(Enum):
	"""4 Members, EIGHth ... QUARter"""
	EIGHth = 0
	FULL = 1
	HALF = 2
	QUARter = 3


# noinspection SpellCheckingInspection
class GeoLocationType(Enum):
	"""4 Members, AAG ... NSUP"""
	AAG = 0
	AFLT = 1
	GPS = 2
	NSUP = 3


# noinspection SpellCheckingInspection
class HookStatus(Enum):
	"""3 Members, OFF ... SOFF"""
	OFF = 0
	ON = 1
	SOFF = 2


# noinspection SpellCheckingInspection
class InsertLossMode(Enum):
	"""3 Members, LACP ... USER"""
	LACP = 0
	NORMal = 1
	USER = 2


# noinspection SpellCheckingInspection
class IpAddressIndex(Enum):
	"""3 Members, IP1 ... IP3"""
	IP1 = 0
	IP2 = 1
	IP3 = 2


# noinspection SpellCheckingInspection
class KeepConstant(Enum):
	"""2 Members, DSHift ... SPEed"""
	DSHift = 0
	SPEed = 1


# noinspection SpellCheckingInspection
class Language(Enum):
	"""41 Members, AFRikaans ... VIETnamese"""
	AFRikaans = 0
	ARABic = 1
	BAHasa = 2
	BENGali = 3
	CHINese = 4
	CZECh = 5
	DANish = 6
	DUTCh = 7
	ENGLish = 8
	FINNish = 9
	FRENch = 10
	GERMan = 11
	GREek = 12
	GUJarati = 13
	HAUSa = 14
	HEBRew = 15
	HINDi = 16
	HUNGarian = 17
	ICELandic = 18
	ITALian = 19
	JAPanese = 20
	KANNada = 21
	KORean = 22
	MALayalam = 23
	NORWegian = 24
	ORIYa = 25
	POLish = 26
	PORTuguese = 27
	PUNJabi = 28
	RUSSian = 29
	SPANish = 30
	SWAHili = 31
	SWEDish = 32
	TAGalog = 33
	TAMil = 34
	TELugu = 35
	THAI = 36
	TURKish = 37
	UNDefined = 38
	URDU = 39
	VIETnamese = 40


# noinspection SpellCheckingInspection
class LogCategory(Enum):
	"""4 Members, CONTinue ... WARNing"""
	CONTinue = 0
	ERRor = 1
	INFO = 2
	WARNing = 3


# noinspection SpellCheckingInspection
class LongSmsHandling(Enum):
	"""2 Members, MSMS ... TRUNcate"""
	MSMS = 0
	TRUNcate = 1


# noinspection SpellCheckingInspection
class MainState(Enum):
	"""3 Members, OFF ... RFHandover"""
	OFF = 0
	ON = 1
	RFHandover = 2


# noinspection SpellCheckingInspection
class MessageHandling(Enum):
	"""2 Members, FILE ... INTernal"""
	FILE = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class MocCallsAcceptMode(Enum):
	"""13 Members, ALL ... SCL1"""
	ALL = 0
	BUAW = 1
	BUFW = 2
	FSC1 = 3
	ICAW = 4
	ICFW = 5
	ICOR = 6
	IGNR = 7
	RERO = 8
	ROAW = 9
	ROFW = 10
	ROOR = 11
	SCL1 = 12


# noinspection SpellCheckingInspection
class Modulation(Enum):
	"""2 Members, HPSK ... QPSK"""
	HPSK = 0
	QPSK = 1


# noinspection SpellCheckingInspection
class NetworkSegment(Enum):
	"""3 Members, A ... C"""
	A = 0
	B = 1
	C = 2


# noinspection SpellCheckingInspection
class OtaspSendMethodA(Enum):
	"""3 Members, NONE ... SO19"""
	NONE = 0
	SO18 = 1
	SO19 = 2


# noinspection SpellCheckingInspection
class OtaspSendMethodB(Enum):
	"""4 Members, NONE ... TCH"""
	NONE = 0
	SO18 = 1
	SO19 = 2
	TCH = 3


# noinspection SpellCheckingInspection
class PagingChannelRate(Enum):
	"""2 Members, R4K8 ... R9K6"""
	R4K8 = 0
	R9K6 = 1


# noinspection SpellCheckingInspection
class PatternGeneration(Enum):
	"""2 Members, FIX ... RAND"""
	FIX = 0
	RAND = 1


# noinspection SpellCheckingInspection
class PdmSendMethodA(Enum):
	"""4 Members, NONE ... SO36"""
	NONE = 0
	PCH = 1
	SO35 = 2
	SO36 = 3


# noinspection SpellCheckingInspection
class PdmSendMethodB(Enum):
	"""5 Members, NONE ... TCH"""
	NONE = 0
	PCH = 1
	SO35 = 2
	SO36 = 3
	TCH = 4


# noinspection SpellCheckingInspection
class PlcmDerivation(Enum):
	"""2 Members, ESN ... MEID"""
	ESN = 0
	MEID = 1


# noinspection SpellCheckingInspection
class PnChips(Enum):
	"""16 Members, C10 ... C80"""
	C10 = 0
	C100 = 1
	C130 = 2
	C14 = 3
	C160 = 4
	C20 = 5
	C226 = 6
	C28 = 7
	C320 = 8
	C4 = 9
	C40 = 10
	C452 = 11
	C6 = 12
	C60 = 13
	C8 = 14
	C80 = 15


# noinspection SpellCheckingInspection
class PowerCtrlBits(Enum):
	"""6 Members, ADOWn ... RTESt"""
	ADOWn = 0
	AUP = 1
	AUTO = 2
	HOLD = 3
	PATTern = 4
	RTESt = 5


# noinspection SpellCheckingInspection
class PriorityB(Enum):
	"""4 Members, EMERgency ... URGent"""
	EMERgency = 0
	INTeractive = 1
	NORMal = 2
	URGent = 3


# noinspection SpellCheckingInspection
class QueueState(Enum):
	"""2 Members, OK ... OVERflow"""
	OK = 0
	OVERflow = 1


# noinspection SpellCheckingInspection
class RadioConfig(Enum):
	"""5 Members, F1R1 ... F5R4"""
	F1R1 = 0
	F2R2 = 1
	F3R3 = 2
	F4R3 = 3
	F5R4 = 4


# noinspection SpellCheckingInspection
class RateRestriction(Enum):
	"""5 Members, AUTO ... QUARter"""
	AUTO = 0
	EIGHth = 1
	FULL = 2
	HALF = 3
	QUARter = 4


# noinspection SpellCheckingInspection
class RegistrationType(Enum):
	"""10 Members, DISTance ... ZONE"""
	DISTance = 0
	IMPLicit = 1
	IORM = 2
	ORDered = 3
	PARChange = 4
	PWDown = 5
	PWUP = 6
	TIMer = 7
	USEZone = 8
	ZONE = 9


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
class Scenario(Enum):
	"""6 Members, HMFading ... UNDefined"""
	HMFading = 0
	HMLite = 1
	HMODe = 2
	SCELl = 3
	SCFading = 4
	UNDefined = 5


# noinspection SpellCheckingInspection
class SegmentBits(Enum):
	"""3 Members, ALTernating ... UP"""
	ALTernating = 0
	DOWN = 1
	UP = 2


# noinspection SpellCheckingInspection
class ServiceOption(Enum):
	"""12 Members, SO1 ... SO9"""
	SO1 = 0
	SO17 = 1
	SO2 = 2
	SO3 = 3
	SO32 = 4
	SO33 = 5
	SO55 = 6
	SO68 = 7
	SO70 = 8
	SO73 = 9
	SO8000 = 10
	SO9 = 11


# noinspection SpellCheckingInspection
class SmsSendMethod(Enum):
	"""5 Members, ACH ... TCH"""
	ACH = 0
	PCH = 1
	SO14 = 2
	SO6 = 3
	TCH = 4


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class StopConditionB(Enum):
	"""4 Members, ALEXeeded ... NONE"""
	ALEXeeded = 0
	MCLexceeded = 1
	MFER = 2
	NONE = 3


# noinspection SpellCheckingInspection
class Supported(Enum):
	"""2 Members, NSUP ... SUPP"""
	NSUP = 0
	SUPP = 1


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
class TimeSource(Enum):
	"""3 Members, CMWTime ... SYNC"""
	CMWTime = 0
	DATE = 1
	SYNC = 2


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
class VoiceCoder(Enum):
	"""2 Members, CODE ... ECHO"""
	CODE = 0
	ECHO = 1


# noinspection SpellCheckingInspection
class YesNoStatus(Enum):
	"""2 Members, NO ... YES"""
	NO = 0
	YES = 1
