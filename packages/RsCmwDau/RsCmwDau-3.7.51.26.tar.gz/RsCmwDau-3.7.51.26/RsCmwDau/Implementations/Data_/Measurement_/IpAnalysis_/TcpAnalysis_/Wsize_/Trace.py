from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Wsize_Ul: List[float]: Uplink TCP window size Unit: byte
			- Wsize_Dl: List[float]: Downlink TCP window size Unit: byte"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Wsize_Ul', DataType.FloatList, None, False, True, 1),
			ArgStruct('Wsize_Dl', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Wsize_Ul: List[float] = None
			self.Wsize_Dl: List[float] = None

	def fetch(self, flow_id: float) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:WSIZe:TRACe \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.tcpAnalysis.wsize.trace.fetch(flow_id = 1.0) \n
		Queries the window size traces for a specific connection, selected via its flow ID. The values for the uplink and
		downlink traces are returned in pairs: <Reliability>, <WSizeUL>1, <WSizeDL>1, <WSizeUL>2, <WSizeDL>2, ... The traces are
		returned from right to left (last to first measurement) . \n
			:param flow_id: Selects the connection for which the trace is queried
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:WSIZe:TRACe? {param}', self.__class__.FetchStruct())
