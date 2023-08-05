from enum import Enum


# noinspection SpellCheckingInspection
class AllocatedSlots(Enum):
	"""1 Members, ALL ... ALL"""
	ALL = 0


# noinspection SpellCheckingInspection
class Band(Enum):
	"""32 Members, OB1 ... OB86"""
	OB1 = 0
	OB12 = 1
	OB2 = 2
	OB20 = 3
	OB25 = 4
	OB28 = 5
	OB3 = 6
	OB34 = 7
	OB38 = 8
	OB39 = 9
	OB40 = 10
	OB41 = 11
	OB5 = 12
	OB50 = 13
	OB51 = 14
	OB66 = 15
	OB7 = 16
	OB70 = 17
	OB71 = 18
	OB74 = 19
	OB75 = 20
	OB76 = 21
	OB77 = 22
	OB78 = 23
	OB79 = 24
	OB8 = 25
	OB80 = 26
	OB81 = 27
	OB82 = 28
	OB83 = 29
	OB84 = 30
	OB86 = 31


# noinspection SpellCheckingInspection
class BandwidthPart(Enum):
	"""1 Members, BWP0 ... BWP0"""
	BWP0 = 0


# noinspection SpellCheckingInspection
class CarrierPosition(Enum):
	"""2 Members, LONR ... RONR"""
	LONR = 0
	RONR = 1


# noinspection SpellCheckingInspection
class ChannelBwidth(Enum):
	"""12 Members, B005 ... B100"""
	B005 = 0
	B010 = 1
	B015 = 2
	B020 = 3
	B025 = 4
	B030 = 5
	B040 = 6
	B050 = 7
	B060 = 8
	B080 = 9
	B090 = 10
	B100 = 11


# noinspection SpellCheckingInspection
class ChannelBwidthB(Enum):
	"""4 Members, B005 ... B020"""
	B005 = 0
	B010 = 1
	B015 = 2
	B020 = 3


# noinspection SpellCheckingInspection
class ChannelTypeA(Enum):
	"""2 Members, PUCCh ... PUSCh"""
	PUCCh = 0
	PUSCh = 1


# noinspection SpellCheckingInspection
class ChannelTypeB(Enum):
	"""4 Members, OFF ... PUSCh"""
	OFF = 0
	ON = 1
	PUCCh = 2
	PUSCh = 3


# noinspection SpellCheckingInspection
class CmwsConnector(Enum):
	"""48 Members, R11 ... RB8"""
	R11 = 0
	R12 = 1
	R13 = 2
	R14 = 3
	R15 = 4
	R16 = 5
	R17 = 6
	R18 = 7
	R21 = 8
	R22 = 9
	R23 = 10
	R24 = 11
	R25 = 12
	R26 = 13
	R27 = 14
	R28 = 15
	R31 = 16
	R32 = 17
	R33 = 18
	R34 = 19
	R35 = 20
	R36 = 21
	R37 = 22
	R38 = 23
	R41 = 24
	R42 = 25
	R43 = 26
	R44 = 27
	R45 = 28
	R46 = 29
	R47 = 30
	R48 = 31
	RA1 = 32
	RA2 = 33
	RA3 = 34
	RA4 = 35
	RA5 = 36
	RA6 = 37
	RA7 = 38
	RA8 = 39
	RB1 = 40
	RB2 = 41
	RB3 = 42
	RB4 = 43
	RB5 = 44
	RB6 = 45
	RB7 = 46
	RB8 = 47


# noinspection SpellCheckingInspection
class ConfigType(Enum):
	"""2 Members, T1 ... T2"""
	T1 = 0
	T2 = 1


# noinspection SpellCheckingInspection
class CyclicPrefix(Enum):
	"""2 Members, EXTended ... NORMal"""
	EXTended = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class DuplexModeB(Enum):
	"""2 Members, FDD ... TDD"""
	FDD = 0
	TDD = 1


# noinspection SpellCheckingInspection
class Generator(Enum):
	"""2 Members, DID ... PHY"""
	DID = 0
	PHY = 1


# noinspection SpellCheckingInspection
class Lagging(Enum):
	"""3 Members, MS05 ... OFF"""
	MS05 = 0
	MS25 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class Leading(Enum):
	"""2 Members, MS25 ... OFF"""
	MS25 = 0
	OFF = 1


# noinspection SpellCheckingInspection
class ListMode(Enum):
	"""2 Members, ONCE ... SEGMent"""
	ONCE = 0
	SEGMent = 1


