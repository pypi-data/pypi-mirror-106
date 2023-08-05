from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlink:
	"""Dlink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dlink", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Sum_Th_Curr_Dlink: float: Current throughput Unit: bit/s
			- Sum_Th_Min_Dlink: float: Minimum throughput Unit: bit/s
			- Sum_Th_Max_Dlink: float: Maximum throughput Unit: bit/s
			- Sum_Th_Avg_Dlink: float: Average throughput Unit: bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Sum_Th_Curr_Dlink'),
			ArgStruct.scalar_float('Sum_Th_Min_Dlink'),
			ArgStruct.scalar_float('Sum_Th_Max_Dlink'),
			ArgStruct.scalar_float('Sum_Th_Avg_Dlink')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Sum_Th_Curr_Dlink: float = None
			self.Sum_Th_Min_Dlink: float = None
			self.Sum_Th_Max_Dlink: float = None
			self.Sum_Th_Avg_Dlink: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:THRoughput:RAN:TOTal:SUM:DLINk \n
		Snippet: value: ResultData = driver.data.measurement.throughput.ran.total.sum.dlink.fetch() \n
		Query the statistical results of the throughput measurement for the sum of all RAN slots in downlink direction. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:THRoughput:RAN:TOTal:SUM:DLINk?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:DATA:MEASurement<Instance>:THRoughput:RAN:TOTal:SUM:DLINk \n
		Snippet: value: ResultData = driver.data.measurement.throughput.ran.total.sum.dlink.read() \n
		Query the statistical results of the throughput measurement for the sum of all RAN slots in downlink direction. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:DATA:MEASurement<MeasInstance>:THRoughput:RAN:TOTal:SUM:DLINk?', self.__class__.ResultData())
