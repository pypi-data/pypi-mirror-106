from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Flow_Id: List[int]: Flow ID of the connection
			- Th_Down: List[float]: Throughput in downlink direction Unit: bit/s
			- Tcpws_Down: List[enums.OverhUp]: OK | FULL Threshold check result for downlink TCP window size
			- Retr_Down: List[enums.OverhUp]: OK | NOK Threshold check result for downlink retransmissions
			- Overh_Down: List[enums.OverhUp]: OK | NOK Only for backward compatibility - no longer used
			- Th_Up: List[float]: Throughput in uplink direction Unit: bit/s
			- Tcpws_Up: List[enums.OverhUp]: OK | FULL Threshold check result for uplink TCP window size
			- Retr_Up: List[enums.OverhUp]: OK | NOK Threshold check result for uplink retransmissions
			- Overh_Up: List[enums.OverhUp]: OK | NOK Only for backward compatibility - no longer used
			- Destination: List[str]: Destination address as string
			- Rtt_Status: List[enums.OverhUp]: OK | NOK Threshold check result for round-trip time
			- Pkt_Size_Ul: List[int]: Layer 3 uplink packet size Unit: byte
			- Pkt_Size_Dl: List[int]: Layer 3 downlink packet size Unit: byte"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Flow_Id', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Th_Down', DataType.FloatList, None, False, True, 1),
			ArgStruct('Tcpws_Down', DataType.EnumList, enums.OverhUp, False, True, 1),
			ArgStruct('Retr_Down', DataType.EnumList, enums.OverhUp, False, True, 1),
			ArgStruct('Overh_Down', DataType.EnumList, enums.OverhUp, False, True, 1),
			ArgStruct('Th_Up', DataType.FloatList, None, False, True, 1),
			ArgStruct('Tcpws_Up', DataType.EnumList, enums.OverhUp, False, True, 1),
			ArgStruct('Retr_Up', DataType.EnumList, enums.OverhUp, False, True, 1),
			ArgStruct('Overh_Up', DataType.EnumList, enums.OverhUp, False, True, 1),
			ArgStruct('Destination', DataType.StringList, None, False, True, 1),
			ArgStruct('Rtt_Status', DataType.EnumList, enums.OverhUp, False, True, 1),
			ArgStruct('Pkt_Size_Ul', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Pkt_Size_Dl', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Flow_Id: List[int] = None
			self.Th_Down: List[float] = None
			self.Tcpws_Down: List[enums.OverhUp] = None
			self.Retr_Down: List[enums.OverhUp] = None
			self.Overh_Down: List[enums.OverhUp] = None
			self.Th_Up: List[float] = None
			self.Tcpws_Up: List[enums.OverhUp] = None
			self.Retr_Up: List[enums.OverhUp] = None
			self.Overh_Up: List[enums.OverhUp] = None
			self.Destination: List[str] = None
			self.Rtt_Status: List[enums.OverhUp] = None
			self.Pkt_Size_Ul: List[int] = None
			self.Pkt_Size_Dl: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:ALL \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.tcpAnalysis.all.fetch() \n
		Queries the threshold check and throughput results for all connections. After the reliability indicator, 13 results are
		returned for each connection (flow) : <Reliability>, {<FlowID>, <ThDown>, <TCPWSDown>, <RetrDown>, <OverhDown>, <ThUp>,
		<TCPWSUp>, <RetrUp>, <OverhUp>, <Destination>, <RTTStatus>, <PKTSizeUL>, <PKTSizeDL>}connection 1, {...}connection 2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:ALL?', self.__class__.FetchStruct())
