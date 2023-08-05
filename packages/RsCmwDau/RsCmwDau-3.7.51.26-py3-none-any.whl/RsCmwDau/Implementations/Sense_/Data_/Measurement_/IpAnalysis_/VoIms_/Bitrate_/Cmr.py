from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmr:
	"""Cmr commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cmr", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Flow_Id: int: Flow ID, as returned by [CMDLINK: FETCh:DATA:MEASi:IPANalysis:VOIMs:ALL CMDLINK]
			- Direction: enums.DirectionB: UL | DL | UNK Flow direction uplink, downlink or unknown
			- Curr_Bitrate: float: Current measured bitrate Unit: bit/s
			- Avg_Bitrate: float: Average measured bitrate Unit: bit/s
			- Min_Bitrate: float: Minimum measured bitrate Unit: bit/s
			- Max_Bitrate: float: Maximum measured bitrate Unit: bit/s
			- Curr_Cmr_Bitrate: float: Bitrate currently requested for the other direction Unit: bit/s
			- Min_Cmr_Bitrate: float: Minimum of the bitrates requested for the other direction Unit: bit/s
			- Max_Cmr_Bitrate: float: Maximum of the bitrates requested for the other direction Unit: bit/s
			- Curr_Cmr_Bw: str: String indicating the bandwidth currently requested for the other direction
			- Min_Cmr_Bw: str: String indicating the minimum of the bandwidths requested for the other direction
			- Max_Cmr_Bw: str: String indicating the maximum of the bandwidths requested for the other direction"""
		__meta_args_list = [
			ArgStruct.scalar_int('Flow_Id'),
			ArgStruct.scalar_enum('Direction', enums.DirectionB),
			ArgStruct.scalar_float('Curr_Bitrate'),
			ArgStruct.scalar_float('Avg_Bitrate'),
			ArgStruct.scalar_float('Min_Bitrate'),
			ArgStruct.scalar_float('Max_Bitrate'),
			ArgStruct.scalar_float('Curr_Cmr_Bitrate'),
			ArgStruct.scalar_float('Min_Cmr_Bitrate'),
			ArgStruct.scalar_float('Max_Cmr_Bitrate'),
			ArgStruct.scalar_str('Curr_Cmr_Bw'),
			ArgStruct.scalar_str('Min_Cmr_Bw'),
			ArgStruct.scalar_str('Max_Cmr_Bw')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Flow_Id: int = None
			self.Direction: enums.DirectionB = None
			self.Curr_Bitrate: float = None
			self.Avg_Bitrate: float = None
			self.Min_Bitrate: float = None
			self.Max_Bitrate: float = None
			self.Curr_Cmr_Bitrate: float = None
			self.Min_Cmr_Bitrate: float = None
			self.Max_Cmr_Bitrate: float = None
			self.Curr_Cmr_Bw: str = None
			self.Min_Cmr_Bw: str = None
			self.Max_Cmr_Bw: str = None

	def get(self, session_id: float, flow_id: int, direction: enums.DirectionB) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:VOIMs:BITRate:CMR \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipAnalysis.voIms.bitrate.cmr.get(session_id = 1.0, flow_id = 1, direction = enums.DirectionB.DL) \n
		Queries bitrates and CMR information related to a voice over IMS call. A query returns all parameters except the
		<SessionID>: <FlowID>, <Direction>, <CurrBitrate>, <AvgBitrate>, ..., <MaxCMRBW> \n
			:param session_id: Call ID, as returned by method RsCmwDau.Data.Measurement.IpAnalysis.VoIms.All.fetch
			:param flow_id: Flow ID, as returned by method RsCmwDau.Data.Measurement.IpAnalysis.VoIms.All.fetch
			:param direction: UL | DL | UNK Flow direction uplink, downlink or unknown
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('session_id', session_id, DataType.Float), ArgSingle('flow_id', flow_id, DataType.Integer), ArgSingle('direction', direction, DataType.Enum))
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:VOIMs:BITRate:CMR? {param}'.rstrip(), self.__class__.GetStruct())
