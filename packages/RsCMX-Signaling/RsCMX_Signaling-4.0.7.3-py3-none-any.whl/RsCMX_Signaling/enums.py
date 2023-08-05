from enum import Enum


# noinspection SpellCheckingInspection
class AckOrDtx(Enum):
	"""2 Members, CONTinue ... STOP"""
	CONTinue = 0
	STOP = 1


# noinspection SpellCheckingInspection
class Action(Enum):
	"""1 Members, DISConnect ... DISConnect"""
	DISConnect = 0


# noinspection SpellCheckingInspection
class Algorithm(Enum):
	"""4 Members, ERC1 ... ERC4"""
	ERC1 = 0
	ERC2 = 1
	ERC3 = 2
	ERC4 = 3


# noinspection SpellCheckingInspection
class Alpha(Enum):
	"""8 Members, A00 ... A10"""
	A00 = 0
	A04 = 1
	A05 = 2
	A06 = 3
	A07 = 4
	A08 = 5
	A09 = 6
	A10 = 7


# noinspection SpellCheckingInspection
class AntNoPorts(Enum):
	"""3 Members, P1 ... P4"""
	P1 = 0
	P2 = 1
	P4 = 2


# noinspection SpellCheckingInspection
class AntNoPortsB(Enum):
	"""4 Members, P1 ... P8"""
	P1 = 0
	P2 = 1
	P4 = 2
	P8 = 3


# noinspection SpellCheckingInspection
class Assignment(Enum):
	"""8 Members, NONE ... SA6"""
	NONE = 0
	SA0 = 1
	SA1 = 2
	SA2 = 3
	SA3 = 4
	SA4 = 5
	SA5 = 6
	SA6 = 7


# noinspection SpellCheckingInspection
class BeamNoPorts(Enum):
	"""5 Members, NONE ... P8"""
	NONE = 0
	P1 = 1
	P2 = 2
	P4 = 3
	P8 = 4


# noinspection SpellCheckingInspection
class CellsToMeasure(Enum):
	"""4 Members, ALL ... OFF"""
	ALL = 0
	LTE = 1
	NRADio = 2
	OFF = 3


# noinspection SpellCheckingInspection
class CellType(Enum):
	"""2 Members, LTE ... NR"""
	LTE = 0
	NR = 1


# noinspection SpellCheckingInspection
class Class(Enum):
	"""4 Members, C0 ... C3"""
	C0 = 0
	C1 = 1
	C2 = 2
	C3 = 3


# noinspection SpellCheckingInspection
class Coding(Enum):
	"""3 Members, EIGHt ... UCS2"""
	EIGHt = 0
	GSM = 1
	UCS2 = 2


# noinspection SpellCheckingInspection
class ConfigMode(Enum):
	"""2 Members, AUTO ... UDEFined"""
	AUTO = 0
	UDEFined = 1


# noinspection SpellCheckingInspection
class Control(Enum):
	"""5 Members, CLOop ... PATTern"""
	CLOop = 0
	KEEP = 1
	MAX = 2
	MIN = 3
	PATTern = 4


# noinspection SpellCheckingInspection
class CoreNetwork(Enum):
	"""2 Members, EPS ... FG"""
	EPS = 0
	FG = 1


# noinspection SpellCheckingInspection
class Counter(Enum):
	"""9 Members, N1 ... N8"""
	N1 = 0
	N10 = 1
	N2 = 2
	N20 = 3
	N3 = 4
	N4 = 5
	N5 = 6
	N6 = 7
	N8 = 8


# noinspection SpellCheckingInspection
class DataFlow(Enum):
	"""3 Members, MCGSplit ... SCGSplit"""
	MCGSplit = 0
	SCG = 1
	SCGSplit = 2


# noinspection SpellCheckingInspection
class DciFormat(Enum):
	"""10 Members, D0 ... D2D"""
	D0 = 0
	D1 = 1
	D1A = 2
	D1B = 3
	D1C = 4
	D2 = 5
	D2A = 6
	D2B = 7
	D2C = 8
	D2D = 9


# noinspection SpellCheckingInspection
class DciFormatB(Enum):
	"""2 Members, D10 ... D11"""
	D10 = 0
	D11 = 1


# noinspection SpellCheckingInspection
class DciFormatC(Enum):
	"""2 Members, D00 ... D01"""
	D00 = 0
	D01 = 1


# noinspection SpellCheckingInspection
class DcMode(Enum):
	"""4 Members, ENDC ... OFF"""
	ENDC = 0
	LTE = 1
	NR = 2
	OFF = 3


# noinspection SpellCheckingInspection
class DlIqDataStreams(Enum):
	"""4 Members, S1 ... S8"""
	S1 = 0
	S2 = 1
	S4 = 2
	S8 = 3


