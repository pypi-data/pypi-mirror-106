from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FlowId:
	"""FlowId commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("flowId", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Th_Down: float: Throughput in downlink direction Unit: bit/s
			- Tcpws_Down: enums.OverhUp: OK | FULL Threshold check result for downlink TCP window size
			- Retr_Down: enums.OverhUp: OK | NOK Threshold check result for downlink retransmissions
			- Overh_Down: enums.OverhUp: OK | NOK Only for backward compatibility - no longer used
			- Th_Up: float: Throughput in uplink direction Unit: bit/s
			- Tcpws_Up: enums.OverhUp: OK | FULL Threshold check result for uplink TCP window size
			- Retr_Up: enums.OverhUp: OK | NOK Threshold check result for uplink retransmissions
			- Overh_Up: enums.OverhUp: OK | NOK Only for backward compatibility - no longer used
			- Destination: str: Destination address as string
			- Rtt: enums.OverhUp: OK | NOK Threshold check result for round-trip time
			- Pkt_Size_Up: int: Layer 3 uplink packet size Unit: byte
			- Pkt_Size_Dl: int: Layer 3 downlink packet size Unit: byte"""
		__meta_args_list = [
			ArgStruct.scalar_float('Th_Down'),
			ArgStruct.scalar_enum('Tcpws_Down', enums.OverhUp),
			ArgStruct.scalar_enum('Retr_Down', enums.OverhUp),
			ArgStruct.scalar_enum('Overh_Down', enums.OverhUp),
			ArgStruct.scalar_float('Th_Up'),
			ArgStruct.scalar_enum('Tcpws_Up', enums.OverhUp),
			ArgStruct.scalar_enum('Retr_Up', enums.OverhUp),
			ArgStruct.scalar_enum('Overh_Up', enums.OverhUp),
			ArgStruct.scalar_str('Destination'),
			ArgStruct.scalar_enum('Rtt', enums.OverhUp),
			ArgStruct.scalar_int('Pkt_Size_Up'),
			ArgStruct.scalar_int('Pkt_Size_Dl')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Th_Down: float = None
			self.Tcpws_Down: enums.OverhUp = None
			self.Retr_Down: enums.OverhUp = None
			self.Overh_Down: enums.OverhUp = None
			self.Th_Up: float = None
			self.Tcpws_Up: enums.OverhUp = None
			self.Retr_Up: enums.OverhUp = None
			self.Overh_Up: enums.OverhUp = None
			self.Destination: str = None
			self.Rtt: enums.OverhUp = None
			self.Pkt_Size_Up: int = None
			self.Pkt_Size_Dl: int = None

	def get(self, flow_id: float) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:FLOWid \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipAnalysis.tcpAnalysis.flowId.get(flow_id = 1.0) \n
		Queries the threshold check and throughput results for a specific connection, selected via its flow ID. \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:FLOWid? {param}', self.__class__.GetStruct())
