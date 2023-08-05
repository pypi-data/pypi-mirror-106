from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self, dlink=repcap.Dlink.Default) -> List[float]:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:THRoughput:TRACe:RAN:DLINk<Index>:CURRent \n
		Snippet: value: List[float] = driver.data.measurement.throughput.trace.ran.dlink.current.fetch(dlink = repcap.Dlink.Default) \n
		Query the values of the throughput trace for RAN slot number <Index> in uplink (ULINk) or downlink (DLINk) direction. The
		trace values are returned from right to left (last to first measurement) , one result per interval, see method RsCmwDau.
		Configure.Data.Measurement.Throughput.mcount. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:param dlink: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Dlink')
			:return: results: Comma-separated list of throughput values, one result per interval Unit: bit/s"""
		dlink_cmd_val = self._base.get_repcap_cmd_value(dlink, repcap.Dlink)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:DATA:MEASurement<MeasInstance>:THRoughput:TRACe:RAN:DLINk{dlink_cmd_val}:CURRent?', suppressed)
		return response

	def read(self, dlink=repcap.Dlink.Default) -> List[float]:
		"""SCPI: READ:DATA:MEASurement<Instance>:THRoughput:TRACe:RAN:DLINk<Index>:CURRent \n
		Snippet: value: List[float] = driver.data.measurement.throughput.trace.ran.dlink.current.read(dlink = repcap.Dlink.Default) \n
		Query the values of the throughput trace for RAN slot number <Index> in uplink (ULINk) or downlink (DLINk) direction. The
		trace values are returned from right to left (last to first measurement) , one result per interval, see method RsCmwDau.
		Configure.Data.Measurement.Throughput.mcount. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:param dlink: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Dlink')
			:return: results: Comma-separated list of throughput values, one result per interval Unit: bit/s"""
		dlink_cmd_val = self._base.get_repcap_cmd_value(dlink, repcap.Dlink)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:DATA:MEASurement<MeasInstance>:THRoughput:TRACe:RAN:DLINk{dlink_cmd_val}:CURRent?', suppressed)
		return response
