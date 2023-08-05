from enum import Enum


# noinspection SpellCheckingInspection
class AckNack(Enum):
	"""3 Members, ACK ... NACK"""
	ACK = 0
	DTX = 1
	NACK = 2


# noinspection SpellCheckingInspection
class AmrCodecModeNarrow(Enum):
	"""9 Members, A ... M"""
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	F = 5
	G = 6
	H = 7
	M = 8


# noinspection SpellCheckingInspection
class AmrCodecModeWide(Enum):
	"""12 Members, A ... M2"""
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	F = 5
	G = 6
	H = 7
	I = 8
	M = 9
	M1 = 10
	M2 = 11


# noinspection SpellCheckingInspection
class AutoManualMode(Enum):
	"""2 Members, AUTO ... MANual"""
	AUTO = 0
	MANual = 1


# noinspection SpellCheckingInspection
class AveragingMode(Enum):
	"""2 Members, CONTinuous ... WINDow"""
	CONTinuous = 0
	WINDow = 1


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
class BasebandBoard(Enum):
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
class BitPattern(Enum):
	"""7 Members, ALL0 ... PRBS9"""
	ALL0 = 0
	ALL1 = 1
	ALTernating = 2
	PRBS11 = 3
	PRBS13 = 4
	PRBS15 = 5
	PRBS9 = 6


# noinspection SpellCheckingInspection
class Bsic(Enum):
	"""2 Members, NONVerified ... VERified"""
	NONVerified = 0
	VERified = 1


# noinspection SpellCheckingInspection
class BtfdDataRate(Enum):
	"""9 Members, R10K2 ... R7K95"""
	R10K2 = 0
	R12K2 = 1
	R1K95 = 2
	R4K75 = 3
	R5K15 = 4
	R5K9 = 5
	R6K7 = 6
	R7K4 = 7
	R7K95 = 8


# noinspection SpellCheckingInspection
class CallRelease(Enum):
	"""2 Members, LOCal ... NORMal"""
	LOCal = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class CbsMessageSeverity(Enum):
	"""9 Members, AAMBer ... UDEFined"""
	AAMBer = 0
	AEXTreme = 1
	APResidentia = 2
	ASEVere = 3
	EARThquake = 4
	ETWarning = 5
	ETWTest = 6
	TSUNami = 7
	UDEFined = 8


# noinspection SpellCheckingInspection
class CellConfig(Enum):
	"""16 Members, _3CHS ... WCDMa"""
	_3CHS = 0
	_3DUPlus = 1
	_3HDU = 2
	_4CHS = 3
	_4DUPlus = 4
	_4HDU = 5
	DCHS = 6
	DDUPlus = 7
	DHDU = 8
	HDUPlus = 9
	HSDPa = 10
	HSPA = 11
	HSPLus = 12
	HSUPa = 13
	QPSK = 14
	WCDMa = 15


# noinspection SpellCheckingInspection
class CellPower(Enum):
	"""4 Members, NAV ... UFL"""
	NAV = 0
	OFL = 1
	OK = 2
	UFL = 3


# noinspection SpellCheckingInspection
class ChannelType(Enum):
	"""3 Members, CQI ... UDEFined"""
	CQI = 0
	FIXed = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class Cipher(Enum):
	"""3 Members, UEA0 ... UEA2"""
	UEA0 = 0
	UEA1 = 1
	UEA2 = 2


# noinspection SpellCheckingInspection
class ClosedLoopPower(Enum):
	"""2 Members, DPCH ... TOTal"""
	DPCH = 0
	TOTal = 1


# noinspection SpellCheckingInspection
class CmodeActivation(Enum):
	"""2 Members, MEASurement ... RAB"""
	MEASurement = 0
	RAB = 1


# noinspection SpellCheckingInspection
class CmodePatternSelection(Enum):
	"""4 Members, NONE ... ULCM"""
	NONE = 0
	SINGle = 1
	UEReport = 2
	ULCM = 3


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
	"""3 Members, DCMClass ... REServed"""
	DCMClass = 0
	GDCoding = 1
	REServed = 2


