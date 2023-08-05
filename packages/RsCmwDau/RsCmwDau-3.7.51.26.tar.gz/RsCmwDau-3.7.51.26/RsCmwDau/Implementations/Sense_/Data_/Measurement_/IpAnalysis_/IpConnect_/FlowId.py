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
			- Conn_Status: enums.ConnStatus: OPEN | CLOSed Connection status
			- Protocol: str: Layer 4 protocol as string ('TCP', 'UDP', ...)
			- Dpi_Protocol: str: Layer 7 protocol as string ('HTTP', 'FTP', ...)
			- Ip_Addr_Source: str: IP address of the connection source as string
			- Ip_Port_Source: int: Port number of the connection source Range: 0 to 65654
			- Ip_Addr_Dest: str: IP address of the connection destination as string
			- Ip_Port_Dest: int: Port number of the connection destination Range: 0 to 65654
			- Overh_Down: float: Downlink overhead as percentage of the packet Range: 0 % to 100 %, Unit: %
			- Overh_Up: float: Uplink overhead as percentage of the packet Range: 0 % to 100 %, Unit: %
			- Avg_Ps_Down: float: Average downlink packet size Range: 0 bytes to 65535 bytes, Unit: bytes
			- Avg_Ps_Up: float: Average uplink packet size Range: 0 bytes to 65535 bytes, Unit: bytes
			- App: str: Application name as string
			- Country: str: Country of the destination as string (two-letter country code)"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Conn_Status', enums.ConnStatus),
			ArgStruct.scalar_str('Protocol'),
			ArgStruct.scalar_str('Dpi_Protocol'),
			ArgStruct.scalar_str('Ip_Addr_Source'),
			ArgStruct.scalar_int('Ip_Port_Source'),
			ArgStruct.scalar_str('Ip_Addr_Dest'),
			ArgStruct.scalar_int('Ip_Port_Dest'),
			ArgStruct.scalar_float('Overh_Down'),
			ArgStruct.scalar_float('Overh_Up'),
			ArgStruct.scalar_float('Avg_Ps_Down'),
			ArgStruct.scalar_float('Avg_Ps_Up'),
			ArgStruct.scalar_str('App'),
			ArgStruct.scalar_str('Country')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Conn_Status: enums.ConnStatus = None
			self.Protocol: str = None
			self.Dpi_Protocol: str = None
			self.Ip_Addr_Source: str = None
			self.Ip_Port_Source: int = None
			self.Ip_Addr_Dest: str = None
			self.Ip_Port_Dest: int = None
			self.Overh_Down: float = None
			self.Overh_Up: float = None
			self.Avg_Ps_Down: float = None
			self.Avg_Ps_Up: float = None
			self.App: str = None
			self.Country: str = None

	def get(self, flow_id: float) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:IPConnect:FLOWid \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipAnalysis.ipConnect.flowId.get(flow_id = 1.0) \n
		Queries the 'IP Connectivity' results for a specific connection, selected via its flow ID. \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:IPConnect:FLOWid? {param}', self.__class__.GetStruct())
