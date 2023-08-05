from enum import Enum


# noinspection SpellCheckingInspection
class AveragingMode(Enum):
	"""2 Members, LINear ... LOGarithmic"""
	LINear = 0
	LOGarithmic = 1


# noinspection SpellCheckingInspection
class CcdfMode(Enum):
	"""2 Members, POWer ... STATistic"""
	POWer = 0
	STATistic = 1


# noinspection SpellCheckingInspection
class CmwsConnector(Enum):
	"""96 Members, R11 ... RH8"""
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
	RC1 = 48
	RC2 = 49
	RC3 = 50
	RC4 = 51
	RC5 = 52
	RC6 = 53
	RC7 = 54
	RC8 = 55
	RD1 = 56
	RD2 = 57
	RD3 = 58
	RD4 = 59
	RD5 = 60
	RD6 = 61
	RD7 = 62
	RD8 = 63
	RE1 = 64
	RE2 = 65
	RE3 = 66
	RE4 = 67
	RE5 = 68
	RE6 = 69
	RE7 = 70
	RE8 = 71
	RF1 = 72
	RF2 = 73
	RF3 = 74
	RF4 = 75
	RF5 = 76
	RF6 = 77
	RF7 = 78
	RF8 = 79
	RG1 = 80
	RG2 = 81
	RG3 = 82
	RG4 = 83
	RG5 = 84
	RG6 = 85
	RG7 = 86
	RG8 = 87
	RH1 = 88
	RH2 = 89
	RH3 = 90
	RH4 = 91
	RH5 = 92
	RH6 = 93
	RH7 = 94
	RH8 = 95


# noinspection SpellCheckingInspection
class Detector(Enum):
	"""6 Members, AUTopeak ... SAMPle"""
	AUTopeak = 0
	AVERage = 1
	MAXPeak = 2
	MINPeak = 3
	RMS = 4
	SAMPle = 5


# noinspection SpellCheckingInspection
class DetectorBasic(Enum):
	"""2 Members, PEAK ... RMS"""
	PEAK = 0
	RMS = 1


# noinspection SpellCheckingInspection
class DigitalFilterType(Enum):
	"""5 Members, BANDpass ... WCDMa"""
	BANDpass = 0
	CDMA = 1
	GAUSs = 2
	TDSCdma = 3
	WCDMa = 4


# noinspection SpellCheckingInspection
class FileSave(Enum):
	"""3 Members, OFF ... ONLY"""
	OFF = 0
	ON = 1
	ONLY = 2


# noinspection SpellCheckingInspection
class FilterType(Enum):
	"""3 Members, GAUSs ... NYQuist"""
	GAUSs = 0
	NY1Mhz = 1
	NYQuist = 2


# noinspection SpellCheckingInspection
class IqFormat(Enum):
	"""2 Members, IQ ... RPHI"""
	IQ = 0
	RPHI = 1


# noinspection SpellCheckingInspection
class MagnitudeUnit(Enum):
	"""2 Members, RAW ... VOLT"""
	RAW = 0
	VOLT = 1


# noinspection SpellCheckingInspection
class MeasTab(Enum):
	"""6 Members, EPSensor ... SPECtrum"""
	EPSensor = 0
	FFTSanalyzer = 1
	IQRecorder = 2
	IQVSlot = 3
	POWer = 4
	SPECtrum = 5


# noinspection SpellCheckingInspection
class MeasurementMode(Enum):
	"""2 Members, NORMal ... TALignment"""
	NORMal = 0
	TALignment = 1


# noinspection SpellCheckingInspection
class OffsetMode(Enum):
	"""2 Members, FIXed ... VARiable"""
	FIXed = 0
	VARiable = 1


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class PathIndex(Enum):
	"""8 Members, P1 ... P8"""
	P1 = 0
	P2 = 1
	P3 = 2
	P4 = 3
	P5 = 4
	P6 = 5
	P7 = 6
	P8 = 7


# noinspection SpellCheckingInspection
class PathLossState(Enum):
	"""3 Members, NCAP ... RDY"""
	NCAP = 0
	PEND = 1
	RDY = 2


# noinspection SpellCheckingInspection
class PwrSensorResolution(Enum):
	"""4 Members, PD0 ... PD3"""
	PD0 = 0
	PD1 = 1
	PD2 = 2
	PD3 = 3


# noinspection SpellCheckingInspection
class RbwFilterType(Enum):
	"""2 Members, BANDpass ... GAUSs"""
	BANDpass = 0
	GAUSs = 1


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
class RfConnector(Enum):
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
	"""5 Members, CSPath ... UNDefined"""
	CSPath = 0
	MAIQ = 1
	MAPR = 2
	SALone = 3
	UNDefined = 4


# noinspection SpellCheckingInspection
class SignalSlopeExt(Enum):
	"""4 Members, FALLing ... RISing"""
	FALLing = 0
	FEDGe = 1
	REDGe = 2
	RISing = 3


# noinspection SpellCheckingInspection
class SpanMode(Enum):
	"""2 Members, FSWeep ... ZSPan"""
	FSWeep = 0
	ZSPan = 1


# noinspection SpellCheckingInspection
class Statistic(Enum):
	"""4 Members, AVERage ... MINimum"""
	AVERage = 0
	CURRent = 1
	MAXimum = 2
	MINimum = 3


# noinspection SpellCheckingInspection
class Timing(Enum):
	"""2 Members, CENTered ... STEP"""
	CENTered = 0
	STEP = 1


# noinspection SpellCheckingInspection
class TriggerPowerMode(Enum):
	"""4 Members, ALL ... SWEep"""
	ALL = 0
	ONCE = 1
	PRESelect = 2
	SWEep = 3


# noinspection SpellCheckingInspection
class TriggerSequenceMode(Enum):
	"""2 Members, ONCE ... PRESelect"""
	ONCE = 0
	PRESelect = 1


# noinspection SpellCheckingInspection
class TriggerSource(Enum):
	"""4 Members, EXTernal ... IFPower"""
	EXTernal = 0
	FREerun = 1
	IF = 2
	IFPower = 3


# noinspection SpellCheckingInspection
class UserDebugMode(Enum):
	"""2 Members, DEBug ... USER"""
	DEBug = 0
	USER = 1


# noinspection SpellCheckingInspection
class ZeroingState(Enum):
	"""2 Members, FAILed ... PASSed"""
	FAILed = 0
	PASSed = 1
