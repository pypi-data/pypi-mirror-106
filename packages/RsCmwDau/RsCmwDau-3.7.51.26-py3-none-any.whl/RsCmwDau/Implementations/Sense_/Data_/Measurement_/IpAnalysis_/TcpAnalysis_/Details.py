from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Details:
	"""Details commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("details", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ip_Addr_Source: str: IP address of the connection source as string
			- Ip_Port_Source: int: Port number of the connection source Range: 0 to 65654
			- Ip_Addr_Dest: str: IP address of the connection destination as string
			- Ip_Port_Dest: int: Port number of the connection destination Range: 0 to 65654
			- Curr_Tcpws_Down: float: Measured downlink TCP window size Unit: byte
			- Max_Tcpws_Down: float: Negotiated maximum downlink TCP window size Unit: byte
			- Retr_Down: float: Downlink retransmission rate Range: 0 % to 100 %, Unit: %
			- Overh_Down: float: Only for backward compatibility - no longer used Range: 0 % to 100 %, Unit: %
			- Curr_Tcpws_Up: float: Measured uplink TCP window size Unit: byte
			- Max_Tcpws_Up: float: Negotiated maximum uplink TCP window size Unit: byte
			- Retr_Up: float: Uplink retransmission rate Range: 0 % to 100 %, Unit: %
			- Overh_Up: float: Only for backward compatibility - no longer used Range: 0 % to 100 %, Unit: %
			- Rtt: int: Round-trip time Unit: ms"""
		__meta_args_list = [
			ArgStruct.scalar_str('Ip_Addr_Source'),
			ArgStruct.scalar_int('Ip_Port_Source'),
			ArgStruct.scalar_str('Ip_Addr_Dest'),
			ArgStruct.scalar_int('Ip_Port_Dest'),
			ArgStruct.scalar_float('Curr_Tcpws_Down'),
			ArgStruct.scalar_float('Max_Tcpws_Down'),
			ArgStruct.scalar_float('Retr_Down'),
			ArgStruct.scalar_float('Overh_Down'),
			ArgStruct.scalar_float('Curr_Tcpws_Up'),
			ArgStruct.scalar_float('Max_Tcpws_Up'),
			ArgStruct.scalar_float('Retr_Up'),
			ArgStruct.scalar_float('Overh_Up'),
			ArgStruct.scalar_int('Rtt')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ip_Addr_Source: str = None
			self.Ip_Port_Source: int = None
			self.Ip_Addr_Dest: str = None
			self.Ip_Port_Dest: int = None
			self.Curr_Tcpws_Down: float = None
			self.Max_Tcpws_Down: float = None
			self.Retr_Down: float = None
			self.Overh_Down: float = None
			self.Curr_Tcpws_Up: float = None
			self.Max_Tcpws_Up: float = None
			self.Retr_Up: float = None
			self.Overh_Up: float = None
			self.Rtt: int = None

	def get(self, flow_id: float) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:DETails \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipAnalysis.tcpAnalysis.details.get(flow_id = 1.0) \n
		Queries the 'TCP Analysis' details for a specific connection, selected via its flow ID. \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:DETails? {param}', self.__class__.GetStruct())
