from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class History:
	"""History commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("history", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Sms_Timestamps: str: Timestamp of the message transfer as string in the format 'hh:mm:ss'
			- Sms_Type: enums.SmsTypeA: TGPP | TGPP2 | OGPP | OGPP2 | OPAGer | TPAGer TGPP: mobile-terminating message, 3GPP TGPP2: mobile-terminating message, 3GPP2 OGPP: mobile-originating message, 3GPP OGPP2: mobile-originating message, 3GPP2 OPAGer: mobile-originating message, RCS pager mode TPAGer: mobile-terminating message, RCS pager mode
			- Sms_Encoding: enums.SmsEncoding: GSM7 | GSM8 | UCS | ASCI | IAF5 | NENC | BASE64 Encoding of the message
			- Sms_Text: str: Message text as string
			- History_State: enums.SessionState: OK | NOK | PROGgres | RINGing | ESTablished | HOLD | RESumed | RELeased | MEDiaupdate | BUSY | DECLined | RCSTxt | INITialmedia | FILetransfer | SRVCcrelease | TERMinated | CANCeled | REJected Status of the call
			- History_Timestamps: str: Timestamp of the call as string in the format 'hh:mm:ss'
			- Signaling_Type: enums.SignalingType: PRECondit | NOPRecondit | SIMPle | REQU100 | REQuprecondi | WOTPrec183 | EARLymedia Signaling type of the call
			- Audio_Codec_Type: enums.CodecType: NARRowband | WIDeband | EVS Audio codec type of the call
			- Amr_Align_Mode: enums.AlignMode: OCTetaligned | BANDwidtheff AMR voice codec alignment mode of the call
			- Amr_Mode: str: Codec mode as string
			- Video_Codec: enums.VideoCodec: H263 | H264 Video codec of the video call
			- Video_Attributes: str: Video codec attributes of the video call"""
		__meta_args_list = [
			ArgStruct.scalar_str('Sms_Timestamps'),
			ArgStruct.scalar_enum('Sms_Type', enums.SmsTypeA),
			ArgStruct.scalar_enum('Sms_Encoding', enums.SmsEncoding),
			ArgStruct.scalar_str('Sms_Text'),
			ArgStruct.scalar_enum('History_State', enums.SessionState),
			ArgStruct.scalar_str('History_Timestamps'),
			ArgStruct.scalar_enum('Signaling_Type', enums.SignalingType),
			ArgStruct.scalar_enum('Audio_Codec_Type', enums.CodecType),
			ArgStruct.scalar_enum('Amr_Align_Mode', enums.AlignMode),
			ArgStruct.scalar_str('Amr_Mode'),
			ArgStruct.scalar_enum('Video_Codec', enums.VideoCodec),
			ArgStruct.scalar_str('Video_Attributes')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sms_Timestamps: str = None
			self.Sms_Type: enums.SmsTypeA = None
			self.Sms_Encoding: enums.SmsEncoding = None
			self.Sms_Text: str = None
			self.History_State: enums.SessionState = None
			self.History_Timestamps: str = None
			self.Signaling_Type: enums.SignalingType = None
			self.Audio_Codec_Type: enums.CodecType = None
			self.Amr_Align_Mode: enums.AlignMode = None
			self.Amr_Mode: str = None
			self.Video_Codec: enums.VideoCodec = None
			self.Video_Attributes: str = None

	def get(self, idn: str, ims=repcap.Ims.Default) -> GetStruct:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:HISTory \n
		Snippet: value: GetStruct = driver.sense.data.control.ims.history.get(idn = '1', ims = repcap.Ims.Default) \n
		Queries details for a selected event log entry.
			INTRO_CMD_HELP: The returned sequence depends on the type of the entry. Examples: \n
			- Four values are returned for a message entry of the type 3GPP, 3GPP2 or RCS pager mode: <SMSTimestamps>, <SMSType>, <SMSEncoding>, <SMSText>
			- Eight values are returned for each recorded state of a call entry: {<HistoryState>, <HistoryTimestamps>, <SignalingType>, <AudioCodecType>, <AMRAlignMode>, <AMRMode>, <VideoCodec>, <VideoAttributes>}state 1, {...}state 2, ..., {...}state n If a parameter is not relevant for a state, INV is returned for this parameter. \n
			:param idn: String selecting the event log entry To query IDs, see method RsCmwDau.Sense.Data.Control.Ims.Events.get_.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(idn)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		return self._core.io.query_struct(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:HISTory? {param}', self.__class__.GetStruct())
