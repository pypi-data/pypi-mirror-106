from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interface:
	"""Interface commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("interface", core, parent)

	def set(self, filename: str, network_interface: enums.NetworkInterface) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPReplay:INTerface \n
		Snippet: driver.configure.data.measurement.ipReplay.interface.set(filename = '1', network_interface = enums.NetworkInterface.IP) \n
		Specifies the network interface for a selected file in the playlist. A query returns all files in the playlist as
		follows: {<FileName>, <NetworkInterface>}file 1, {...}file 2, ..., {...}file n \n
			:param filename: File name as a string. Specify the file name with extension but without path, for example 'myfile.pcap'.
			:param network_interface: LANDau | IP | MULTicast LANDau: IP traffic to the LAN DAU connector IP: IP unicast traffic to the DUT MULTicast: IP multicast traffic to the DUT
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('network_interface', network_interface, DataType.Enum))
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPReplay:INTerface {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Files_Names: List[str]: No parameter help available
			- Network_Interfaces: List[enums.NetworkInterface]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Files_Names', DataType.StringList, None, False, True, 1),
			ArgStruct('Network_Interfaces', DataType.EnumList, enums.NetworkInterface, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Files_Names: List[str] = None
			self.Network_Interfaces: List[enums.NetworkInterface] = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPReplay:INTerface \n
		Snippet: value: GetStruct = driver.configure.data.measurement.ipReplay.interface.get() \n
		Specifies the network interface for a selected file in the playlist. A query returns all files in the playlist as
		follows: {<FileName>, <NetworkInterface>}file 1, {...}file 2, ..., {...}file n \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:DATA:MEASurement<MeasInstance>:IPReplay:INTerface?', self.__class__.GetStruct())
