from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	def fetch(self, flow_id: float) -> List[float]:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:RTT:TRACe \n
		Snippet: value: List[float] = driver.data.measurement.ipAnalysis.tcpAnalysis.rtt.trace.fetch(flow_id = 1.0) \n
		Queries the round-trip time trace for a specific connection, selected via its flow ID. The trace values are returned from
		right to left (last to first measurement) . \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:param flow_id: Selects the connection for which the trace is queried
			:return: rtt: Comma-separated list of round-trip time values Range: 0 ms to 5000 ms, Unit: ms"""
		param = Conversions.decimal_value_to_str(flow_id)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:RTT:TRACe? {param}', suppressed)
		return response
