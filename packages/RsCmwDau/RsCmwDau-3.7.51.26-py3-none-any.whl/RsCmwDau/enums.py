from enum import Enum


# noinspection SpellCheckingInspection
class AddressModeA(Enum):
	"""3 Members, AUTomatic ... STATic"""
	AUTomatic = 0
	DHCPv4 = 1
	STATic = 2


# noinspection SpellCheckingInspection
class AddressModeB(Enum):
	"""3 Members, ACONf ... STATic"""
	ACONf = 0
	AUTO = 1
	STATic = 2


# noinspection SpellCheckingInspection
class AddressType(Enum):
	"""2 Members, IPVFour ... IPVSix"""
	IPVFour = 0
	IPVSix = 1


# noinspection SpellCheckingInspection
class AkaVersion(Enum):
	"""3 Members, AKA1 ... HTTP"""
	AKA1 = 0
	AKA2 = 1
	HTTP = 2


# noinspection SpellCheckingInspection
class AlignMode(Enum):
	"""2 Members, BANDwidtheff ... OCTetaligned"""
	BANDwidtheff = 0
	OCTetaligned = 1


# noinspection SpellCheckingInspection
class AmRnbBitrate(Enum):
	"""9 Members, NOReq ... R795"""
	NOReq = 0
	R1020 = 1
	R1220 = 2
	R475 = 3
	R515 = 4
	R590 = 5
	R670 = 6
	R740 = 7
	R795 = 8


# noinspection SpellCheckingInspection
class AmrType(Enum):
	"""2 Members, NARRowband ... WIDeband"""
	NARRowband = 0
	WIDeband = 1


# noinspection SpellCheckingInspection
class AmRwbBitRate(Enum):
	"""10 Members, NOReq ... RA2385"""
	NOReq = 0
	R1265 = 1
	R1425 = 2
	R1585 = 3
	R1825 = 4
	R1985 = 5
	R2305 = 6
	R660 = 7
	R885 = 8
	RA2385 = 9


# noinspection SpellCheckingInspection
class ApplicationType(Enum):
	"""9 Members, AUDiodelay ... THRoughput"""
	AUDiodelay = 0
	DNSReq = 1
	IPANalysis = 2
	IPERf = 3
	IPLogging = 4
	IPReplay = 5
	OVERview = 6
	PING = 7
	THRoughput = 8


# noinspection SpellCheckingInspection
class AudioInstance(Enum):
	"""2 Members, INST1 ... INST2"""
	INST1 = 0
	INST2 = 1


# noinspection SpellCheckingInspection
class AudioRouting(Enum):
	"""3 Members, AUDioboard ... LOOPback"""
	AUDioboard = 0
	FORWard = 1
	LOOPback = 2


# noinspection SpellCheckingInspection
class AuthAlgorithm(Enum):
	"""2 Members, MILenage ... XOR"""
	MILenage = 0
	XOR = 1


# noinspection SpellCheckingInspection
class AuthScheme(Enum):
	"""3 Members, AKA1 ... NOAuthentic"""
	AKA1 = 0
	AKA2 = 1
	NOAuthentic = 2


# noinspection SpellCheckingInspection
class AvTypeA(Enum):
	"""2 Members, AUDio ... VIDeo"""
	AUDio = 0
	VIDeo = 1


# noinspection SpellCheckingInspection
class AvTypeB(Enum):
	"""3 Members, AUDio ... VIDeo"""
	AUDio = 0
	UNKNow = 1
	VIDeo = 2


# noinspection SpellCheckingInspection
class AvTypeC(Enum):
	"""4 Members, AUDio ... VIDeo"""
	AUDio = 0
	EMER = 1
	UNK = 2
	VIDeo = 3


# noinspection SpellCheckingInspection
class Bandwidth(Enum):
	"""7 Members, FB ... WB"""
	FB = 0
	NB = 1
	NBFB = 2
	NBSWb = 3
	NBWB = 4
	SWB = 5
	WB = 6


# noinspection SpellCheckingInspection
class BehaviourA(Enum):
	"""7 Members, AFTRng ... NOANswer"""
	AFTRng = 0
	ANSWer = 1
	BEFRng = 2
	BUSY = 3
	CD = 4
	DECLined = 5
	NOANswer = 6


