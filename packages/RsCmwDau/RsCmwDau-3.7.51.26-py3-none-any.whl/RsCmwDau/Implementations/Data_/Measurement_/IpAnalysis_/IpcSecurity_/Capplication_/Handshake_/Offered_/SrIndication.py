from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrIndication:
	"""SrIndication commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("srIndication", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Server_Id: List[str]: Server ID as hexadecimal value
			- Server_Name: List[str]: Server name indication (SNI) as string
			- Server_Type: List[str]: Type of the server name as string"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Server_Id', DataType.RawStringList, None, False, True, 1),
			ArgStruct('Server_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Server_Type', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Server_Id: List[str] = None
			self.Server_Name: List[str] = None
			self.Server_Type: List[str] = None

	def fetch(self, flow_id: int) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:OFFered:SRINdication \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.capplication.handshake.offered.srIndication.fetch(flow_id = 1) \n
		Queries information about the server that the client wants to contact, as sent by the client during the handshake for a
		specific connection. After the reliability indicator, three results are returned for each entry: <Reliability>,
		{<ServerID>, <ServerName>, <ServerType>}1, {...}2, ... \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:OFFered:SRINdication? {param}', self.__class__.FetchStruct())