# noinspection SpellCheckingInspection
class CompressedMode(Enum):
	"""4 Members, NN ... YY"""
	NN = 0
	NY = 1
	YN = 2
	YY = 3


# noinspection SpellCheckingInspection
class CompressedModeBand(Enum):
	"""25 Members, OB1 ... OB9"""
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
	OB25 = 15
	OB26 = 16
	OB3 = 17
	OB32 = 18
	OB4 = 19
	OB5 = 20
	OB6 = 21
	OB7 = 22
	OB8 = 23
	OB9 = 24


# noinspection SpellCheckingInspection
class Condition(Enum):
	"""5 Members, ALTernating ... TPOWer"""
	ALTernating = 0
	MAXPower = 1
	MINPower = 2
	NONE = 3
	TPOWer = 4


# noinspection SpellCheckingInspection
class ConditionB(Enum):
	"""4 Members, ALTernating ... TPOWer"""
	ALTernating = 0
	MAXPower = 1
	MINPower = 2
	TPOWer = 3


# noinspection SpellCheckingInspection
class CounterValue(Enum):
	"""8 Members, N1 ... N50"""
	N1 = 0
	N10 = 1
	N100 = 2
	N2 = 3
	N20 = 4
	N200 = 5
	N4 = 6
	N50 = 7


# noinspection SpellCheckingInspection
class Cqi(Enum):
	"""32 Members, _0 ... DTX"""
	_0 = 0
	_1 = 1
	_10 = 2
	_11 = 3
	_12 = 4
	_13 = 5
	_14 = 6
	_15 = 7
	_16 = 8
	_17 = 9
	_18 = 10
	_19 = 11
	_2 = 12
	_20 = 13
	_21 = 14
	_22 = 15
	_23 = 16
	_24 = 17
	_25 = 18
	_26 = 19
	_27 = 20
	_28 = 21
	_29 = 22
	_3 = 23
	_30 = 24
	_4 = 25
	_5 = 26
	_6 = 27
	_7 = 28
	_8 = 29
	_9 = 30
	DTX = 31


# noinspection SpellCheckingInspection
class CsFallbackConnectionType(Enum):
	"""2 Members, TMRMc ... VOICe"""
	TMRMc = 0
	VOICe = 1


# noinspection SpellCheckingInspection
class CswitchedAction(Enum):
	"""5 Members, CONNect ... UNRegister"""
	CONNect = 0
	DISConnect = 1
	HANDover = 2
	SSMS = 3
	UNRegister = 4


# noinspection SpellCheckingInspection
class CswitchedState(Enum):
	"""15 Members, ALERting ... SIGNaling"""
	ALERting = 0
	CESTablished = 1
	CONNecting = 2
	IHANdover = 3
	IHPReparate = 4
	IREDirection = 5
	IRPReparate = 6
	OFF = 7
	OHANdover = 8
	ON = 9
	OREDirection = 10
	PAGing = 11
	REGister = 12
	RELeasing = 13
	SIGNaling = 14


# noinspection SpellCheckingInspection
class CurrentConnectionType(Enum):
	"""8 Members, NONE ... VOPacket"""
	NONE = 0
	PACKet = 1
	SRB = 2
	TEST = 3
	VIDeo = 4
	VIPacket = 5
	VOICe = 6
	VOPacket = 7


# noinspection SpellCheckingInspection
class DataRateDownlink(Enum):
	"""7 Members, HSDPa ... R8"""
	HSDPa = 0
	R128 = 1
	R16 = 2
	R32 = 3
	R384 = 4
	R64 = 5
	R8 = 6


# noinspection SpellCheckingInspection
class DataRateUplink(Enum):
	"""7 Members, HSUPa ... R8"""
	HSUPa = 0
	R128 = 1
	R16 = 2
	R32 = 3
	R384 = 4
	R64 = 5
	R8 = 6


# noinspection SpellCheckingInspection
class DchEnhanced(Enum):
	"""3 Members, BASic ... NO"""
	BASic = 0
	FULL = 1
	NO = 2