# noinspection SpellCheckingInspection
class BehaviourB(Enum):
	"""4 Members, FAILure ... NORMal"""
	FAILure = 0
	NOACcept = 1
	NOANswer = 2
	NORMal = 3


# noinspection SpellCheckingInspection
class Bitrate(Enum):
	"""12 Members, R1280 ... R960"""
	R1280 = 0
	R132 = 1
	R164 = 2
	R244 = 3
	R320 = 4
	R480 = 5
	R59 = 6
	R640 = 7
	R72 = 8
	R80 = 9
	R96 = 10
	R960 = 11


# noinspection SpellCheckingInspection
class BwRange(Enum):
	"""2 Members, COMMon ... SENDrx"""
	COMMon = 0
	SENDrx = 1


# noinspection SpellCheckingInspection
class CallState(Enum):
	"""7 Members, CALLing ... RINGing"""
	CALLing = 0
	CERRor = 1
	CESTablished = 2
	NOACtion = 3
	NOResponse = 4
	RELeased = 5
	RINGing = 6


# noinspection SpellCheckingInspection
class CallType(Enum):
	"""8 Members, ACK ... RCSGrpchat"""
	ACK = 0
	GENeric = 1
	GPP = 2
	GPP2 = 3
	LARGe = 4
	PAGer = 5
	RCSChat = 6
	RCSGrpchat = 7


# noinspection SpellCheckingInspection
class ChawMode(Enum):
	"""7 Members, DIS ... TWO"""
	DIS = 0
	FIVE = 1
	NP = 2
	NUSed = 3
	SEVen = 4
	THRee = 5
	TWO = 6


# noinspection SpellCheckingInspection
class Cmr(Enum):
	"""4 Members, DISable ... PRESent"""
	DISable = 0
	ENABle = 1
	NP = 2
	PRESent = 3


# noinspection SpellCheckingInspection
class CodecType(Enum):
	"""3 Members, EVS ... WIDeband"""
	EVS = 0
	NARRowband = 1
	WIDeband = 2


# noinspection SpellCheckingInspection
class ConnStatus(Enum):
	"""2 Members, CLOSed ... OPEN"""
	CLOSed = 0
	OPEN = 1


# noinspection SpellCheckingInspection
class DataType(Enum):
	"""8 Members, AUDio ... VIDeo"""
	AUDio = 0
	CALL = 1
	FILetransfer = 2
	FTLMode = 3
	INValid = 4
	RCSLmsg = 5
	SMS = 6
	VIDeo = 7


# noinspection SpellCheckingInspection
class DauState(Enum):
	"""7 Members, ADJusted ... PENDing"""
	ADJusted = 0
	AUTonomous = 1
	COUPled = 2
	INValid = 3
	OFF = 4
	ON = 5
	PENDing = 6


# noinspection SpellCheckingInspection
class DauStatus(Enum):
	"""2 Members, CONN ... NOTConn"""
	CONN = 0
	NOTConn = 1


# noinspection SpellCheckingInspection
class DirectionA(Enum):
	"""3 Members, DL ... UNKN"""
	DL = 0
	UL = 1
	UNKN = 2


# noinspection SpellCheckingInspection
class DirectionB(Enum):
	"""3 Members, DL ... UNK"""
	DL = 0
	UL = 1
	UNK = 2


# noinspection SpellCheckingInspection
class DtxRecv(Enum):
	"""3 Members, DISable ... NP"""
	DISable = 0
	ENABle = 1
	NP = 2


# noinspection SpellCheckingInspection
class EcallType(Enum):
	"""2 Members, AUTO ... MANU"""
	AUTO = 0
	MANU = 1


# noinspection SpellCheckingInspection
class EvsBitrate(Enum):
	"""41 Members, AW1265 ... WLO7"""
	AW1265 = 0
	AW1425 = 1
	AW1585 = 2
	AW1825 = 3
	AW1985 = 4
	AW2305 = 5
	AW66 = 6
	AW885 = 7
	AWB2385 = 8
	NONE = 9
	NOReq = 10
	P1280 = 11
	P132 = 12
	P164 = 13
	P244 = 14
	P320 = 15
	P480 = 16
	P640 = 17
	P960 = 18
	PR28 = 19
	PR59 = 20
	PR72 = 21
	PR80 = 22
	PR96 = 23
	SDP = 24
	SHO2 = 25
	SHO3 = 26
	SHO5 = 27
	SHO7 = 28
	SLO2 = 29
	SLO3 = 30
	SLO5 = 31
	SLO7 = 32
	WHO2 = 33
	WHO3 = 34
	WHO5 = 35
	WHO7 = 36
	WLO2 = 37
	WLO3 = 38
	WLO5 = 39
	WLO7 = 40