# noinspection SpellCheckingInspection
class LowHigh(Enum):
	"""2 Members, HIGH ... LOW"""
	HIGH = 0
	LOW = 1


# noinspection SpellCheckingInspection
class MappingType(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class MaxLength(Enum):
	"""2 Members, DOUBle ... SINGle"""
	DOUBle = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class MeasFilter(Enum):
	"""2 Members, BANDpass ... GAUSs"""
	BANDpass = 0
	GAUSs = 1


# noinspection SpellCheckingInspection
class MeasurementMode(Enum):
	"""2 Members, MELMode ... NORMal"""
	MELMode = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class MeasureSlot(Enum):
	"""5 Members, ALL ... MS3"""
	ALL = 0
	MS0 = 1
	MS1 = 2
	MS2 = 3
	MS3 = 4


# noinspection SpellCheckingInspection
class Modulation(Enum):
	"""6 Members, BPSK ... QPSK"""
	BPSK = 0
	BPWS = 1
	Q16 = 2
	Q256 = 3
	Q64 = 4
	QPSK = 5


# noinspection SpellCheckingInspection
class ModulationScheme(Enum):
	"""7 Members, AUTO ... QPSK"""
	AUTO = 0
	BPSK = 1
	BPWS = 2
	Q16 = 3
	Q256 = 4
	Q64 = 5
	QPSK = 6


# noinspection SpellCheckingInspection
class NetworkSigVal(Enum):
	"""33 Members, NS01 ... NS35"""
	NS01 = 0
	NS02 = 1
	NS03 = 2
	NS04 = 3
	NS05 = 4
	NS06 = 5
	NS07 = 6
	NS08 = 7
	NS09 = 8
	NS10 = 9
	NS11 = 10
	NS12 = 11
	NS13 = 12
	NS14 = 13
	NS15 = 14
	NS16 = 15
	NS17 = 16
	NS18 = 17
	NS19 = 18
	NS20 = 19
	NS21 = 20
	NS22 = 21
	NS23 = 22
	NS24 = 23
	NS25 = 24
	NS26 = 25
	NS27 = 26
	NS28 = 27
	NS29 = 28
	NS30 = 29
	NS31 = 30
	NS32 = 31
	NS35 = 32


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class Periodicity(Enum):
	"""9 Members, MS05 ... MS5"""
	MS05 = 0
	MS1 = 1
	MS10 = 2
	MS125 = 3
	MS2 = 4
	MS25 = 5
	MS3 = 6
	MS4 = 7
	MS5 = 8


# noinspection SpellCheckingInspection
class PeriodPreamble(Enum):
	"""3 Members, MS05 ... MS20"""
	MS05 = 0
	MS10 = 1
	MS20 = 2


# noinspection SpellCheckingInspection
class PhaseComp(Enum):
	"""3 Members, CAF ... UDEF"""
	CAF = 0
	OFF = 1
	UDEF = 2


# noinspection SpellCheckingInspection
class PreambleFormat(Enum):
	"""13 Members, PF0 ... PFC2"""
	PF0 = 0
	PF1 = 1
	PF2 = 2
	PF3 = 3
	PFA1 = 4
	PFA2 = 5
	PFA3 = 6
	PFB1 = 7
	PFB2 = 8
	PFB3 = 9
	PFB4 = 10
	PFC0 = 11
	PFC2 = 12


# noinspection SpellCheckingInspection
class PucchFormat(Enum):
	"""7 Members, F1 ... F3"""
	F1 = 0
	F1A = 1
	F1B = 2
	F2 = 3
	F2A = 4
	F2B = 5
	F3 = 6


# noinspection SpellCheckingInspection
class RbwA(Enum):
	"""3 Members, K030 ... PC1"""
	K030 = 0
	M1 = 1
	PC1 = 2


# noinspection SpellCheckingInspection
class RbwB(Enum):
	"""5 Members, K030 ... PC2"""
	K030 = 0
	K100 = 1
	M1 = 2
	PC1 = 3
	PC2 = 4


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
class RestrictedSet(Enum):
	"""1 Members, URES ... URES"""
	URES = 0


# noinspection SpellCheckingInspection
class ResultStatus2(Enum):
	"""10 Members, DC ... ULEU"""
	DC = 0
	INV = 1
	NAV = 2
	NCAP = 3
	OFF = 4
	OFL = 5
	OK = 6
	UFL = 7
	ULEL = 8
	ULEU = 9


# noinspection SpellCheckingInspection
class RetriggerFlag(Enum):
	"""3 Members, IFPower ... ON"""
	IFPower = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class RfConverter(Enum):
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
class RxConnector(Enum):
	"""163 Members, I11I ... RH8"""
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
	IFI1 = 16
	IFI2 = 17
	IFI3 = 18
	IFI4 = 19
	IFI5 = 20
	IFI6 = 21
	IQ1I = 22
	IQ3I = 23
	IQ5I = 24
	IQ7I = 25
	R10D = 26
	R11 = 27
	R11C = 28
	R11D = 29
	R12 = 30
	R12C = 31
	R12D = 32
	R12I = 33
	R13 = 34
	R13C = 35
	R14 = 36
	R14C = 37
	R14I = 38
	R15 = 39
	R16 = 40
	R17 = 41
	R18 = 42
	R21 = 43
	R21C = 44
	R22 = 45
	R22C = 46
	R22I = 47
	R23 = 48
	R23C = 49
	R24 = 50
	R24C = 51
	R24I = 52
	R25 = 53
	R26 = 54
	R27 = 55
	R28 = 56
	R31 = 57
	R31C = 58
	R32 = 59
	R32C = 60
	R32I = 61
	R33 = 62
	R33C = 63
	R34 = 64
	R34C = 65
	R34I = 66
	R35 = 67
	R36 = 68
	R37 = 69
	R38 = 70
	R41 = 71
	R41C = 72
	R42 = 73
	R42C = 74
	R42I = 75
	R43 = 76
	R43C = 77
	R44 = 78
	R44C = 79
	R44I = 80
	R45 = 81
	R46 = 82
	R47 = 83
	R48 = 84
	RA1 = 85
	RA2 = 86
	RA3 = 87
	RA4 = 88
	RA5 = 89
	RA6 = 90
	RA7 = 91
	RA8 = 92
	RB1 = 93
	RB2 = 94
	RB3 = 95
	RB4 = 96
	RB5 = 97
	RB6 = 98
	RB7 = 99
	RB8 = 100
	RC1 = 101
	RC2 = 102
	RC3 = 103
	RC4 = 104
	RC5 = 105
	RC6 = 106
	RC7 = 107
	RC8 = 108
	RD1 = 109
	RD2 = 110
	RD3 = 111
	RD4 = 112
	RD5 = 113
	RD6 = 114
	RD7 = 115
	RD8 = 116
	RE1 = 117
	RE2 = 118
	RE3 = 119
	RE4 = 120
	RE5 = 121
	RE6 = 122
	RE7 = 123
	RE8 = 124
	RF1 = 125
	RF1C = 126
	RF2 = 127
	RF2C = 128
	RF2I = 129
	RF3 = 130
	RF3C = 131
	RF4 = 132
	RF4C = 133
	RF4I = 134
	RF5 = 135
	RF5C = 136
	RF6 = 137
	RF6C = 138
	RF7 = 139
	RF7C = 140
	RF8 = 141
	RF8C = 142
	RF9C = 143
	RFAC = 144
	RFBC = 145
	RFBI = 146
	RG1 = 147
	RG2 = 148
	RG3 = 149
	RG4 = 150
	RG5 = 151
	RG6 = 152
	RG7 = 153
	RG8 = 154
	RH1 = 155
	RH2 = 156
	RH3 = 157
	RH4 = 158
	RH5 = 159
	RH6 = 160
	RH7 = 161
	RH8 = 162


# noinspection SpellCheckingInspection
class Scenario(Enum):
	"""4 Members, CSPath ... SALone"""
	CSPath = 0
	MAPRotocol = 1
	NAV = 2
	SALone = 3


# noinspection SpellCheckingInspection
class SignalSlope(Enum):
	"""2 Members, FEDGe ... REDGe"""
	FEDGe = 0
	REDGe = 1


# noinspection SpellCheckingInspection
class StopCondition(Enum):
	"""2 Members, NONE ... SLFail"""
	NONE = 0
	SLFail = 1


# noinspection SpellCheckingInspection
class SubCarrSpacing(Enum):
	"""3 Members, S15K ... S60K"""
	S15K = 0
	S30K = 1
	S60K = 2


# noinspection SpellCheckingInspection
class SubCarrSpacingB(Enum):
	"""5 Members, S15K ... S60K"""
	S15K = 0
	S1K2 = 1
	S30K = 2
	S5K = 3
	S60K = 4


# noinspection SpellCheckingInspection
class SyncMode(Enum):
	"""2 Members, ENHanced ... NORMal"""
	ENHanced = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class TimeMask(Enum):
	"""3 Members, GOO ... SBLanking"""
	GOO = 0
	PPSRs = 1
	SBLanking = 2