# noinspection SpellCheckingInspection
class DestinationState(Enum):
	"""4 Members, CPCH ... UPCH"""
	CPCH = 0
	FACH = 1
	IDLE = 2
	UPCH = 3


# noinspection SpellCheckingInspection
class DsTime(Enum):
	"""4 Members, OFF ... P2H"""
	OFF = 0
	ON = 1
	P1H = 2
	P2H = 3


# noinspection SpellCheckingInspection
class EhichIndicatorMode(Enum):
	"""5 Members, ACK ... NACK"""
	ACK = 0
	ALTernating = 1
	CRC = 2
	DTX = 3
	NACK = 4


# noinspection SpellCheckingInspection
class Enable(Enum):
	"""1 Members, ON ... ON"""
	ON = 0


# noinspection SpellCheckingInspection
class ErgchIndicatorMode(Enum):
	"""7 Members, ALTernating ... UP"""
	ALTernating = 0
	CONTinuous = 1
	DOWN = 2
	DTX = 3
	HARQ = 4
	SINGle = 5
	UP = 6


# noinspection SpellCheckingInspection
class Etfci(Enum):
	"""129 Members, _0 ... DTX"""
	_0 = 0
	_1 = 1
	_10 = 2
	_100 = 3
	_101 = 4
	_102 = 5
	_103 = 6
	_104 = 7
	_105 = 8
	_106 = 9
	_107 = 10
	_108 = 11
	_109 = 12
	_11 = 13
	_110 = 14
	_111 = 15
	_112 = 16
	_113 = 17
	_114 = 18
	_115 = 19
	_116 = 20
	_117 = 21
	_118 = 22
	_119 = 23
	_12 = 24
	_120 = 25
	_121 = 26
	_122 = 27
	_123 = 28
	_124 = 29
	_125 = 30
	_126 = 31
	_127 = 32
	_13 = 33
	_14 = 34
	_15 = 35
	_16 = 36
	_17 = 37
	_18 = 38
	_19 = 39
	_2 = 40
	_20 = 41
	_21 = 42
	_22 = 43
	_23 = 44
	_24 = 45
	_25 = 46
	_26 = 47
	_27 = 48
	_28 = 49
	_29 = 50
	_3 = 51
	_30 = 52
	_31 = 53
	_32 = 54
	_33 = 55
	_34 = 56
	_35 = 57
	_36 = 58
	_37 = 59
	_38 = 60
	_39 = 61
	_4 = 62
	_40 = 63
	_41 = 64
	_42 = 65
	_43 = 66
	_44 = 67
	_45 = 68
	_46 = 69
	_47 = 70
	_48 = 71
	_49 = 72
	_5 = 73
	_50 = 74
	_51 = 75
	_52 = 76
	_53 = 77
	_54 = 78
	_55 = 79
	_56 = 80
	_57 = 81
	_58 = 82
	_59 = 83
	_6 = 84
	_60 = 85
	_61 = 86
	_62 = 87
	_63 = 88
	_64 = 89
	_65 = 90
	_66 = 91
	_67 = 92
	_68 = 93
	_69 = 94
	_7 = 95
	_70 = 96
	_71 = 97
	_72 = 98
	_73 = 99
	_74 = 100
	_75 = 101
	_76 = 102
	_77 = 103
	_78 = 104
	_79 = 105
	_8 = 106
	_80 = 107
	_81 = 108
	_82 = 109
	_83 = 110
	_84 = 111
	_85 = 112
	_86 = 113
	_87 = 114
	_88 = 115
	_89 = 116
	_9 = 117
	_90 = 118
	_91 = 119
	_92 = 120
	_93 = 121
	_94 = 122
	_95 = 123
	_96 = 124
	_97 = 125
	_98 = 126
	_99 = 127
	DTX = 128


