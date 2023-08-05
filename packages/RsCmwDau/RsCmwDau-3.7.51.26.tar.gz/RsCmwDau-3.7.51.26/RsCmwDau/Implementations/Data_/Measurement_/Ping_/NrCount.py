from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrCount:
	"""NrCount commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nrCount", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:PING:NRCount \n
		Snippet: value: int = driver.data.measurement.ping.nrCount.fetch() \n
		Queries the number of ping requests that have not been answered (no reply) . \n
			:return: req_no: Range: 0 to 1000"""
		response = self._core.io.query_str(f'FETCh:DATA:MEASurement<MeasInstance>:PING:NRCount?')
		return Conversions.str_to_int(response)
