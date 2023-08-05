from enum import Enum


# noinspection SpellCheckingInspection
class AccessDuration(Enum):
	"""4 Members, S128 ... S64"""
	S128 = 0
	S16 = 1
	S32 = 2
	S64 = 3


# noinspection SpellCheckingInspection
class ApplicationMode(Enum):
	"""4 Members, FAR ... REV"""
	FAR = 0
	FWD = 1
	PACKet = 2
	REV = 3


# noinspection SpellCheckingInspection
class ApplyTimeAt(Enum):
	"""3 Members, EVER ... SUSO"""
	EVER = 0
	NEXT = 1
	SUSO = 2


# noinspection SpellCheckingInspection
class AutoManualMode(Enum):
	"""2 Members, AUTO ... MANual"""
	AUTO = 0
	MANual = 1


# noinspection SpellCheckingInspection
class AwgnMode(Enum):
	"""2 Members, HPOWer ... NORMal"""
	HPOWer = 0
	NORMal = 1


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
class CarrierStatus(Enum):
	"""4 Members, INACtive ... VIOLated"""
	INACtive = 0
	OK = 1
	STALe = 2
	VIOLated = 3


# noinspection SpellCheckingInspection
class ConnectionState(Enum):
	"""7 Members, CONNected ... SOPen"""
	CONNected = 0
	IDLE = 1
	OFF = 2
	ON = 3
	PAGing = 4
	SNEGotiation = 5
	SOPen = 6


# noinspection SpellCheckingInspection
class CswitchedAction(Enum):
	"""4 Members, CLOSe ... HANDoff"""
	CLOSe = 0
	CONNect = 1
	DISConnect = 2
	HANDoff = 3


# noinspection SpellCheckingInspection
class CtrlChannelDataRate(Enum):
	"""2 Members, R384 ... R768"""
	R384 = 0
	R768 = 1


# noinspection SpellCheckingInspection
class DisplayTab(Enum):
	"""6 Members, CTRLchper ... THRoughput"""
	CTRLchper = 0
	DATA = 1
	OVERview = 2
	PER = 3
	RLQ = 4
	THRoughput = 5


# noinspection SpellCheckingInspection
class ExpPowerMode(Enum):
	"""5 Members, AUTO ... OLRule"""
	AUTO = 0
	MANual = 1
	MAX = 2
	MIN = 3
	OLRule = 4


# noinspection SpellCheckingInspection
class Fmode(Enum):
	"""3 Members, AALWays ... NUSed"""
	AALWays = 0
	NAALways = 1
	NUSed = 2


# noinspection SpellCheckingInspection
class FsimStandard(Enum):
	"""5 Members, P1 ... P5"""
	P1 = 0
	P2 = 1
	P3 = 2
	P4 = 3
	P5 = 4


# noinspection SpellCheckingInspection
class InsertLossMode(Enum):
	"""2 Members, NORMal ... USER"""
	NORMal = 0
	USER = 1


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
class LinkCarrier(Enum):
	"""4 Members, ACTive ... NCConnected"""
	ACTive = 0
	DISabled = 1
	NACTive = 2
	NCConnected = 3


# noinspection SpellCheckingInspection
class LogCategory(Enum):
	"""4 Members, CONTinue ... WARNing"""
	CONTinue = 0
	ERRor = 1
	INFO = 2
	WARNing = 3


# noinspection SpellCheckingInspection
class LteBand(Enum):
	"""45 Members, OB1 ... UDEFined"""
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
	OB26 = 18
	OB27 = 19
	OB28 = 20
	OB29 = 21
	OB3 = 22
	OB30 = 23
	OB31 = 24
	OB32 = 25
	OB33 = 26
	OB34 = 27
	OB35 = 28
	OB36 = 29
	OB37 = 30
	OB38 = 31
	OB39 = 32
	OB4 = 33
	OB40 = 34
	OB41 = 35
	OB42 = 36
	OB43 = 37
	OB44 = 38
	OB5 = 39
	OB6 = 40
	OB7 = 41
	OB8 = 42
	OB9 = 43
	UDEFined = 44