# noinspection SpellCheckingInspection
class Fader(Enum):
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
class FadingStandard(Enum):
	"""19 Members, B261 ... VA30"""
	B261 = 0
	B262 = 1
	B263 = 2
	BDEath = 3
	C1 = 4
	C2 = 5
	C3 = 6
	C4 = 7
	C5 = 8
	C6 = 9
	C8 = 10
	HST = 11
	MPRopagation = 12
	PA3 = 13
	PB3 = 14
	USER = 15
	VA12 = 16
	VA3 = 17
	VA30 = 18


# noinspection SpellCheckingInspection
class FilledBlocks(Enum):
	"""17 Members, P0031 ... P1000"""
	P0031 = 0
	P0033 = 1
	P0036 = 2
	P0038 = 3
	P0042 = 4
	P0045 = 5
	P0050 = 6
	P0056 = 7
	P0062 = 8
	P0071 = 9
	P0083 = 10
	P0100 = 11
	P0125 = 12
	P0167 = 13
	P0250 = 14
	P0500 = 15
	P1000 = 16


# noinspection SpellCheckingInspection
class GapSize(Enum):
	"""3 Members, ANY ... M5"""
	ANY = 0
	M10 = 1
	M5 = 2


# noinspection SpellCheckingInspection
class GeneratorState(Enum):
	"""3 Members, OFF ... RFHandover"""
	OFF = 0
	ON = 1
	RFHandover = 2


# noinspection SpellCheckingInspection
class GeoScope(Enum):
	"""4 Members, CIMMediate ... SERVice"""
	CIMMediate = 0
	CNORmal = 1
	PLMN = 2
	SERVice = 3


# noinspection SpellCheckingInspection
class GsmBand(Enum):
	"""5 Members, G04 ... G19"""
	G04 = 0
	G085 = 1
	G09 = 2
	G18 = 3
	G19 = 4


# noinspection SpellCheckingInspection
class Handover(Enum):
	"""3 Members, PACKet ... VOICe"""
	PACKet = 0
	TM = 1
	VOICe = 2


# noinspection SpellCheckingInspection
class HappyBit(Enum):
	"""3 Members, DTX ... UNHappy"""
	DTX = 0
	HAPPy = 1
	UNHappy = 2


# noinspection SpellCheckingInspection
class HoverExtDestination(Enum):
	"""5 Members, CDMA ... WCDMa"""
	CDMA = 0
	EVDO = 1
	GSM = 2
	LTE = 3
	WCDMa = 4


# noinspection SpellCheckingInspection
class HrVersion(Enum):
	"""2 Members, RV0 ... TABLe"""
	RV0 = 0
	TABLe = 1


# noinspection SpellCheckingInspection
class HsdpaModulation(Enum):
	"""3 Members, Q16 ... QPSK"""
	Q16 = 0
	Q64 = 1
	QPSK = 2


# noinspection SpellCheckingInspection
class HsetFixed(Enum):
	"""45 Members, H1AI ... HCMT"""
	H1AI = 0
	H1BI = 1
	H1CI = 2
	H1M1 = 3
	H1M2 = 4
	H1MI = 5
	H2M1 = 6
	H2M2 = 7
	H3A1 = 8
	H3A2 = 9
	H3B1 = 10
	H3B2 = 11
	H3C1 = 12
	H3C2 = 13
	H3M1 = 14
	H3M2 = 15
	H4M1 = 16
	H5M1 = 17
	H6A1 = 18
	H6A2 = 19
	H6B1 = 20
	H6B2 = 21
	H6C1 = 22
	H6C2 = 23
	H6M1 = 24
	H6M2 = 25
	H8A3 = 26
	H8AI = 27
	H8B3 = 28
	H8BI = 29
	H8C3 = 30
	H8CI = 31
	H8M3 = 32
	H8MI = 33
	H8MT = 34
	HAA1 = 35
	HAA2 = 36
	HAB1 = 37
	HAB2 = 38
	HAC1 = 39
	HAC2 = 40
	HAM1 = 41
	HAM2 = 42
	HCM1 = 43
	HCMT = 44


# noinspection SpellCheckingInspection
class HspaTestModeDirection(Enum):
	"""2 Members, HSDPa ... HSPA"""
	HSDPa = 0
	HSPA = 1


