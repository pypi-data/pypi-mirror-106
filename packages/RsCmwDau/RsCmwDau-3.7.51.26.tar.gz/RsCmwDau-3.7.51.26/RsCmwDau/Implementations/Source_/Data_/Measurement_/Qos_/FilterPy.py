from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("filterPy", core, parent)

	def get_catalog(self) -> str:
		"""SCPI: SOURce:DATA:MEASurement<Instance>:QOS:FILTer:CATalog \n
		Snippet: value: str = driver.source.data.measurement.qos.filterPy.get_catalog() \n
		Queries a list of all existing QoS profiles. \n
			:return: catalog: String with comma-separated list of profile names, for example: 'Filter 1,Filter 2,Filter 3'
		"""
		response = self._core.io.query_str('SOURce:DATA:MEASurement<MeasInstance>:QOS:FILTer:CATalog?')
		return trim_str_response(response)
