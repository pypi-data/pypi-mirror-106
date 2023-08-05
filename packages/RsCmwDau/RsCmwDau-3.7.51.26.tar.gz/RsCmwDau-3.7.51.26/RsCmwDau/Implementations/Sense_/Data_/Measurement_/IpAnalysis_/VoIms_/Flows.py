from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flows:
	"""Flows commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("flows", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Flow_Id: int: Flow ID, as returned by [CMDLINK: FETCh:DATA:MEASi:IPANalysis:VOIMs:ALL CMDLINK]
			- Direction: enums.DirectionB: UL | DL | UNK Flow direction uplink, downlink or unknown
			- Type_Py: enums.AvTypeB: AUDio | VIDeo | UNKNow Flow type audio, video or unknown
			- Codec: str: String indicating the used codec
			- Seq_Number: int: Sequence number of the currently processed packet
			- Num_Pack: int: Number of already processed packets
			- Throughput: float: Current audio or video data throughput at the RTP level Unit: bit/s
			- Dest_Port: int: Port used at the flow destination
			- Evs_Mode: str: String indicating the EVS mode (primary or AMR-WB-IO)
			- Evs_Format: str: String indicating the EVS format (header-full or compact)
			- Num_Evs_Comp: int: Number of EVS packets with compact format
			- Num_Ev_Shp: int: Number of EVS packets with header-full format
			- Video_Resolution: str: String indicating the video resolution
			- Video_Frate: int: Video frame rate in frames per second
			- Video_Oreintation: str: String indicating the counter-clockwise video rotation
			- Video_Profile: str: String indicating the H.264 profile
			- Video_Level: str: String indicating the H.264 level
			- Video_Constraint: str: String indicating the H.264 constraint set
			- Bitrate: float: Audio codec rate"""
		__meta_args_list = [
			ArgStruct.scalar_int('Flow_Id'),
			ArgStruct.scalar_enum('Direction', enums.DirectionB),
			ArgStruct.scalar_enum('Type_Py', enums.AvTypeB),
			ArgStruct.scalar_str('Codec'),
			ArgStruct.scalar_int('Seq_Number'),
			ArgStruct.scalar_int('Num_Pack'),
			ArgStruct.scalar_float('Throughput'),
			ArgStruct.scalar_int('Dest_Port'),
			ArgStruct.scalar_str('Evs_Mode'),
			ArgStruct.scalar_str('Evs_Format'),
			ArgStruct.scalar_int('Num_Evs_Comp'),
			ArgStruct.scalar_int('Num_Ev_Shp'),
			ArgStruct.scalar_str('Video_Resolution'),
			ArgStruct.scalar_int('Video_Frate'),
			ArgStruct.scalar_str('Video_Oreintation'),
			ArgStruct.scalar_str('Video_Profile'),
			ArgStruct.scalar_str('Video_Level'),
			ArgStruct.scalar_str('Video_Constraint'),
			ArgStruct.scalar_float('Bitrate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Flow_Id: int = None
			self.Direction: enums.DirectionB = None
			self.Type_Py: enums.AvTypeB = None
			self.Codec: str = None
			self.Seq_Number: int = None
			self.Num_Pack: int = None
			self.Throughput: float = None
			self.Dest_Port: int = None
			self.Evs_Mode: str = None
			self.Evs_Format: str = None
			self.Num_Evs_Comp: int = None
			self.Num_Ev_Shp: int = None
			self.Video_Resolution: str = None
			self.Video_Frate: int = None
			self.Video_Oreintation: str = None
			self.Video_Profile: str = None
			self.Video_Level: str = None
			self.Video_Constraint: str = None
			self.Bitrate: float = None

	def get(self, session_id: float, flow_id: int, direction: enums.DirectionB, type_py: enums.AvTypeB = None) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:VOIMs:FLOWs \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipAnalysis.voIms.flows.get(session_id = 1.0, flow_id = 1, direction = enums.DirectionB.DL, type_py = enums.AvTypeB.AUDio) \n
		Queries flow information related to a voice over IMS call. A query returns all parameters except the <SessionID>:
		<FlowID>, <Direction>, <Type>, <Codec>, <SeqNumber>, ..., <Bitrate> \n
			:param session_id: Call ID, as returned by method RsCmwDau.Data.Measurement.IpAnalysis.VoIms.All.fetch
			:param flow_id: Flow ID, as returned by method RsCmwDau.Data.Measurement.IpAnalysis.VoIms.All.fetch
			:param direction: UL | DL | UNK Flow direction uplink, downlink or unknown
			:param type_py: AUDio | VIDeo | UNKNow Flow type audio, video or unknown
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('session_id', session_id, DataType.Float), ArgSingle('flow_id', flow_id, DataType.Integer), ArgSingle('direction', direction, DataType.Enum), ArgSingle('type_py', type_py, DataType.Enum, True))
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:VOIMs:FLOWs? {param}'.rstrip(), self.__class__.GetStruct())