# noinspection SpellCheckingInspection
class HsScchType(Enum):
	"""6 Members, AUTomatic ... RANDom"""
	AUTomatic = 0
	CH1 = 1
	CH2 = 2
	CH3 = 3
	CH4 = 4
	RANDom = 5


# noinspection SpellCheckingInspection
class HsupaModulation(Enum):
	"""2 Members, Q16 ... QPSK"""
	Q16 = 0
	QPSK = 1


# noinspection SpellCheckingInspection
class InsertLossMode(Enum):
	"""2 Members, NORMal ... USER"""
	NORMal = 0
	USER = 1


# noinspection SpellCheckingInspection
class IpAddrIndex(Enum):
	"""3 Members, IP1 ... IP3"""
	IP1 = 0
	IP2 = 1
	IP3 = 2


# noinspection SpellCheckingInspection
class LevelSeqState(Enum):
	"""5 Members, FAILed ... SCONflict"""
	FAILed = 0
	IDLE = 1
	RUNNing = 2
	SCHanged = 3
	SCONflict = 4


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
class LteBand(Enum):
	"""68 Members, OB1 ... UDEFined"""
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
	UDEFined = 67


# noinspection SpellCheckingInspection
class MaxChanCode(Enum):
	"""8 Members, S16 ... S8"""
	S16 = 0
	S22 = 1
	S224 = 2
	S24 = 3
	S32 = 4
	S4 = 5
	S64 = 6
	S8 = 7


# noinspection SpellCheckingInspection
class MaxRelVersion(Enum):
	"""9 Members, AUTO ... R99"""
	AUTO = 0
	R10 = 1
	R11 = 2
	R5 = 3
	R6 = 4
	R7 = 5
	R8 = 6
	R9 = 7
	R99 = 8


# noinspection SpellCheckingInspection
class MeasType(Enum):
	"""2 Members, GENeral ... MISSed"""
	GENeral = 0
	MISSed = 1


# noinspection SpellCheckingInspection
class MessageClass(Enum):
	"""5 Members, CL0 ... NONE"""
	CL0 = 0
	CL1 = 1
	CL2 = 2
	CL3 = 3
	NONE = 4


# noinspection SpellCheckingInspection
class MessageHandling(Enum):
	"""2 Members, FILE ... INTernal"""
	FILE = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class MobilityMode(Enum):
	"""4 Members, CCORder ... REDirection"""
	CCORder = 0
	HANDover = 1
	NAV = 2
	REDirection = 3


# noinspection SpellCheckingInspection
class MonitoredHarq(Enum):
	"""9 Members, ALL ... H7"""
	ALL = 0
	H0 = 1
	H1 = 2
	H2 = 3
	H3 = 4
	H4 = 5
	H5 = 6
	H6 = 7
	H7 = 8


# noinspection SpellCheckingInspection
class NetworkAndGps(Enum):
	"""4 Members, BOTH ... UE"""
	BOTH = 0
	NETWork = 1
	NONE = 2
	UE = 3


# noinspection SpellCheckingInspection
class NominalPowerMode(Enum):
	"""3 Members, AUToranging ... ULPC"""
	AUToranging = 0
	MANual = 1
	ULPC = 2


# noinspection SpellCheckingInspection
class NrOfDigits(Enum):
	"""2 Members, D2 ... D3"""
	D2 = 0
	D3 = 1


# noinspection SpellCheckingInspection
class NtOperMode(Enum):
	"""2 Members, M1 ... M2"""
	M1 = 0
	M2 = 1


# noinspection SpellCheckingInspection
class OcnsChannelType(Enum):
	"""5 Members, AUTO ... R99"""
	AUTO = 0
	R5 = 1
	R6 = 2
	R7 = 3
	R99 = 4


# noinspection SpellCheckingInspection
class OperationBand(Enum):
	"""30 Members, OB1 ... UDEFined"""
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
	OB25 = 15
	OB26 = 16
	OB3 = 17
	OB32 = 18
	OB4 = 19
	OB5 = 20
	OB6 = 21
	OB7 = 22
	OB8 = 23
	OB9 = 24
	OBL1 = 25
	OBS1 = 26
	OBS2 = 27
	OBS3 = 28
	UDEFined = 29


