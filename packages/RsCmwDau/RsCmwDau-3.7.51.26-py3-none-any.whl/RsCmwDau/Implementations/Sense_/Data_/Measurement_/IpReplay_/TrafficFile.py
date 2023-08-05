from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrafficFile:
	"""TrafficFile commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trafficFile", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- L_4_Protocol: List[str]: Layer 4 protocol as string ('TCP', 'UDP', ...)
			- No_Of_Packets: List[int]: Number of IP packets for the connection
			- Ip_Src_Address: List[str]: IP address of the connection source as string
			- Ip_Src_Port: List[int]: Port number of the connection source
			- Ip_Dest_Address: List[str]: IP address of the connection destination as string
			- Ip_Dest_Port: List[int]: Port number of the connection destination"""
		__meta_args_list = [
			ArgStruct('L_4_Protocol', DataType.StringList, None, False, True, 1),
			ArgStruct('No_Of_Packets', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Ip_Src_Address', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip_Src_Port', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Ip_Dest_Address', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip_Dest_Port', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.L_4_Protocol: List[str] = None
			self.No_Of_Packets: List[int] = None
			self.Ip_Src_Address: List[str] = None
			self.Ip_Src_Port: List[int] = None
			self.Ip_Dest_Address: List[str] = None
			self.Ip_Dest_Port: List[int] = None

	def get(self, filename: str) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPReplay:TRAFficfile \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipReplay.trafficFile.get(filename = '1') \n
		Queries information about all IP connections contained in a selected file of the playlist. If the file has not yet been
		analyzed and the measurement state is RUN, the command triggers file analysis. The analysis takes some time. Repeat the
		command until the analysis results are available. The results are returned as follows: {<L4Protocol>, <NoOfPackets>, ...,
		<IPDstPort>}conn 1, {...}conn 2, ... \n
			:param filename: File name as a string. Specify the file name with extension but without path, for example 'myfile.pcap'.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(filename)
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPReplay:TRAFficfile? {param}', self.__class__.GetStruct())
