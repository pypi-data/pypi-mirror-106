from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fthroughput:
	"""Fthroughput commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fthroughput", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Flow_Id: int: Flow ID of the connection assigned to the selected trace index
			- Throughput: List[float]: Comma-separated list of throughput values Unit: bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Flow_Id'),
			ArgStruct('Throughput', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Flow_Id: int = None
			self.Throughput: List[float] = None

	def fetch(self, trace=repcap.Trace.Default) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:FTTRigger:TRACes<TraceIndex>:FTHRoughput \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ftTrigger.traces.fthroughput.fetch(trace = repcap.Trace.Default) \n
		Queries a selected throughput trace. The trace is selected via its trace index. To assign a specific connection to a
		trace index, see method RsCmwDau.Configure.Data.Measurement.IpAnalysis.FtTrigger.Trace.TflowId.set. The trace is returned
		from right to left (last to first measurement) . \n
			:param trace: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Traces')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		trace_cmd_val = self._base.get_repcap_cmd_value(trace, repcap.Trace)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:FTTRigger:TRACes{trace_cmd_val}:FTHRoughput?', self.__class__.FetchStruct())
