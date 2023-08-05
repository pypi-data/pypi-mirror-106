from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PacketLoss:
	"""PacketLoss commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("packetLoss", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPERf:PACKetloss \n
		Snippet: value: List[int] = driver.data.measurement.iperf.packetLoss.fetch() \n
		Queries the packet loss for all uplink instances. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:return: packet_loss: Comma-separated list of eight results (instance 1 to 8) Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:DATA:MEASurement<MeasInstance>:IPERf:PACKetloss?', suppressed)
		return response