# noinspection SpellCheckingInspection
class EvsBw(Enum):
	"""9 Members, DEAC ... WBCA"""
	DEAC = 0
	FB = 1
	IO = 2
	NB = 3
	NOReq = 4
	SWB = 5
	SWBCa = 6
	WB = 7
	WBCA = 8


# noinspection SpellCheckingInspection
class EvsIoModeCnfg(Enum):
	"""2 Members, AMRWb ... EVSamrwb"""
	AMRWb = 0
	EVSamrwb = 1


# noinspection SpellCheckingInspection
class FileTransferType(Enum):
	"""2 Members, FILetransfer ... LARGe"""
	FILetransfer = 0
	LARGe = 1


# noinspection SpellCheckingInspection
class FilterConnect(Enum):
	"""3 Members, BOTH ... OPEN"""
	BOTH = 0
	CLOSed = 1
	OPEN = 2


# noinspection SpellCheckingInspection
class FilterType(Enum):
	"""8 Members, APPL ... SRCP"""
	APPL = 0
	CTRY = 1
	DSTP = 2
	FLOWid = 3
	IPADd = 4
	L4PR = 5
	L7PRotocol = 6
	SRCP = 7


# noinspection SpellCheckingInspection
class ForceModeEvs(Enum):
	"""22 Members, A1265 ... SDP"""
	A1265 = 0
	A1425 = 1
	A1585 = 2
	A1825 = 3
	A1985 = 4
	A2305 = 5
	A2385 = 6
	A660 = 7
	A885 = 8
	P1280 = 9
	P132 = 10
	P164 = 11
	P244 = 12
	P28 = 13
	P320 = 14
	P480 = 15
	P640 = 16
	P72 = 17
	P80 = 18
	P96 = 19
	P960 = 20
	SDP = 21


# noinspection SpellCheckingInspection
class ForceModeNb(Enum):
	"""9 Members, FIVE ... ZERO"""
	FIVE = 0
	FOUR = 1
	FREE = 2
	ONE = 3
	SEVN = 4
	SIX = 5
	THRE = 6
	TWO = 7
	ZERO = 8


# noinspection SpellCheckingInspection
class ForceModeWb(Enum):
	"""10 Members, EIGH ... ZERO"""
	EIGH = 0
	FIVE = 1
	FOUR = 2
	FREE = 3
	ONE = 4
	SEVN = 5
	SIX = 6
	THRE = 7
	TWO = 8
	ZERO = 9


# noinspection SpellCheckingInspection
class HfOnly(Enum):
	"""3 Members, BOTH ... NP"""
	BOTH = 0
	HEADfull = 1
	NP = 2


# noinspection SpellCheckingInspection
class IdType(Enum):
	"""7 Members, ASND ... RFC"""
	ASND = 0
	ASNG = 1
	FQDN = 2
	IPVF = 3
	IPVS = 4
	KEY = 5
	RFC = 6


# noinspection SpellCheckingInspection
class InfoType(Enum):
	"""4 Members, ERRor ... WARNing"""
	ERRor = 0
	INFO = 1
	NONE = 2
	WARNing = 3


# noinspection SpellCheckingInspection
class IpSecEalgorithm(Enum):
	"""4 Members, AES ... NOC"""
	AES = 0
	AUTO = 1
	DES = 2
	NOC = 3


# noinspection SpellCheckingInspection
class IpSecIalgorithm(Enum):
	"""3 Members, AUTO ... HMSH"""
	AUTO = 0
	HMMD = 1
	HMSH = 2


# noinspection SpellCheckingInspection
class IpV6AddLgh(Enum):
	"""2 Members, L16 ... L17"""
	L16 = 0
	L17 = 1


# noinspection SpellCheckingInspection
class JitterDistrib(Enum):
	"""4 Members, NORMal ... UNIForm"""
	NORMal = 0
	PAReto = 1
	PNORmal = 2
	UNIForm = 3


# noinspection SpellCheckingInspection
class KeyType(Enum):
	"""2 Members, OP ... OPC"""
	OP = 0
	OPC = 1


