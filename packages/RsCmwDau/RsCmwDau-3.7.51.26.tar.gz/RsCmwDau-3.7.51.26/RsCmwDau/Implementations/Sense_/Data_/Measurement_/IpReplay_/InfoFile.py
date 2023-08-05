from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InfoFile:
	"""InfoFile commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("infoFile", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Of_Packets: int: Number of IP packets in the file
			- File_Size: int: Unit: byte
			- Bitrate: float: Unit: bit/s
			- Duration: int: Unit: s
			- Type_Py: str: String indicating the file type and information about the capturing application
			- Encapsulation: str: 'Raw IP': file contains raw IP traffic 'Ethernet': file contains IP traffic plus Ethernet headers"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Of_Packets'),
			ArgStruct.scalar_int('File_Size'),
			ArgStruct.scalar_float('Bitrate'),
			ArgStruct.scalar_int('Duration'),
			ArgStruct.scalar_str('Type_Py'),
			ArgStruct.scalar_str('Encapsulation')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Of_Packets: int = None
			self.File_Size: int = None
			self.Bitrate: float = None
			self.Duration: int = None
			self.Type_Py: str = None
			self.Encapsulation: str = None

	def get(self, filename: str) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPReplay:INFofile \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipReplay.infoFile.get(filename = '1') \n
		Queries information about a selected file in the playlist. If the file has not yet been analyzed and the measurement
		state is RUN, the command triggers file analysis. The analysis takes some time. Repeat the command until the analysis
		results are available. \n
			:param filename: File name as a string. Specify the file name with extension but without path, for example 'myfile.pcap'.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(filename)
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPReplay:INFofile? {param}', self.__class__.GetStruct())