# noinspection SpellCheckingInspection
class OperBandConfig(Enum):
	"""7 Members, C1 ... UDEFined"""
	C1 = 0
	C2 = 1
	C3 = 2
	C4 = 3
	C5 = 4
	C6 = 5
	UDEFined = 6


# noinspection SpellCheckingInspection
class ParameterType(Enum):
	"""2 Members, PRIMary ... SECondary"""
	PRIMary = 0
	SECondary = 1


# noinspection SpellCheckingInspection
class PatternType(Enum):
	"""2 Members, DU ... UD"""
	DU = 0
	UD = 1


# noinspection SpellCheckingInspection
class PhaseReference(Enum):
	"""2 Members, PCPich ... SCPich"""
	PCPich = 0
	SCPich = 1


# noinspection SpellCheckingInspection
class PowerControlMode(Enum):
	"""4 Members, M0 ... ON"""
	M0 = 0
	M1 = 1
	OFF = 2
	ON = 3


# noinspection SpellCheckingInspection
class PowerStrategy(Enum):
	"""3 Members, AF ... CE"""
	AF = 0
	BF = 1
	CE = 2


# noinspection SpellCheckingInspection
class Priority(Enum):
	"""3 Members, BACKground ... NORMal"""
	BACKground = 0
	HIGH = 1
	NORMal = 2


# noinspection SpellCheckingInspection
class Procedure(Enum):
	"""3 Members, CSOPs ... PS"""
	CSOPs = 0
	CSPS = 1
	PS = 2


# noinspection SpellCheckingInspection
class PswitchedAction(Enum):
	"""4 Members, ACONnect ... HANDover"""
	ACONnect = 0
	CONNect = 1
	DISConnect = 2
	HANDover = 3


# noinspection SpellCheckingInspection
class PswitchedState(Enum):
	"""14 Members, ATTached ... SIGNaling"""
	ATTached = 0
	CESTablished = 1
	CONNecting = 2
	IHANdover = 3
	IHPReparate = 4
	IREDirection = 5
	IRPReparate = 6
	OFF = 7
	OHANdover = 8
	ON = 9
	OREDirection = 10
	PAGing = 11
	RELeasing = 12
	SIGNaling = 13


# noinspection SpellCheckingInspection
class ReducedSignState(Enum):
	"""3 Members, OFF ... PROCessing"""
	OFF = 0
	ON = 1
	PROCessing = 2


# noinspection SpellCheckingInspection
class RefChannelDataRate(Enum):
	"""6 Members, BTFD ... R768k"""
	BTFD = 0
	R12K2 = 1
	R144k = 2
	R384k = 3
	R64K = 4
	R768k = 5


# noinspection SpellCheckingInspection
class RejectCause(Enum):
	"""6 Members, CSCongestion ... PSUNspecific"""
	CSCongestion = 0
	CSUNspecific = 1
	OFF = 2
	ON = 3
	PSCongestion = 4
	PSUNspecific = 5


# noinspection SpellCheckingInspection
class RejectionCauseA(Enum):
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
class RejectionCauseB(Enum):
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
class RepetitionB(Enum):
	"""3 Members, CONTinuous ... SGINit"""
	CONTinuous = 0
	ONCE = 1
	SGINit = 2


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
class ResultState(Enum):
	"""3 Members, FAIL ... RUN"""
	FAIL = 0
	PASS = 1
	RUN = 2


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
class RetransmisionSeqNr(Enum):
	"""5 Members, _0 ... DTX"""
	_0 = 0
	_1 = 1
	_2 = 2
	_3 = 3
	DTX = 4


# noinspection SpellCheckingInspection
class RlcMode(Enum):
	"""2 Members, ACKNowledge ... TRANsparent"""
	ACKNowledge = 0
	TRANsparent = 1


# noinspection SpellCheckingInspection
class RmcDomain(Enum):
	"""2 Members, CS ... PS"""
	CS = 0
	PS = 1