# noinspection SpellCheckingInspection
class Layer(Enum):
	"""5 Members, APP ... L7"""
	APP = 0
	FEATure = 1
	L3 = 2
	L4 = 3
	L7 = 4


# noinspection SpellCheckingInspection
class LoggingType(Enum):
	"""5 Members, LANDau ... UPPP"""
	LANDau = 0
	UIPClient = 1
	UPIP = 2
	UPMulti = 3
	UPPP = 4


# noinspection SpellCheckingInspection
class MediaEndpoint(Enum):
	"""4 Members, AUDioboard ... PCAP"""
	AUDioboard = 0
	FORWard = 1
	LOOPback = 2
	PCAP = 3


# noinspection SpellCheckingInspection
class MobileStatus(Enum):
	"""5 Members, EMERgency ... UNRegistered"""
	EMERgency = 0
	EXPired = 1
	REGistered = 2
	TERMinated = 3
	UNRegistered = 4


# noinspection SpellCheckingInspection
class MtSmsEncoding(Enum):
	"""2 Members, BASE64 ... NENCoding"""
	BASE64 = 0
	NENCoding = 1


# noinspection SpellCheckingInspection
class NetworkInterface(Enum):
	"""3 Members, IP ... MULTicast"""
	IP = 0
	LANDau = 1
	MULTicast = 2


# noinspection SpellCheckingInspection
class Origin(Enum):
	"""3 Members, MO ... UNK"""
	MO = 0
	MT = 1
	UNK = 2


# noinspection SpellCheckingInspection
class OverhUp(Enum):
	"""3 Members, FULL ... OK"""
	FULL = 0
	NOK = 1
	OK = 2


# noinspection SpellCheckingInspection
class PauHeader(Enum):
	"""8 Members, COGE ... REGE"""
	COGE = 0
	CONF = 1
	CONRege = 2
	CORE = 3
	RECN = 4
	RECoge = 5
	REGD = 6
	REGE = 7


# noinspection SpellCheckingInspection
class PcapMode(Enum):
	"""2 Members, CYC ... SING"""
	CYC = 0
	SING = 1


# noinspection SpellCheckingInspection
class PcScfStatus(Enum):
	"""6 Members, ERRor ... UNKNown"""
	ERRor = 0
	OFF = 1
	RUNNing = 2
	STARting = 3
	STOPping = 4
	UNKNown = 5


# noinspection SpellCheckingInspection
class PrefixType(Enum):
	"""2 Members, DHCP ... STATic"""
	DHCP = 0
	STATic = 1


# noinspection SpellCheckingInspection
class Protocol(Enum):
	"""2 Members, TCP ... UDP"""
	TCP = 0
	UDP = 1


# noinspection SpellCheckingInspection
class ProtocolB(Enum):
	"""3 Members, ALL ... UDP"""
	ALL = 0
	TCP = 1
	UDP = 2


# noinspection SpellCheckingInspection
class QosMode(Enum):
	"""2 Members, PRIO ... SAMeprio"""
	PRIO = 0
	SAMeprio = 1


# noinspection SpellCheckingInspection
class ReceiveStatusA(Enum):
	"""3 Members, EMPT ... SUCC"""
	EMPT = 0
	ERR = 1
	SUCC = 2


# noinspection SpellCheckingInspection
class ReceiveStatusB(Enum):
	"""3 Members, EMPT ... SUCC"""
	EMPT = 0
	ERRO = 1
	SUCC = 2


# noinspection SpellCheckingInspection
class RegisterType(Enum):
	"""2 Members, IANA ... OID"""
	IANA = 0
	OID = 1


# noinspection SpellCheckingInspection
class Repetition(Enum):
	"""2 Members, ENDLess ... ONCE"""
	ENDLess = 0
	ONCE = 1


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
class Result(Enum):
	"""4 Members, EMPT ... SUCC"""
	EMPT = 0
	ERR = 1
	PEND = 2
	SUCC = 3


# noinspection SpellCheckingInspection
class RoutingType(Enum):
	"""2 Members, MANual ... RPRotocols"""
	MANual = 0
	RPRotocols = 1


# noinspection SpellCheckingInspection
class ServerType(Enum):
	"""4 Members, FOReign ... NONE"""
	FOReign = 0
	IAForeign = 1
	INTernal = 2
	NONE = 3