# noinspection SpellCheckingInspection
class DuplexModeB(Enum):
	"""3 Members, FDD ... TDD"""
	FDD = 0
	SDL = 1
	TDD = 2


# noinspection SpellCheckingInspection
class EsmCause(Enum):
	"""45 Members, C100 ... C99"""
	C100 = 0
	C101 = 1
	C111 = 2
	C112 = 3
	C113 = 4
	C16 = 5
	C26 = 6
	C27 = 7
	C28 = 8
	C29 = 9
	C30 = 10
	C31 = 11
	C32 = 12
	C33 = 13
	C34 = 14
	C35 = 15
	C36 = 16
	C37 = 17
	C38 = 18
	C39 = 19
	C41 = 20
	C42 = 21
	C43 = 22
	C44 = 23
	C45 = 24
	C46 = 25
	C47 = 26
	C49 = 27
	C50 = 28
	C51 = 29
	C52 = 30
	C53 = 31
	C54 = 32
	C55 = 33
	C56 = 34
	C59 = 35
	C60 = 36
	C65 = 37
	C66 = 38
	C81 = 39
	C95 = 40
	C96 = 41
	C97 = 42
	C98 = 43
	C99 = 44


# noinspection SpellCheckingInspection
class FilterCoeff(Enum):
	"""15 Members, FC0 ... FC9"""
	FC0 = 0
	FC1 = 1
	FC11 = 2
	FC13 = 3
	FC15 = 4
	FC17 = 5
	FC19 = 6
	FC2 = 7
	FC3 = 8
	FC4 = 9
	FC5 = 10
	FC6 = 11
	FC7 = 12
	FC8 = 13
	FC9 = 14


# noinspection SpellCheckingInspection
class FrequencyRange(Enum):
	"""2 Members, FR1 ... FR2"""
	FR1 = 0
	FR2 = 1


# noinspection SpellCheckingInspection
class Info(Enum):
	"""1 Members, ALL ... ALL"""
	ALL = 0


# noinspection SpellCheckingInspection
class ItRateUnit(Enum):
	"""25 Members, G1 ... T64"""
	G1 = 0
	G16 = 1
	G256 = 2
	G4 = 3
	G64 = 4
	K1 = 5
	K16 = 6
	K256 = 7
	K4 = 8
	K64 = 9
	M1 = 10
	M16 = 11
	M256 = 12
	M4 = 13
	M64 = 14
	P1 = 15
	P16 = 16
	P256 = 17
	P4 = 18
	P64 = 19
	T1 = 20
	T16 = 21
	T256 = 22
	T4 = 23
	T64 = 24


# noinspection SpellCheckingInspection
class Level(Enum):
	"""5 Members, AL1 ... AL8"""
	AL1 = 0
	AL16 = 1
	AL2 = 2
	AL4 = 3
	AL8 = 4


# noinspection SpellCheckingInspection
class Location(Enum):
	"""3 Members, HIGH ... MID"""
	HIGH = 0
	LOW = 1
	MID = 2


# noinspection SpellCheckingInspection
class LogLevel(Enum):
	"""3 Members, BRIef ... VERBose"""
	BRIef = 0
	NONE = 1
	VERBose = 2


# noinspection SpellCheckingInspection
class LogType(Enum):
	"""4 Members, DISable ... PAYLoad"""
	DISable = 0
	FULL = 1
	HEADer = 2
	PAYLoad = 3


