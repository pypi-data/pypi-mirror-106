from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:THRoughput:TRACe:OVERall:DLINk[:CURRent] \n
		Snippet: value: List[float] = driver.data.measurement.throughput.trace.overall.dlink.current.fetch() \n
		Query the values of the overall throughput trace in uplink (ULINk) or downlink (DLINk) direction. The trace values are
		returned from right to left (last to first measurement) , one result per interval, see method RsCmwDau.Configure.Data.
		Measurement.Throughput.mcount. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:return: results: Comma-separated list of throughput values, one result per interval Unit: bit/s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:DATA:MEASurement<MeasInstance>:THRoughput:TRACe:OVERall:DLINk:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:DATA:MEASurement<Instance>:THRoughput:TRACe:OVERall:DLINk[:CURRent] \n
		Snippet: value: List[float] = driver.data.measurement.throughput.trace.overall.dlink.current.read() \n
		Query the values of the overall throughput trace in uplink (ULINk) or downlink (DLINk) direction. The trace values are
		returned from right to left (last to first measurement) , one result per interval, see method RsCmwDau.Configure.Data.
		Measurement.Throughput.mcount. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:return: results: Comma-separated list of throughput values, one result per interval Unit: bit/s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:DATA:MEASurement<MeasInstance>:THRoughput:TRACe:OVERall:DLINk:CURRent?', suppressed)
		return response
