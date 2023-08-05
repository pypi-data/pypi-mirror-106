from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlink:
	"""Dlink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dlink", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:ADELay:DLINk \n
		Snippet: value: List[float] = driver.data.measurement.adelay.dlink.fetch() \n
		Query the statistical audio delay results for 'Uplink', 'Downlink' and 'Loopback'. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:return: results: Comma-separated list of four results: Current, Average, Minimum, Maximum value Unit: s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:DATA:MEASurement<MeasInstance>:ADELay:DLINk?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:DATA:MEASurement<Instance>:ADELay:DLINk \n
		Snippet: value: List[float] = driver.data.measurement.adelay.dlink.read() \n
		Query the statistical audio delay results for 'Uplink', 'Downlink' and 'Loopback'. \n
		Use RsCmwDau.reliability.last_value to read the updated reliability indicator. \n
			:return: results: Comma-separated list of four results: Current, Average, Minimum, Maximum value Unit: s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:DATA:MEASurement<MeasInstance>:ADELay:DLINk?', suppressed)
		return response
