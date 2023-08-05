from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


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
			- Application: List[str]: Application name as string
			- Flow_Id: List[int]: ID of the flow used by the connection
			- Source_Ip: List[str]: IP address of the DUT as string
			- Local_Port: List[int]: Port number used at the DUT side
			- Destination_Ip: List[str]: Destination IP address as string
			- Destination_Port: List[int]: Port number of the destination
			- Fqdn: List[str]: Fully qualified domain name of the destination as string
			- Ran: List[str]: Used radio access network as string
			- Apn: List[str]: Access point name as string
			- Protocol: List[str]: Used protocol, for example SSL or HTTP, as string
			- Country_Code: List[str]: Country of the destination as string (two-letter country code)
			- Location: List[str]: City of the destination, as string
			- Latitude: List[str]: Latitude of the destination, as string
			- Longitude: List[str]: Longitude of the destination, as string
			- Ul_Data: List[float]: Layer 3 UL data exchanged via the connection Unit: bytes
			- Ul_Pkt: List[int]: Number of UL packets exchanged via the connection
			- Dl_Data: List[float]: Layer 3 DL data exchanged via the connection Unit: bytes
			- Dl_Pkt: List[int]: Number of DL packets exchanged via the connection
			- Hand_Sk_Available: List[bool]: OFF | ON Handshake information available for the connection or not
			- Certif_Available: List[bool]: OFF | ON Certificate information available for the connection or not"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Application', DataType.StringList, None, False, True, 1),
			ArgStruct('Flow_Id', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Source_Ip', DataType.StringList, None, False, True, 1),
			ArgStruct('Local_Port', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Destination_Ip', DataType.StringList, None, False, True, 1),
			ArgStruct('Destination_Port', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Fqdn', DataType.StringList, None, False, True, 1),
			ArgStruct('Ran', DataType.StringList, None, False, True, 1),
			ArgStruct('Apn', DataType.StringList, None, False, True, 1),
			ArgStruct('Protocol', DataType.StringList, None, False, True, 1),
			ArgStruct('Country_Code', DataType.StringList, None, False, True, 1),
			ArgStruct('Location', DataType.StringList, None, False, True, 1),
			ArgStruct('Latitude', DataType.StringList, None, False, True, 1),
			ArgStruct('Longitude', DataType.StringList, None, False, True, 1),
			ArgStruct('Ul_Data', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ul_Pkt', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dl_Data', DataType.FloatList, None, False, True, 1),
			ArgStruct('Dl_Pkt', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Hand_Sk_Available', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Certif_Available', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Application: List[str] = None
			self.Flow_Id: List[int] = None
			self.Source_Ip: List[str] = None
			self.Local_Port: List[int] = None
			self.Destination_Ip: List[str] = None
			self.Destination_Port: List[int] = None
			self.Fqdn: List[str] = None
			self.Ran: List[str] = None
			self.Apn: List[str] = None
			self.Protocol: List[str] = None
			self.Country_Code: List[str] = None
			self.Location: List[str] = None
			self.Latitude: List[str] = None
			self.Longitude: List[str] = None
			self.Ul_Data: List[float] = None
			self.Ul_Pkt: List[int] = None
			self.Dl_Data: List[float] = None
			self.Dl_Pkt: List[int] = None
			self.Hand_Sk_Available: List[bool] = None
			self.Certif_Available: List[bool] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:CAPPlication:ALL \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.capplication.all.fetch() \n
		Queries information about all connections of all applications. The results after the reliability indicator are returned
		per connection: <Reliability>, {<Application>, <Flowid>, ..., <HandSkAvailable>, <CertifAvailable>}1, {...}2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:CAPPlication:ALL?', self.__class__.FetchStruct())