# noinspection SpellCheckingInspection
class Mapping(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class MappingI(Enum):
	"""2 Members, INT ... NINT"""
	INT = 0
	NINT = 1


# noinspection SpellCheckingInspection
class McsTable(Enum):
	"""3 Members, Q1K ... Q64"""
	Q1K = 0
	Q256 = 1
	Q64 = 2


# noinspection SpellCheckingInspection
class McsTableB(Enum):
	"""3 Members, L64 ... Q64"""
	L64 = 0
	Q256 = 1
	Q64 = 2


# noinspection SpellCheckingInspection
class Mimo(Enum):
	"""4 Members, M22 ... SISO"""
	M22 = 0
	M33 = 1
	M44 = 2
	SISO = 3


# noinspection SpellCheckingInspection
class MimoB(Enum):
	"""2 Members, M22 ... SISO"""
	M22 = 0
	SISO = 1


# noinspection SpellCheckingInspection
class Mode(Enum):
	"""3 Members, MAX ... UDEFined"""
	MAX = 0
	MIN = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class ModeB(Enum):
	"""2 Members, AUTO ... USER"""
	AUTO = 0
	USER = 1


# noinspection SpellCheckingInspection
class ModeC(Enum):
	"""3 Members, AUTO ... USER"""
	AUTO = 0
	NOTC = 1
	USER = 2


# noinspection SpellCheckingInspection
class Modulation(Enum):
	"""7 Members, BPSK ... QPSK"""
	BPSK = 0
	P2BPsk = 1
	Q1024 = 2
	Q16 = 3
	Q256 = 4
	Q64 = 5
	QPSK = 6


# noinspection SpellCheckingInspection
class ModulationB(Enum):
	"""7 Members, AUTO ... QPSK"""
	AUTO = 0
	BPSK = 1
	HPBP = 2
	Q16 = 3
	Q256 = 4
	Q64 = 5
	QPSK = 6


# noinspection SpellCheckingInspection
class NameType(Enum):
	"""2 Members, GUI ... RESource"""
	GUI = 0
	RESource = 1


# noinspection SpellCheckingInspection
class NoSymbols(Enum):
	"""4 Members, S1 ... S4"""
	S1 = 0
	S2 = 1
	S3 = 2
	S4 = 3


# noinspection SpellCheckingInspection
class Pattern(Enum):
	"""4 Members, D1 ... U3"""
	D1 = 0
	KEEP = 1
	U1 = 2
	U3 = 3


# noinspection SpellCheckingInspection
class PdcchFormat(Enum):
	"""5 Members, N1 ... NAV"""
	N1 = 0
	N2 = 1
	N4 = 2
	N8 = 3
	NAV = 4


# noinspection SpellCheckingInspection
class PduState(Enum):
	"""6 Members, ACTive ... MIP"""
	ACTive = 0
	AIP = 1
	AUIP = 2
	DIP = 3
	INACtive = 4
	MIP = 5


# noinspection SpellCheckingInspection
class Periodicity(Enum):
	"""10 Members, P0P5 ... P5"""
	P0P5 = 0
	P0P6 = 1
	P1 = 2
	P10 = 3
	P1P2 = 4
	P2 = 5
	P2P5 = 6
	P3 = 7
	P4 = 8
	P5 = 9


# noinspection SpellCheckingInspection
class Power(Enum):
	"""16 Members, P100 ... P98"""
	P100 = 0
	P102 = 1
	P104 = 2
	P106 = 3
	P108 = 4
	P110 = 5
	P112 = 6
	P114 = 7
	P116 = 8
	P118 = 9
	P120 = 10
	P90 = 11
	P92 = 12
	P94 = 13
	P96 = 14
	P98 = 15


# noinspection SpellCheckingInspection
class PreferredNetw(Enum):
	"""4 Members, AUTO ... NONE"""
	AUTO = 0
	EPS = 1
	FG = 2
	NONE = 3


# noinspection SpellCheckingInspection
class PwrRampingStepA(Enum):
	"""4 Members, S0 ... S6"""
	S0 = 0
	S2 = 1
	S4 = 2
	S6 = 3


# noinspection SpellCheckingInspection
class PwrRampingStepB(Enum):
	"""4 Members, S0 ... S4"""
	S0 = 0
	S2 = 1
	S3 = 2
	S4 = 3


# noinspection SpellCheckingInspection
class Qi(Enum):
	"""21 Members, Q1 ... Q9"""
	Q1 = 0
	Q2 = 1
	Q3 = 2
	Q4 = 3
	Q5 = 4
	Q6 = 5
	Q65 = 6
	Q66 = 7
	Q67 = 8
	Q69 = 9
	Q7 = 10
	Q70 = 11
	Q75 = 12
	Q79 = 13
	Q8 = 14
	Q80 = 15
	Q82 = 16
	Q83 = 17
	Q84 = 18
	Q85 = 19
	Q9 = 20


# noinspection SpellCheckingInspection
class RegState(Enum):
	"""9 Members, DREG ... RIP"""
	DREG = 0
	DRIP = 1
	FREG = 2
	FRIP = 3
	NFReg = 4
	NREG = 5
	NRIP = 6
	REG = 7
	RIP = 8


# noinspection SpellCheckingInspection
class RegStateB(Enum):
	"""9 Members, CREG ... REG"""
	CREG = 0
	CRIP = 1
	DREG = 2
	DRIP = 3
	EREG = 4
	ERIP = 5
	LREG = 6
	LRIP = 7
	REG = 8


# noinspection SpellCheckingInspection
class Repeat(Enum):
	"""2 Members, CONTinuous ... SINGleshot"""
	CONTinuous = 0
	SINGleshot = 1


# noinspection SpellCheckingInspection
class ReportInterval(Enum):
	"""14 Members, I1 ... I9"""
	I1 = 0
	I10 = 1
	I11 = 2
	I12 = 3
	I13 = 4
	I14 = 5
	I2 = 6
	I3 = 7
	I4 = 8
	I5 = 9
	I6 = 10
	I7 = 11
	I8 = 12
	I9 = 13


# noinspection SpellCheckingInspection
class Routing(Enum):
	"""2 Members, DUT ... FIXed"""
	DUT = 0
	FIXed = 1


# noinspection SpellCheckingInspection
class RrcState(Enum):
	"""3 Members, CONNected ... INACtive"""
	CONNected = 0
	IDLE = 1
	INACtive = 2


# noinspection SpellCheckingInspection
class Severity(Enum):
	"""3 Members, ERRor ... WARNing"""
	ERRor = 0
	INFO = 1
	WARNing = 2


# noinspection SpellCheckingInspection
class SpecialPattern(Enum):
	"""12 Members, P0 ... PAV2"""
	P0 = 0
	P1 = 1
	P2 = 2
	P3 = 3
	P4 = 4
	P5 = 5
	P6 = 6
	P7 = 7
	P8 = 8
	P9 = 9
	PAV1 = 10
	PAV2 = 11


# noinspection SpellCheckingInspection
class SrcType(Enum):
	"""3 Members, PUCC ... PUSC"""
	PUCC = 0
	PUPU = 1
	PUSC = 2


# noinspection SpellCheckingInspection
class State(Enum):
	"""3 Members, OFF ... RUN"""
	OFF = 0
	RDY = 1
	RUN = 2


# noinspection SpellCheckingInspection
class StateB(Enum):
	"""9 Members, CREating ... TESTing"""
	CREating = 0
	DELeting = 1
	EXHausted = 2
	IDLE = 3
	NAV = 4
	RUNNing = 5
	STARting = 6
	STOPping = 7
	TESTing = 8


# noinspection SpellCheckingInspection
class StateC(Enum):
	"""2 Members, ERRor ... SUCCess"""
	ERRor = 0
	SUCCess = 1


# noinspection SpellCheckingInspection
class StopConditionB(Enum):
	"""2 Members, SAMPles ... TIME"""
	SAMPles = 0
	TIME = 1


# noinspection SpellCheckingInspection
class Target(Enum):
	"""5 Members, ALL ... TOPology"""
	ALL = 0
	CELL = 1
	LTE = 2
	NRADio = 3
	TOPology = 4


# noinspection SpellCheckingInspection
class TargetState(Enum):
	"""4 Members, OFF ... RDYPending"""
	OFF = 0
	OFFPending = 1
	RDY = 2
	RDYPending = 3


# noinspection SpellCheckingInspection
class TestLoopState(Enum):
	"""2 Members, CLOSe ... OPEN"""
	CLOSe = 0
	OPEN = 1


# noinspection SpellCheckingInspection
class Tmode(Enum):
	"""10 Members, TM1 ... TM9"""
	TM1 = 0
	TM10 = 1
	TM2 = 2
	TM3 = 3
	TM4 = 4
	TM5 = 5
	TM6 = 6
	TM7 = 7
	TM8 = 8
	TM9 = 9


# noinspection SpellCheckingInspection
class Type(Enum):
	"""2 Members, DCMC ... GDC"""
	DCMC = 0
	GDC = 1


# noinspection SpellCheckingInspection
class TypeB(Enum):
	"""1 Members, UDEFined ... UDEFined"""
	UDEFined = 0


# noinspection SpellCheckingInspection
class UecState(Enum):
	"""7 Members, CESTablish ... SCGFailure"""
	CESTablish = 0
	CREestablish = 1
	CRELease = 2
	HANDover = 3
	OK = 4
	PAGing = 5
	SCGFailure = 6


# noinspection SpellCheckingInspection
class UlBandwidth(Enum):
	"""12 Members, B014 ... M5"""
	B014 = 0
	B030 = 1
	B050 = 2
	B100 = 3
	B150 = 4
	B200 = 5
	M10 = 6
	M15 = 7
	M1K4 = 8
	M20 = 9
	M3 = 10
	M5 = 11


# noinspection SpellCheckingInspection
class Version(Enum):
	"""5 Members, AUTO ... RV3"""
	AUTO = 0
	RV0 = 1
	RV1 = 2
	RV2 = 3
	RV3 = 4


# noinspection SpellCheckingInspection
class VoiceHandling(Enum):
	"""3 Members, EFRedirect ... VONR"""
	EFRedirect = 0
	UECap = 1
	VONR = 2


# noinspection SpellCheckingInspection
class Waveform(Enum):
	"""2 Members, CP ... DTFS"""
	CP = 0
	DTFS = 1
