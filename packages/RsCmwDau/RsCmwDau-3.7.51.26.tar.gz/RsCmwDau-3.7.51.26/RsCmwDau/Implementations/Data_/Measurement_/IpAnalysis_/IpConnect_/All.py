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
			- Conn_Status: List[enums.ConnStatus]: OPEN | CLOSed Connection status
			- Lst: List[float]: Local system time, incremented every ms The clock starts when the instrument is switched on.
			- Sys_Clock: List[int]: System clock in units of 10 ns When 1 ms is reached (100*10 ns) , the clock is reset to 0 and the local system time is incremented. Range: 0 to 99
			- Protocol: List[str]: Layer 4 protocol as string ('TCP', 'UDP', ...)
			- Dpi_Protocol: List[str]: Layer 7 protocol as string ('HTTP', 'FTP', ...)
			- Ip_Addr_Source: List[str]: IP address of the connection source as string
			- Ip_Port_Source: List[int]: Port number of the connection source Range: 0 to 65654
			- Ip_Addr_Dest: List[str]: IP address of the connection destination as string
			- Ip_Port_Dest: List[int]: Port number of the connection destination Range: 0 to 65654
			- Overh_Down: List[float]: Downlink overhead as percentage of the packet Range: 0 % to 100 %, Unit: %
			- Overh_Up: List[float]: Uplink overhead as percentage of the packet Range: 0 % to 100 %, Unit: %
			- Avg_Ps_Down: List[float]: Average downlink packet size Range: 0 bytes to 65535 bytes, Unit: bytes
			- Avg_Ps_Up: List[float]: Average uplink packet size Range: 0 bytes to 65535 bytes, Unit: bytes
			- App: List[str]: Application name as string
			- Country: List[str]: Country of the destination as string (two-letter country code)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Flow_Id', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Conn_Status', DataType.EnumList, enums.ConnStatus, False, True, 1),
			ArgStruct('Lst', DataType.FloatList, None, False, True, 1),
			ArgStruct('Sys_Clock', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Protocol', DataType.StringList, None, False, True, 1),
			ArgStruct('Dpi_Protocol', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip_Addr_Source', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip_Port_Source', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Ip_Addr_Dest', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip_Port_Dest', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Overh_Down', DataType.FloatList, None, False, True, 1),
			ArgStruct('Overh_Up', DataType.FloatList, None, False, True, 1),
			ArgStruct('Avg_Ps_Down', DataType.FloatList, None, False, True, 1),
			ArgStruct('Avg_Ps_Up', DataType.FloatList, None, False, True, 1),
			ArgStruct('App', DataType.StringList, None, False, True, 1),
			ArgStruct('Country', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Flow_Id: List[int] = None
			self.Conn_Status: List[enums.ConnStatus] = None
			self.Lst: List[float] = None
			self.Sys_Clock: List[int] = None
			self.Protocol: List[str] = None
			self.Dpi_Protocol: List[str] = None
			self.Ip_Addr_Source: List[str] = None
			self.Ip_Port_Source: List[int] = None
			self.Ip_Addr_Dest: List[str] = None
			self.Ip_Port_Dest: List[int] = None
			self.Overh_Down: List[float] = None
			self.Overh_Up: List[float] = None
			self.Avg_Ps_Down: List[float] = None
			self.Avg_Ps_Up: List[float] = None
			self.App: List[str] = None
			self.Country: List[str] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPConnect:ALL \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipConnect.all.fetch() \n
		Queries the 'IP Connectivity' results for all connections. After the reliability indicator, results are returned per
		connection (flow) : <Reliability>, {<FlowID>, <ConnStatus>, <LST>, <SysClock>, <Protocol>, <DPIProtocol>, <IPAddrSource>,
		<IPPortSource>, <IPAddrDest>, <IPPortDest>, <OverhDown>, <OverhUp>, <AvgPSDown>, <AvgPSUp>, <App>, <Country>}conn 1, {...
		}conn 2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPConnect:ALL?', self.__class__.FetchStruct())
