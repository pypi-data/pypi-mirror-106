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

	def read(self, slot=repcap.Slot.Default) -> List[float]:
		"""SCPI: READ:DATA:MEASurement<Instance>:THRoughput:TRACe:RAN:ULINk<Index>:CURRent \n
		Snippet: value: List[float] = driver.data.measurement.throughput.trace.ran.ulink.current.read(slot = repcap.Slot.Default) \n
		Query the values of the throughput trace for RAN slot number <Index> in uplink (ULINk) or downlink (DLINk) direction. The
		trace values are returned from right to left (last to first measurement) , one result per interval, see method RsCmwDau.
		Configure.Data.Measurement.Throughput.mcount. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ulink')
			:return: results: Comma-separated list of throughput values, one result per interval Unit: bit/s"""
		slot_cmd_val = self._base.get_repcap_cmd_value(slot, repcap.Slot)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:DATA:MEASurement<MeasInstance>:THRoughput:TRACe:RAN:ULINk{slot_cmd_val}:CURRent?', suppressed)
		return response

	def fetch(self, slot=repcap.Slot.Default) -> List[float]:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:THRoughput:TRACe:RAN:ULINk<Index>:CURRent \n
		Snippet: value: List[float] = driver.data.measurement.throughput.trace.ran.ulink.current.fetch(slot = repcap.Slot.Default) \n
		Query the values of the throughput trace for RAN slot number <Index> in uplink (ULINk) or downlink (DLINk) direction. The
		trace values are returned from right to left (last to first measurement) , one result per interval, see method RsCmwDau.
		Configure.Data.Measurement.Throughput.mcount. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ulink')
			:return: results: Comma-separated list of throughput values, one result per interval Unit: bit/s"""
		slot_cmd_val = self._base.get_repcap_cmd_value(slot, repcap.Slot)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:DATA:MEASurement<MeasInstance>:THRoughput:TRACe:RAN:ULINk{slot_cmd_val}:CURRent?', suppressed)
		return response
