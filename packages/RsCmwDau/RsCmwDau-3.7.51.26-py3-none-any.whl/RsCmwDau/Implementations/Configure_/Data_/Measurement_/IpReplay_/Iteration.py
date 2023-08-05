from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iteration:
	"""Iteration commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iteration", core, parent)

	def set(self, filename: str, iteration: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPReplay:ITERation \n
		Snippet: driver.configure.data.measurement.ipReplay.iteration.set(filename = '1', iteration = 1) \n
		Specifies how often a selected file in the playlist is replayed. A query returns all files in the playlist as follows:
		{<FileName>, <Iteration>}file 1, {...}file 2, ..., {...}file n \n
			:param filename: File name as a string. Specify the file name with extension but without path, for example 'myfile.pcap'.
			:param iteration: Specifies how often the file is replayed Range: 0 to 10E+3
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('iteration', iteration, DataType.Integer))
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPReplay:ITERation {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Files_Names: List[str]: No parameter help available
			- Iterations: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Files_Names', DataType.StringList, None, False, True, 1),
			ArgStruct('Iterations', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Files_Names: List[str] = None
			self.Iterations: List[int] = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPReplay:ITERation \n
		Snippet: value: GetStruct = driver.configure.data.measurement.ipReplay.iteration.get() \n
		Specifies how often a selected file in the playlist is replayed. A query returns all files in the playlist as follows:
		{<FileName>, <Iteration>}file 1, {...}file 2, ..., {...}file n \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:DATA:MEASurement<MeasInstance>:IPReplay:ITERation?', self.__class__.GetStruct())
