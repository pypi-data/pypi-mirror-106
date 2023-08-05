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
			- Re_Tx_Ul: List[float]: Uplink retransmission rate Range: 0 % to 100 %, Unit: %
			- Re_Tx_Dl: List[float]: Downlink retransmission rate Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Re_Tx_Ul', DataType.FloatList, None, False, True, 1),
			ArgStruct('Re_Tx_Dl', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Re_Tx_Ul: List[float] = None
			self.Re_Tx_Dl: List[float] = None

	def fetch(self, flow_id: float) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:RETRansmiss:TRACe \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.tcpAnalysis.retransmiss.trace.fetch(flow_id = 1.0) \n
		Queries the retransmission traces for a specific connection, selected via its flow ID. The values for the uplink and
		downlink traces are returned in pairs: <Reliability>, <ReTxUL>1, <ReTxDL>1, <ReTxUL>2, <ReTxDL>2, ... The traces are
		returned from right to left (last to first measurement) . \n
			:param flow_id: Selects the connection for which the trace is queried
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:RETRansmiss:TRACe? {param}', self.__class__.FetchStruct())
