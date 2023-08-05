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
class CreateList:
	"""CreateList commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("createList", core, parent)

	def set(self, filename: str, iteration: float = None, network_interface: enums.NetworkInterface = None) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPReplay:CREatelist \n
		Snippet: driver.configure.data.measurement.ipReplay.createList.set(filename = '1', iteration = 1.0, network_interface = enums.NetworkInterface.IP) \n
		Adds a single file to the playlist (measurement must be OFF) . A query returns all files in the playlist as follows:
		{<FileName>, <Iteration>, <NetworkInterface>}file 1, {...}file 2, ..., {...}file n To query a list of all files in the
		ip_replay directory, see method RsCmwDau.Data.Measurement.IpReplay.FileList.fetch. \n
			:param filename: File name as a string. Specify the file name with extension but without path, for example 'myfile.pcap'.
			:param iteration: Specifies how often the file is replayed Range: 0 to 10E+3
			:param network_interface: LANDau | IP | MULTicast LANDau: IP traffic to the LAN DAU connector IP: IP unicast traffic to the DUT MULTicast: IP multicast traffic to the DUT
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('iteration', iteration, DataType.Float, True), ArgSingle('network_interface', network_interface, DataType.Enum, True))
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPReplay:CREatelist {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Files: List[str]: No parameter help available
			- Iterations: List[int]: No parameter help available
			- Interfaces: List[enums.NetworkInterface]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Files', DataType.StringList, None, False, True, 1),
			ArgStruct('Iterations', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Interfaces', DataType.EnumList, enums.NetworkInterface, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Files: List[str] = None
			self.Iterations: List[int] = None
			self.Interfaces: List[enums.NetworkInterface] = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPReplay:CREatelist \n
		Snippet: value: GetStruct = driver.configure.data.measurement.ipReplay.createList.get() \n
		Adds a single file to the playlist (measurement must be OFF) . A query returns all files in the playlist as follows:
		{<FileName>, <Iteration>, <NetworkInterface>}file 1, {...}file 2, ..., {...}file n To query a list of all files in the
		ip_replay directory, see method RsCmwDau.Data.Measurement.IpReplay.FileList.fetch. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:DATA:MEASurement<MeasInstance>:IPReplay:CREatelist?', self.__class__.GetStruct())