# noinspection SpellCheckingInspection
class RrcState(Enum):
	"""5 Members, CPCH ... UPCH"""
	CPCH = 0
	DCH = 1
	FACH = 2
	IDLE = 3
	UPCH = 4


# noinspection SpellCheckingInspection
class RvcSequence(Enum):
	"""8 Members, S1 ... UDEFined"""
	S1 = 0
	S2 = 1
	S3 = 2
	S4 = 3
	S5 = 4
	S6 = 5
	S7 = 6
	UDEFined = 7


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
	"""12 Members, DBFading ... UNDefined"""
	DBFading = 0
	DBFDiversity = 1
	DCARrier = 2
	DCFading = 3
	DCFDiversity = 4
	DCHSpa = 5
	FCHSpa = 6
	SCELl = 7
	SCFading = 8
	SCFDiversity = 9
	TCHSpa = 10
	UNDefined = 11


# noinspection SpellCheckingInspection
class SimCardType(Enum):
	"""3 Members, C2G ... MILenage"""
	C2G = 0
	C3G = 1
	MILenage = 2


# noinspection SpellCheckingInspection
class SlopeType(Enum):
	"""2 Members, NEGative ... POSitive"""
	NEGative = 0
	POSitive = 1


# noinspection SpellCheckingInspection
class SmsDataCoding(Enum):
	"""3 Members, BIT7 ... REServed"""
	BIT7 = 0
	BIT8 = 1
	REServed = 2


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
class SrbDataRate(Enum):
	"""4 Members, R13K6 ... R3K4"""
	R13K6 = 0
	R1K7 = 1
	R2K5 = 2
	R3K4 = 3


# noinspection SpellCheckingInspection
class SrbSingleType(Enum):
	"""2 Members, CDCH ... CFACh"""
	CDCH = 0
	CFACh = 1


# noinspection SpellCheckingInspection
class StopCondition(Enum):
	"""2 Members, NONE ... SLFail"""
	NONE = 0
	SLFail = 1


# noinspection SpellCheckingInspection
class SubTest(Enum):
	"""5 Members, S1 ... S5"""
	S1 = 0
	S2 = 1
	S3 = 2
	S4 = 3
	S5 = 4


# noinspection SpellCheckingInspection
class SucessState(Enum):
	"""2 Members, FAILed ... SUCCessful"""
	FAILed = 0
	SUCCessful = 1


# noinspection SpellCheckingInspection
class Sync(Enum):
	"""3 Members, NAV ... OK"""
	NAV = 0
	NOSYnc = 1
	OK = 2


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
class TableIndex(Enum):
	"""4 Members, CONFormance ... SEQuence"""
	CONFormance = 0
	FIXed = 1
	FOLLow = 2
	SEQuence = 3


# noinspection SpellCheckingInspection
class TerminatingType(Enum):
	"""5 Members, RMC ... VOICe"""
	RMC = 0
	SRB = 1
	TEST = 2
	VIDeo = 3
	VOICe = 4


# noinspection SpellCheckingInspection
class TestCase(Enum):
	"""2 Members, AWGN ... FADing"""
	AWGN = 0
	FADing = 1


# noinspection SpellCheckingInspection
class TestMode(Enum):
	"""2 Members, HOLD ... UPDown"""
	HOLD = 0
	UPDown = 1


# noinspection SpellCheckingInspection
class TestModeType(Enum):
	"""5 Members, BTFD ... RMC"""
	BTFD = 0
	FACH = 1
	HSPA = 2
	RHSPa = 3
	RMC = 4


# noinspection SpellCheckingInspection
class TpcMode(Enum):
	"""3 Members, A1S1 ... A2S1"""
	A1S1 = 0
	A1S2 = 1
	A2S1 = 2


