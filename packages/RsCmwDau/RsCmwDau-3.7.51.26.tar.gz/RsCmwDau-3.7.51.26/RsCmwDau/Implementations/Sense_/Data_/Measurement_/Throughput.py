from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	def get_interval(self) -> float:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:THRoughput:INTerval \n
		Snippet: value: float = driver.sense.data.measurement.throughput.get_interval() \n
		Queries the time interval between two throughput measurement results. \n
			:return: interval: In the current software version, the value is fixed. Unit: s
		"""
		response = self._core.io.query_str('SENSe:DATA:MEASurement<MeasInstance>:THRoughput:INTerval?')
		return Conversions.str_to_float(response)