# noinspection SpellCheckingInspection
class ServiceTypeA(Enum):
	"""2 Members, SERVer ... TGENerator"""
	SERVer = 0
	TGENerator = 1


# noinspection SpellCheckingInspection
class ServiceTypeB(Enum):
	"""3 Members, BIDirectional ... SERVer"""
	BIDirectional = 0
	CLIent = 1
	SERVer = 2


# noinspection SpellCheckingInspection
class SessionState(Enum):
	"""20 Members, BUSY ... TERMinated"""
	BUSY = 0
	CANCeled = 1
	CREated = 2
	DECLined = 3
	ESTablished = 4
	FILetransfer = 5
	HOLD = 6
	INITialmedia = 7
	MEDiaupdate = 8
	NOK = 9
	NONE = 10
	OK = 11
	PROGgres = 12
	RCSTxt = 13
	REJected = 14
	RELeased = 15
	RESumed = 16
	RINGing = 17
	SRVCcrelease = 18
	TERMinated = 19


# noinspection SpellCheckingInspection
class SessionUsage(Enum):
	"""3 Members, OFF ... ONBYue"""
	OFF = 0
	ONALways = 1
	ONBYue = 2


# noinspection SpellCheckingInspection
class SignalingType(Enum):
	"""7 Members, EARLymedia ... WOTPrec183"""
	EARLymedia = 0
	NOPRecondit = 1
	PRECondit = 2
	REQU100 = 3
	REQuprecondi = 4
	SIMPle = 5
	WOTPrec183 = 6


# noinspection SpellCheckingInspection
class SipTimerSel(Enum):
	"""3 Members, CUSTom ... RFC"""
	CUSTom = 0
	DEFault = 1
	RFC = 2


# noinspection SpellCheckingInspection
class SmsEncoding(Enum):
	"""7 Members, ASCI ... UCS"""
	ASCI = 0
	BASE64 = 1
	GSM7 = 2
	GSM8 = 3
	IAF5 = 4
	NENC = 5
	UCS = 6


# noinspection SpellCheckingInspection
class SmsStatus(Enum):
	"""4 Members, NONE ... SIPRogress"""
	NONE = 0
	SCOMpleted = 1
	SFAiled = 2
	SIPRogress = 3


# noinspection SpellCheckingInspection
class SmsTypeA(Enum):
	"""6 Members, OGPP ... TPAGer"""
	OGPP = 0
	OGPP2 = 1
	OPAGer = 2
	TGPP = 3
	TGPP2 = 4
	TPAGer = 5


# noinspection SpellCheckingInspection
class SmsTypeB(Enum):
	"""2 Members, TGP2 ... TGPP"""
	TGP2 = 0
	TGPP = 1


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class StartMode(Enum):
	"""2 Members, EAMRwbio ... EPRimary"""
	EAMRwbio = 0
	EPRimary = 1


# noinspection SpellCheckingInspection
class Testcall(Enum):
	"""2 Members, FALSe ... TRUE"""
	FALSe = 0
	TRUE = 1


# noinspection SpellCheckingInspection
class TestResult(Enum):
	"""3 Members, FAILed ... SUCCeded"""
	FAILed = 0
	NONE = 1
	SUCCeded = 2


# noinspection SpellCheckingInspection
class ThroughputType(Enum):
	"""2 Members, OVERall ... RAN"""
	OVERall = 0
	RAN = 1


# noinspection SpellCheckingInspection
class TransportSel(Enum):
	"""4 Members, CUSTom ... UDP"""
	CUSTom = 0
	DEFault = 1
	TCP = 2
	UDP = 3


# noinspection SpellCheckingInspection
class UpdateCallEvent(Enum):
	"""2 Members, HOLD ... RESume"""
	HOLD = 0
	RESume = 1


# noinspection SpellCheckingInspection
class VideoCodec(Enum):
	"""2 Members, H263 ... H264"""
	H263 = 0
	H264 = 1


# noinspection SpellCheckingInspection
class VoicePrecondition(Enum):
	"""3 Members, SIMPle ... WPRecondit"""
	SIMPle = 0
	WNPRecondit = 1
	WPRecondit = 2


# noinspection SpellCheckingInspection
class VoimState(Enum):
	"""5 Members, EST ... UNK"""
	EST = 0
	HOLD = 1
	REL = 2
	RING = 3
	UNK = 4