# noinspection SpellCheckingInspection
class MainGenState(Enum):
	"""3 Members, OFF ... RFHandover"""
	OFF = 0
	ON = 1
	RFHandover = 2


# noinspection SpellCheckingInspection
class NetworkRelease(Enum):
	"""3 Members, R0 ... RB"""
	R0 = 0
	RA = 1
	RB = 2


# noinspection SpellCheckingInspection
class NetworkSegment(Enum):
	"""3 Members, A ... C"""
	A = 0
	B = 1
	C = 2


# noinspection SpellCheckingInspection
class PacketSize(Enum):
	"""12 Members, S128 ... TOTal"""
	S128 = 0
	S1K = 1
	S256 = 2
	S2K = 3
	S3K = 4
	S4K = 5
	S512 = 6
	S5K = 7
	S6K = 8
	S7K = 9
	S8K = 10
	TOTal = 11


# noinspection SpellCheckingInspection
class PdState(Enum):
	"""4 Members, CONNected ... ON"""
	CONNected = 0
	DORMant = 1
	OFF = 2
	ON = 3


# noinspection SpellCheckingInspection
class PerEvaluation(Enum):
	"""2 Members, ALLCarriers ... PERCarrier"""
	ALLCarriers = 0
	PERCarrier = 1


# noinspection SpellCheckingInspection
class PerStopCondition(Enum):
	"""4 Members, ALEXceeded ... NONE"""
	ALEXceeded = 0
	MCLexceeded = 1
	MPERexceeded = 2
	NONE = 3


# noinspection SpellCheckingInspection
class PlSlots(Enum):
	"""2 Members, S16 ... S4"""
	S16 = 0
	S4 = 1


# noinspection SpellCheckingInspection
class PlSubtype(Enum):
	"""3 Members, ST01 ... ST3"""
	ST01 = 0
	ST2 = 1
	ST3 = 2


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
class PrefApplication(Enum):
	"""2 Members, DPA ... EMPA"""
	DPA = 0
	EMPA = 1


# noinspection SpellCheckingInspection
class PrefAppMode(Enum):
	"""2 Members, EHRPd ... HRPD"""
	EHRPd = 0
	HRPD = 1


# noinspection SpellCheckingInspection
class ProbesAckMode(Enum):
	"""2 Members, ACKN ... IGN"""
	ACKN = 0
	IGN = 1


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
class RevLinkPerDataRate(Enum):
	"""14 Members, R0K0 ... TOTal"""
	R0K0 = 0
	R115k2 = 1
	R1228k8 = 2
	R153k6 = 3
	R1843k2 = 4
	R19K2 = 5
	R230k4 = 6
	R307k2 = 7
	R38K4 = 8
	R460k8 = 9
	R614k4 = 10
	R76K8 = 11
	R921k6 = 12
	TOTal = 13


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
class RxSignalState(Enum):
	"""4 Members, HIGH ... OK"""
	HIGH = 0
	LOW = 1
	NAV = 2
	OK = 3


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
class SamRate(Enum):
	"""3 Members, R19K ... R9K"""
	R19K = 0
	R38K = 1
	R9K = 2


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
class SectorIdFormat(Enum):
	"""2 Members, A41N ... MANual"""
	A41N = 0
	MANual = 1


# noinspection SpellCheckingInspection
class SegmentBits(Enum):
	"""3 Members, ALTernating ... UP"""
	ALTernating = 0
	DOWN = 1
	UP = 2


# noinspection SpellCheckingInspection
class SlopeType(Enum):
	"""2 Members, NEGative ... POSitive"""
	NEGative = 0
	POSitive = 1


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


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
class T2Pmode(Enum):
	"""2 Members, RFCO ... TPUT"""
	RFCO = 0
	TPUT = 1


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