# noinspection SpellCheckingInspection
class TpcSetType(Enum):
	"""19 Members, ALL0 ... ULCM"""
	ALL0 = 0
	ALL1 = 1
	ALTernating = 2
	CLOop = 3
	CONTinuous = 4
	CTFC = 5
	DHIB = 6
	MPEDch = 7
	PHDown = 8
	PHUP = 9
	SAL0 = 10
	SAL1 = 11
	SALT = 12
	TSABc = 13
	TSE = 14
	TSEF = 15
	TSF = 16
	TSGH = 17
	ULCM = 18


# noinspection SpellCheckingInspection
class TpcState(Enum):
	"""14 Members, ALTernating ... TRANsition"""
	ALTernating = 0
	CONTinous = 1
	FAILed = 2
	IDLE = 3
	MAXPower = 4
	MINPower = 5
	MRESource = 6
	SCHanged = 7
	SCONflict = 8
	SEARching = 9
	SINGle = 10
	TPLocked = 11
	TPUNlocked = 12
	TRANsition = 13


# noinspection SpellCheckingInspection
class TransGapType(Enum):
	"""3 Members, AF ... B"""
	AF = 0
	AR = 1
	B = 2


# noinspection SpellCheckingInspection
class TransGapTypeExtended(Enum):
	"""8 Members, A ... RFB"""
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	F = 5
	RFA = 6
	RFB = 7


# noinspection SpellCheckingInspection
class TransTimeInterval(Enum):
	"""2 Members, M10 ... M2"""
	M10 = 0
	M2 = 1


# noinspection SpellCheckingInspection
class TriggerMode(Enum):
	"""2 Members, ONCE ... PERiodic"""
	ONCE = 0
	PERiodic = 1


# noinspection SpellCheckingInspection
class TtiExtended(Enum):
	"""4 Members, M10 ... M80"""
	M10 = 0
	M20 = 1
	M40 = 2
	M80 = 3


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
class UeAlgorithm(Enum):
	"""2 Members, EXTRapolation ... INTerpolation"""
	EXTRapolation = 0
	INTerpolation = 1


# noinspection SpellCheckingInspection
class UeNaviSupport(Enum):
	"""4 Members, NETWork ... UE"""
	NETWork = 0
	NONE = 1
	NUE = 2
	UE = 3


# noinspection SpellCheckingInspection
class UePowerClass(Enum):
	"""5 Members, PC1 ... PC4"""
	PC1 = 0
	PC2 = 1
	PC3 = 2
	PC3B = 3
	PC4 = 4


# noinspection SpellCheckingInspection
class UnscheduledTransType(Enum):
	"""2 Members, DTX ... DUMMy"""
	DTX = 0
	DUMMy = 1


# noinspection SpellCheckingInspection
class UsedSendMethod(Enum):
	"""1 Members, WDEFault ... WDEFault"""
	WDEFault = 0


# noinspection SpellCheckingInspection
class UtraMode(Enum):
	"""3 Members, BOTH ... TDD"""
	BOTH = 0
	FDD = 1
	TDD = 2


# noinspection SpellCheckingInspection
class UtranTestMode(Enum):
	"""3 Members, MODE1 ... OFF"""
	MODE1 = 0
	MODE2 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class VideoRate(Enum):
	"""1 Members, R64K ... R64K"""
	R64K = 0


# noinspection SpellCheckingInspection
class VoiceCodec(Enum):
	"""2 Members, NB ... WB"""
	NB = 0
	WB = 1


# noinspection SpellCheckingInspection
class VoiceSource(Enum):
	"""2 Members, LOOPback ... SPEech"""
	LOOPback = 0
	SPEech = 1


# noinspection SpellCheckingInspection
class WizzardSelection(Enum):
	"""8 Members, DHIP ... OOS"""
	DHIP = 0
	ERGM = 1
	HCQI = 2
	HDMT = 3
	HSMT = 4
	HUMP = 5
	HUMT = 6
	OOS = 7


# noinspection SpellCheckingInspection
class YesNoStatus(Enum):
	"""2 Members, NO ... YES"""
	NO = 0
	YES = 1


# noinspection SpellCheckingInspection
class Zone(Enum):
	"""2 Members, NONE ... Z1"""
	NONE = 0
	Z1 = 1
