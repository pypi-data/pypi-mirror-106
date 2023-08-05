from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Extended:
	"""Extended commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("extended", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Counter: List[int]: Counter for identification of the result value The counter starts with 1 and is incremented for each result as long as the measurement is running.
			- Result: List[float]: Unit: bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Counter', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Result', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Counter: List[int] = None
			self.Result: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:DATA:MEASurement<Instance>:THRoughput:TRACe:OVERall:DLINk:EXTended \n
		Snippet: value: ResultData = driver.data.measurement.throughput.trace.overall.dlink.extended.read() \n
		Query the values of the overall throughput trace in uplink (ULINk) or downlink (DLINk) direction. The trace values are
		returned from right to left (last to first measurement) . There are two values per interval: <Reliability>, {<Counter>,
		<Result>}interval n, {...}interval n-1, ... The counter is useful if you want to perform repeated queries and combine the
		returned result traces. To configure the number of intervals, see method RsCmwDau.Configure.Data.Measurement.Throughput.
		mcount. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:DATA:MEASurement<MeasInstance>:THRoughput:TRACe:OVERall:DLINk:EXTended?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:THRoughput:TRACe:OVERall:DLINk:EXTended \n
		Snippet: value: ResultData = driver.data.measurement.throughput.trace.overall.dlink.extended.fetch() \n
		Query the values of the overall throughput trace in uplink (ULINk) or downlink (DLINk) direction. The trace values are
		returned from right to left (last to first measurement) . There are two values per interval: <Reliability>, {<Counter>,
		<Result>}interval n, {...}interval n-1, ... The counter is useful if you want to perform repeated queries and combine the
		returned result traces. To configure the number of intervals, see method RsCmwDau.Configure.Data.Measurement.Throughput.
		mcount. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:THRoughput:TRACe:OVERall:DLINk:EXTended?', self.__class__.ResultData())
