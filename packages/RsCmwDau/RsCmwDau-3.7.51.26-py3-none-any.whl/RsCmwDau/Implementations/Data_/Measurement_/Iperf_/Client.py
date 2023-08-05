from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Client:
	"""Client commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("client", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:DATA:MEASurement<Instance>:IPERf:CLIent \n
		Snippet: value: List[float] = driver.data.measurement.iperf.client.read() \n
		Queries the throughput for all client instances. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:return: down_bandwidth: Comma-separated list of eight results (client instance 1 to 8) Unit: bit/s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:DATA:MEASurement<MeasInstance>:IPERf:CLIent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPERf:CLIent \n
		Snippet: value: List[float] = driver.data.measurement.iperf.client.fetch() \n
		Queries the throughput for all client instances. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:return: down_bandwidth: Comma-separated list of eight results (client instance 1 to 8) Unit: bit/s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:DATA:MEASurement<MeasInstance>:IPERf:CLIent?', suppressed)
		return response
